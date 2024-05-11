
file = open("python_data.json", mode="r")
dictionaire_str = file.read()
file.close()
print((dictionaire_str))
dictionaire = {
}
import json

dictionaire = json.loads(dictionaire_str)

print("eau = ", dictionaire["eau"])