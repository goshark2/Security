# **MS Sentinel: Just Looking - TryHackMe**
Microsoft Sentinel challenge for SOC analysts: incident investigation & threat hunting.
![image](https://github.com/user-attachments/assets/b7d1a2bc-255e-457f-8a48-2cd5b5cb9c63)

In this blog, I walk you through an exciting hands-on lab that simulates a real-world SOC Analyst experience using Microsoft Sentinel. 
The challenge? Investigate security incidents, analyze analytics rules, and uncover attacker techniques using KQL and threat intel. 
Ready to jump into the action?
Scenario
You are working as a SOC Analyst, SIEM Practitioner, or Cloud Security Engineer. 
A series of incidents are firing in Microsoft Sentinel, and your mission is clear: investigate, analyze, and respond.


## **Step 1: Join the Lab**
Navigate to the Cloud Details > Environment tab and click "Join Lab".
Head to the Credentials tab, copy the provided credentials, and log into the Azure portal.
If prompted for Microsoft Authenticator, select "Ask later".
In the Azure portal, go to Resource Groups and verify the resource group rg-<labId> is available.

![image](https://github.com/user-attachments/assets/c0579264-ee60-4568-b212-758e9f5fdf0e)


## **Step 2: Ingest Logs into Log Analytics**
Open Cloud Details > Actions tab.
Click "Ingest Logs" — DO NOT click "Deploy Rules" yet.
This step:
Creates the Log Analytics Workspace
Onboards Microsoft Sentinel
Ingests logs required for investigation
Wait ~3 minutes for log ingestion to complete. Use the Deployments tab to monitor progress.

## **Step 3: Confirm Log Ingestion**
Validate log ingestion using KQL queries:

SigninLogs_CL | count
AuditLogs_CL | count

SigninLogs_CL:  rows

AuditLogs_CL:  rows

## **Step 4: Deploy Analytics Rules**
Once the logs are ingested, it’s time to enable detection:
In the Cloud Details > Actions tab, click "Deploy Rules".
Confirm rule deployment via:
Microsoft Sentinel > Configuration > Analytics
Check that rules are active and running.

## **Step 5: Verify Incidents Are Triggered**
Navigate to:
Microsoft Sentinel > Threat Management > Incidents

If no incidents appear in 5 minutes, re-save the rules:
Analytics > Select a rule > Edit > Review + Create > Save
Once triggered, you're ready for the incident investigation challenge. Let's dig in!

## **Incident Investigations**
**Incident #1: Account Created and Deleted in Short Timeframe**
![image](https://github.com/user-attachments/assets/bbe3f68e-0078-4432-a459-e8221d0ed7c5)

![image](https://github.com/user-attachments/assets/889406c6-d820-43ce-ba5f-6f9975a69e35)



Accounts affected: 
Deleted by: 
MITRE ATT&CK Tactic: 
Sub-Technique: T1078.004 – Valid Accounts: 
Workflow ID:
UPN Suffix: 


**Incident #2: Attempts to Sign in to Disabled Accounts**
![image](https://github.com/user-attachments/assets/375622f5-0375-4dc4-b5de-b0bc8ad902a6)

Disabled account: 
IP Address: 
Geolocation: 
ResultType Filter: 
Rule Frequency: 

**Incident #3: Explicit MFA Deny**

![image](https://github.com/user-attachments/assets/57a5bc35-2fdd-494a-85ee-dbfadb680a52)

![image](https://github.com/user-attachments/assets/349016a8-9250-4031-92b0-9cad59abd77b)

![image](https://github.com/user-attachments/assets/5ec76b38-562d-466d-9fe6-40e883daebdc)

Tactic: 
Technique: 
MFA Error Code: 
Access Policy: 
Authentication Method: 
Browser Version: 
Entities Involved: 

**Incident #4: Privileged Role Assigned Outside PIM**

![image](https://github.com/user-attachments/assets/0d3237f9-b886-459d-9fbf-cc20171bc29b)
![image](https://github.com/user-attachments/assets/49b7c360-b9b0-4d20-8941-a6af0740a413)
![image](https://github.com/user-attachments/assets/c002048c-9533-4945-b94f-6ec2dce38cc5)


Escalated by: 
Assigned Role: 
Logged in Table: 
Another Targeted User: 
Initiating IP Address:
Created by: 

This lab was a fantastic opportunity to put theoretical knowledge into practical use. 
From deploying analytics rules to analyzing incidents with KQL, the challenge simulated what real-world threat detection and response looks like in Microsoft Sentinel.
![image](https://github.com/user-attachments/assets/bfd1bff9-f39b-4df5-8a13-9630b7325ddb)



