from newsCrawler import myNewsCrawler

word = "Trump"
newsPapers = {
    "foxnews": {"link": "http://www.foxnews.com/"},

    "cnn": {"link": "https://edition.cnn.com"}
}

def main():
    s = myNewsCrawler(newsPapers)
    s.downloadHtml()
    s.findWord(word)
if __name__ == "__main__":
    main()