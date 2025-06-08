# AuthAuthResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** |  | [optional] 
**roles** | **List[str]** | Added: Include assigned role names | [optional] 
**token** | **str** |  | [optional] 
**type** | **str** | \&quot;local\&quot;, \&quot;github\&quot;, \&quot;google\&quot;, etc. | [optional] 
**user** | [**GithubComTakifouhalCrudsqlPkgInternalAuthModelsUser**](GithubComTakifouhalCrudsqlPkgInternalAuthModelsUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.auth_auth_result import AuthAuthResult

# TODO update the JSON string below
json = "{}"
# create an instance of AuthAuthResult from a JSON string
auth_auth_result_instance = AuthAuthResult.from_json(json)
# print the JSON string representation of the object
print(AuthAuthResult.to_json())

# convert the object into a dict
auth_auth_result_dict = auth_auth_result_instance.to_dict()
# create an instance of AuthAuthResult from a dict
auth_auth_result_from_dict = AuthAuthResult.from_dict(auth_auth_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


