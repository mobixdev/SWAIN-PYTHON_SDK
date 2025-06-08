# openapi_client.DynamicApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**model_count_post**](DynamicApi.md#model_count_post) | **POST** /{model}/count | Count entities by filter
[**model_filter_post**](DynamicApi.md#model_filter_post) | **POST** /{model}/filter | Filter entities
[**model_get**](DynamicApi.md#model_get) | **GET** /{model} | List entities
[**model_id_delete**](DynamicApi.md#model_id_delete) | **DELETE** /{model}/{id} | Delete an entity
[**model_id_get**](DynamicApi.md#model_id_get) | **GET** /{model}/{id} | Get an entity by ID
[**model_id_put**](DynamicApi.md#model_id_put) | **PUT** /{model}/{id} | Update an entity
[**model_post**](DynamicApi.md#model_post) | **POST** /{model} | Create a new entity


# **model_count_post**
> Dict[str, object] model_count_post(model, filter=filter)

Count entities by filter

Count entities that match the given filter criteria.

### Example


```python
import openapi_client
from openapi_client.models.api_filter_payload import ApiFilterPayload
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
    api_instance = openapi_client.DynamicApi(api_client)
    model = 'model_example' # str | Model name
    filter = openapi_client.ApiFilterPayload() # ApiFilterPayload | Filter conditions (optional) (optional)

    try:
        # Count entities by filter
        api_response = api_instance.model_count_post(model, filter=filter)
        print("The response of DynamicApi->model_count_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicApi->model_count_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model name | 
 **filter** | [**ApiFilterPayload**](ApiFilterPayload.md)| Filter conditions (optional) | [optional] 

### Return type

**Dict[str, object]**

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

# **model_filter_post**
> QueryFilterResponse model_filter_post(model, filter, page=page, page_size=page_size)

Filter entities

Filter entities using complex conditions in the request body, including field expressions, logical operations, and relationship filtering

### Example


```python
import openapi_client
from openapi_client.models.query_filter import QueryFilter
from openapi_client.models.query_filter_response import QueryFilterResponse
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
    api_instance = openapi_client.DynamicApi(api_client)
    model = 'model_example' # str | model name
    filter = openapi_client.QueryFilter() # QueryFilter | Filter conditions, including optional 'sort' array (e.g., {\\
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 10 # int | Items per page (optional) (default to 10)

    try:
        # Filter entities
        api_response = api_instance.model_filter_post(model, filter, page=page, page_size=page_size)
        print("The response of DynamicApi->model_filter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicApi->model_filter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| model name | 
 **filter** | [**QueryFilter**](QueryFilter.md)| Filter conditions, including optional &#39;sort&#39; array (e.g., {\\ | 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 10]

### Return type

[**QueryFilterResponse**](QueryFilterResponse.md)

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
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_get**
> QueryFilterResponse model_get(model, page=page, page_size=page_size)

List entities

Get a list of entities. Supports pagination and sorting.

### Example


```python
import openapi_client
from openapi_client.models.query_filter_response import QueryFilterResponse
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
    api_instance = openapi_client.DynamicApi(api_client)
    model = 'model_example' # str | Model Name
    page = 56 # int | Page number (optional)
    page_size = 56 # int | Items per page (optional)

    try:
        # List entities
        api_response = api_instance.model_get(model, page=page, page_size=page_size)
        print("The response of DynamicApi->model_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicApi->model_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model Name | 
 **page** | **int**| Page number | [optional] 
 **page_size** | **int**| Items per page | [optional] 

### Return type

[**QueryFilterResponse**](QueryFilterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_id_delete**
> object model_id_delete(model, id)

Delete an entity

Delete an entity by its ID

### Example


```python
import openapi_client
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
    api_instance = openapi_client.DynamicApi(api_client)
    model = 'model_example' # str | Model Name
    id = 'id_example' # str | Entity ID

    try:
        # Delete an entity
        api_response = api_instance.model_id_delete(model, id)
        print("The response of DynamicApi->model_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicApi->model_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model Name | 
 **id** | **str**| Entity ID | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted entity |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_id_get**
> object model_id_get(model, id)

Get an entity by ID

Retrieve a single entity by its ID

### Example


```python
import openapi_client
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
    api_instance = openapi_client.DynamicApi(api_client)
    model = 'model_example' # str | Model Name
    id = 'id_example' # str | Entity ID

    try:
        # Get an entity by ID
        api_response = api_instance.model_id_get(model, id)
        print("The response of DynamicApi->model_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicApi->model_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model Name | 
 **id** | **str**| Entity ID | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_id_put**
> object model_id_put(model, id, entity)

Update an entity

Update an existing entity by its ID

### Example


```python
import openapi_client
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
    api_instance = openapi_client.DynamicApi(api_client)
    model = 'model_example' # str | Model Name
    id = 'id_example' # str | Entity ID
    entity = None # object | Entity Data

    try:
        # Update an entity
        api_response = api_instance.model_id_put(model, id, entity)
        print("The response of DynamicApi->model_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicApi->model_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model Name | 
 **id** | **str**| Entity ID | 
 **entity** | **object**| Entity Data | 

### Return type

**object**

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_post**
> object model_post(model, entity)

Create a new entity

Create a new entity of the specified model type

### Example


```python
import openapi_client
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
    api_instance = openapi_client.DynamicApi(api_client)
    model = 'model_example' # str | Model Name
    entity = None # object | Entity Data

    try:
        # Create a new entity
        api_response = api_instance.model_post(model, entity)
        print("The response of DynamicApi->model_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DynamicApi->model_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model Name | 
 **entity** | **object**| Entity Data | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

