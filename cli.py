"""
cli.py

Simple CLI entry point for the InterviewBot.
"""

from interview import InterviewBot


def main() -> None:
    print("=== AI Interview Bot (CLI) ===")
    career = input("Enter Career (e.g. Python Developer, AIML, DSA, Data Science, Web Dev, Cybersecurity): ")
    level = input("Enter Difficulty (Fresher / Intermediate / Professional): ")

    bot = InterviewBot(career, level)
    knowledge, confidence, final = bot.start()

    print("\n===== FINAL SUMMARY (CLI) =====")
    print(f"Knowledge Score:  {knowledge:.2f}")
    print(f"Confidence Score: {confidence:.2f}")
    print(f"Final Score:      {final:.2f} / 100")
    print("===============================")


if __name__ == "_main_":
    main()