This `README.md` provides all the necessary information for understanding, setting up, and running the Traffic Signs Recognition project.

# Traffic Signs Recognition Project

## Overview
This project is focused on recognizing and classifying traffic signs with 95% accuracy using Convolutional Neural Networks (CNN) and Keras. The application is designed to aid in the development of autonomous vehicles by interpreting traffic signs and making decisions accordingly.

## Inspiration
With the rise of self-driving cars by companies like Tesla, Uber, Google, Mercedes-Benz, Toyota, Ford, and Audi, it's crucial for these vehicles to understand and follow all traffic rules. To achieve Level 5 autonomy, the ability to accurately recognize traffic signs is a fundamental requirement.

## Technologies Used
The project is built using the following technologies:

- **Keras**: 3.5.0 - For building and training the neural network.
- **TensorFlow**: 2.17.0 - Backend for Keras, used for model optimization and performance.
- **PyQt5**: 5.15.11 - For creating the graphical user interface (GUI) of the application.
- **OpenCV**: 4.10.0.84 - For image processing tasks, such as loading and pre-processing traffic sign images.
- **scikit-learn**: 1.5.1 - For machine learning utilities and performance metrics.
- **NumPy**: 1.26.4 - For numerical operations, such as handling arrays and matrices.
- **Pillow**: 10.4.0 - For image manipulation tasks.
- **Matplotlib**: 3.9.2 - For visualizing the results and metrics.

## Project Structure
- `model/`: Contains the trained CNN model.
- `data/`: Includes the dataset of traffic signs used for training and testing.
- `code/`: All source code, including model training, evaluation, and GUI implementation.
- `results/`: Stores the results, including accuracy metrics and graphs.

## Getting Started

### Prerequisites
- **Python Version**: Ensure you have Python 3.10.11 installed.
- **Virtual Environment**: It is recommended to use a virtual environment for this project.

### Setting Up the Environment
1. **Create a Virtual Environment**:
   ```bash
   python -m venv myenv
   ```
2. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

3. **Install the Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install and Use ipykernel**:
   To run the code in a Jupyter Notebook or other IDEs that use Jupyter, install `ipykernel`:
   ```bash
   pip install ipykernel
   python -m ipykernel install --user --name=myenv
   ```

### Running the Project
1. **Train the Model**: Run the training script to train the CNN model on the traffic sign dataset.(/code/code.py)
2. **Test the Model**: Use the test script to evaluate the model's accuracy.(/code/code.py)
3. **Launch the Application**: Start the GUI application to recognize traffic signs using images.(/code/tikinter.py)

## Conclusion
This project represents a significant step towards developing autonomous vehicles capable of safely navigating roads by recognizing and interpreting traffic signs. With continued research and development, the goal is to achieve even higher accuracy and real-time performance.
