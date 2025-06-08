# QueryAggregateFunctionSpec

Example: { \"type\": \"COUNT\", \"field\": \"id\", \"alias\": \"count_of_id\" } Represents a single aggregation operation to perform on data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | @Description Optional alias for the result of this aggregation @Description If omitted, the function name may be used as an alias @Description Example: \&quot;total_amount\&quot; for SUM(amount) | [optional] 
**var_field** | **str** | @Description The field on which the aggregation function is applied @Description For COUNT(*), use \&quot;*\&quot; or leave empty | [optional] 
**type** | **str** | @Description The aggregation function type (e.g., COUNT, SUM, MIN, MAX) @Description Common types: COUNT, SUM, AVG, MIN, MAX | [optional] 

## Example

```python
from openapi_client.models.query_aggregate_function_spec import QueryAggregateFunctionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAggregateFunctionSpec from a JSON string
query_aggregate_function_spec_instance = QueryAggregateFunctionSpec.from_json(json)
# print the JSON string representation of the object
print(QueryAggregateFunctionSpec.to_json())

# convert the object into a dict
query_aggregate_function_spec_dict = query_aggregate_function_spec_instance.to_dict()
# create an instance of QueryAggregateFunctionSpec from a dict
query_aggregate_function_spec_from_dict = QueryAggregateFunctionSpec.from_dict(query_aggregate_function_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


