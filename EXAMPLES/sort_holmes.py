"""Sort titles, ignoring leading articles"""
books = [
    "A Study in Scarlet",
    "The Sign of the Four",
    "The Hound of the Baskervilles",
    "The Valley of Fear",
    "The Adventures of Sherlock Holmes",
    "The Memoirs of Sherlock Holmes",
    "The Return of Sherlock Holmes",
    "His Last Bow",
    "The Case-Book of Sherlock Holmes",
]

def move_article(title):
    for article in 'a ', 'an ', 'the ':
        if title.lower().startswith(article):
            words = title.split()
            title =  ' '.join(words[1:]) + f", {words[0]}"
    return title

new_titles = [move_article(t) for t in books]


def strip_article(title):  # create function which takes element to compare and returns comparison key
    title = title.lower()
    for article in 'a ', 'an ', 'the ':
        if title.startswith(article):
            title = title.removeprefix(article)  # remove article
            break
    return title


for book in sorted(books, key=strip_article):  # sort using custom function
    print(book)
print('-' * 60)

for book in sorted(new_titles):
    print(book)