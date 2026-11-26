# **Real-Time Data Ingestion with Amazon Kinesis Data Streams**  

> 🎓 Hands-on lab completed during the **DeepLearning.AI & AWS Data Engineering** program on Coursera. Lab environment and starter material by DeepLearning.AI; implementation and write-up by Faizan Saleem Siddiqui.


## **Overview**  
This project focuses on **real-time data ingestion** using **Amazon Kinesis Data Streams**. The goal is to build a streaming data pipeline that efficiently collects, processes, and routes data in real time.  

The project consists of two main parts:  

1. **Streaming Data Pipeline**  
   - Set up a **Kinesis Data Stream** to act as an intermediary between a **producer** (data generator) and a **consumer** (data processor).  
   - Manually generate and write data to the Kinesis stream using a producer application.  
   - Retrieve and process the streamed data using a consumer application.  

2. **Streaming ETL Process**  
   - Consume raw data from a **Kinesis stream** and apply transformations.  
   - Route the transformed data into two separate **Kinesis Data Streams**.  
   - Process and deliver the transformed data to **Amazon S3** using **Kinesis Firehose**, making it available for further analytics and storage.  

---

## **Technologies Used**  
- 🟢 **Amazon Kinesis Data Streams**  
- 🟢 **Amazon Kinesis Firehose**  
- 🟢 **Amazon S3**  
- 🟢 **Python (`boto3` SDK)**  
- 🟢 **AWS CLI**  

---

## **Project Structure**  
```plaintext
📂 Real-Time-Data-Ingestion  
│── 📜 README.md              # Project documentation  
│── 📂 src                    # Source code  
│   ├── producer.py           # Data producer script  
│   ├── consumer.py           # Data consumer script  
│   ├── etl_process.py        # Streaming ETL script  
│── 📂 data                   # Sample data files  
│── 📂 docs                   # Project documentation and reports  

```

## **Prerequisites**
Before starting the project, ensure that you have:
✔️ An AWS account with permissions to create and manage Kinesis Data Streams and S3 buckets.
✔️ AWS CLI installed and configured.
✔️ Python 3.x installed with the boto3 library.


## **Expected Outcomes**
✅ A working real-time data ingestion pipeline with Amazon Kinesis.
✅ Successfully streamed and processed data stored in Amazon S3.
✅ Hands-on experience with AWS Kinesis Firehose and ETL transformations in streaming data.

## **License**
📜 This project is licensed under the MIT License – feel free to modify and use it for your own projects.

Acknowledgments
📌 AWS Kinesis Documentation: Amazon Kinesis[https://aws.amazon.com/kinesis/]
📌 Python SDK for AWS: boto3 Documentation[https://docs.aws.amazon.com/pythonsdk/]

### **Improvements:**  
- Used **bold headers** (`## **Header**`) for better readability.  
- Used **emojis** for enhanced visual appeal.  
- Used proper **code blocks** (`bash` and `plaintext`) for clarity.  
- Improved **step-by-step formatting** for easy navigation.  



---

## **Conclusion**  
This project provided hands-on experience with **real-time data ingestion** using **Amazon Kinesis Data Streams**. By implementing a **streaming pipeline**, we explored how data flows from producers to consumers, applied transformations in a **Streaming ETL process**, and delivered processed data to **Amazon S3** using **Kinesis Firehose**.  

Through this lab, we gained a deeper understanding of **event-driven architectures**, **stream processing**, and the practical applications of **AWS cloud services** in handling high-velocity data. This knowledge can be leveraged for **real-time analytics**, **IoT applications**, **log processing**, and **other big data use cases**.  

🚀 **Next Steps**: You can further enhance this project by integrating **AWS Lambda** for serverless processing, incorporating **Amazon OpenSearch Service** for real-time search analytics, or exploring **AWS Glue** for additional ETL capabilities.  

Happy coding! 🎯

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
