import requests
import json
import time

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from Hugging Face API: {response.status_code}")
    models = response.json()
    sorted_models = sorted(models, key=lambda x: x.get("downloads", 0), reverse=True)
    top_10_models = sorted_models[:10]
    return top_10_models

def generate_report():
    top_10_models = fetch_top_models()
    report = "Top 10 Hugging Face Models by Downloads:\n"
    report += "="*40 + "\n"
    for model in top_10_models:
        report += f"Model: {model['modelId']}\n"
        report += f"Downloads: {model['downloads']}\n"
        report += "-"*40 + "\n"
    with open("report.txt", "w") as file:
        file.write(report)
    print("Report generated successfully.")

if __name__ == "__main__":
    while True:
        generate_report()
        time.sleep(86400)  # Wait for 24 hours (86400 seconds)
