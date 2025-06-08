# ApiSuccessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.api_success_response import ApiSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSuccessResponse from a JSON string
api_success_response_instance = ApiSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(ApiSuccessResponse.to_json())

# convert the object into a dict
api_success_response_dict = api_success_response_instance.to_dict()
# create an instance of ApiSuccessResponse from a dict
api_success_response_from_dict = ApiSuccessResponse.from_dict(api_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


