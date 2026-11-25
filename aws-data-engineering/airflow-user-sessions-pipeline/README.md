# Building a Data Pipeline for DeFtunes - Data Engineering Project

> 🎓 Hands-on lab completed during the **DeepLearning.AI & AWS Data Engineering** program on Coursera. Lab environment and starter material by DeepLearning.AI; implementation and write-up by Faizan Saleem Siddiqui.


In this project, I implemented a **data pipeline** using **Apache Airflow** to support **DeFtunes**, a fictitious company in the music industry. DeFtunes offers a subscription-based app for streaming songs and has recently expanded its services to include digital song purchases. With this new retail feature, DeFtunes required a data pipeline to extract purchase data from their API and make it available for downstream systems.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [How to Run the Project](#how-to-run-the-project)
- [Conclusion](#conclusion)

---

## Project Overview

As a Data Engineer at DeFtunes, I was tasked with developing a pipeline to extract user and session data from the API. The pipeline was designed to:
1. Extract information about new users for a given date.
2. Retrieve session data for users on a specific date.
3. Fetch detailed information about users within those sessions.

The pipeline was scheduled to run daily, ensuring that the data is always up-to-date for downstream systems.

---

## Key Features

- **API Integration**: Performed API requests to extract user and session data.
- **Daily Scheduling**: Configured the pipeline to run every day for up-to-date data.
- **Error Handling**: Implemented robust error handling to ensure pipeline reliability.
- **Downstream Integration**: Made the extracted data available for analytics and other processes.

---

## Technologies Used

- **Apache Airflow**: For orchestrating the data pipeline.
- **Python**: For scripting the API requests and data processing logic.
- **Docker**: For containerizing the Airflow environment.
- **AWS EC2**: For hosting the Airflow instance.

---


---

## How to Run the Project

### Prerequisites
1. **Apache Airflow**: Ensure Airflow is installed and configured.
2. **Docker**: Install Docker if using a containerized Airflow environment.
3. **AWS EC2**: Set up an EC2 instance for hosting Airflow (if applicable).

### Steps
1. **Set Up Airflow**:
   - Install Airflow and configure connections to the API.
   - Install required libraries using:
     ```bash
     pip install -r requirements.txt
     ```

2. **Upload DAGs**:
   - Place the DAG files (`extract_users.py`, `extract_sessions.py`, `process_data.py`) in the `dags/` directory of your Airflow environment.

3. **Trigger DAGs**:
   - Activate and trigger the DAGs from the Airflow UI.

4. **Monitor and Debug**:
   - Use the Airflow logs to monitor task execution and debug any issues.

---

## Conclusion

This project provided hands-on experience in building and orchestrating data pipelines using Apache Airflow. By extracting user and session data from the API and making it available for downstream systems, I ensured that DeFtunes could effectively support its new retail feature. The pipeline is scalable and can be extended to handle additional data sources or use cases.

---

Feel free to explore the code and adapt it for your own data pipelines!

---
## 👤 About the Author

**Faizan Saleem Siddiqui**, Embedded Firmware Engineer | Visiting Faculty | Research Scholar

Electronics engineer with 2+ years of experience in embedded systems and firmware development.
I build production firmware for **BLE wearables and biosignal devices** on Nordic nRF52 (Zephyr / nRF
Connect SDK), including **secure OTA updates (MCUboot, signed images)**, **low-power battery
management** and **true-wireless Bluetooth audio**. My background also covers STM32 and ESP32 with
FreeRTOS, real-time data acquisition, digital signal processing, industrial IoT, and Python tooling
for data, automation and machine learning.

- 🎓 MS Electronics, Quaid-i-Azam University, Islamabad (BS Electronics: 1st position, merit scholar)
- 🧑‍🏫 Visiting Faculty Member, Quaid-i-Azam University: teaching Real-Time Systems (STM32, FreeRTOS),
  Microcontroller Interfacing (ESP32) and AI/ML on Embedded Devices (TinyML)
- 🔬 Former Research Assistant, Autonomous Vehicle Engineering (COMSIP Lab, QAU)
- 🌍 Open to embedded / firmware engineering opportunities worldwide

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Faizan%20Saleem%20Siddiqui-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/faizan-saleem-siddiqui-4411bb247/)
[![GitHub](https://img.shields.io/badge/GitHub-FaizanSSDQ-181717?logo=github&logoColor=white)](https://github.com/FaizanSSDQ)
[![Email](https://img.shields.io/badge/Email-faizansaleemsdq%40gmail.com-D14836?logo=gmail&logoColor=white)](mailto:faizansaleemsdq@gmail.com)

Licensed under the [MIT License](../../LICENSE) (lab starter material © DeepLearning.AI).
