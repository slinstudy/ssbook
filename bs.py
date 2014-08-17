from douban_client import DoubanClient

API_KEY = '0e5eae024adb9ce12b1c0a06e092d6a3'
API_SECRET = '9f7ef068498fc361'

# 在 OAuth 2.0 中，
# 获取权限需要指定相应的 scope，请注意!!
# scope 权限可以在申请应用的 "API 权限" 查看。

SCOPE = 'douban_basic_common,shuo_basic_r,shuo_basic_w'

client = DoubanClient(API_KEY, API_SECRET,"http://opac.whsw.tk", SCOPE)

# 以下方式 2 选 1:
# 1. 引导用户授权
print ('Go to the following link in your browser:') 
print (client.authorize_url)
code = input('Enter the verification code:')
client.auth_with_code(code)

# 2. 如果有之前有 token，则可以
#client.auth_with_token(token)

# Token Code
token_code = client.token_code

# Refresh Token
# 请注意：`refresh_token_code` 值仅可在授权完成时获取(即在 `auth_with_code`, `auth_with_password` 之后)
refresh_token_code = client.refresh_token_code
client.refresh_token(refresh_token_code) # refresh token