import base64

def encode_text(plain_text):
    encoded_bytes = base64.b64encode(plain_text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return caesar_cipher_encode(encoded_text, 3)

def decode_text(encoded_text):
    decoded_caesar_text = caesar_cipher_decode(encoded_text, 3)
    decoded_bytes = base64.b64decode(decoded_caesar_text.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

def caesar_cipher_encode(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                result.append(chr(start + (ord(char) - start + shift_amount) % 26))
            elif char.isupper():
                start = ord('A')
                result.append(chr(start + (ord(char) - start + shift_amount) % 26))
        else:
            result.append(char)
    return ''.join(result)

def caesar_cipher_decode(text, shift):
    return caesar_cipher_encode(text, -shift)

def main():
    print("欢迎使用编码和解码程序。这是一个使用base64模块进行的编码程序，用来对抗阿瓦隆。")
    while True:
        print("\n请选择操作:")
        print("1. 编码文本")
        print("2. 解码文本")
        print("3. 退出")

        choice = input("输入选择(1/2/3): ")

        if choice == '1':
            plain_text = input("输入要编码的文本: ")
            encoded_text = encode_text(plain_text)
            print(f"编码后的文本: {encoded_text}")

        elif choice == '2':
            encoded_text = input("输入要解码的文本: ")
            try:
                decoded_text = decode_text(encoded_text)
                print(f"解码结果: {decoded_text}")
            except Exception as e:
                print(f"解码失败: {str(e)}")

        elif choice == '3':
            print("退出程序")
            break

        else:
            print("无效选择，请重新输入")

if __name__ == '__main__':
    main()