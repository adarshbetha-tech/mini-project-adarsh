import time
import random
from datetime import datetime

# List of sentences to choose from
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Python makes programming fun and simple",
    "Typing speed increases with regular practice",
    "Artificial intelligence is the future of technology",
    "Discipline and consistency lead to success",
    "Learning new skills improves confidence",
    "Hard work beats talent when talent doesn't work hard",
    "Stay positive and keep pushing forward",
    "Every expert was once a beginner",
    "Focus on progress not perfection"
]

print("===== Typing Speed Tester =====")
print("You will be given 3 random sentences to type.\n")
input("Press Enter to begin...")

# Pick 3 random sentences without repeating
selected_sentences = random.sample(sentences, 3)

total_wpm = 0
total_accuracy = 0

for i, test_sentence in enumerate(selected_sentences, start=1):
    print(f"\nSentence {i}:\n")
    print(test_sentence)
    print()
    
    start_time = time.time()
    typed_sentence = input("Type here:\n")
    end_time = time.time()
    
    time_taken = round(end_time - start_time, 2)
    
    # Calculate accuracy
    correct_chars = sum(1 for a, b in zip(test_sentence, typed_sentence) if a == b)
    accuracy = (correct_chars / len(test_sentence)) * 100
    accuracy = round(accuracy, 2)
    
    # Calculate WPM
    words = len(typed_sentence.split())
    wpm = round((words / time_taken) * 60)
    
    print(f"\nResult for Sentence {i}:")
    print(f"Time: {time_taken} sec | WPM: {wpm} | Accuracy: {accuracy}%")
    
    total_wpm += wpm
    total_accuracy += accuracy

# Average results
avg_wpm = round(total_wpm / 3)
avg_accuracy = round(total_accuracy / 3)

print("\n===== Final Results =====")
print(f"Average Speed: {avg_wpm} WPM")
print(f"Average Accuracy: {avg_accuracy}%")

if avg_accuracy > 90:
    message = "Excellent typing! Very accurate and fast. 💪"
elif avg_accuracy > 70:
    message = "Good job! Keep practicing to reach perfection. 👍"
else:
    message = "Keep trying! Practice will make you faster and more accurate. 💻"

print(message)

# === Save Results to File ===
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("typing_results.txt", "a") as file:
    file.write(f"\nDate & Time: {timestamp}\n")
    file.write(f"Average Speed: {avg_wpm} WPM\n")
    file.write(f"Average Accuracy: {avg_accuracy}%\n")
    file.write(f"Feedback: {message}\n")
    file.write("-" * 40 + "\n")

print("\nYour results have been saved in 'typing_results.txt' ✅")
