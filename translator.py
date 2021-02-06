import requests
from bs4 import BeautifulSoup


def get_translations(soup_):

    words = soup_.findAll('a', class_="ltr", limit=5)
    translations = []

    for word in words:

        translations.append(word.text.strip())

    return translations


def get_examples(soup_, subject):

    cl = "src ltr" if subject == "original" else "trg ltr"
    examples = []

    words = soup_.findAll('div', class_=cl, limit=5)

    for word in words:

        examples.append(word.text.strip())

    return examples


languages = {
    1: "Arabic",
    2: "German",
    3: "English",
    4: "Spanish",
    5: "French",
    6: "Hebrew",
    7: "Japanese",
    8: "Dutch",
    9: "Polish",
    10: "Portuguese",
    11: "Romanian",
    12: "Russian",
    13: "Turkish"}

print("Hello, you're welcome to the translator. \nTranslator supports: \n")
for k, v in languages.items():
    print(f"{k}. {v}")

try:

    lang_original = languages[int(input("\nType the number of your language: \n"))]
    lang_to = languages[int(input("\nType the number of language you want to translate to: \n"))]
    word = input("\nType the word you want to translate: \n")

except (ValueError, IndexError):

    print("\nIncorrect input!")
    input("Press enter to exit.")

translation = lang_original + "-" + lang_to

url = f"https://context.reverso.net/translation/{translation}/{word}".lower()
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)

if r.ok:

    soup = BeautifulSoup(r.content, 'html.parser')

    translations = get_translations(soup)
    examples_original = get_examples(soup, "original")
    examples_translated = get_examples(soup, "translated")

    print()
    print(lang_to, "Translations:\n")
    print(*translations, sep="\n")
    print(f"\n{lang_to} Examples:\n")

    for i in range(5):

        print(examples_original[i])
        print(examples_translated[i])
        print()

else:

    print("\nNo connection, or there's no such word.")

input("Press enter to exit.")
