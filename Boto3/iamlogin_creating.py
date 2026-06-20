
import boto3
from random import choice


def iamuser_object():
    iamuser = boto3.client(service_name='iam', region_name='us-east-1', aws_access_key_id='',
                           aws_secret_access_key='/')
    return iamuser


def random_password():
    length_of_pass = 8
    valid_chars_password = "qwertyuiop[]asdfghjkl;'zxcvbnm,./123456789!@~#$%^&*()_+-="
    password = []
    for each in range(len(length_of_pass)):
        password.append(choice(valid_chars_password))

    return "".join(password)


def main():
    iamuser = iamuser_object()
    Username = "yegnasivasai@gmail.com"
    Password = random_password()
    PolicyArnn = "arn:aws:iam::aws:policy/AdministratorAccess"
    iamuser.create_user(UserName=Username)
    iamuser.create_login_profile(
        UserName=Username, Password=Password, PasswordResetRequired=False)
    iamuser.attach_user_policy(UserName=Username, PolicyArn=PolicyArnn)
    print("i am username={} and Password={}".format(Username, Password))
    return None


if __name__ == "__main_":
    main()
