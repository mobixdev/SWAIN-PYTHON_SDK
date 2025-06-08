# QuerySortSpec

Specifies a field and the direction for sorting (ascending or descending) Example: {\"field\": \"name\", \"direction\": \"asc\"} Field names can be struct field names, JSON field names, or database column names

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | @Description The sort direction: \&quot;asc\&quot; for ascending, \&quot;desc\&quot; for descending @Description Case-insensitive, so \&quot;ASC\&quot;, \&quot;asc\&quot;, and \&quot;Asc\&quot; are all valid | [optional] 
**var_field** | **str** | @Description The name of the field to sort by @Description Can be a struct field name (e.g., \&quot;FirstName\&quot;), JSON field name (from json tag), @Description or database column name (e.g., \&quot;first_name\&quot;) | [optional] 

## Example

```python
from openapi_client.models.query_sort_spec import QuerySortSpec

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySortSpec from a JSON string
query_sort_spec_instance = QuerySortSpec.from_json(json)
# print the JSON string representation of the object
print(QuerySortSpec.to_json())

# convert the object into a dict
query_sort_spec_dict = query_sort_spec_instance.to_dict()
# create an instance of QuerySortSpec from a dict
query_sort_spec_from_dict = QuerySortSpec.from_dict(query_sort_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


