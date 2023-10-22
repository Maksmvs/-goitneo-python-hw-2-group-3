# Декоратор для обробки помилок введення
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError as e:
            return f"Contact '{e.args[0]}' not found."
        except IndexError:
            return "Invalid command format. Please use 'add [name] [phone]' or 'change [name] [new phone]'."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise IndexError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise IndexError
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError(name)

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError(name)

@input_error
def show_all(contacts):
    if not contacts:
        raise IndexError
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            result = show_phone(args, contacts)
            print(result)
        elif command == "all":
            result = show_all(contacts)
            print(result)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()