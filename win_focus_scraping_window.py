import time
import pygetwindow as gw
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def focus_scarping_window(driver):
    try:

        # Step 2: Get window handle of the Chrome instance opened with remote debugging
        remote_debugging_handle = driver.current_window_handle
        remote_window_title = driver.title
        remote_window_url = driver.current_url

        print(f"Connected to Chrome window: {remote_window_title} ({remote_window_url})")
        print(f"Remote Debugging Window Handle: {remote_debugging_handle}")

        # Step 3: Get all open Chrome windows and find the correct one
        all_windows = gw.getWindowsWithTitle("Google Chrome")  # Get all Chrome windows

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
