import datetime
import random
import locale
from number_converter import IndicNumberConverter  # Relative import

def generate_date_examples(num_examples, number_converter, language_config):
    """Generates date examples in various formats."""
    locale_str = language_config["locale"]
    try:
        locale.setlocale(locale.LC_ALL, locale_str + '.UTF-8')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, locale_str)
        except locale.Error:
            print(f"Warning: Locale {locale_str} not supported.  Using default locale.")
            locale_str = '' # Use the default locale instead

    formats = language_config["formats"]
    month_names_hindi = language_config["month_names"]

    contexts = language_config["date_contexts"]

    examples = []
    for _ in range(num_examples):
        year = random.randint(1900, 2024)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(0,23)
        minute = random.randint(0, 59)
        second = random.randint(0,59)

        date_obj = datetime.date(year, month, day)
        time_obj = datetime.time(hour, minute, second)

        date_format = random.choice(formats)
        input_date = date_obj.strftime(date_format)

        month_name = date_obj.strftime("%B") if locale_str else date_obj.strftime("%B") #Use english if locale fails
        year_str = number_converter.convert_to_words(year)
        day_str = number_converter.convert_to_words(day)

        normalized_date = f"{day_str} {month_names_hindi.get(month_name, month_name)} {year_str}" # Month Mapping

        context = random.choice(contexts)
        normalized_context = context.replace("{input_date}", normalized_date) # Correct Replacement

        examples.append({"input": context.replace("{input_date}", input_date), "output": normalized_context}) #Correct replacement

    return examples

def generate_currency_examples(num_examples, number_converter, language_config):
    """Generates currency examples."""
    currencies = {
        "USD": ["$", "USD"],
        "EUR": ["€", "EUR"],
        "GBP": ["£", "GBP"],
        "INR": ["Rs.", "INR", "₹"],
        "JPY": ["¥", "JPY"]
    }

    currency_names_hindi = language_config["currency_names"]
    contexts = language_config["currency_contexts"]

    examples = []
    for _ in range(num_examples):
        currency_code = random.choice(list(currencies.keys()))
        currency_symbols = currencies[currency_code]
        symbol = random.choice(currency_symbols)
        amount = round(random.uniform(1, 10000), 2)

        formats = [
            f"{symbol}{amount}",
            f"{symbol} {amount}",
            f"{amount}{symbol}",
            f"{amount} {symbol}",
            f"{currency_code} {amount}",
            f"{amount} {currency_code}"
        ]
        input_currency = random.choice(formats)

        amount_words = number_converter.convert_to_words(amount)
        normalized_currency = f"{amount_words} {currency_names_hindi.get(currency_code, currency_code)}" 
        context = random.choice(contexts)
        normalized_context = context.replace("{input_currency}", normalized_currency) #Correct replacement

        examples.append({"input": context.replace("{input_currency}", input_currency), "output": normalized_context})

    return examples

def generate_scientific_unit_examples(num_examples, number_converter, language_config):
    """Generates scientific unit examples."""
    units = {
        "length": ["m", "cm", "mm", "km"],
        "mass": ["g", "kg", "mg"],
        "volume": ["L", "mL"],
        "temperature": ["°C", "°F", "K"]
    }

    unit_names_hindi = language_config["scientific_units"]

    contexts = language_config["scientific_unit_contexts"]

    examples = []
    for _ in range(num_examples):
        unit_type = random.choice(list(units.keys()))
        unit = random.choice(units[unit_type])
        value = round(random.uniform(0.1, 100), 2)

        formats = [
            f"{value}{unit}",
            f"{value} {unit}",
            f"{unit}{value}", #Rare, but possible
            f"{unit} {value}"  #Rare, but possible
        ]
        input_unit = random.choice(formats)

        value_words = number_converter.convert_to_words(value)
        #normalized_unit = f"{value_words} {unit}" # Old
        normalized_unit = f"{value_words} {unit_names_hindi.get(unit, unit)}" #New

        context = random.choice(contexts)
        normalized_context = context.replace("{input_unit}", normalized_unit) # Correct replacement

        examples.append({"input": context.replace("{input_unit}", input_unit), "output": normalized_context})

    return examples

def generate_dataset(num_examples=20000, language="hi"):
    """Generates the complete dataset for a given language."""
    from language_config import get_language_config  
    language_config = get_language_config(language)
    number_converter = IndicNumberConverter(language=language)

    num_date_examples = int(num_examples * 0.35)
    num_currency_examples = int(num_examples * 0.35)
    num_scientific_examples = int(num_examples * 0.30)

    date_examples = generate_date_examples(num_date_examples, number_converter, language_config)
    currency_examples = generate_currency_examples(num_currency_examples, number_converter, language_config)
    scientific_examples = generate_scientific_unit_examples(num_scientific_examples, number_converter, language_config)

    dataset = date_examples + currency_examples + scientific_examples
    random.shuffle(dataset)

    return dataset