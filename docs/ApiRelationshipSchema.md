# ApiRelationshipSchema

Schema information for a model relationship

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foreign_key** | **str** | ForeignKey is the foreign key in the relationship | [optional] 
**is_polymorphic** | **bool** | IsPolymorphic indicates if the relationship is polymorphic | [optional] 
**is_slice** | **bool** | IsSlice indicates if the relationship is a slice | [optional] 
**join_table** | **str** | JoinTable is the join table in the relationship | [optional] 
**json_name** | **str** | JsonName of the relationship (from JSON tag if available) | [optional] 
**name** | **str** | Name of the relationship (from JSON tag if available) | [optional] 
**polymorphic_type** | **str** | PolymorphicType is the type of the polymorphic relationship | [optional] 
**references** | **str** | References are the references in the relationship | [optional] 
**related_model** | **str** | Name of the related model | [optional] 
**related_table** | **str** | Name of the related table | [optional] 
**type** | **str** | Type of relationship (hasOne, hasMany, belongsTo, manyToMany) | [optional] 

## Example

```python
from openapi_client.models.api_relationship_schema import ApiRelationshipSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRelationshipSchema from a JSON string
api_relationship_schema_instance = ApiRelationshipSchema.from_json(json)
# print the JSON string representation of the object
print(ApiRelationshipSchema.to_json())

# convert the object into a dict
api_relationship_schema_dict = api_relationship_schema_instance.to_dict()
# create an instance of ApiRelationshipSchema from a dict
api_relationship_schema_from_dict = ApiRelationshipSchema.from_dict(api_relationship_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


