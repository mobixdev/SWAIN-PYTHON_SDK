# QueryAggregationSpec

Allows specifying functions like COUNT, SUM on fields, with an optional group-by clause Used for aggregating data in queries, similar to SQL GROUP BY with aggregate functions Example: {\"functions\": [{\"type\": \"COUNT\", \"field\": \"id\"}], \"group_by\": [\"status\"]}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expressions** | **List[object]** | @Description Optional aggregator-based conditions to be applied in a HAVING clause (if using SQL) @Description These expressions may reference aggregator functions like SUM(...) or COUNT(...) | [optional] 
**functions** | [**List[QueryAggregateFunctionSpec]**](QueryAggregateFunctionSpec.md) | @Description A list of aggregation functions (e.g., COUNT, SUM, MIN, MAX) to apply @Description Each function specifies the type, field, and optional alias | [optional] 
**group_by** | **List[str]** | @Description Fields for grouping results (e.g., by \&quot;status\&quot; or [\&quot;status\&quot;,\&quot;category\&quot;]) @Description Similar to SQL GROUP BY clause | [optional] 

## Example

```python
from openapi_client.models.query_aggregation_spec import QueryAggregationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAggregationSpec from a JSON string
query_aggregation_spec_instance = QueryAggregationSpec.from_json(json)
# print the JSON string representation of the object
print(QueryAggregationSpec.to_json())

# convert the object into a dict
query_aggregation_spec_dict = query_aggregation_spec_instance.to_dict()
# create an instance of QueryAggregationSpec from a dict
query_aggregation_spec_from_dict = QueryAggregationSpec.from_dict(query_aggregation_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


