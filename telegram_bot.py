from bs4 import BeautifulSoup

def count_emoji_in_html(file_path, target_emoji):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract all text from the HTML
        text_content = soup.get_text()
        
        # Count occurrences of the target emoji
        emoji_count = text_content.count(target_emoji)
        
        return emoji_count
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage
file_path = 'E:\Vs code\Python\chat_01\messages24.html'
target_emoji = ''  # Replace with the emoji you want to count

emoji_count = count_emoji_in_html(file_path, target_emoji)
print(f"The emoji '{target_emoji}' appears {emoji_count} times in the file '{file_path}'.")
