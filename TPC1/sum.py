def process_text(text):
    total_sum = 0
    is_on = True
    
    buffer = ""
    i = 0
    
    while i < len(text):
        char = text[i]
        
        buffer += char.lower()
        
        if len(buffer) > 3:
            buffer = buffer[1:]
        
        if buffer.endswith("on"):
            is_on = True
            buffer = ""
        elif buffer.endswith("off"):
            is_on = False
            buffer = ""
        
        if char == '=':
            print(f"Current sum: {total_sum}")
        
        if is_on and char.isdigit():
            number_str = ""
            while i < len(text) and text[i].isdigit():
                number_str += text[i]
                i += 1
            if number_str:
                total_sum += int(number_str)
            continue
        
        i += 1
    
    return total_sum

def main():
    choice = input("Choose an option:\n1. Write a String\n2. Read from file\nOption: ")
    
    if choice == '1':
        text = input("Type your String: ")
    elif choice == '2':
        file_path = input("Type the file path: ")
        with open(file_path, 'r') as file:
            text = file.read()
    else:
        print("Invalid option.")
        return
    
    final_sum = process_text(text)
    print(f"Final sum: {final_sum}")

if __name__ == "__main__":
    main()
