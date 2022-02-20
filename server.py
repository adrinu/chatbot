from socketserver import TCPServer, UDPServer, BaseRequestHandler
from random import choice

# Chatbot responses and keywords to trigger response
greeting_response = ["Hello!", "Hi", "Bonjour", "Hola", "Nice to meet you!", "heyyy <3"], 
greeting_keywords = ["hi", "hello", "hey", "bonjour", "meet", "greetings", "hola"]

feels_response = ["Thats great to hear!", "Cheer up!", "Sounds like you a bitch", "Grow up", "I aint ur therapist"]
feels_keywords = ["sad", "happy", "mad", "angry", "tired", "stressed", "stress", "frustrated", "good", "great"], 

robot_feels_reponse = ["Im doing good", "I am not capable of emotions", "I wish I was a human", "Amazing! How are you doing?"]
robot_feels_keywords = ["are you", "mood", "how"]

creator_response = ["I was created by Adrian!", "Some kid in university", "I was created in python"]
creator_keywords = ["creator", "maker", "birth", "created", "create"]

weather_response = ["I have no idea!", "Its sunny somewhere!", "Its raining somewhere!"]
weather_keywords = ["rain", "snow", "hail", "sunny", "weather", "temperature"]

sports_response = ["I like basketball!", "I like futbol!", "I like baseball!", "I wish I could be a human to experience the sensatition of playing sports"]

food_response = ["I cant eat :(", "I like to eat memory!", "If I was a human, I would eat pizza!"]

name_response = ["My name is Chatbot!", "My creator did not give me human name", "I AM ROBOT"]

joke_response = ["What do you call an ant who fights crime? A vigilANTe", "How does the ocean say hi? It waves!", "What's Thanos' favorite app on his phone? Snapchat"]

def generate_response(msg):
    """
    Generates a response for the client

    Args:
        msg (str): Message from client

    Returns:
        str: Random response that is related to the client query
    """
    lower = str(msg.lower())
    # Checks for keyword and returns a random response
    if "sports" in lower:
        return choice(sports_response)
    if "food" in lower:
        return choice(food_response)
    if "joke" in lower:
        return choice(joke_response)
    if "name" in lower:
        return choice(name_response)
    
    for keyword in greeting_keywords:
        if keyword in lower:
            return choice(greeting_response)
    
    for keyword in weather_keywords:
        if keyword in lower:
            return choice(weather_response)
    
    for keyword in creator_keywords:
        if keyword in lower:
            return choice(creator_response)
    
    for keyword in robot_feels_keywords:
        if keyword in lower:
            return choice(robot_feels_reponse)
    
    for keyword in feels_keywords:
        if keyword in lower:
            return choice(feels_response)
    
    return "I dont know how to response to that! >:("
    
def run_server(HOST, PORT, SERVER_TYPE):
    """
    Runs ChatBot Server

    Args:
        HOST (str): IP Address
        PORT (int): Port to IP Address
        SERVER_TYPE (str): TCP or UDP
    """
    class ChatBot(BaseRequestHandler):
        def handle(self):
            if SERVER_TYPE == "TCP":
                # Receive the message from client
                self.data = self.request.recv(1024).strip()
                
                # Send response to client
                self.request.sendall(bytes(generate_response(self.data), "utf-8"))
            else:
                # Receive the message from client
                data = self.request[0].strip()
                
                # Gets address of client
                socket = self.request[1]
                
                # Send response to client
                socket.sendto(bytes(generate_response(data), "utf-8"), self.client_address)

    # Starts server whether client wanted TCP or UDP
    if SERVER_TYPE == "TCP":
        with TCPServer((HOST, PORT), ChatBot) as server:
            server.serve_forever()
    else:
        with UDPServer((HOST, PORT), ChatBot) as server:
            server.serve_forever()
        
 