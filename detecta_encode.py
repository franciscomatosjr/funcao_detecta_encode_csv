def detect_encoding(file_name):
    # Tentativa de detecção do encoding
    with open(file_name, 'rb') as file:
        raw_data = file.read(10000)

    encoding_info = chardet.detect(raw_data)
    encoding = encoding_info['encoding']

    return encoding


if __name__ == "__main__":
    file_path = 'c:\\temp\\arquivo.csv'
    encode_encontrado = detect_encoding(file_path)    
    print(encode_encontrado)