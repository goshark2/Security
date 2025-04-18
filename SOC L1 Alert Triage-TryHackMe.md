# **SOC L1 Alert Triage - TryHackMe**
As part of my continuous learning in cybersecurity, today I completed the Alert Triage room on TryHackMe, designed for SOC L1 analysts. 
This beginner-friendly yet vital lab taught me the lifecycle of alerts, from how they’re created to how to respond to them effectively.
## **Here’s what the lab aimed to teach:**

1. What SOC alerts are and why they matter
2. How alerts are structured and categorized
3. The lifecycle of an alert: from detection to resolution
4. How to prioritize and triage alerts as a SOC L1 analyst
5. Practical experience using a simulated SOC dashboard

## **From Events to Alerts**
It all starts with an event — a login attempt, file download, or command execution. These events are logged by systems like your OS, firewall, or cloud platform. 
But reading logs manually? Not efficient.

That’s where alerts come in — automated flags generated by SIEMs or EDR tools when certain patterns are recognized.

![image](https://github.com/user-attachments/assets/34a34bef-24e9-4f3e-8f02-f6a885761023)

## **SOC L1's Role in Triage**
As a SOC Level 1 analyst, you're the gatekeeper. Your responsibilities include:

1. Reviewing alerts
2. Identifying true vs false positives
3. Escalating serious issues to L2 analysts
4. Providing detailed notes and initial analysis
Other team members like SOC L2s, engineers, and managers support this lifecycle — but the L1 analyst is often the first to act.

## **Understanding Alert Properties**
Here’s a quick overview of alert components I worked with:

1. Alert Time: When the alert was created
2. Alert Name: e.g., Email Marked as Phishing, Mimikatz Usage
3. Severity: Ranges from Low 🟢 to Critical 🔴
4. Status: New, In Progress, Closed
5. Verdict: True Positive or False Positive
6. Assignee: The analyst currently handling the alert
7. Description & Fields: Context, impacted users/hosts, and actions

## **Hands-On Triage Time!**

![image](https://github.com/user-attachments/assets/b4d25014-91bf-494f-b033-330de0bdf2c3)

**Scenario 1:** Potential Data Exfiltration
I assigned myself the critical alert named "Potential Data Exfiltration", marked it as In Progress, and began investigating.
After reviewing login events, IP addresses, and file transfer patterns, I confirmed it was a ✅True positive.

**Scenario 2:** Unusual VPN Login Location
I reviewed the alert details and found it was triggered due to a login from an unfamiliar location. However, after checking logs, I discovered it was the user's known secondary location.
❌ False Positive

**Scenario 3:** Email Marked as Phishing
This one was obvious — a suspicious email link had already been clicked. The user fell for a classic phishing trick. I quickly confirmed it was malicious.
✅ True Positive

![image](https://github.com/user-attachments/assets/173e9c57-ce8f-4fec-945e-fa305212ae97)

## **Here’s what I learned from this lab:**

1. Not every alert is a threat — false positives are common!
2. A methodical approach to alert triage prevents burnout and missed threats
3. Severity and timing are key to prioritizing alerts
4. Triage is a blend of logic, intuition, and technical knowledge
5. Good documentation and communication are crucial — especially when escalating alerts


This TryHackMe lab was more than just checkboxes and flags — it simulated the real-world pace, pressure, and mindset of a SOC analyst. 
As someone passionate about cybersecurity, it was a rewarding experience to practice the fundamentals in such a hands-on way.
Whether you’re just getting into security operations or brushing up for certifications like SAL1, I highly recommend this lab as a foundational stepping stone.




![image](https://github.com/user-attachments/assets/97260373-5bbc-408d-b8df-a9879b12e3fe)
