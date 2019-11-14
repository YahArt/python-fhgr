from urllib.request import urlopen


success = False

while success == False:
    try:
        url = input("Please enter the url which should be opened: ")
        with urlopen(url) as website:
            web_content = website.read()
            web_content = web_content.decode('utf-8')

            word_count = len(web_content.split(' '))
            print("There are", word_count, "words on the website", url)
            success = True

    except Exception:
        success = False
        print("Something went wrong with opening the url", url)
