# GithubComTakifouhalCrudsqlPkgInternalAuthModelsPermission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_actions** | **str** | Comma-separated actions: \&quot;read,create,update,delete\&quot;, \&quot;*\&quot; | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**entity_name** | **str** | e.g., \&quot;users\&quot;, \&quot;orders\&quot;, \&quot;*\&quot; | [optional] 
**id** | **int** |  | [optional] 
**roles** | [**List[GithubComTakifouhalCrudsqlPkgInternalAuthModelsRole]**](GithubComTakifouhalCrudsqlPkgInternalAuthModelsRole.md) |  | [optional] 
**scope_expression** | **List[int]** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.github_com_takifouhal_crudsql_pkg_internal_auth_models_permission import GithubComTakifouhalCrudsqlPkgInternalAuthModelsPermission

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTakifouhalCrudsqlPkgInternalAuthModelsPermission from a JSON string
github_com_takifouhal_crudsql_pkg_internal_auth_models_permission_instance = GithubComTakifouhalCrudsqlPkgInternalAuthModelsPermission.from_json(json)
# print the JSON string representation of the object
print(GithubComTakifouhalCrudsqlPkgInternalAuthModelsPermission.to_json())

# convert the object into a dict
github_com_takifouhal_crudsql_pkg_internal_auth_models_permission_dict = github_com_takifouhal_crudsql_pkg_internal_auth_models_permission_instance.to_dict()
# create an instance of GithubComTakifouhalCrudsqlPkgInternalAuthModelsPermission from a dict
github_com_takifouhal_crudsql_pkg_internal_auth_models_permission_from_dict = GithubComTakifouhalCrudsqlPkgInternalAuthModelsPermission.from_dict(github_com_takifouhal_crudsql_pkg_internal_auth_models_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


