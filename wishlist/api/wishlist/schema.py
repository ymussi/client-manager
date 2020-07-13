from marshmallow import Schema, fields, validate


class WishlistSchema(Schema):
    client_id = fields.Integer(description="Client id", required=True)
    product_id = fields.Integer(description="Product id", required=True)
