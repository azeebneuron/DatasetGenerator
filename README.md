# Hindi Text Normalization Data Generation Script

This repository contains a Python script for generating synthetic data for Hindi text normalization. The script creates examples of dates, currencies, and scientific units in various formats, along with their corresponding normalized forms.

## Purpose

This script was created as part of an internship project for building a deep learning-based text normalization model for Indic languages. The generated data is intended to be used for training and evaluating such a model.

## Requirements

*   Python 3.7+
*   The following Python libraries:
    *   scikit-learn
    *   pandas

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <cloned_directory>
    ```

    Replace `<repository_url>` with the actual URL of your repository (e.g., `https://github.com/your_username/hindi-normalization-data-gen.git`) and `<cloned_directory>` with the name of the directory git creates as a result of cloning.

2.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    ```

3.  Activate the virtual environment:

    *   On Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

    *   On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

4.  Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

    Create a `requirements.txt` file with the following content:

    ```
    scikit-learn
    pandas
    datasets
    huggingface_hub
    ```

## Usage

1.  Navigate to the `normalisation_task` directory (or the directory containing `main.py`).

2.  Run the `main.py` script:

    ```bash
    python main.py
    ```

    The script will generate a JSON file (e.g., `hindi_normalization_dataset.json`) containing the synthetic data.

### Customization

You can adjust the following parameters in the `main.py` script:

*   `num_examples`: The total number of examples to generate.
*   `num_date_examples`: The number of date examples to generate.
*   `num_currency_examples`: The number of currency examples to generate.
*   `num_scientific_examples`: The number of scientific unit examples to generate.

You can also modify the context sentences, date formats, currency symbols, and scientific units used by the script to create more diverse and realistic data.

## Output

The script will generate a JSON file containing a list of dictionaries. Each dictionary represents a single example and has the following format:

```json
{
  "input": "Original text with an entity (date, currency, or unit)",
  "output": "Normalized text with the entity converted to Hindi words"
}