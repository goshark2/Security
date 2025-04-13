# **Compromised Windows Analysis**

Recently, I completed the Compromised Windows Analysis room on TryHackMe, and it was an incredibly insightful dive into Windows Forensics and Incident Response. 
Here I’ll walk through the key investigation steps, forensic tools, and the attacker’s full timeline I uncovered during the challenge.

**This challenge was an excellent hands-on experience in:**
1. Using Eric Zimmerman tools like LECmd, PECmd, AmcacheParser
2. Parsing and correlating LNK, Prefetch, and Amcache artifacts
3. Investigating Scheduled Tasks and Windows Event Logs
4. Reconstructing a complete attack timeline

## **Tools Used**
1. Eric Zimmerman's Tools
2. Windows Event Viewer
3. Timeline Explorer

## **Scenario:**

TKM, a small tech startup, detected suspicious SSH traffic to a known malicious IP from one of its employee's machines (Aashir’s host).
The junior security engineer, Joe, noticed:

**SSH connection attempts every minute**

**Windows Defender was disabled**

**The user was unaware of any such activity**

**A recurring prompt showed up every minute**

Joe quickly blocked the IP, contained the host, and escalated for a deeper investigation. That’s where I step in as forensic investigators.
To analyze the compromise, I relied on Eric Zimmerman’s forensic tools and a structured investigation approach using several key Windows artifacts.

**Step 1: Scheduled Tasks – Persistence Mechanism**
I suspected the recurring prompt every minute was tied to a Scheduled Task.

I opened Task Scheduler and confirmed a task was created at 10:29 AM, intended to reach out to the C2 server via SSH on a one-minute interval.
This indicated persistence and possibly automated command execution.

![image](https://github.com/user-attachments/assets/0b0364bc-9665-4ad0-8110-3581387b2023)


**Step 2: LNK Files – Tracking File Access**
I checked .LNK (shortcut) files to determine what files were accessed before the scheduled task creation.
Located in: C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Recent Items
I found an LNK pointing to a RAR file accessed at 10:27 AM—just two minutes before the scheduled task was created.
However, the original RAR file had been deleted.

![image](https://github.com/user-attachments/assets/d235b342-b755-44c9-858a-4c151e2de100)


**Step 3: LECmd – Parsing LNK Files**
Using LECmd, I parsed the LNK files:
cd "C:\Users\Administrator\Desktop\Forensics Tools\LECmd"
.\LECmd.exe -d C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Recent --csvf Parsed-LNK.csv --csv C:\Users\Administrator\Desktop
Imported the results into Timeline Explorer to visualize the activity timeline.
I confirmed:
File accessed at 10:27
Target: A suspicious RAR archive

![image](https://github.com/user-attachments/assets/4dd161b4-4485-42fd-86a5-1414782ba09a)


**Step 4: Prefetch Files – Program Execution**
Next, I parsed Prefetch files using PECmd to confirm if any executables from the RAR were launched.
cd "C:\Users\Administrator\Desktop\Forensics Tools\PECmd"
.\PECmd.exe -d "C:\Windows\Prefetch" --csv C:\Users\Administrator\Desktop --csvf Prefetch-Parsed.csv
results were visualized via Timeline Explorer.
I saw a suspicious executable was run immediately after the RAR file was accessed—likely the malicious payload.

![image](https://github.com/user-attachments/assets/5f6118ce-2944-4d1e-a01d-ea9fd18dbb16)



**Step 5: Amcache – File Metadata & Hashes**
I leveraged Amcache to find metadata like full path and hash of the executed file:
Pre-parsed file Amcache-Parsed.csv was available on Desktop.
It revealed:
Full path to the executable
SHA1 hash
Execution time consistent with previous evidence

![image](https://github.com/user-attachments/assets/2f5fcacb-04a0-4120-9f76-0f7314d9439a)


**Step 6: Windows Event Logs – RDP & Defender Tampering**
Using Event Viewer, I uncovered more breadcrumbs:
RDP Logon (Event ID 1149) – successful RDP session just before the RAR file was accessed.
Windows Defender Disabled (Event ID 5001) – confirming tampering to avoid detection.

![image](https://github.com/user-attachments/assets/a9294f6e-873a-47bc-98cc-b7849f50a1b5)


![image](https://github.com/user-attachments/assets/f991b8ed-63be-4c88-8b92-1229ad58fce4)


