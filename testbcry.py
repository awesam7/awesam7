import bcrypt

# The hash to verify
stored_hash = b"$2a$12$31K.FXu96zDKdauSwLCwTe6M9qhwQof8/Xq4WgUVI6u47XbaSWSVy"

# The plaintext value to verify
password = b"pAasW0rd"

# Verify the password
if bcrypt.checkpw(password, stored_hash):
        print("Password matches!")
else:
        print("Password does not match.")

