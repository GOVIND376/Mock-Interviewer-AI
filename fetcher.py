"""
    Fetch interview questions from the web (Indeed) as a fallback when 
    there is no structured question bank for a give career/domain.
"""

import requests
from bs4  import BeautifulSoup
from config import USER_AGENT, DEFAULT_QUESTIONS


def fetch_questions(career:str):
    """
    
    Fetch interview quetions for the given career from Indeed.
    Return up to 5 questions, or DEFAULT_QUESTIONS if anything fails.
    
    """
    career = career.strip().lower()
    slug = career.replace("","-")
    url = F"https://wwww.indeed.com/career-advice/interviewing/{slug}-interview-questions"
    
    try:
        response = requests.get(url,headers={"User-Agent":USER_AGENT},timeout=6)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text,"html.parser")
        
        
        questions = [
            h2.get_text(strip= True)
            for h2 in soup.find_all("h2")
            if "?" in h2.get_text()
        ]
        return questions[:5] if questions else DEFAULT_QUESTIONS
    except Exception as exc:
        print(f"[Fetcher Error]{exc}")
        return DEFAULT_QUESTIONS
        
    