import time
from playwright.sync_api import Page

def wait_for_response_complete(page: Page, timeout: int = 30) -> str:
    """
    Waits for the assistant's response to stabilize after submission.
    
    This method polls the latest assistant message's inner text until it no longer changes
    within a specified interval, indicating the streaming response has completed.
    
    Args:
        page (Page): The Playwright page object.
        timeout (int, optional): Maximum time in seconds to wait for stabilization. Defaults to 30.
    
    Returns:
        str: The complete response text.
    
    Raises:
        TimeoutError: If the response does not stabilize within the timeout period.
    """
    latest_response_locator = page.locator('[data-message-author-role="assistant"]').last
    
    start_time = time.time()
    previous_text = ""
    while time.time() - start_time < timeout:
        current_text = latest_response_locator.inner_text()
        if current_text == previous_text and current_text != "":
            return current_text
        previous_text = current_text
        time.sleep(1)  # Poll every second to check for changes
    
    raise TimeoutError("Response did not stabilize within the timeout period.")