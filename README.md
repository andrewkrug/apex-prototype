# Apex prototype deployment

This apex project was created to demonstrate what is possible.  In order to use
it with Mozilla's MFA configuration you'll need to use a python command line module called
aws-mfa since the GoSDK does not have the same support as boto.  

To use this start by:

1. `pip install -r requirements.txt`
2. Edit your ~/.aws/credentials file and create a profile that looks like this with
static access keys that give you the ability to assume_role.
```
[defult-long-term]
aws_access_key_id = YOUR_LONGTERM_KEY_ID
aws_secret_access_key = YOUR_LONGTERM_ACCESS_KEY
```

I set up a bash alias for convenience after this that looks like:

alias idaws="/Users/akrug/Library/Python/2.7/bin/aws-mfa --device arn:aws:iam::371522382791:mfa/akrug --assume-role arn:aws:iam::656532927350:role/InfosecAdmin --role-session-name \"andrew-mac\""

My creds generated in this manner are good for 60-minutes.  I could set up additional aliases for additional profiles if necessary.

### Install Apex
