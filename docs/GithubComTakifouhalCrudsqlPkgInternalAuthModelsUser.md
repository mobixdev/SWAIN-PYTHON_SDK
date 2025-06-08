# GithubComTakifouhalCrudsqlPkgInternalAuthModelsUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_data** | **Dict[str, object]** |  | [optional] 
**anonymous** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**last_login** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**roles** | [**List[GithubComTakifouhalCrudsqlPkgInternalAuthModelsRole]**](GithubComTakifouhalCrudsqlPkgInternalAuthModelsRole.md) |  | [optional] 

## Example

```python
from openapi_client.models.github_com_takifouhal_crudsql_pkg_internal_auth_models_user import GithubComTakifouhalCrudsqlPkgInternalAuthModelsUser

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTakifouhalCrudsqlPkgInternalAuthModelsUser from a JSON string
github_com_takifouhal_crudsql_pkg_internal_auth_models_user_instance = GithubComTakifouhalCrudsqlPkgInternalAuthModelsUser.from_json(json)
# print the JSON string representation of the object
print(GithubComTakifouhalCrudsqlPkgInternalAuthModelsUser.to_json())

# convert the object into a dict
github_com_takifouhal_crudsql_pkg_internal_auth_models_user_dict = github_com_takifouhal_crudsql_pkg_internal_auth_models_user_instance.to_dict()
# create an instance of GithubComTakifouhalCrudsqlPkgInternalAuthModelsUser from a dict
github_com_takifouhal_crudsql_pkg_internal_auth_models_user_from_dict = GithubComTakifouhalCrudsqlPkgInternalAuthModelsUser.from_dict(github_com_takifouhal_crudsql_pkg_internal_auth_models_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


