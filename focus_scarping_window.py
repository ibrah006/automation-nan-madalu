import time
import pygetwindow as gw
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.ie.webdriver import WebDriver

# Connect to the existing Chrome instance
chrome_options = webdriver.ChromeOptions()
chrome_options.debugger_address = "127.0.0.1:9222"  # Remote debugging port


def focus_scarping_window(driver: WebDriver):
    # Create a Selenium WebDriver session (Attach to running Chrome)
    try:

        # Get the current window title
        window_title = driver.title
        print(f"Connected to Chrome window: {window_title}")

        remote_window_title = driver.title

        # Check if the window is currently in focus
        all_windows = gw.getWindowsWithTitle(window_title)

        matched_window = None
        for window in all_windows:
            if remote_window_title in window.title:
                matched_window = window  # Potential match
                break  # Stop once we find the correct window

        # Step 4: Check if the found window is active; if not, bring it to focus
        if matched_window:
            if matched_window.isActive:
                print("User is already focused on the correct Chrome window.")
            else:
                print("User is NOT in the correct Chrome window. Bringing it to focus...")
                matched_window.activate()
        else:
            print("Could not find the remote-debugging Chrome window among open windows.")

    except Exception as e:
        print(f"Error connecting to Chrome: {e}")

    time.sleep(5)  # Keep the script running for debugging purposes
