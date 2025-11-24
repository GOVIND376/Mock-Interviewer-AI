"""
scorer.py

Scoring and analysis utilities:
- knowledge_score
- confidence_score
- analyze_answer (checks against expected keywords)
"""

from typing import List, Optional, Tuple
from config import HESITATION_WORDS


def knowledge_score(answer: str) -> float:
    """
    Basic knowledge score:
    - longer answers score higher (up to 10)
    - more 'keyword-like' words (length > 4) score higher (up to 10)
    - 'don't know' gives a penalty
    """
    if not answer.strip():
        return 0.0

    words = answer.split()
    length_score = min(len(words) / 5, 10)  # +1 per 5 words, cap at 10

    keywords = [w for w in words if len(w) > 4]
    keyword_score = min(len(keywords), 10)

    clarity_penalty = -5 if "don't know" in answer.lower() else 0

    return max(0.0, length_score + keyword_score + clarity_penalty)


def confidence_score(answer: str, duration: float) -> float:
    """
    Confidence score:
    - penalizes hesitation words
    - penalizes speaking too slow or too fast
    """
    answer_lower = answer.lower()
    hesitations = sum(answer_lower.count(w) for w in HESITATION_WORDS)
    pace = len(answer.split()) / max(duration, 1.0)  # words per second

    score = 10 - hesitations

    if pace < 0.5:
        score -= 3  # too slow
    elif pace > 3:
        score -= 2  # too fast

    return max(0.0, min(score, 10.0))


def analyze_answer(
    answer: str,
    expected_keywords: Optional[List[str]] = None,
    ideal_answer: Optional[str] = None,
) -> Tuple[str, List[str], str]:
    """
    Compare the answer content with expected keywords and produce feedback.

    Returns:
        verdict: 'strong', 'partial', 'weak', or 'no_answer'
        missing_keywords: list[str]
        feedback_text: str
    """
    answer_clean = answer.strip()
    if not answer_clean:
        return "no_answer", [], (
            "You didn't give an answer. In an interview, always try to say something, "
            "even if it's not perfect."
        )

    if expected_keywords:
        lower_ans = answer_clean.lower()
        matched = [k for k in expected_keywords if k.lower() in lower_ans]
        missing = [k for k in expected_keywords if k.lower() not in lower_ans]

        coverage = len(matched) / len(expected_keywords) if expected_keywords else 0.0

        if coverage >= 0.7:
            verdict = "strong"
        elif coverage >= 0.4:
            verdict = "partial"
        else:
            verdict = "weak"

        feedback_parts = []

        if verdict == "strong":
            feedback_parts.append("Good answer. You covered most of the important points.")
        elif verdict == "partial":
            feedback_parts.append("Decent answer, but you missed a few important points.")
        else:
            feedback_parts.append(
                "Your answer is missing several key ideas the interviewer expects."
            )

        if missing:
            feedback_parts.append("You could also mention: " + ", ".join(missing) + ".")

        if ideal_answer:
            feedback_parts.append("A concise way to answer is: " + ideal_answer)

        feedback = " ".join(feedback_parts)
        return verdict, missing, feedback

    # No structured expectations
    feedback = (
        "Thanks for your answer. I don't have a strict checklist for this question, "
        "but try to be clear, structured, and give concrete examples."
    )
    return "partial", [], feedback