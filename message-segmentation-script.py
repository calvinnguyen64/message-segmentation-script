def message_segementation(string_to_convert, limit):
    """
    message_segementation
    string_to_convert: the message to be segmented, converted into a string.
    limit: the maximum number of characters allowed before splitting the message into segments.
    gets string of a message and segments it when given character limit is reached. 
    """
    count = 0
    result = ''

    for character in string_to_convert:
        count+=1
        # If the character limit is reached, crop the message at the last space.
        # Add a segment line to indicate where the user should copy and paste to reach the limit.
        if count % limit == 0:
            last_space_index = result.rfind(" ")
            if last_space_index != -1:
                separator = "\n\n--------------------------------------------\n\n"
                result = result[:last_space_index] + separator + result[last_space_index + 1:] + character
        else: result += character

        # Replace the keyword "IMAGE " (case-sensitive) with a placeholder for the user to paste an image
        if count >= 6 and ''.join(string_to_convert[count - 6:count]) == "IMAGE ":
            result = result[:-6]
            result += ("\n\nPASTE IMAGE HERE\n\n")
    return result

with open("original_message_to_read.txt", "r", encoding='utf-8') as file_to_read:
    lines = file_to_read.readlines()
    while True:
        character_limit = input("Please enter a character limit: ")
        if character_limit.isdigit():
            character_limit = int(character_limit)
            break
        print("Invalid input. Please enter a valid whole number.")
    print(f"Character limit set to: {character_limit}")

    with open("formatted_message_to_paste.txt", "w", encoding='utf-8') as file_to_write:
        file_to_write.write(message_segementation(''.join(lines), character_limit)) #run function with designated character limit
print("Successfully segmented the message.")

# TODO Tests
# assert that IMAGE not in result
# assert first para is less than 2000 chars?
# hit as many lines as possible dont have to do it
# test 1 empty txt file || assert result = ''
# test 2 txt file has less character limit and no IMAGE || assert result = result
# test 3 if spacing goes back to previous space correctly if character limit is in the middle of a word || assert that end of string cuts off assert with result = 'exact string where words are cut off'
# test 4 if I have exact mutliple of 2000s (ex 6000) what happens to the new line at the end? expectation is nothing 
# test 5 has image, does paste image 
# test 6 has no image