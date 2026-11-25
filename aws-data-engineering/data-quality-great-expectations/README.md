# Automated Data Validation with Great Expectations on AWS

> 🎓 Hands-on lab completed during the **DeepLearning.AI & AWS Data Engineering** program on Coursera. Lab environment and starter material by DeepLearning.AI; implementation and write-up by Faizan Saleem Siddiqui.


This project demonstrates the implementation of automated data validation using Great Expectations on AWS, ensuring data quality and reliability in a production environment.

## Project Description

This project focuses on automating data validation processes by leveraging Great Expectations to create and manage expectation suites and checkpoints. It emphasizes the importance of moving from manual validation to an automated, scalable approach suitable for production environments. The project also showcases how to configure Data Docs storage on AWS S3, ensuring proper documentation and artifact management.

## Key Features

* **Automated Data Validation:** Implementation of Checkpoint objects to automate data validation against stored expectation suites.
* **Modular Expectation Suites:** Creation of reusable expectation suites that can be applied across different data batches.
* **AWS S3 Integration:** Configuration of Data Docs storage on AWS S3 for secure and accessible documentation.
* **Batch Request Management:** Creation and management of batch requests for efficient data processing.
* **Production-Ready Validation:** Transition from manual to automated validation, suitable for production environments.
* **Workflow Flexibility:** Implementation of a data quality pipeline that can be triggered based on various events or schedules.

## Getting Started

1.  **Prerequisites:**
    * An AWS account with appropriate permissions.
    * Python 3.x installed.
    * Great Expectations library installed.
    * AWS CLI configured.

2.  **Clone the Repository:**

    ```bash
    git clone [repository URL]
    cd [repository directory]
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Great Expectations:**
    * Modify the `great_expectations.yml` file to configure your data source and Data Docs storage on S3.
    * Replace the placeholder `<GX-DOCS-BUCKET>` with your actual S3 bucket name.

5.  **Create Batch Requests and Validations List:**
    * Follow the instructions in the Jupyter Notebook to create batch requests and validations list.

6.  **Run Checkpoints:**
    * Execute the Checkpoint objects to validate data against expectation suites.

7.  **View Data Docs:**
    * Access the generated Data Docs in the configured S3 bucket.

## Architecture

The architecture includes:

* Great Expectations for data validation.
* AWS S3 for storing Data Docs.
* Jupyter Notebooks for project implementation.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any improvements or bug fixes.

## License

This repository is licensed under the MIT License - see the LICENSE file for details

## Conclusion

This project provides a practical example of how to implement automated data validation using Great Expectations on AWS. By leveraging reusable expectation suites and Checkpoint objects, we can ensure data quality and reliability in a production environment. The integration with AWS S3 for Data Docs storage enhances documentation and artifact management, making this project a valuable resource for data engineering teams.

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
