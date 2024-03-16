import os
import json
import logging.config
import yaml
from views import feedback, messages
from models.bill import Bill
from models.flatmate import Flatmate
from models.report import ReportGenerator


def load_config():
    with open("./config/app_config.json", "r") as config_file:
        return json.load(config_file)
    

def setup_logging(default_path='./config/logging_config.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
    """Setup logging configuration

    Args:
        default_path (str): Default path to the logging configuration file.
        default_level (logging.LEVEL): Default logging level.
        env_key (str): Environment variable key for the logging configuration file.
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def main():
    # Load application configurations
    config = load_config()

    # Load the logging configuration 
    setup_logging(default_path=config["logging"]["config_path"])
    logger = logging.getLogger(__name__)

    # Start the application
    logger.info("Application started.")
    feedback.show_message(messages.welcome_message)

    period = feedback.input_with_prompt(messages.bill_period)
    total_amount = float(feedback.input_with_prompt(messages.bill_amount))
    bill = Bill(total_amount, period)

    flatmates = []
    while True:
        feedback.show_message(messages.exit_option)
        name = feedback.input_with_prompt(messages.flatmate_name)

        if name.lower() == "exit":
            break
        
        days_in_house = int(feedback.input_with_prompt(f"Enter the number of days {name} stayed: "))
        flatmates.append(Flatmate(name, days_in_house))

    report_filename = config["report"]["filename"]
    report_pathname = config["report"]["output_path"] + report_filename
    report = ReportGenerator(report_pathname)
    report.generate_pdf(flatmates, bill)

    logger.info(f"Report generated at {report_pathname}")
    feedback.show_message(f"Report Generated: {report_filename}")

if __name__ == "__main__":
    main()