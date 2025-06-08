# GithubComTakifouhalCrudsqlPkgInternalAuthModelsRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** | Role name must be unique | [optional] 
**permissions** | [**List[GithubComTakifouhalCrudsqlPkgInternalAuthModelsPermission]**](GithubComTakifouhalCrudsqlPkgInternalAuthModelsPermission.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**users** | [**List[GithubComTakifouhalCrudsqlPkgInternalAuthModelsUser]**](GithubComTakifouhalCrudsqlPkgInternalAuthModelsUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.github_com_takifouhal_crudsql_pkg_internal_auth_models_role import GithubComTakifouhalCrudsqlPkgInternalAuthModelsRole

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTakifouhalCrudsqlPkgInternalAuthModelsRole from a JSON string
github_com_takifouhal_crudsql_pkg_internal_auth_models_role_instance = GithubComTakifouhalCrudsqlPkgInternalAuthModelsRole.from_json(json)
# print the JSON string representation of the object
print(GithubComTakifouhalCrudsqlPkgInternalAuthModelsRole.to_json())

# convert the object into a dict
github_com_takifouhal_crudsql_pkg_internal_auth_models_role_dict = github_com_takifouhal_crudsql_pkg_internal_auth_models_role_instance.to_dict()
# create an instance of GithubComTakifouhalCrudsqlPkgInternalAuthModelsRole from a dict
github_com_takifouhal_crudsql_pkg_internal_auth_models_role_from_dict = GithubComTakifouhalCrudsqlPkgInternalAuthModelsRole.from_dict(github_com_takifouhal_crudsql_pkg_internal_auth_models_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


