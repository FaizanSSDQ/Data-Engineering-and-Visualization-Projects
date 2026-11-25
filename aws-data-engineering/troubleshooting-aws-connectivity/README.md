# Database Connectivity Troubleshooting on AWS

> 🎓 Hands-on lab completed during the **DeepLearning.AI & AWS Data Engineering** program on Coursera. Lab environment and starter material by DeepLearning.AI; implementation and write-up by Faizan Saleem Siddiqui.


## Overview

This project focuses on troubleshooting and resolving common issues encountered when connecting to an Amazon RDS database from an EC2 instance. By working through various challenges, you will gain hands-on experience in diagnosing connectivity problems, adjusting security configurations, and executing SQL queries in a cloud-based environment.

## Key Objectives

- **Set Up the Lab Environment:** Deploy an RDS instance and an EC2 instance on AWS.
- **Troubleshoot Connectivity Issues:** Identify and resolve network and access-related problems.
- **Enhance RDS Security Configurations:** Modify security groups and IAM roles to establish secure database connections.
- **Query the Database:** Insert and retrieve data using SQL commands.

## Technologies Used

- **Amazon RDS** – Managed relational database service for cloud-based applications.
- **Amazon EC2** – Virtual computing environment for hosting applications.
- **AWS Security Groups & IAM Roles** – For managing access and security.
- **SQL** – For interacting with the database.

## Steps Involved

1. **Access the AWS Console**  
   - Run the necessary commands to log into AWS and set up the required resources.

2. **Connect EC2 to RDS**  
   - Configure the network and firewall settings to establish a stable connection between the EC2 instance and the RDS instance.

3. **Debug and Fix Connectivity Issues**  
   - Investigate potential issues such as security group misconfigurations, VPC settings, and incorrect credentials.
   - Implement fixes to ensure a secure and efficient connection.

4. **Perform Database Operations**  
   - Execute SQL queries to insert, retrieve, and manipulate data in the RDS instance.

## Prerequisites

- AWS account with necessary permissions.
- Basic understanding of **AWS EC2, RDS, and networking**.
- Familiarity with SQL for database interactions.

## Getting Started

To begin, run the following command in the terminal:  
```bash
aws configure
```


## License
This project is licensed under the MIT License – you are free to modify and use it for learning purposes.





## Conclusion
This project provides practical experience in identifying and resolving database connectivity issues on AWS. By working through real-world troubleshooting scenarios, you will enhance your cloud computing and database administration skills. The knowledge gained will be valuable for managing cloud-based applications and ensuring secure and efficient database connections

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
