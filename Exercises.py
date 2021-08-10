def sort_word(word):
    reverse_word_list = []
    reverse_word_list[:0] = word
    reverse_word_list.reverse()
    reverse_word = ""
    reverse_word = reverse_word.join(reverse_word_list)

    return reverse_word

def main():
    message = input("Plz enter the message: ")
    reverse_message_list = []
    for word in message.split():
        reverse_message_list.append(sort_word(word))
    reverse_message_list.reverse()
    reverse_message = "".join(reverse_message_list)

    print("The reversed message is: ",
          reverse_message)

main()

