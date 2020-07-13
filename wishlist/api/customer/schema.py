from marshmallow import Schema, fields, validate


class CostumerSchema(Schema):
    name = fields.String(description='Customer name', required=True)
    email = fields.String(description='Customer email', required=True)
