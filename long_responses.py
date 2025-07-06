import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

def unknown(reason="default"):
    if reason == "empty":
        return "I need something to work with. Try asking me a question!"
    elif reason == "short":
        return "That’s a bit short. Try asking more clearly, like: 'Tell me a joke'."
    else:
        return random.choice([
            "I'm not sure I understand. Try asking: 'weather in Pune' or 'convert 5 km to miles'",
            "Hmm... try a clear question like 'news in Delhi'",
            "Could you rephrase that?",
            "I'm not sure I understand. You can ask me things like:\n- weather in Mumbai\n- tell me a joke\n- convert 10 km to miles",
            "Hmm... try asking: 'What's the time?' or 'Roll a dice'",
            "Could you please rephrase that?",
            "Try asking about the weather, news, jokes, or math help!",
        ])
