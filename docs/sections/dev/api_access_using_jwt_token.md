# API Access using JWT token

The API endpoints are secured and expect a Bearer token in the headers.

You can get the required token (for Enterprise customers) using this endpoint:

[http://userstore.NICKNAME.biodati.com/#/Authentication/get_api_token_auth_api_token_post](http://userstore.NICKNAME.biodati.com/#/Authentication/get_api_token_auth_api_token_post)

Just replace NICKNAME with the appropriate value.

or for the BioDati Studio Demo server:

[http://userstore.biodatistudio.com/#/Authentication/get_api_token_auth_api_token_post](http://userstore.biodatistudio.com/#/Authentication/get_api_token_auth_api_token_post)


Add the token to any REST API requests you have by adding an http header using the following format:

    AUTHORIZATION: Bearer <token>

!!! note
    The token will expire after a year and will need to be updated. If you get a 401 error from the API call, the token is invalid and needs to be updated. Of course, this token is basically the same as your password.

!!! warning
    This token is basically your password for this account. Please keep it secure. If you need to change it, just access
    the endpoint to get a new token which will invalidate the old token.
