# ResolveIQ

### AI-Powered Customer Support Memory & Escalation Agent

ResolveIQ is an AI-powered customer support system designed to give support agents **persistent customer memory**. It remembers previous customer interactions, identifies recurring unresolved issues, recognizes previous troubleshooting attempts, and recommends escalation when repeating the same troubleshooting process is no longer appropriate.

## 🚀 Live Demo

**Try ResolveIQ:**  
https://resolveiq-zrybe6cvazztu3cnobbayk.streamlit.app/

---

## 📌 Problem Statement

Traditional customer support systems often treat each support interaction as an isolated conversation.

When a customer returns with the same problem:

- Previous support history may not be effectively recalled.
- Customers may be asked to repeat the same troubleshooting steps.
- Previously attempted solutions may be repeated even when they did not permanently resolve the issue.
- Recurring problems can be difficult to identify quickly.
- Customer frustration may increase when the same issue continues without meaningful escalation.

This creates a gap between **customer history** and **real-time support decision-making**.

### The core problem

> How can an AI support agent remember what happened previously, recognize recurring unresolved issues, and recommend an appropriate escalation instead of repeatedly starting the troubleshooting process from the beginning?

---

## 💡 Solution

ResolveIQ addresses this problem by combining an AI support interface with **persistent organizational memory**.

The system retrieves relevant historical information about a customer and analyzes it alongside the customer's current issue.

For example:

**Customer:** C102  
**Current Issue:** Payment failed again

ResolveIQ can recall that:

- The customer experienced the same payment failure previously.
- Bank verification was already completed.
- The previous troubleshooting attempt did not permanently resolve the issue.
- The customer has reported the problem again.
- The customer is frustrated by the recurring issue.

Based on this history, ResolveIQ recommends:

**🔴 ESCALATION RECOMMENDED**

Instead of simply repeating the previous troubleshooting process, the support agent is advised to review the previous case and escalate the issue to the appropriate specialist or payment support team.

---

## 🎯 What ResolveIQ Provides

### 1. Persistent Customer Memory

ResolveIQ stores and retrieves relevant information from previous customer interactions.

This allows the support agent to understand the customer's history rather than treating every interaction as a completely new case.

### 2. Recurring Issue Detection

The system identifies patterns such as:

- Repeated payment failures
- Persistent unresolved problems
- Previous troubleshooting attempts
- Repeated customer complaints

### 3. Previous Solution Awareness

ResolveIQ checks whether a troubleshooting step or verification process has already been attempted.

This helps prevent unnecessary repetition.

### 4. Escalation Recommendation

When a recurring issue has already gone through previous troubleshooting, ResolveIQ can recommend escalation rather than continuing the same process.

### 5. Customer Frustration Awareness

The system considers indicators of customer frustration present in the support history.

This provides additional context for support decisions.

### 6. Actionable Next Steps

Instead of only displaying historical information, ResolveIQ provides a suggested next action, such as:

> Review the previous case before repeating troubleshooting and escalate to specialist/payment support when appropriate.

---

## 🧠 How It Works

```text
Customer Issue
      │
      ▼
ResolveIQ Support Interface
      │
      ▼
Retrieve Relevant Customer History
      │
      ▼
Analyze Previous Interactions
      │
      ├── Previous Issue?
      ├── Previous Troubleshooting?
      ├── Issue Recurring?
      └── Customer Frustration?
      │
      ▼
Escalation Decision
      │
      ├── 🟢 Standard Support
      │
      └── 🔴 Escalation Recommended
