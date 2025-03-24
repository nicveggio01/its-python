def build_profile(user_info):
    profile = {
        "first_name":input("Enter your first name: "),
        "last_name":input("Enter your last name: "),
        "age":input("Enter your age: "),
        "city":input("Enter your city: "),
        "height":input("Enter your height: ")
  }
    return profile

for key, value in build_profile("user_info").items():
    print(f"{key}:{value}")
