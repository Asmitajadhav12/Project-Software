A simple Python project to analyze the sentiment of text data (positive, negative, or neutral).
This project uses basic NLP techniques to process text and visualize the results.

Project Structure

Sentiment analysis/
│── emotions.txt # List of words with their emotions
│── read.txt # Input text file
│── main.py # Main script for sentiment analysis
│── settings.py # Configuration/settings
│── graph.png # Output graph visualization

Features

Reads text input from a file (read.txt).

Identifies emotions using keywords from emotions.txt.

Generates a sentiment graph (graph.png).

Simple and beginner-friendly.

How to Run

Clone the repository:
git clone https://github.com/AsmitaJadhav12/Project-Software.git

Navigate to the project folder:
cd Project-Software/"Sentiment analysis"

Run the program:
python main.py

Example Output

Input text:
"I am happy but also a little worried"

Output:

Positive → 1

Negative → 1

Visualization:
(Sentiment graph is saved as graph.png)

Requirements

Python 3.x

Libraries:
pip install matplotlib
pip install nltk

Future Improvements

Add machine learning model for better accuracy.

Support for multiple languages.

Real-time sentiment analysis on live data (e.g., Twitter API).

👩‍💻 Author

Asmita Jadhav
