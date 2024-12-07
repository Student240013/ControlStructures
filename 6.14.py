facebook = True
twitter = False
instagram = True

account_count = sum([facebook, twitter, instagram])

if account_count >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")