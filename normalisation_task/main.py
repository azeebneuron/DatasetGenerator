import sys
import os
import json

# Add the project root to the Python path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
sys.path.insert(0, PROJECT_ROOT)  # Add it to the beginning of sys.path

from data_generator import generate_dataset 
if __name__ == "__main__":
    # Generate the dataset
    language = "hi" # Set the language here
    dataset = generate_dataset(language=language)

    # Save the dataset to a JSON file
    with open(f"normalization_dataset_{language}_20k.json", "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=4, ensure_ascii=False)

    print(f"Generated dataset with {len(dataset)} examples for language {language} and saved to normalization_dataset_{language}_20k.json")