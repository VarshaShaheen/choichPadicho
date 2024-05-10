import json


# Load questions from the file
def load_questions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


# Function to classify the response and fetch corresponding questions
def classify_and_fetch(response, questions_dict):
    keywords = {
        "asexual_reproduction": ["asexual", "binary fission", "budding", "regeneration", "fragmentation"],
        "sexual_reproduction_in_plants": ["pollination", "flowering plants", "seeds"],
        "reproduction_in_human_beings": ["fertilization", "hormones", "human reproduction"]
    }

    # Determine the class based on keywords
    for category, key_list in keywords.items():
        if any(key in response.lower() for key in key_list):
            print(f"Classified as: {category}")
            return questions_dict.get(category, ["No questions found"])

    print("No classification matched.")
    return ["No questions found"]


# Example usage within the script for testing
if __name__ == "__main__":
    questions_dict = load_questions("previous_questions.json")
    sample_response = "Flowering plants reproduce through the process of seed formation."
    related_questions = classify_and_fetch(sample_response, questions_dict)
    print("Related questions:", related_questions)
