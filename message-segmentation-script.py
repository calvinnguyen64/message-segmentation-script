# message_segementation
# string_to_convert: the message to be segmented, converted into a string.
# character_limit: the maximum number of characters allowed before splitting the message into segments.
# gets string of a message and segments it when given character limit is reached.
def message_segementation(string_to_convert, character_limit):
    count = 0
    result = ''

    for character in string_to_convert:
        count+=1
        if count % character_limit == 0:
            result = result + "\n\n--------------------------------------------\n\n"
        else: result+="{}".format(character)
        #if keyword "IMAGE " is typed in the document (case-sensitive), replace the word and create a space that notifies the user to paste in their image when pasting over the message
        if count >= 6 and ''.join(string_to_convert[count - 6:count]) == "IMAGE ":
            result = result[:-6]
            result += ("\n\nPASTE IMAGE HERE\n\n")
    return result

with open("original_message_to_read.txt", "r", encoding='utf-8') as file_to_read:
    lines = file_to_read.readlines()
    with open("formatted_message_to_paste.txt", "w", encoding='utf-8') as file_to_write:
        file_to_write.write(message_segementation(''.join(lines), 2000)) #run function with 2000 character limit

#ToDo ask for keyboard input of how character limit

#ToDo Tests
#assert that IMAGE not in result
#assert first para is less than 2000 chars?
#hit as many lines as possible dont have to do it
#test 1 empty txt file || assert result = ''
#test 2 txt file has less character limit and no IMAGE || assert result = result
#test 3 if spacing goes back to previous space correctly if character limit is in the middle of a word || assert that end of string cuts off assert with result = 'exact string where words are cut off'
#test 4 if I have exact mutliple of 2000s (ex 6000) what happens to the new line at the end? expectation is nothing 
#test 5 has image, does paste image 
#test 6 has no image