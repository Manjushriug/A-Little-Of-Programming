### Country Capital Chatbot
1. DEFINE dictionary country_capitals
   a. SET key-value pairs with country names in lowercase and their capitals

2. FUNCTION get_user_input
   a. WHILE True
      i. PROMPT user for input with message "Enter a country name (or type 'exit' to quit):"
      ii. IF user input is None OR user input is "exit"
          A. CALL display_response with message "Thank you for using the bot! Goodbye!"
          B. BREAK loop
      iii. NORMALIZE user input to lowercase
      iv. LOOKUP normalized_input in country_capitals
      v. IF found
          A. SET answer to the corresponding capital
      vi. ELSE
          A. SET answer to "Sorry, I don't know that country."
      vii. CALL display_response with answer

3. FUNCTION display_response(text)
   a. CLEAR previous display
   b. DISPLAY text at center of the screen

4. SET UP turtle graphics
   a. TITLE window "Country Capital Chatbot"
   b. SET background color to light blue

5. DISPLAY instruction message "Press Enter to ask for a country capital."

6. LISTEN for key presses
   a. BIND Enter key to call get_user_input

7. START turtle main loop
