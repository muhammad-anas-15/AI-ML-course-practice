import json

class Chatbot:

    def __init__(self, name):
        self.name = name

    # Response rules (keyword → response)
        self.response_rules = {
            # Greetings
            "hello": "Hello! How can I help you?",
            "hi": "Hi there!",
            "hey": "Hey! Nice to meet you.",

            # Farewell
            "bye": "Goodbye! Have a nice day!",
            "goodbye": "See you later!",

            # FAST questions
            "fast": "FAST University is one of the top computing universities in Pakistan.",
            "nuces": "FAST NUCES is known for strong programming education.",

            # Peshawar
            "peshawar": "Peshawar is one of the oldest cities in Pakistan, famous for culture and food.",

            # AI
            "ai": "Artificial Intelligence helps machines learn from data.",
            "machine learning": "Machine learning is a subset of AI.",
            "deep learning": "Deep learning uses neural networks.",

            # Jokes
            "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",

            # Compliments
            "good": "Thank you! 😊",

            # Insults
            "stupid": "I'm still learning. Please be kind!",
            "bad": "I will try to improve my responses.",

            # Help
            "help": "Ask me about greetings, AI, FAST, Peshawar or tell me something!"
        }

        self.conversation_history = []
        self.sentiment_tracker = 0

        self.positive_words = ["good","great","excellent","nice","love","awesome","happy"]
        self.negative_words = ["bad","hate","stupid","worst","ugly","angry","sad"]

    # Respond Method 

    def respond(self, user_input):

        text = user_input.lower()

        self.conversation_history.append(text)

        # Functional filtering of matching rules
        matches = list(filter(lambda rule: rule in text, self.response_rules.keys()))

        # Choose most specific match (longest keyword)
        if matches:
            best_match = max(matches, key=len)
            response = self.response_rules[best_match]

        else:
            response = None

        # Sentiment tracking
        words = text.split()

        pos_count = 0
        neg_count = 0

        for w in words:
            if w in self.positive_words:
                pos_count += 1

            if w in self.negative_words:
                neg_count += 1

        self.sentiment_tracker += (pos_count - neg_count)

        # Cheer user if sentiment is low
        if self.sentiment_tracker < -3:
            return "Hey, don't be sad 😊 I'm here to help you!"

        # Learning mode
        if response is None:
            print("I don't know the answer.")
            new_answer = input("Teach me the response: ")

            self.response_rules[text] = new_answer
            return new_answer

        return response

    # Save Conversation 

    def save_history(self, filename="chat_history.txt"):
        with open(filename, "w") as f:
            for msg in self.conversation_history:
                f.write(msg + "\n")

        print("Conversation saved.")


# Chatbot Test

bot = Chatbot("FASTBot")

print("Chatbot Started (type 'exit' to stop)")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        bot.save_history()
        break

    reply = bot.respond(user_input)
    print(bot.name + ":", reply)