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


![image](https://github.com/user-attachments/assets/2aabfcf2-3707-487a-8fbf-0fc5acc94110)


![image](https://github.com/user-attachments/assets/0c8e3bb0-f0a7-4b89-89cc-c204cda02e17)


1. Accounts affected: 
2. Deleted by: 
3. Tactic: 
4. Sub-Technique: 
5. Valid Accounts: 
6. Workflow ID:
7. UPN Suffix: 


**Incident #2: Attempts to Sign in to Disabled Accounts**


![image](https://github.com/user-attachments/assets/97592ce7-4dd6-41e5-86b0-93841e8e73c4)


1. Disabled account: 
2. IP Address: 
3. Geolocation: 
4. ResultType Filter: 
5. Rule Frequency: 

**Incident #3: Explicit MFA Deny**


![image](https://github.com/user-attachments/assets/da41a490-b7d3-41ed-a05c-bed0a1d5b09c)

![image](https://github.com/user-attachments/assets/6d0fad3f-60a2-4370-8a29-3c4ad07da8df)

![image](https://github.com/user-attachments/assets/32195fe6-ea57-48f8-bb90-5f558bcaa87b)


1. Tactic: 
2. Technique: 
3. MFA Error Code: 
4. Access Policy: 
5. Authentication Method: 
6. Browser Version: 
7. Entities Involved: 

**Incident #4: Privileged Role Assigned Outside PIM**


![image](https://github.com/user-attachments/assets/1a3391d9-f1c9-493e-a9df-26f43e5debf8)

![image](https://github.com/user-attachments/assets/9152be04-3736-4732-99fe-15bda9e04de4)

![image](https://github.com/user-attachments/assets/2e117b78-1ad0-449f-bc56-d49ebf7aa30c)

1. Escalated by: 
2. Assigned Role: 
3. Logged in Table: 
4. Another Targeted User: 
5. Initiating IP Address:
6. Created by: 

This lab was a fantastic opportunity to put theoretical knowledge into practical use. 
From deploying analytics rules to analyzing incidents with KQL, the challenge simulated what real-world threat detection and response looks like in Microsoft Sentinel.

![image](https://github.com/user-attachments/assets/bfd1bff9-f39b-4df5-8a13-9630b7325ddb)



