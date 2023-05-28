# ImmersiveCinema

ImmersiveCinema is a project designed to enhance your movie watching experience at home by controlling your environment based on the movie scene. This is accomplished through using computer vision to analyze the movie scenes and then controlling IoT devices such as lights or smart plugs to match the movie's environment.

## Setup

1. **Clone the repository:**

    ```
    git clone https://github.com/username/ImmersiveCinema.git
    ```

2. **Install dependencies:**

    Navigate to the project directory (i.e., `cd ImmersiveCinema`) and then run:

    ```
    pip install -r requirements.txt
    ```

3. **Configuration:**

    Inside the `config/` directory, you will find two JSON files:

    - `credentials.json`: Contains your email and password to access the Meross IoT platform.
    - `constants.json`: Contains the dark and light thresholds, buffer size, and capture region for the screen to be analyzed.

    Make sure to adjust these files according to your own needs.

## Usage

To run the program, navigate to the `src/` directory and run:

    ```
    python main.py
    ```

The program will start analyzing your screen and control the IoT devices accordingly.

## Project Structure

- `src/main.py`: The main script for the project.
- `src/utils.py`: Contains helper functions for controlling the IoT plug and loading the configuration.
- `config/`: Contains the configuration files (credentials.json and constants.json).

## Possible Enhancements

- Use NLP and transcriptions to detect the environment in the movie and adjust the environment accordingly. For instance, if a desert is detected, the heating could be increased.
- Implement sound analysis AI to detect environmental sounds like rain or wind and act accordingly.
- Use object detection or sentiment analysis to further understand the scene and respond in a more nuanced way.
