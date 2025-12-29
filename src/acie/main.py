#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from acie.crew import Acie

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    print("Welcome to the Autonomous Competitive Intelligence Engine (ACIE)")
    print("---------------------------------------------------------------")
   # topic = input("Enter the company name or URL to research: ")

    inputs = {
        'topic': "Matrixhive Technologies PVT LTD",
        'current_year': str(datetime.now().year)
    }

    try:
        result = Acie().crew().kickoff(inputs=inputs)
        # Print the result
        print("\n\n=== FINAL REPORT ===\n\n")
        print(result.raw)

        print("\n\nReport has been saved to output/report.md")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()
