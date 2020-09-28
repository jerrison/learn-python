def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything we know about a user.
    """
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_info = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_info)

# For arbitrary keyword arguments, a dictionary named "kwargs" is created and the
# key-value pairs are created in the dictionary