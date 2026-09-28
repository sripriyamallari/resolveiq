
import asyncio
import streamlit as st
from hindsight_client import Hindsight

st.set_page_config(
    page_title="ResolveIQ",
    page_icon="🧠",
    layout="centered"
)

# Securely read the API key from Streamlit Secrets
HINDSIGHT_API_KEY = st.secrets["HINDSIGHT_API_KEY"]

client = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=HINDSIGHT_API_KEY
)

BANK_ID = "resolveiq"

st.title("🧠 ResolveIQ")
st.subheader("AI Customer Support Memory & Escalation")

st.divider()

customer_id = st.text_input(
    "Customer ID",
    value="C102"
)

current_issue = st.text_area(
    "Current Issue",
    value="Payment failed again"
)

if st.button("🔍 Analyze Customer", use_container_width=True):

    if not customer_id.strip():
        st.warning("Please enter a Customer ID.")
        st.stop()

    if not current_issue.strip():
        st.warning("Please enter the current issue.")
        st.stop()

    query = f"""
    Previous support history for customer {customer_id}.
    Current issue: {current_issue}.
    Find previous cases, attempted solutions,
    recurring problems, and customer frustration.
    """

    try:
        result = asyncio.run(
            client.arecall(
                bank_id=BANK_ID,
                query=query
            )
        )

        memories = result.results

        st.success("Customer history found")

        st.subheader("🧠 Customer History")

        if memories:
            for memory in memories[:8]:
                st.write(f"• {memory.text}")
        else:
            st.info("No previous customer history found.")

        history = " ".join(
            memory.text.lower()
            for memory in memories
        )

        issue_repeat = (
            "payment failure" in history
            or "payment failed" in history
            or "recurring" in history
            or "persistent" in history
        )

        previous_attempt = (
            "bank verification" in history
            or "verification" in history
        )

        frustrated = (
            "frustrated" in history
            or "frustration" in history
        )

        st.divider()

        if issue_repeat and previous_attempt:

            st.error("🔴 ESCALATION RECOMMENDED")

            st.write("### Reason")

            st.write(
                "The customer has a recurring issue and a previous "
                "troubleshooting attempt did not permanently resolve it."
            )

            if frustrated:
                st.write(
                    "The customer is also showing frustration."
                )

            st.write("### Next Action")

            st.write(
                "➡️ Escalate to specialist/payment support."
            )

            st.write(
                "➡️ Review the previous case before repeating troubleshooting."
            )

        else:

            st.success("🟢 STANDARD SUPPORT")

            st.write("### Next Action")

            st.write(
                "➡️ Continue normal troubleshooting."
            )

    except Exception as e:
        st.error("Unable to retrieve customer history.")
        st.code(str(e))

st.divider()
st.caption("ResolveIQ — Remember the case. Resolve the issue.")
