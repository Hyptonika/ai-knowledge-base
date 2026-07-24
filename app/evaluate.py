from app.search import search
from data.eval_set import eval_questions

def run_evaluation():
    correct = 0
    total = len(eval_questions)

    for item in eval_questions:
        question = item["question"]
        keywords = item["expected_keywords"]

        results = search(question, top_k=2)
        combined_text = " ".join([text for score, text in results]).lower()

        found = any(keyword.lower() in combined_text for keyword in keywords)

        status = "✅" if found else "❌"
        print(f"{status} {question}")

        if found:
            correct += 1

    accuracy = (correct / total) * 100
    print(f"\nAccuracy: {correct}/{total} ({accuracy:.1f}%)")

if __name__ == "__main__":
    run_evaluation()