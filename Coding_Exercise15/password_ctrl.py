# Coding Exercise No.15
# Password Controller

def pass_ctrl(password):
    return len(password) > 8

password = password = input("Enter your password: ")

if pass_ctrl(password):
    print("Password is valid ✅")
else:
    print("Password is too short ❌ (must be more than 8 characters)")