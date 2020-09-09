def machine():

    keys='abcdefghijklmnopqrstuvwxyz !'
    values=keys[-1]+keys[0:-1]

    """
    In encrytpDict:       In decryptDict:
      keys   Values       keys   Values
       'a'    '!'          '!'    'a'
       'b'    'a'          'a'    'b'
        .      .            .      .
        .      .            .      .
        .      .            .      .
    """
    

    encryptDict=dict(zip(keys,values))
    decryptDict=dict(zip(values,keys))

    """
    Asking user for the user input and the mode.

    """

    message=input("Please enter your secret message")
    mode=input("Please enter your mode: Encode(E) or Decode(D)")

    """
    if the mode is encryption(E)/decryption(D):
        We will create a listin which we run a dictionary comprehension and 
        if that particular letter is there in  encrytion/decryption dictionary , we will 
        fetch the value of that letter and we will append that to list.Similary 
        for other letters in the message.
    """

    if mode.upper()=='E':
        newMessage=''.join([encryptDict[letter] for letter in message.lower()])
    elif mode.upper()=='D':
        newMessage=''.join([decryptDict[letter] for letter in message.lower()])
    else:
        print("Please enter a correct choice")

    return newMessage

print(machine())


