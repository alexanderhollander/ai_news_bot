import feedparser
from newspaper import Article
import openai

# Установи свой API ключ OpenAI
openai.api_key = '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'

# RSS-источники новостей об ИИ
rss_urls = [
    'https://techcrunch.com/tag/artificial-intelligence/feed/',
]

# Функция для извлечения текста статьи с помощью newspaper3k
def extract_article_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return f"Ошибка при извлечении статьи: {e}"

# Функция для перевода текста
def translate_text(text):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  # Используем модель для перевода
            prompt=f"Translate the following text to Russian:\n\n{text}",
            max_tokens=1000
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Ошибка при переводе: {e}"

# Основная функция сбора новостей и перевода
def get_news():
    for url in rss_urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:  # ограничиваем 3 статьями
            title = entry.title
            link = entry.link
            print(f"Заголовок: {title}")
            print(f"Ссылка: {link}")
            print("Текст статьи:")
            article_text = extract_article_text(link)  # Извлечение текста
            translated_text = translate_text(article_text)  # Перевод текста
            print("Переведённый текст:")
            print(translated_text)  # Вывод переведённого текста
            print("\n" + "-"*80 + "\n")

get_news()