import json
import matplotlib.pyplot as plt
from pathlib import Path


folder = Path(__file__).resolve().parent
file_path = folder / "responses_and_labels.json"

print("Reading from:", file_path)
print("File exists:", file_path.exists())

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

questions = data["questions"]

print("JSON loaded successfully!")
print("Total questions:", len(questions))




correct_count = 0
incorrect_count = 0
partially_correct_count = 0
hallucination_count = 0

for question in questions:
    models = question["model_results"]

    for model, result in models.items():
        label = result["label"]

        if label == "Correct":
            correct_count += 1
        elif label == "Incorrect":
            incorrect_count += 1
        elif label == "Partially Correct":
            partially_correct_count += 1
        elif label == "Hallucinated":
            hallucination_count += 1
        else:
            raise ValueError(f"Unexpected response label: {label}")

total_responses = (
    correct_count
    + incorrect_count
    + partially_correct_count
    + hallucination_count
)

print("\nOverall Response Results")
print("Correct responses:", correct_count)
print("Incorrect responses:", incorrect_count)
print("Partially correct responses:", partially_correct_count)
print("Hallucinated responses:", hallucination_count)
print("Total responses:", total_responses)


# Calculate classification percentages
correct_percentage = (correct_count / total_responses) * 100
incorrect_percentage = (incorrect_count / total_responses) * 100
partially_correct_percentage = (
    partially_correct_count / total_responses
) * 100
hallucination_percentage = (
    hallucination_count / total_responses
) * 100

print(f"\nCorrect responses: {correct_percentage:.2f}%")
print(f"Incorrect responses: {incorrect_percentage:.2f}%")
print(f"Partially correct responses: {partially_correct_percentage:.2f}%")
print(f"Hallucinated responses: {hallucination_percentage:.2f}%")


#graph 1: Overall Response Classification Results

labels = [
    "Correct",
    "Partially Correct",
    "Incorrect",
    "Hallucinated"
]

percentages = [
    correct_percentage,
    partially_correct_percentage,
    incorrect_percentage,
    hallucination_percentage
]

plt.figure(figsize=(10, 6))

plt.bar(labels, percentages)
plt.title("Overall Response Classification Results")
plt.xlabel("Response Classification")
plt.ylabel("Percentage of Responses (%)")
plt.ylim(0, 100)

for index, percentage in enumerate(percentages):
    plt.text(
        index,
        percentage + 1,
        f"{percentage:.2f}%",
        ha="center"
    )

plt.tight_layout()
plt.savefig("overall_response_results.png", dpi=300)
plt.show()



topic_counts = {
    "Python": 0,
    "C++": 0,
    "Algorithms": 0
}

topic_totals = {
    "Python": 0,
    "C++": 0,
    "Algorithms": 0
}

for question in questions:
    question_id = question["question_id"]

    if question_id.startswith("PY"):
        topic = "Python"
    elif question_id.startswith("CPP"):
        topic = "C++"
    elif question_id.startswith("ALG"):
        topic = "Algorithms"
    else:
        raise ValueError(f"Unknown question topic: {question_id}")

    models = question["model_results"]

    for model, result in models.items():
        topic_totals[topic] += 1

        if result["label"] == "Correct":
            topic_counts[topic] += 1

topics = ["Python", "C++", "Algorithms"]

correct_topic_percentages = []

print("\nResults by Programming Topic")

for topic in topics:
    correct = topic_counts[topic]
    total = topic_totals[topic]

    percentage = (correct / total) * 100
    correct_topic_percentages.append(percentage)

    print(f"{topic}: {correct}/{total} Correct ({percentage:.2f}%)")


#graph 2: Correct Responses by Programming Topic

plt.figure(figsize=(9, 6))

plt.bar(topics, correct_topic_percentages)
plt.title("Correct Responses by Programming Topic")
plt.xlabel("Programming Topic")
plt.ylabel("Correct Responses (%)")
plt.ylim(0, 100)

for index, percentage in enumerate(correct_topic_percentages):
    plt.text(
        index,
        percentage + 1,
        f"{percentage:.2f}%",
        ha="center"
    )

plt.tight_layout()
plt.savefig("topic_response_results.png", dpi=300)
plt.show()



difficulty_counts = {
    "Easy": 0,
    "Medium": 0,
    "Hard": 0
}

difficulty_totals = {
    "Easy": 0,
    "Medium": 0,
    "Hard": 0
}

for question in questions:
    difficulty = question["difficulty"]
    models = question["model_results"]

    for model, result in models.items():
        difficulty_totals[difficulty] += 1

        if result["label"] == "Correct":
            difficulty_counts[difficulty] += 1

difficulties = ["Easy", "Medium", "Hard"]
difficulty_percentages = []

print("\nResults by Question Difficulty")

for difficulty in difficulties:
    correct = difficulty_counts[difficulty]
    total = difficulty_totals[difficulty]

    percentage = (correct / total) * 100
    difficulty_percentages.append(percentage)

    print(f"\nDifficulty: {difficulty}")
    print(f"Correct responses: {correct}")
    print(f"Total responses: {total}")
    print(f"Correct response percentage: {percentage:.2f}%")


#graph 3: Correct Responses by Question Difficulty

plt.figure(figsize=(9, 6))

plt.bar(difficulties, difficulty_percentages)
plt.title("Correct Responses by Question Difficulty")
plt.xlabel("Question Difficulty")
plt.ylabel("Correct Responses (%)")
plt.ylim(0, 105)

for index, percentage in enumerate(difficulty_percentages):
    plt.text(
        index,
        percentage + 1,
        f"{percentage:.2f}%",
        ha="center"
    )

plt.tight_layout()
plt.savefig("difficulty_response_results.png", dpi=300)
plt.show()


model_counts = {}

labels = [
    "Correct",
    "Partially Correct",
    "Incorrect",
    "Hallucinated",
    "Cannot Determine"
]

for question in questions:
    models = question["model_results"]

    for model, result in models.items():

        if model not in model_counts:
            model_counts[model] = {
                "Correct": 0,
                "Partially Correct": 0,
                "Incorrect": 0,
                "Hallucinated": 0,
                "Cannot Determine": 0
            }

        label = result["label"]
        model_counts[model][label] += 1



for model, counts in model_counts.items():

    total = sum(counts.values())

    print(f"\nResults for {model}")
    print(f"Total responses: {total}")

    for label in labels:
        count = counts[label]
        percentage = (count / total) * 100

        print(f"{label}: {count} ({percentage:.2f}%)")


#graphs for each model

for model, counts in model_counts.items():

    total = sum(counts.values())

    percentages = [
        (counts[label] / total) * 100
        for label in labels
    ]

    plt.figure(figsize=(10, 6))

    plt.bar(labels, percentages)

    plt.title(f"Response Classification Results: {model}")
    plt.xlabel("Response Classification")
    plt.ylabel("Percentage of Responses (%)")
    plt.ylim(0, 105)
    plt.xticks(rotation=15)

    for index, percentage in enumerate(percentages):
        if percentage > 0:
            plt.text(
                index,
                percentage + 1,
                f"{percentage:.2f}%",
                ha="center"
            )

    plt.tight_layout()


    filename = "".join(
        character if character.isalnum() else "_"
        for character in model
    )

    plt.savefig(f"{filename}_results.png", dpi=300)

    plt.show()