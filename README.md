# Voiced_ChatGPT_in_French
Voice interaction with ChartGPT in French

I wanted to make chatGPT accessible to my kids who are too young to write on computer and do not speak english. So I wrote this script that:
- Get their request in french from teh microphone
- Get it to text
- Translate it to english
- Submit it to chatGPT
- translate it to french
- voice it.

The connection to chatGPT uses a python wrapper from this repo:
https://github.com/mmabrouk/chatgpt-wrapper
I modified the file chatGPT.py of this project to stop the prompt from this project, and let my code continue take over. This is done by introducing these few lines of code line 492.

![image](https://user-images.githubusercontent.com/55462061/210446876-32a015dc-1c87-43e2-862b-352c92f1e879.png)
