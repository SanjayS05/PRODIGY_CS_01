def caesar_cipher(inp_str, shift, dirr):
    out_str = ""
    for i in inp_str:
        if i == " ":
            out_str += " "
        elif i.isupper():
            out_str += chr((ord(i) + shift - 65) % 26 + 65)
        else:
            out_str += chr((ord(i) + shift - 97) % 26 + 97)
    return out_str

def main():
    inp_str = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    dirr = int(input("Enter the direction (0 for left, 1 for right): "))
    if dirr == 0:
        shift = -shift
    print(caesar_cipher(inp_str, shift, dirr))

if __name__ == "__main__":
    main()