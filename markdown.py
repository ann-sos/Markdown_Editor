t_prompt = "- Text: "
filename = input("Name of your file: ")
try:
    with open(filename, "r") as f:
        working_text = f.read()
        print("The file content is: \n", working_text)
except IOError:
    print("Your file has been created.")
    working_text = ""


def f_line_break():
    return "\n"


def f_plain():
    return input("- Text: ")


def f_bold():
    return f"**{input(t_prompt)}**"


def f_italic():
    return f"*{input(t_prompt)}*"


def f_inline_code():
    return f"`{input(t_prompt)}`"


def f_header():
    h_level = int(input("- Level: "))
    user_text = input(t_prompt)
    return h_level * "#" + f" {user_text}\n"


def f_link():
    l_label = input("- Label: ")
    url = input("- URL: ")
    return f"[{l_label}]({url})"


def f_list():
    while True:
        rows = int(input("- Number of rows: "))
        if rows > 0:
            break
        print("The number of rows should be greater than zero")
    user_text = ""
    for i in range(rows):
        if user_input == "ordered-list":
            counter = f"{i + 1}. "
        elif user_input == "unordered-list":
            counter = "* "
        user_text += counter + input(f"- Row #{i+1}") + "\n"
    return user_text


available_formatters = {'plain': f_plain, 'bold': f_bold, 'italic': f_italic, 'header': f_header,
                        'ordered-list': f_list, 'unordered-list': f_list, 'link': f_link,
                        'inline-code': f_inline_code, 'line-break': f_line_break}

while True:
    user_input = input("- Choose a formatter: ")
    if user_input == "!help":
        print("Available formatters: ", " ".join(available_formatters))
        print("Special commands: !help !done")

    elif user_input == "!done":
        with open(filename, "w") as f:
            f.write(working_text)
        break
    elif user_input not in available_formatters:
        print("Unknown formatting type or command. Please try again")
    elif user_input in available_formatters:
        working_text += available_formatters[f"{user_input}"]()
        print(working_text)
