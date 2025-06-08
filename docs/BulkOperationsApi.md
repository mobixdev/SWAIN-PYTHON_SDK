# openapi_client.BulkOperationsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**model_filter_delete**](BulkOperationsApi.md#model_filter_delete) | **DELETE** /{model}/filter | Mass delete entities by filter
[**model_filter_put**](BulkOperationsApi.md#model_filter_put) | **PUT** /{model}/filter | Mass update entities by filter


# **model_filter_delete**
> ApiSuccessResponse model_filter_delete(model, filter)

Mass delete entities by filter

Delete multiple entities that match the given filter criteria. This operation allows deleting multiple records in a single request.

### Example


```python
import openapi_client
from openapi_client.models.api_filter_payload import ApiFilterPayload
from openapi_client.models.api_success_response import ApiSuccessResponse
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
    api_instance = openapi_client.BulkOperationsApi(api_client)
    model = 'model_example' # str | Model name
    filter = openapi_client.ApiFilterPayload() # ApiFilterPayload | Filter conditions

    try:
        # Mass delete entities by filter
        api_response = api_instance.model_filter_delete(model, filter)
        print("The response of BulkOperationsApi->model_filter_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkOperationsApi->model_filter_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model name | 
 **filter** | [**ApiFilterPayload**](ApiFilterPayload.md)| Filter conditions | 

### Return type

[**ApiSuccessResponse**](ApiSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_filter_put**
> ApiSuccessResponse model_filter_put(model, filter)

Mass update entities by filter

Perform bulk updates on multiple entities that match the given filter criteria. This operation allows updating multiple records in a single request.

### Example


```python
import openapi_client
from openapi_client.models.api_success_response import ApiSuccessResponse
from openapi_client.models.api_update_filter_payload import ApiUpdateFilterPayload
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
    api_instance = openapi_client.BulkOperationsApi(api_client)
    model = 'model_example' # str | Model name
    filter = openapi_client.ApiUpdateFilterPayload() # ApiUpdateFilterPayload | Filter conditions and update data

    try:
        # Mass update entities by filter
        api_response = api_instance.model_filter_put(model, filter)
        print("The response of BulkOperationsApi->model_filter_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BulkOperationsApi->model_filter_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model name | 
 **filter** | [**ApiUpdateFilterPayload**](ApiUpdateFilterPayload.md)| Filter conditions and update data | 

### Return type

[**ApiSuccessResponse**](ApiSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

