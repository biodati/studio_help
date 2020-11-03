# API Access using JWT token

## How to access the secured API endpoints

The API endpoints are secured and expect a Bearer token in the headers.

You can get the required token from:
http://studio\_api.<STUDIO\_NICKNAME>.biodati.com/docs#/Security/token\_token\_post

Just replace STUDIO\_NICKNAME with the appropriate value.

You only need to fill in your  **email**  and  **password**  to get the token (the other options are for other types of token requests).

From this endpoint, you will get an id\_token and an access\_token. Please use the id\_token.

Add the id\_token to any REST API requests you have by adding an http header using the following format:

AUTHORIZATION: Bearer <id\_token>

The token will periodically expire (after 24 hours) and will need to be updated. If you get a 401 error from the API call, the token is invalid and needs to be updated.
