import urllib.request
import os

url = "https://drive.google.com/uc?export=download&id=1AXRgLoxI6WTmTM0BnDFFToh0QDwP5Mv7"
output_path = "C:/Users/ACER/.gemini/antigravity/scratch/creatomy-website/client_requirements.pdf"

print(f"Downloading from {url}...")
try:
    # Use a User-Agent to avoid being blocked
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    with urllib.request.urlopen(req) as response, open(output_path, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
    print(f"Downloaded successfully! Size: {os.path.getsize(output_path)} bytes")
except Exception as e:
    print(f"Error: {e}")
