import cv2
import numpy as np
from markups import (
    HighlightExtractor,
)

def main():
    src = cv2.imread('image.jpg')
    src_small = cv2.resize(src, (0,0), fx=0.5, fy=0.5)

    extractor = HighlightExtractor()
    mask = extractor.extract(src_small)

    cv2.imshow('image', src_small & mask[:, :, np.newaxis])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
