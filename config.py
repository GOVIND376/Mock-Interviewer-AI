"""
config.py

Global configuration for the AI Interview Bot project.

This file centralizes:
- HTTP / scraping settings
- Voice (TTS) configuration
- Scoring-related constants
- Structured question banks for different careers / domains
"""

# ---------------------------------------------------------------------------
# HTTP / SCRAPING SETTINGS
# ---------------------------------------------------------------------------

# User-Agent string used when scraping interview questions from websites
USER_AGENT: str = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

# ---------------------------------------------------------------------------
# DEFAULT QUESTIONS (FALLBACK)
# ---------------------------------------------------------------------------

# Generic HR-style questions used if scraping or structured banks are unavailable
DEFAULT_QUESTIONS = [
    "Tell me about yourself.",
    "What are your strengths?",
    "What are your weaknesses?",
    "Why should we hire you?",
    "Where do you see yourself in 5 years?",
]

# ---------------------------------------------------------------------------
# VOICE / TTS SETTINGS
# ---------------------------------------------------------------------------

# Text-to-speech speed
TTS_RATE: int = 165

# Text-to-speech volume (0.0 to 1.0)
TTS_VOLUME: float = 1.0

# ---------------------------------------------------------------------------
# SCORING CONSTANTS
# ---------------------------------------------------------------------------

# Words considered as “hesitation” markers for confidence scoring
HESITATION_WORDS = ["um", "uh", "hmm", "maybe", "i think"]

# Conceptual maximum scores (used for normalization / interpretation)
MAX_KNOWLEDGE_SCORE: int = 10
MAX_CONFIDENCE_SCORE: int = 10

# ---------------------------------------------------------------------------
# STRUCTURED QUESTION BANK
# ---------------------------------------------------------------------------

