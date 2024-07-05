from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float
    
def get_mood(input_text: str, *,  threshold: float) -> Mood:
    sentiment: float = TextBlob(input_text).sentiment.polarity
    
    nice_threshold: float = threshold
    mean_threshold: float = -threshold
    
    if sentiment >= nice_threshold:
        return Mood('😊', sentiment)
    elif sentiment <= mean_threshold:
        return Mood('😠', sentiment)
    else:
        return Mood('😐', sentiment)

print("Welcome to the Text Sentiment Analyzer! Enter a message, and the analyzer will determine how positive or negative your message is on a scale of 1 to -1.")
if __name__ == '__main__':
    while True:
        text: str = input('Enter a message: ')
        mood: Mood = get_mood(text, threshold = 0.3)
        
        print(f'{mood.emoji} ({mood.sentiment})')