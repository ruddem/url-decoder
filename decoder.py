import urllib.parse
encodedStr = input("Input String to decode:")
encoded = urllib.parse.unquote(encodedStr)
print("--------------------------------------------------------------------------------------------------------")
print("Encoded-String:")
print(encoded)
