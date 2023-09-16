import cv2
import zlib
import numpy as np

class TextToImageEncoder:
    def __init__(self, min_dim: int = 128):
        """
        Initialize the TextToImage class.

        Args:
            min_dim (int): Minimum dimension for the output image.
        """
        self._min_dim = min_dim
        self._delimiter = np.array([255, 255, 255, 0], dtype=np.uint8)

    def _compress(self, buffer: bytes) -> bytes:
        """
        Compresses a bytes buffer using zlib compression.

        Args:
            buffer (bytes): The input data buffer.

        Returns:
            bytes: The compressed data buffer.
        """
        return zlib.compress(buffer)

    def _decompress(self, buffer: bytes) -> bytes:
        """
        Decompresses a zlib-compressed bytes buffer.

        Args:
            buffer (bytes): The compressed data buffer.

        Returns:
            bytes: The decompressed data buffer.
        """
        return zlib.decompress(buffer)

    def encode(self, inputfile: str, outputfile: str) -> None:
        """
        Encodes a binary file into an image.

        Args:
            inputfile (str): The path to the input binary file.
            outputfile (str): The path to the output image file.
        """
        with open(inputfile, "rb") as f:
            buffer = f.read()
            buffer = self._compress(buffer)
            
        data = np.frombuffer(buffer + self._delimiter.tobytes(), dtype=np.uint8)
        
        length = len(data)
        side = np.ceil(length / 3)
        dim = int(max(self._min_dim, np.ceil(np.sqrt(side))))
        
        image = np.zeros(dim * dim * 3, dtype=np.uint8)
        image[:length] = data
        image = image.reshape((dim, dim, 3))
        
        cv2.imwrite(outputfile, image)

    def decode(self, inputfile: str, outputfile: str):
        """
        Decodes an image back into a binary file.

        Args:
            inputfile (str): The path to the input image file.
            outputfile (str): The path to the output text file.
        """
        image = cv2.imread(inputfile)
        
        data = image.reshape(-1)
        
        for i in range(0, len(data), 3):
            if np.array_equal(data[i:i+3], self._delimiter):
                data = data[:i]
                break
                
        try:
            data = self._decompress(data.tobytes())
            with open(outputfile, 'wb') as f:
                f.write(data)
                
        except Exception as e:
            print(e)

        