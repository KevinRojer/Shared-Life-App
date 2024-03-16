# Flatmate Bill Calculator

## Description

The Flatmate Bill Calculator is a Python application designed to help flatmates split bills based on the number of days each person stayed in the flat. It calculates individual shares of a given bill and generates a detailed PDF report.

## Features

- Calculates bill shares based on individual days stayed in the flat.
- Generates a PDF report outlining the bill period, total amount, and each flatmate's share.
- Configurable report output path and logging via external files.

## Installation

Ensure you have Python 3.6 or later installed on your system. The application also requires the installation of the `FPDF` library for PDF generation and `PyYAML` for configuration management.

```bash
pip install fpdf PyYAML
```

## Features

- Logging: Customize logging settings through config/logging_config.yaml. Adjust log levels, formats, and output destinations as needed.
- Application Settings: Set application-specific configurations such as report output paths in config/app_config.json.

## Run
Run the application by navigating to the project directory and executing:
```bash
python main.py
```

Follow the on-screen prompts to enter the bill period, total amount, and details for each flatmate. Once all information is provided, the application will generate a PDF report in the specified output directory.

