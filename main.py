import requests

url = "https://fly.wordfinderapi.com/api/search?length=5&page_token=1&page_size=500000&word_sorting=az&group_by_length=true&dictionary=wordle"

res = requests.get(url)

json = res.json()

word_list = json["word_pages"][0]["word_list"]

result = []
with open('final.txt', 'a') as file:
    for word in word_list:
        result.append(word["word"])
        file.write(word["word"])
        file.write('\n')

print(result)
print(len(result))
