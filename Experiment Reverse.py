def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]

def main():
    message = input("enter messaage: ")
    print(reverse(message))

main()