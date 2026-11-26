# Spotify API Data Pipeline Project

> 🎓 Hands-on lab completed during the **DeepLearning.AI & AWS Data Engineering** program on Coursera. Lab environment and starter material by DeepLearning.AI; implementation and write-up by Faizan Saleem Siddiqui.


Welcome to one of my Projects. I am Faizan Saleem Siddiqui, an AI/ML Engineer, specialized in NLP, Computer Version, and Autonomous Vehicles Engineering. You can learn more about me on at my linkedin:4
<br>
https://www.linkedin.com/in/faizan-saleem-siddiqui-4411bb247/



This project demonstrates how to build a **batch data pipeline** using the **Spotify API** to extract and process data about new album releases and their tracks. The pipeline is designed to handle pagination, token refresh, and rate limits, making it a robust solution for working with APIs in real-world data engineering scenarios.

---

## Project Overview

### What is Being Done?
In this project, I:
1. **Interacted with the Spotify API** to fetch data about new album releases and their tracks.
2. Built a **batch data pipeline** that:
   - Retrieves new album releases using the [Get New Releases endpoint](https://developer.spotify.com/documentation/web-api/reference/get-new-releases).
   - Extracts track information for each album using the [Get Album Tracks endpoint](https://developer.spotify.com/documentation/web-api/reference/get-an-albums-tracks).
3. Implemented **pagination** to handle large datasets and ensure all data is retrieved.
4. Added **token refresh functionality** to handle access token expiration during long-running tasks.
5. Managed **API rate limits** to prevent exceeding request quotas and ensure smooth operation.

### Key Features
- **Pagination Handling**: Efficiently retrieves all data, even for large datasets.
- **Token Refresh**: Automatically refreshes the access token to avoid unauthorized requests.
- **Rate Limit Management**: Implements best practices to handle API rate limits.
- **Modular Code Structure**: Organized into reusable scripts (`authentication.py`, `endpoint.py`, `main.py`) for easy maintenance and scalability.

---

## Importance of the Project

### Why is This Project Important?
1. **Real-World API Interaction**:
   - This project provides hands-on experience with API integration, a critical skill in data engineering and software development.
   - It demonstrates how to handle common challenges like pagination, authentication, and rate limiting.

2. **Data Pipeline Development**:
   - The project showcases how to build a scalable and reliable data pipeline, which is essential for processing large volumes of data in production environments.

3. **Industry-Relevant Skills**:
   - Working with APIs and building data pipelines are core competencies in data engineering, making this project highly relevant for professionals in the field.

---

## Industry Implications

### How Does This Project Apply to the Industry?
1. **Music and Entertainment Industry**:
   - This pipeline can be used by music platforms to analyze trends in new album releases, track popularity, and listener preferences.
   - It enables data-driven decision-making for content curation, marketing, and artist promotion.

2. **Data Engineering and Analytics**:
   - The project demonstrates best practices for building ETL (Extract, Transform, Load) pipelines, which are widely used in data engineering.
   - It highlights the importance of handling API limitations (e.g., rate limits, token expiration) in production-grade systems.

3. **Scalability and Automation**:
   - The modular design and token refresh mechanism make the pipeline scalable and suitable for automation in large-scale data processing workflows.

---

## Potential Extensions

### How Can This Project Be Extended?
1. **Data Storage and Analysis**:
   - Store the extracted data in a database (e.g., PostgreSQL, MongoDB) or a data warehouse (e.g., Amazon Redshift, Snowflake) for further analysis.
   - Perform analytics to identify trends, such as the most popular genres or artists.

2. **Real-Time Data Processing**:
   - Extend the pipeline to process data in real-time using streaming technologies like Apache Kafka or AWS Kinesis.

3. **Integration with Other APIs**:
   - Combine data from multiple APIs (e.g., YouTube, Apple Music) to create a comprehensive music analytics platform.

4. **Dashboard and Visualization**:
   - Build a dashboard using tools like Tableau, Power BI, or Dash to visualize insights from the data.

5. **Machine Learning Applications**:
   - Use the data to train machine learning models for tasks like recommendation systems, genre classification, or trend prediction.

---

## Getting Started

### Prerequisites
- Python 3.x
- Spotify Developer Account (to obtain API credentials)
- Required Python libraries: `requests`, `python-dotenv`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/spotify-data-pipeline.git
   ```
2. Install the required dependencies:
   pip install -r requirements.txt

3. Copy `src/env.example` to `src/env` and add your own Spotify API credentials (never commit this file).


## Conclusion
This project provides a practical introduction to building data pipelines using APIs, with a focus on handling real-world challenges like pagination, token refresh, and rate limits. It serves as a foundation for more advanced data engineering projects and demonstrates the importance of robust, scalable solutions in the industry.

Feel free to explore the code, extend the pipeline, and adapt it to your specific use cases!

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
