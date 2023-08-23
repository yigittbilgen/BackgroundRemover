from rembg import remove

input_path = "image.jpg"
output_path = "output.png"

with open(input_path,'rb') as i:
    with open(output_path, 'wb') as o:
        inputFile = i.read()
        outputFile = remove(inputFile)
        o.write(outputFile)