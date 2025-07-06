import re
import random
from datetime import datetime
import long_responses as long
from weather_api import get_weather
from joke_api import get_joke
from dice_api import roll_dice_api
from wiki_api import get_wikipedia_summary
from translate_api import translate_text
from currency_api import convert_currency
from news_api import get_news
from math_solver import safe_eval
from reminder_timer import set_reminder
from alarm import set_alarm
from unit_converter import convert_unit
from movie_api import get_movie_info

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words)) if recognised_words else 0

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    return int(percentage * 100) if has_required_words or single_response else 0

def check_all_messages(message, user_input_raw=""):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response("Hello there! How can I assist you today?", ["hello", "hi", "hey", "yo", "greetings", "good", "morning", "evening"], single_response=True)
    response("Goodbye! Take care 😊", ["bye", "goodbye", "see", "you", "later", "take", "care"], single_response=True)
    response("You're welcome!", ["thanks", "thank"], single_response=True)
    response("I'm a bot created to help you.", ["who", "are", "you"], required_words=["who", "are", "you"])
    response("The current time is " + datetime.now().strftime("%H:%M:%S"), ["current", "time"], required_words=["current", "time"])
    response("The current date is " + datetime.now().strftime("%Y-%m-%d"), ["current", "date"], required_words=["current", "date"])
    response("The current date and time is " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ["date", "time"], required_words=["date", "time"])
    response(long.R_ADVICE, ["advice"], required_words=["advice"])
    response(get_joke(), ["tell", "joke"], required_words=["joke"])
    response(long.R_EATING, ["what", "you", "eat"], required_words=["you", "eat"])
    
    if len(message) <= 1 and not highest_prob_list:
        return long.unknown("short")

    dice_match = re.search(r"\b(\d+)d(\d+)\b", user_input_raw.lower())
    if dice_match:
        num_dice = int(dice_match.group(1))
        sides = int(dice_match.group(2))
        if num_dice > 20 or sides > 100:
            return "That's too many dice or too many sides!"
        rolls = [random.randint(1, sides) for _ in range(num_dice)]
        return f"You rolled {num_dice}d{sides}: {rolls} → Total: {sum(rolls)}"

    # Fallback: Only roll 1d6 if it's literally "roll a dice" without any other dice pattern
    if re.fullmatch(r"roll a dice", user_input_raw.strip().lower()):
        return f"You rolled a 1d6: {random.randint(1, 6)}"


    for word in message:
        if word == "weather":
            city = message[-1]
            return get_weather(city)
        
    news_match = re.search(r"news (about|in)?\s*(.+)", user_input_raw, re.IGNORECASE)
    if news_match:
        city = news_match.group(2).strip()
        return get_news(city)
    elif "news" in user_input_raw.lower():
        return get_news()
 
    alarm_match = re.search(r"set alarm for (\d{1,2}):(\d{2})", user_input_raw)
    if alarm_match:
        hour = alarm_match.group(1).zfill(2)
        minute = alarm_match.group(2).zfill(2)
        alarm_time = f"{hour}:{minute}"
        return set_alarm(alarm_time)
    
    unit_match = re.search(r"convert (\d+(\.\d+)?)\s+(\w+)\s+to\s+(\w+)", user_input_raw, re.IGNORECASE)
    if unit_match:
        amount = float(unit_match.group(1))
        from_unit = unit_match.group(3)
        to_unit = unit_match.group(4)
        return convert_unit(amount, from_unit, to_unit)
     
    match = re.search(r'convert\s+(\d+(?:\.\d+)?)\s+([a-zA-Z]{3})\s+to\s+([a-zA-Z]{3})', user_input_raw, re.IGNORECASE)
    if match:
        amount = float(match.group(1))
        from_currency = match.group(2)
        to_currency = match.group(3)
        return convert_currency(amount, from_currency, to_currency)

    
    match = re.search(r'translate\s+(.*?)\s+to\s+(\w+)', user_input_raw, re.IGNORECASE)
    if match:
        sentence = match.group(1).strip()
        lang = match.group(2).strip().lower()
        return translate_text(sentence, lang)
    
    math_match = re.search(r"(what is|solve|calculate|evaluate)\s+(.+)", user_input_raw, re.IGNORECASE)
    if math_match:
        expression = math_match.group(2).strip()
        return safe_eval(expression)
    
    movie_match = re.search(r"(movie info|movie details|movie)\s+(.*)", user_input_raw, re.IGNORECASE)
    if movie_match:
        title = movie_match.group(2).strip()
        return get_movie_info(title)

    # OR fallback if someone types only "movie info Inception"
    if user_input_raw.lower().startswith("movie info "):
        title = user_input_raw[10:].strip()
        return get_movie_info(title)
 
    wiki_match = re.search(r"(who is|what is|tell me about|explain|define)\s+(.*)", user_input_raw, re.IGNORECASE)
    if wiki_match:
        topic = wiki_match.group(2).strip()
        return get_wikipedia_summary(topic)
            
    reminder_match = re.search(r"remind me in (\d+)\s*(seconds|minutes|minute|secs|sec|min)\s*to (.+)", user_input_raw, re.IGNORECASE)
    if reminder_match:
        value = int(reminder_match.group(1))
        unit = reminder_match.group(2)
        task = reminder_match.group(3)
        seconds = value * 60 if "min" in unit else value
        return set_reminder(task, seconds)
        
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    if not user_input.strip():
        return long.unknown("empty")
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    return check_all_messages(split_message, user_input.strip())
