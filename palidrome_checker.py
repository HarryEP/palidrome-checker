def check_palidrome(word: str) -> bool:
    top = len(word) - 1
    bottom = 0
    while top > bottom:
        if word[top] != word[bottom]:
            return False
        top -= 1
        bottom += 1
    return True


if __name__ == "__main__":
    user_input = input("Enter a palidrome: ")
    print(f"is {user_input} a palidrome -> {check_palidrome(user_input.lower())}")
