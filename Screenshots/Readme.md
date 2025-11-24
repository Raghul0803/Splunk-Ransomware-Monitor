# AI-Driven Ransomware Early Warning System 🛡️

## 📌 Project Overview
This project is a real-time security monitoring system designed to detect ransomware-like activities on a Windows environment. It utilizes a Python-based agent to monitor file system entropy and modifications, streaming security telemetry to a Splunk SIEM for analysis.

## 🚀 Features
* **Real-time Monitoring:** Python `watchdog` library tracks file creation and modification events instantly.
* **SIEM Integration:** Data is ingested into Splunk Enterprise via HTTP Event Collector (HEC).
* **Live Dashboard:** Visualizes attack vectors, file targets, and total incident counts.
* **Lightweight Agent:** Runs with minimal resource usage on the endpoint.

## 🛠️ Technologies Used
* **Splunk Enterprise:** Log management and visualization.
* **Python:** Endpoint agent logic.
* **Watchdog & Requests:** Python libraries for file monitoring and HTTP transmission.

## 📸 Proof of Concept (Dashboard)
Here is the live dashboard capturing a simulated ransomware attack pattern:

![Dashboard Screenshot](Screenshots/Splunk_dashboard.jpg)clear

## 🔧 How to Run
1.  Install Splunk Enterprise and enable HEC (HTTP Event Collector).
2.  Update the `TOKEN` variable in `agent.py` with your Splunk HEC token.
3.  Run the agent:
    ```bash
    python agent.py
    ```
4.  Simulate an attack by modifying files in `C:\Users\Public`.