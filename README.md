# Llama3.2ChatBot
Llama3.2ChatBot 


ollama installation: 
curl -fsSL https://ollama.com/install.sh | sh

or :

curl -L https://ollama.com/download/ollama-linux-amd64.tgz -o ollama-linux-amd64.tgz
sudo tar -C /usr -xzf ollama-linux-amd64.tgz

check the installation using: 
ollama -v

downloading model:

ollama pull llama3.2
ollama pull mistral
ollama pull starcoder2
ollama pull phi3

start model:

ollama serve phi3
ollama run llama3.2



this app needs python customtkinter
pip3 install gtts

