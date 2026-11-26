# AWS Infrastructure Monitoring with CloudWatch and SNS

> 🎓 Hands-on lab completed during the **DeepLearning.AI & AWS Data Engineering** program on Coursera. Lab environment and starter material by DeepLearning.AI; implementation and write-up by Faizan Saleem Siddiqui.


This project focuses on implementing robust monitoring and alerting for an AWS infrastructure involving a bastion host and an RDS database. By leveraging Amazon CloudWatch and SNS, we ensure the reliability and availability of critical resources.

## Project Description

The project addresses the need for proactive infrastructure monitoring by setting up CloudWatch alarms to detect potential failures in the bastion host. When an alarm is triggered, an SNS topic sends an email notification, enabling rapid response and recovery. This project also demonstrates the use of `sysbench` for performance testing and the enabling of RDS Performance Insights for in-depth database monitoring.

## Key Features

* **Bastion Host Monitoring:** Implementation of CloudWatch alarms to monitor the health of the bastion host.
* **Real-time Alerts:** Configuration of an SNS topic and subscription for immediate email notifications upon alarm triggers.
* **RDS Performance Insights:** Enabling and utilizing RDS Performance Insights for detailed database monitoring.
* **Performance Testing:** Usage of `sysbench` for stress testing and performance evaluation.
* **Infrastructure as Code (IaC):** Utilizes Terraform for infrastructure provisioning and management.

## Getting Started

1.  **Prerequisites:**
    * An AWS account with appropriate permissions.
    * Terraform installed.
    * AWS CLI configured.

2.  **Clone the Repository:**

    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```

3.  **Initialize Terraform:**

    ```bash
    terraform init
    ```

4.  **Apply Terraform Configuration:**

    ```bash
    terraform apply
    ```

    * Confirm the deployment by typing `yes`.

5.  **Connect to Bastion Host:**
    * Navigate to the EC2 console.
    * Find the bastion host `de-c2w3lab2-bastion-host`.
    * Connect via SSH.

6.  **Run Sysbench Tests:**
    * Use the provided sysbench commands on the bastion host terminal to generate load and monitor metrics.

7.  **Monitor CloudWatch and SNS:**
    * Observe CloudWatch metrics and alarms.
    * Verify email notifications from SNS.
    * To see the rds performance insights, navigate to the RDS dashboard, and then to the database instance.

## Architecture

The architecture consists of:

* A bastion host for secure access to the private network.
* An RDS database instance with Performance Insights enabled.
* CloudWatch alarms to monitor the bastion host.
* An SNS topic and subscription for email notifications.
* Terraform files for infrastructure creation.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any improvements or bug fixes.

## License

[This repository is licensed under the MIT License - see the LICENSE file for details]


## Conclusion

This project successfully demonstrates the implementation of robust monitoring and alerting mechanisms for a critical AWS infrastructure. By leveraging CloudWatch, SNS, and best practices in infrastructure management, we have established a proactive approach to ensuring the availability and reliability of our systems. The insights gained from this project, including the use of `sysbench` for performance testing and RDS Performance Insights for database monitoring, can be applied to other AWS environments, enhancing overall operational efficiency and minimizing downtime. This project not only reinforces the importance of proactive monitoring but also provides a practical guide for setting up similar systems in production environments.

---
## 👤 About the Author

**Faizan Saleem Siddiqui**, Embedded Firmware Engineer | Visiting Faculty | Research Scholar

Electronics engineer with 2+ years of experience in embedded systems and firmware development.
I build firmware for **BLE wearables** and **Bluetooth TWS audio devices** on Nordic nRF52 (Zephyr /
nRF Connect SDK), including **secure OTA updates (MCUboot, signed images)**, **low-power battery
management** and **charging-case firmware**. My background also covers STM32 and ESP32 with
FreeRTOS, real-time data acquisition, digital signal processing, industrial IoT, and Python tooling
for data, automation and machine learning.

- 🎓 MS Electronics, Quaid-i-Azam University, Islamabad (BS Electronics: 1st position, merit scholar)
- 🧑‍🏫 Visiting Faculty Member, Quaid-i-Azam University: teaching Real-Time Systems (STM32, FreeRTOS),
  Microcontroller Interfacing (ESP32) and AI/ML on Embedded Devices (TinyML)
- 🔬 Former Research Assistant, Autonomous Vehicle Engineering (COMSIP Lab, QAU)
- 🌍 Open to embedded / firmware engineering opportunities worldwide

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Faizan%20Saleem%20Siddiqui-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/faizan-saleem-siddiqui-4411bb247/)
[![GitHub](https://img.shields.io/badge/GitHub-FaizanSSDQ-181717?logo=github&logoColor=white)](https://github.com/FaizanSSDQ)
[![Email](https://img.shields.io/badge/Email-faizansaleemsdq%40yahoo.com-6001D2?logo=yahoo&logoColor=white)](mailto:faizansaleemsdq@yahoo.com)

Licensed under the [MIT License](../../LICENSE) (lab starter material © DeepLearning.AI).
