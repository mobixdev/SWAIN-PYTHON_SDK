# QueryFilter

Filter conditions for querying entities using complex expressions Supports logical operations (AND, OR, NOT), field comparisons, and relationship filtering Example: { \"expressions\": [ {\"field\": \"age\", \"operator\": \"gte\", \"value\": 18}, { \"operator\": \"AND\", \"expressions\": [ {\"field\": \"status\", \"operator\": \"eq\", \"value\": \"active\"} ] } ] }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregations** | [**QueryAggregationSpec**](QueryAggregationSpec.md) | @Description Aggregations can specify functions like COUNT, SUM, GROUP BY, etc. @Description If not provided, no aggregations will be performed. @Description Used for data analysis and reporting queries | [optional] 
**expressions** | **List[object]** | @Description Array of expressions to filter entities @Description Each expression can be a FieldExpression, LogicalExpression, or RelationshipExpression @Description If empty, no filtering will be applied | [optional] 
**projections** | **List[str]** | @Description Array of field names to select from the main entity @Description If empty, all fields will be selected @Description Example: [\&quot;id\&quot;, \&quot;name\&quot;, \&quot;email\&quot;] to select only those fields | [optional] 
**sort** | [**List[QuerySortSpec]**](QuerySortSpec.md) | @Description Array of sort specifications to order the results @Description Example: [{\&quot;field\&quot;: \&quot;name\&quot;, \&quot;direction\&quot;: \&quot;asc\&quot;}, {\&quot;field\&quot;: \&quot;createdAt\&quot;, \&quot;direction\&quot;: \&quot;desc\&quot;}] @Description Field names can be struct field names or database column names. Direction is case-insensitive (&#39;asc&#39; or &#39;desc&#39;). | [optional] 

## Example

```python
from openapi_client.models.query_filter import QueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of QueryFilter from a JSON string
query_filter_instance = QueryFilter.from_json(json)
# print the JSON string representation of the object
print(QueryFilter.to_json())

# convert the object into a dict
query_filter_dict = query_filter_instance.to_dict()
# create an instance of QueryFilter from a dict
query_filter_from_dict = QueryFilter.from_dict(query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


