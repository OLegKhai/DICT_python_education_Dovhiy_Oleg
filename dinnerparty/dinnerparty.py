import random
def main():

    num_friends = int(input("Enter the number of friends joining (including you):\n"))

    if num_friends <= 0:
        print("No one is joining for the party")
        return

    friends_dict = {}

    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        name = input("> ")
        friends_dict[name] = 0

    print(friends_dict)
    total_amount = float(input("Enter the total amount:\n"))

    if total_amount <= 0:
        print("Invalid total amount")
        return

    amount_per_friend = round(total_amount / num_friends, 2)

    for friend in friends_dict:
        friends_dict[friend] = amount_per_friend

    print(friends_dict)

    lucky_choice = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")

    if lucky_choice.lower() == "yes":
        lucky_one = random.choice(list(friends_dict.keys()))
        print(f"{lucky_one} is the lucky one!")

        amount_per_friend = round(total_amount / (num_friends - 1), 2)

        for friend in friends_dict:
            if friend != lucky_one:
                friends_dict[friend] = amount_per_friend
            else:
                friends_dict[friend] = 0

        print(friends_dict)
    else:
        print("No one is going to be lucky")
        print(friends_dict)

if __name__ == "__main__":
    main()
