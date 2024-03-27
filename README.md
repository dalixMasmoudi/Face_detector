# Face Detection System for ID Comparison

This ready to deploy face detection system is designed to compare a person's face against a database of known faces to determine if they exist in the database or not. The system utilizes computer vision techniques to detect faces in images and compare them against a set of reference images stored in a database.
![aHR0cHM6Ly9pbWFnZXMuZ2l0ZWUuY29tL3VwbG9hZHMvaW1hZ2VzLzIwMjAvMDIwMy8xNTUzMTRfNzhmYTlkMTNfMzk4OTQwLmdpZg](https://github.com/dalixMasmoudi/Face_detector/assets/94851502/8dc441f1-4230-4538-a4ad-b0275b4766a9)

## How It Works

1. **Face Detection**: The system first detects faces in the input image using a pre-trained deep learning model of the world simplest detection model.

2. **Feature Extraction**: After detecting a face, the system extracts features from the face image using techniques such as face embeddings or local binary patterns (LBP).

3. **Database Comparison**: The extracted features are then compared against a database of known faces. If a match is found, the system identifies the person associated with the matched face.

4. **Output**: If the person is recognized and exists in the database, the system outputs their identity. If the person is not recognized, the system outputs "Unknown".

## Usage

To use the face detection system:

1. **Setup**: Install the required dependencies such as OpenCV, dlib, or any other relevant libraries.

2. **Database Creation**: Create a database of known faces by collecting images of individuals and extracting features from their faces. Store these features along with the corresponding identities in the database.

3. **Face Detection**: Provide an input image containing a face to the system.

4. **Processing**: The system detects the face in the input image, extracts features, and compares them against the database.

5. **Output**: If a match is found, the system outputs the identity of the recognized person. If no match is found, the system outputs "Unknown".

## Example

Run 
