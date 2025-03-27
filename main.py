from elevenlabs.client import ElevenLabs
import elevenlabs
import os


api_key = "YOUR_API_KEY" # Ваш апі ключ від ElevenLabs

client = elevenlabs.ElevenLabs(api_key=api_key) # Ініціалізація

voice_id = "0ZQZuw8Sn4cU0rN1Tm2K"  # voice id потрібного голосу. Дізнатись можна на сайті ElevenLabs



choice = input("Виберіть спосіб вводу тексту:\n1 - Ввести вручну\n2 - Завантажити з .txt файлу\nВиберіть 1 чи 2: ") # Запитуємо у користувача, як він хоче ввести текст

if choice == "1":
    # Введення вручну
    text = input("Введіть текст для перетворення: ").strip()
elif choice == "2":
    # Введення шляху до файлу
    txt_file_path = input("Введіть шлях до .txt файлу: ").strip()

    # Перевіряємо, чи існує файл
    if not os.path.isfile(txt_file_path):
        print("Помилка! Файл не знайдено")
        exit()

    # Читаємо текст з файлу
    with open(txt_file_path, "r", encoding="utf-8") as file:
        text = file.read().strip()

    if not text:
        print("Помилка! Файл пустий")
        exit()
else:
    print("Помилка! Невірний вибір")
    exit()

# Перевіряємо, чи є текст
if not text:
    print("Помилка! Файл має містити текст")
    exit()

audio = client.text_to_speech.convert( # Виклик методу convert від апі елевен лабс
    voice_id=voice_id, # Вказує апі голосу
    text=text, # Вказує текст вочевидь
    output_format="mp3_44100_128", # Вказує формат файлу. Зараз це мп3 з частотою 44100 кілогерц і бітрейтом у 128 кілобіт на секунду
    model_id="eleven_multilingual_v2" # Айді моделі. Зараз це мультілангуаге (ха-ха) модель, яка підтримує багато мов одночасно. Вибрана саме ця модель задля ефективності озвучення текстових файлів для навчання, адже вони містять в собі не тільки українську мову, а ще й іноді російську і англійську
)


output_filename = input("Введіть назву аудіофайлу: ") # Збереження аудіофайлу
if not output_filename.lower().endswith(".mp3"): # Перевіряємо, чи є в кінці .mp3
    output_filename += ".mp3" # Якщо ні, то додаємо

with open(output_filename, "wb") as f:
    for chunk in audio:  # Читання потоку за чанками. Чанки дозволяють обробляти інформацію шматками, що впливає на ефективність програми (навіть коли в ній 59 строк). Почитати про це докладніше (російською) можна тут https://habr.com/ru/articles/744656/
        f.write(chunk)
    print(f"Аудіофайл збережено як {output_filename}") # Вивід в аудіофайл
