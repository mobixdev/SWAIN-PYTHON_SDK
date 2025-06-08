# openapi_client.AuthenticationApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_login_post**](AuthenticationApi.md#auth_login_post) | **POST** /auth/login | User login


# **auth_login_post**
> AuthAuthResult auth_login_post(credentials)

User login

Authenticate with username and password and return JWT and refresh tokens

### Example


```python
import openapi_client
from openapi_client.models.auth_auth_result import AuthAuthResult
from openapi_client.models.auth_login_request import AuthLoginRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthenticationApi(api_client)
    credentials = openapi_client.AuthLoginRequest() # AuthLoginRequest | Login credentials

    try:
        # User login
        api_response = api_instance.auth_login_post(credentials)
        print("The response of AuthenticationApi->auth_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->auth_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | [**AuthLoginRequest**](AuthLoginRequest.md)| Login credentials | 

### Return type

[**AuthAuthResult**](AuthAuthResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

