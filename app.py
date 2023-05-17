import os
from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array, load_img ,ImageDataGenerator

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        # Save the uploaded image temporarily
        image_path = 'temp_image.jpg'
        file.save(image_path)

        # Create a temporary directory
        temp_dir = '/path/to/temp_dir'
        os.makedirs(temp_dir, exist_ok=True)

        # Copy the image to the temporary directory
        # image_path = '/path/to/image.jpg'
        destination_path = os.path.join(temp_dir, 'image.jpg')
        shutil.copy(image_path, destination_path)


        # Load and preprocess the image
        
        test_datagen=ImageDataGenerator(
                           rescale=1./255.
                        )
        test_generator=test_datagen.flow_from_directory(
                    directory=temp_dir,
                    color_mode='rgb',
                    class_mode= None,
                    batch_size=1,
                    shuffle=False,
                    target_size=(240,240)
                  )
        
        # Make predictions
        predictions = pred(image_array)
        # predicted_class = class_names[np.argmax(predictions[0])]

        # Delete the temporary image file
        os.remove(image_path)
        
        return jsonify({'prediction': predictions})
    except Exception as e: 
        print(e) 
        return {
            'message':'Error',
            'success':False
        } 

if __name__ == '__main__':
    app.run(debug=True)