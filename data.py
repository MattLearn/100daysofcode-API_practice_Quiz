import requests

quiz_params = {
    "amount": 10,
    "type": "boolean"
}

quiz_source = requests.get("https://opentdb.com/api.php", params=quiz_params)
quiz_source.raise_for_status()
data = quiz_source.json()
# print(data)
question_data = data["results"]
# print(question_data)