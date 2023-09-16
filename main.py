from model import TextToImageEncoder

if __name__ == '__main__':
    txtToImg = TextToImageEncoder()
    txtToImg.encode('input.txt', 'output.png')
    txtToImg.decode('output.png', 'output.txt')
    
    