import requests
import json

def buscar_dados_id(id):
    request = requests.get(f"https://language-api-mmacedoaraujo.herokuapp.com/languages?id={id}")
    todos = json.loads(request.content)
    print(todos)
    print(todos[0]['title'])
    print(todos[0]['image'])
    print(todos[0]['ranking'])

if __name__ == '__main__':
    buscar_dados_id("62dc8fdb66bde6b9e40fff38")

print(buscar_dados_id())