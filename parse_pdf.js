const { PDFParse } = require('pdf-parse');
const fs = require('fs');

const parser = new PDFParse({ data: new Uint8Array(fs.readFileSync('C:/Users/ACER/.gemini/antigravity/scratch/creatomy-website/client_requirements.pdf')) });
parser.load()
  .then(() => parser.getText())
  .then(res => {
      fs.writeFileSync('C:/Users/ACER/.gemini/antigravity/scratch/creatomy-website/extracted_text.txt', res.text);
      console.log("Successfully extracted text to extracted_text.txt!");
  })
  .catch(err => console.error(err));
