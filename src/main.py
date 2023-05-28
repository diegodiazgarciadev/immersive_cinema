import asyncio
import cv2
import numpy as np
from datetime import datetime
from mss import mss
from utils import control_plug, load_config, setup_device

async def main():
    # Load configuration
    credentials = load_config("../config/credentials.json")
    config = load_config("../config/constants.json")

    # Initialize the device
    dev, manager = await setup_device(credentials["email"], credentials["password"], "mss210")
    if dev is None:
        return

    # Initialize MSS and buffer for brightness tracking
    sct = mss()
    brightness_buffer = [0] * config['buffer_size']
    is_dark = False

    # Main loop
    while True:
        # Capture a screenshot and process it
        screenshot = sct.grab(config['capture_region'])
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
        frame = cv2.resize(frame, (frame.shape[1] // 3, frame.shape[0] // 3))

        # Convert to grayscale and compute average brightness
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        current_brightness = np.mean(gray)
        brightness_buffer.pop(0)
        brightness_buffer.append(current_brightness)
        buffer_average = np.mean(brightness_buffer)

        # Act on brightness change
        if len(brightness_buffer) == config['buffer_size']:
            if buffer_average < config['dark_threshold'] and not is_dark:
                print(f"{datetime.now()}: Change of brightness detected in the movie - it got darker.")
                await control_plug(dev, 'off')
                is_dark = True
            elif buffer_average > config['light_threshold'] and is_dark:
                print(f"{datetime.now()}: Change of brightness detected in the movie - it got brighter.")
                await control_plug(dev, 'on')
                is_dark = False

        # Handle key events
        cv2.imshow("Output", frame)
        if cv2.waitKey(15) & 0xFF == ord('q'):
            break

    # Cleanup
    cv2.destroyAllWindows()
    manager.close()
    await manager.http_client.async_logout()

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
