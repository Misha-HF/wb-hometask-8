import connect
from models import Author, Quote


def name_handler(author_name):
    author = Author.objects(fullname=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        return quotes


def tag_handler(tag):
    quotes = Quote.objects(tags=tag)
    if quotes:
        return quotes


def tags_handler(tags):
    quotes = Quote.objects(tags__in=tags)
    if quotes:
        return quotes


def main():
    table = {
        "name": name_handler,
        "tag": tag_handler,
        "tags": tags_handler,
    }

    while True:
        user_input = str(input(">>> "))

        if user_input.lower() == "exit":
            print("Good Bye!")
            break

        handler_name, args = user_input.split(":", 1)
        handler_name = handler_name.strip().lower()
        args = args.strip()     

        if handler_name in table:
            
            if handler_name == "tags":
                args = args.split(",")

            try:
           
                result = table[handler_name](args)

                if result:
                    for index, quote in enumerate(result):
                        print(f"{index + 1}. {quote.to_json()}")

                else:
                    print("Inncorect value")

            except (ValueError, KeyError) as e:
                print(f"{e}")
        else:
            print("No such command")

if __name__ == "__main__":
    main()

"""щоб код повертав не об'єкт, а просто цитату: """
# import connect
# from models import Author, Quote


# def name_handler(author_name):
#     author = Author.objects(fullname=author_name).first()
#     if author:
#         quotes = Quote.objects(author=author)
#         return [quote.quote for quote in quotes]


# def tag_handler(tag):
#     quotes = Quote.objects(tags=tag)
#     if quotes:
#         return [quote.quote for quote in quotes]


# def tags_handler(tags):
#     quotes = Quote.objects(tags__in=tags)
#     if quotes:
#         return [quote.quote for quote in quotes]


# def main():
#     table = {
#         "name": name_handler,
#         "tag": tag_handler,
#         "tags": tags_handler,
#     }

#     while True:
#         user_input = str(input(">>> "))

#         if user_input.lower() == "exit":
#             print("Good Bye!")
#             break

#         handler_name, args = user_input.split(":", 1)
#         handler_name = handler_name.strip().lower()
#         args = args.strip()     

#         if handler_name in table:
            
#             if handler_name == "tags":
#                 args = args.split(",")

#             try:
           
#                 result = table[handler_name](args)

#                 if result:
#                     for index, quote in enumerate(result):
#                         print(f"{index + 1}. {quote}")

#                 else:
#                     print("Inncorect value")

#             except (ValueError, KeyError) as e:
#                 print(f"{e}")
#         else:
#             print("No such command")

# if __name__ == "__main__":
#     main()