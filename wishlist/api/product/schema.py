from marshmallow import Schema, fields, validate


class ProductSchema(Schema):
    title = fields.String(description="Product Name", required=False)
    brand = fields.String(description="Product Brand", required=False)
    image = fields.String(description="Product image URL", required=False)
    price = fields.Float(description="Product Price", required=False)
    reviewScore = fields.Float(description="Product Review Score", required=False)
