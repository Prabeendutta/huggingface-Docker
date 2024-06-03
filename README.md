# Hugging Face Report Generator

This project creates a Docker container that periodically generates a report of the top 10 downloaded models from the Hugging Face model hub and writes the report to a text file.

## Prerequisites

- Podman installed on your system.
- An active internet connection.

## Project Structure

- `Dockerfile`: Defines the Docker image and sets up the environment.
- `generate_report.py`: Python script to fetch data from Hugging Face API and generate a report.
- `report.txt`: Output file where the report will be written.

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/huggingface-report-generator.git
    cd huggingface-report-generator
    ```

2. **Build the Docker Image**:
    ```bash
    podman build -t huggingface-report-generator .
    ```

3. **Run the Docker Container**:
    ```bash
    podman run --name huggingface-report -v $(pwd)/report.txt:/usr/src/app/report.txt huggingface-report-generator
    ```

4. **Check the Report**:
    - After the container finishes running, check the `report.txt` file in the project directory to see the generated report.

## Project Structure

- `Dockerfile`: Defines the Docker image and sets up the environment.
- `generate_report.py`: Python script to fetch data from Hugging Face API and generate a report.
- `report.txt`: Output file where the report will be written.
