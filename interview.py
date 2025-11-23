"""
interview.py

InterviewBot:
- Picks questions (structured or scraped)
- Asks via voice
- Listens to your answers
- Scores knowledge & confidence
- Analyzes correctness vs keywords
- Gives feedback like a real interviewer
"""

import time
from typing import Dict, Any, List

from voice import JarvisVoice
from fetcher import fetch_questions
from scorer import knowledge_score, confidence_score, analyze_answer
from config import STRUCTURED_QUESTIONS


class InterviewBot:
    """
    Flow:

    1. _init_           -> set career, level, voice, questions
    2. start()            -> orchestrates the full interview
    3. _greet_candidate() -> welcome + instructions
    4. _prepare_questions()-> choose structured or scraped questions
    5. _run_interview_loop()-> loop over all questions
    6. _ask_and_evaluate_question() -> per-question logic
    7. _summarize_results() -> final scoring & feedback
    """

    def _init_(self, career: str, level: str) -> None:
        self.career = career.lower()
        self.level = level.lower()
        self.voice = JarvisVoice()
        self.questions: List[Dict[str, Any]] = self._prepare_questions()
        self.total_knowledge: float = 0.0
        self.total_confidence: float = 0.0

    # ------------------------------------------------------------------
    # PREPARE QUESTIONS
    # ------------------------------------------------------------------
    def _prepare_questions(self) -> List[Dict[str, Any]]:
        """
        Prefer structured questions. If none for this career, fall back to web-scraped ones.
        """

        # Map career string to a structured key
        if "python" in self.career:
            key = "python"
        elif "aiml" in self.career or "ml" in self.career or "machine learning" in self.career:
            key = "aiml"
        elif "dsa" in self.career or "algorithm" in self.career:
            key = "dsa"
        elif "data science" in self.career or "data scientist" in self.career or "datascience" in self.career:
            key = "datascience"
        elif "web" in self.career or "frontend" in self.career or "fullstack" in self.career:
            key = "webdev"
        elif "cyber" in self.career or "security" in self.career:
            key = "cybersecurity"
        elif "hr" in self.career or "fresher" in self.career or "student" in self.career:
            key = "general_hr"
        else:
            key = None

        if key and key in STRUCTURED_QUESTIONS:
            return STRUCTURED_QUESTIONS[key]

        # Fallback: scrape
        fetched = fetch_questions(self.career)
        return [
            {
                "question": q,
                "keywords": None,
                "difficulty": "all",
                "ideal_answer": None,
            }
            for q in fetched
        ]

    # ------------------------------------------------------------------
    # GREETING
    # ------------------------------------------------------------------
    def _greet_candidate(self) -> None:
        """Greet candidate and explain how the interview works."""
        self.voice.speak(f"Hello. We are starting your {self.career} interview.")
        self.voice.speak(f"Difficulty level: {self.level}.")
        self.voice.speak(
            "I will ask you a series of questions. Answer them as if this were a real interview. "
            "After each answer, I will give you feedback on your content and confidence."
        )

    # ------------------------------------------------------------------
    # SINGLE QUESTION FLOW
    # ------------------------------------------------------------------
    def _ask_and_evaluate_question(self, question_dict: Dict[str, Any], index: int) -> None:
        """
        Single question lifecycle:
        - Ask
        - Listen
        - Score
        - Analyze correctness
        - Give feedback
        """

        question_text = question_dict.get("question", "")
        expected_keywords = question_dict.get("keywords")
        ideal_answer = question_dict.get("ideal_answer")

        # Ask
        self.voice.speak(f"Question {index}: {question_text}")
        print(f"\n[Question {index}] {question_text}")

        # Listen
        start_time = time.time()
        answer = self.voice.listen()
        duration = time.time() - start_time

        print(f"[Your answer] {answer}")

        # Score
        ks = knowledge_score(answer)
        cs = confidence_score(answer, duration)

        self.total_knowledge += ks
        self.total_confidence += cs

        # Analyze correctness
        verdict, missing, feedback = analyze_answer(
            answer,
            expected_keywords=expected_keywords,
            ideal_answer=ideal_answer,
        )

        # Interviewer-style reaction
        if verdict == "strong":
            spoken = "Good, that's a strong answer."
        elif verdict == "partial":
            spoken = "That's a decent answer, but there is room to improve."
        elif verdict == "weak":
            spoken = "Not quite. Let me highlight what you should add next time."
        else:  # no_answer
            spoken = "You didn't really answer that. In an interview, always try to say something."

        self.voice.speak(spoken)

        # Detailed feedback in console
        print(f"[Feedback] {feedback}")
        print(f"[Scores] Knowledge: {ks:.1f} / 10, Confidence: {cs:.1f} / 10")

    # ------------------------------------------------------------------
    # QUESTION LOOP
    # ------------------------------------------------------------------
    def _run_interview_loop(self) -> None:
        """Iterate through all questions."""
        for idx, q in enumerate(self.questions, start=1):
            self._ask_and_evaluate_question(q, idx)

    # ------------------------------------------------------------------
    # SUMMARY
    # ------------------------------------------------------------------
    def _summarize_results(self):
        """Compute final score and give a summary like a real interviewer."""
        final_score = (self.total_knowledge * 0.7) + (self.total_confidence * 0.3)

        self.voice.speak("We have finished the interview.")
        self.voice.speak(f"Your final score is {int(final_score)} out of 100.")

        print("\n===== INTERVIEW SUMMARY =====")
        print(f"Total Knowledge Score:  {self.total_knowledge:.2f}")
        print(f"Total Confidence Score: {self.total_confidence:.2f}")
        print(f"Final Score:            {final_score:.2f} / 100")
        print("=============================")

        # Extra verbal verdict
        if final_score >= 75:
            self.voice.speak(
                "Overall, this is a strong performance. You would be a good fit for many junior roles."
            )
        elif final_score >= 50:
            self.voice.speak(
                "You have some good points, but you need more practice to structure your answers "
                "and sound more confident."
            )
        else:
            self.voice.speak(
                "You need to strengthen your fundamentals and practice answering out loud. "
                "Focus on clarity, key concepts, and reducing hesitations."
            )

        return self.total_knowledge, self.total_confidence, final_score

    # ------------------------------------------------------------------
    # PUBLIC ENTRY
    # ------------------------------------------------------------------
    def start(self):
        """
        Main entry:
        1. greet
        2. question loop
        3. summary
        """
        self._greet_candidate()
        self._run_interview_loop()
        return self._summarize_results()