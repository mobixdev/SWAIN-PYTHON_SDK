# ApiModelsResponse

Response containing a map of all registered models and their table names

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | **Dict[str, str]** | Models is a map of model names to their corresponding table names example: {\&quot;User\&quot;: \&quot;users\&quot;, \&quot;Post\&quot;: \&quot;posts\&quot;} | [optional] 

## Example

```python
from openapi_client.models.api_models_response import ApiModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiModelsResponse from a JSON string
api_models_response_instance = ApiModelsResponse.from_json(json)
# print the JSON string representation of the object
print(ApiModelsResponse.to_json())

# convert the object into a dict
api_models_response_dict = api_models_response_instance.to_dict()
# create an instance of ApiModelsResponse from a dict
api_models_response_from_dict = ApiModelsResponse.from_dict(api_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


