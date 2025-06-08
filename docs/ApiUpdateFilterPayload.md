# ApiUpdateFilterPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expressions** | **List[object]** |  | [optional] 
**update_data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from openapi_client.models.api_update_filter_payload import ApiUpdateFilterPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUpdateFilterPayload from a JSON string
api_update_filter_payload_instance = ApiUpdateFilterPayload.from_json(json)
# print the JSON string representation of the object
print(ApiUpdateFilterPayload.to_json())

# convert the object into a dict
api_update_filter_payload_dict = api_update_filter_payload_instance.to_dict()
# create an instance of ApiUpdateFilterPayload from a dict
api_update_filter_payload_from_dict = ApiUpdateFilterPayload.from_dict(api_update_filter_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


