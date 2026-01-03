import pytesseract
import cv2
import os

# Windows Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    if not os.path.exists(image_path):
        return ""

    img = cv2.imread(image_path)
    if img is None:
        return ""

    # Resize for better OCR
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Remove noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Thresholding
    _, thresh = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # OCR configuration
    custom_config = r'--oem 3 --psm 6'

    try:
        text = pytesseract.image_to_string(
            thresh,
            lang="eng",
            config=custom_config
        )
        return text
    except Exception as e:
        print("OCR Error:", e)
        return ""