STRUCTURED_QUESTIONS = {
    # -------------------------------------------------------------------
    # PYTHON (BEGINNER–INTERMEDIATE)
    # -------------------------------------------------------------------
    "python": [
        {
            "question": "What is a list in Python and how is it different from a tuple?",
            "keywords": ["list", "mutable", "tuple", "immutable", "square brackets", "parentheses"],
            "ideal_answer": (
                "A list is an ordered, mutable collection defined with square brackets []. "
                "A tuple is also ordered but immutable and defined using parentheses (). "
                "You can change, add, or remove elements in a list, but not in a tuple."
            ),
            "difficulty": "fresher",
        },
        {
            "question": "Explain what a dictionary is in Python.",
            "keywords": ["key", "value", "mapping", "curly braces"],
            "ideal_answer": (
                "A dictionary is a key–value mapping in Python. "
                "You access values using keys instead of indexes, and it is defined using curly braces "
                "with key: value pairs."
            ),
            "difficulty": "fresher",
        },
        {
            "question": "What is a virtual environment in Python and why do we use it?",
            "keywords": ["isolation", "dependencies", "project", "packages", "environment"],
            "ideal_answer": (
                "A virtual environment is an isolated Python environment for a project. "
                "It keeps that project's dependencies separate from the global Python installation, "
                "so different projects can use different package versions without conflicts."
            ),
            "difficulty": "intermediate",
        },
    ],

    # -------------------------------------------------------------------
    # GENERAL HR / FRESHER BEHAVIORAL
    # -------------------------------------------------------------------
    "general_hr": [
        {
            "question": "Tell me about yourself.",
            "keywords": ["background", "skills", "experience", "role"],
            "ideal_answer": (
                "A strong answer briefly covers your background, your key skills, "
                "and how they relate to the job you are applying for."
            ),
            "difficulty": "all",
        },
        {
            "question": "What are your strengths?",
            "keywords": ["strength", "strong", "example"],
            "ideal_answer": (
                "Mention 2–3 relevant strengths and support each with a concrete example "
                "from your projects, studies, or previous experience."
            ),
            "difficulty": "all",
        },
        {
            "question": "What are your weaknesses?",
            "keywords": ["weakness", "improve", "learning", "self-awareness"],
            "ideal_answer": (
                "Mention a real but not critical weakness and explain what you are doing to improve it. "
                "This shows honesty and a growth mindset."
            ),
            "difficulty": "all",
        },
    ],

    # -------------------------------------------------------------------
    # AIML BASICS
    # -------------------------------------------------------------------
    "aiml": [
        {
            "question": "What is supervised learning?",
            "keywords": ["labeled data", "training", "prediction", "classification", "regression"],
            "ideal_answer": (
                "Supervised learning uses labeled data to train a model to make predictions. "
                "It is commonly used for classification and regression tasks."
            ),
            "difficulty": "fresher",
        },
        {
            "question": "What is unsupervised learning?",
            "keywords": ["unlabeled data", "patterns", "clustering", "groups"],
            "ideal_answer": (
                "Unsupervised learning uses unlabeled data to discover patterns or groupings, "
                "such as clustering similar data points together."
            ),
            "difficulty": "fresher",
        },
        {
            "question": "What is overfitting in machine learning?",
            "keywords": ["memorizing", "training data", "poor generalization", "high variance"],
            "ideal_answer": (
                "Overfitting occurs when a model learns the training data too well, including noise, "
                "and performs poorly on unseen data due to poor generalization."
            ),
            "difficulty": "intermediate",
        },
        {
            "question": "What is the difference between classification and regression?",
            "keywords": ["discrete", "continuous", "output", "labels", "values"],
            "ideal_answer": (
                "Classification predicts discrete labels or classes, while regression predicts continuous "
                "numeric values such as prices or temperatures."
            ),
            "difficulty": "fresher",
        },
    ],

    # -------------------------------------------------------------------
    # DSA & ALGORITHMS
    # -------------------------------------------------------------------
    "dsa": [
        {
            "question": "What is the difference between an array and a linked list?",
            "keywords": ["contiguous", "memory", "dynamic", "nodes", "pointers", "indexing"],
            "ideal_answer": (
                "Arrays store elements in contiguous memory and support fast random indexing. "
                "Linked lists store nodes connected by pointers, making insertions and deletions easier "
                "but with slower random access."
            ),
            "difficulty": "fresher",
        },
        {
            "question": "What is the time complexity of binary search and when can you use it?",
            "keywords": ["O(log n)", "sorted", "divide", "half"],
            "ideal_answer": (
                "Binary search has a time complexity of O(log n) and can be used on sorted collections. "
                "It repeatedly divides the search range in half to find the target."
            ),
            "difficulty": "fresher",
        },
        {
            "question": "Explain what a stack is and give a real-world example.",
            "keywords": ["LIFO", "push", "pop", "top"],
            "ideal_answer": (
                "A stack is a LIFO (last in, first out) data structure where elements are added and removed "
                "from the top using push and pop operations. A real-world example is a stack of plates."
            ),
            "difficulty": "fresher",
        },
        {
            "question": "What is a queue and how is it different from a stack?",
            "keywords": ["FIFO", "enqueue", "dequeue", "order"],
            "ideal_answer": (
                "A queue is a FIFO (first in, first out) data structure where elements are added at the back "
                "and removed from the front. Unlike a stack, the first inserted element is the first removed."
            ),
            "difficulty": "fresher",
        },
    ],

    # -------------------------------------------------------------------
    # DATA SCIENCE
    # -------------------------------------------------------------------
    "datascience": [
        {
            "question": "What is the difference between correlation and causation?",
            "keywords": ["relationship", "association", "cause", "effect"],
            "ideal_answer": (
                "Correlation indicates that two variables move together, while causation means one variable "
                "directly influences or causes changes in the other."
            ),
            "difficulty": "fresher",
        },
        {
            "question": "What is feature scaling and why is it important?",
            "keywords": ["normalization", "standardization", "range", "gradient descent"],
            "ideal_answer": (
                "Feature scaling transforms features to a similar range using normalization or standardization. "
                "It helps many algorithms, especially those using gradient descent, converge faster and "
                "prevents features with large scales from dominating the model."
            ),
            "difficulty": "intermediate",
        },
        {
            "question": "What is a confusion matrix?",
            "keywords": ["true positive", "true negative", "false positive", "false negative"],
            "ideal_answer": (
                "A confusion matrix is a table that summarizes classification performance by showing the counts "
                "of true positives, true negatives, false positives, and false negatives."
            ),
            "difficulty": "fresher",
        },
    ],

    # -------------------------------------------------------------------
    # WEB DEVELOPMENT
    # -------------------------------------------------------------------
    "webdev": [
        {
            "question": "What is the difference between HTML and CSS?",
            "keywords": ["structure", "content", "styling", "presentation"],
            "ideal_answer": (
                "HTML defines the structure and content of a webpage, while CSS controls the styling "
                "and visual presentation of that content."
            ),
            "difficulty": "fresher",
        },
        {
            "question": "What is responsive design?",
            "keywords": ["mobile", "screen sizes", "flexible", "media queries"],
            "ideal_answer": (
                "Responsive design ensures that a website adapts to different screen sizes and devices "
                "using flexible layouts, images, and CSS media queries."
            ),
            "difficulty": "fresher",
        },
        {
            "question": "What is an API in the context of web development?",
            "keywords": ["interface", "communication", "request", "response", "HTTP"],
            "ideal_answer": (
                "An API is an interface that allows different software systems to communicate, usually "
                "by sending HTTP requests and receiving responses, often with JSON data."
            ),
            "difficulty": "fresher",
        },
    ],

    # -------------------------------------------------------------------
    # CYBERSECURITY
    # -------------------------------------------------------------------
    "cybersecurity": [
        {
            "question": "What is phishing?",
            "keywords": ["social engineering", "fraud", "email", "steal information"],
            "ideal_answer": (
                "Phishing is a social engineering attack where attackers trick users, often through fake emails "
                "or messages, into revealing sensitive information like passwords or credit card numbers."
            ),
            "difficulty": "fresher",
        },
        {
            "question": "What is encryption?",
            "keywords": ["protect data", "cipher", "key", "confidentiality"],
            "ideal_answer": (
                "Encryption converts readable data into an unreadable format using an algorithm and a key, "
                "so that only someone with the key can decrypt and read it."
            ),
            "difficulty": "fresher",
        },
        {
            "question": "What is a firewall?",
            "keywords": ["network", "traffic", "filtering", "protection"],
            "ideal_answer": (
                "A firewall monitors and filters network traffic based on security rules to block "
                "unauthorized access while allowing legitimate communication."
            ),
            "difficulty": "fresher",
        },
    ],
}