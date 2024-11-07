import io
import chardet


def detect_encoding(file):
    raw_data = file.read()
    file.seek(0)  # Reset file pointer to the beginning after reading
    result = chardet.detect(raw_data)
    return result['encoding']


def encode_utf8(file, encoding):
    # Read the file with the original encoding
    content = file.read().decode(encoding)
    file.seek(0)  # Reset file pointer to the beginning after reading

    if encoding != 'utf-8':
        # Write the content in UTF-8 encoding
        file_name = file.name.split('.')
        new_file_path = file_name[0] + '_utf8.' + file_name[1]
        # Write the content to a BytesIO stream in UTF-8 encoding
        utf8_stream = io.BytesIO()
        utf8_stream.write(content.encode('utf-8'))
        utf8_stream.seek(0)  # Reset the stream's position to the beginning

        return utf8_stream
