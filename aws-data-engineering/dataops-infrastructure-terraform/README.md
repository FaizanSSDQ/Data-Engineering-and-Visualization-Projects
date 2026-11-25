# Project: Implementing DataOps with Terraform

> 🎓 Hands-on lab completed during the **DeepLearning.AI & AWS Data Engineering** program on Coursera. Lab environment and starter material by DeepLearning.AI; implementation and write-up by Faizan Saleem Siddiqui.


In this project, I used **[Terraform](https://www.terraform.io/intro)**, an **Infrastructure as Code (IaC)** tool, to deploy a **database instance** via a **bastion host**. This project demonstrated how to automate infrastructure provisioning and management, ensuring consistency and scalability in a DataOps environment.

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

The goal of this project was to:
1. **Automate Infrastructure Deployment**: Use Terraform to provision a database instance and a bastion host.
2. **Ensure Secure Access**: Configure the bastion host to securely access the database instance.
3. **Apply DataOps Principles**: Implement infrastructure as code to streamline deployment and management processes.

---

## Key Features

- **Infrastructure as Code**: Defined and managed infrastructure using Terraform configuration files.
- **Bastion Host**: Set up a secure gateway for accessing the database instance.
- **Scalability**: Designed the infrastructure to be easily scalable for future needs.
- **Reproducibility**: Ensured consistent deployments across environments.

---

## Technologies Used

- **Terraform**: For infrastructure provisioning and management.
- **AWS**: For hosting the database instance and bastion host.
- **Bastion Host**: For secure access to the database instance.
- **SSH Key Pair**: For secure authentication between the user and the bastion host.
- **CloudFormation**: For pre-configured networking resources (VPC, subnets).

---


---

## How to Run the Project

### Prerequisites
1. **Terraform**: Install Terraform on your local machine.
2. **AWS Account**: Set up an AWS account and configure credentials.
3. **SSH Key Pair**: Generate an SSH key pair for secure access to the bastion host.

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/terraform-dataops.git
   cd terraform-dataops
   ```
   
   
   
# Conclusion
This project provided hands-on experience in implementing DataOps principles using Terraform. By automating infrastructure deployment and ensuring secure access via a bastion host, I created a scalable and reproducible solution for managing database instances. This approach can be extended to other infrastructure components and cloud environments.

---
## 👤 About the Author

**Faizan Saleem Siddiqui**, Embedded Firmware Engineer | Research Scholar

Electronics engineer with 2+ years of experience in embedded systems and firmware development.
I build production firmware for **BLE wearables and biosignal devices** on Nordic nRF52 (Zephyr / nRF
Connect SDK), including **secure OTA updates (MCUboot, signed images)**, **low-power battery
management** and **true-wireless Bluetooth audio**. My background also covers STM32 and ESP32 with
FreeRTOS, real-time data acquisition, digital signal processing, industrial IoT, and Python tooling
for data, automation and machine learning.

- 🎓 MS Electronics, Quaid-i-Azam University, Islamabad (BS Electronics: 1st position, merit scholar)
- 🧑‍🏫 Former Visiting Faculty, Embedded Systems, and Research Assistant, Autonomous Vehicles (COMSIP Lab)
- 🌍 Open to embedded / firmware engineering opportunities worldwide

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Faizan%20Saleem%20Siddiqui-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/faizan-saleem-siddiqui-4411bb247/)
[![GitHub](https://img.shields.io/badge/GitHub-FaizanSSDQ-181717?logo=github&logoColor=white)](https://github.com/FaizanSSDQ)
[![Email](https://img.shields.io/badge/Email-faizansaleemsdq%40gmail.com-D14836?logo=gmail&logoColor=white)](mailto:faizansaleemsdq@gmail.com)

Licensed under the [MIT License](../../LICENSE) (lab starter material © DeepLearning.AI).
