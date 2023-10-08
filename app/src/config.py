import json
import os
import logging

# print pwd
print(f"pwd: {os.getcwd()}")
# Read the configuration from the JSON file
config = None
with open("config.json", "r") as config_file:
    config = json.load(config_file)

logging.basicConfig(
    level=getattr(logging, config["logging"]["level"]),
    format=config["logging"]["format"],
    filename=config["logging"]["file"],
    filemode=config["logging"]["file_mode"],
)
