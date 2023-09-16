# Text to Image Encoder-Decoder
The Text to Image Encoder-Decoder is a Python tool that allows you to convert any text file into an image file (.png) format and decode it back to the original text, all without any loss in data. This project is particularly useful when you need to hide or transmit textual information in a visual format.

### Features
- Encode text files into images.
- Decode images back to text files.
- Compression to reduce image size.
- Customizable minimum image dimensions.

### Examples

```py
    from model import TextToImageEncoder

    textToImage = TextToImageEncoder()

    textToImage.encode("my_text.txt", "encoded_image.png")

    textToImage.decode("encoded_image.png", "decoded_text.txt")

```