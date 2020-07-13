from marshmallow import Schema, fields, validate


class RegisterSchema(Schema):
    username = fields.String(description='Your Fullname', required=True)
    email = fields.String(description='Your email', required=True)
    password = fields.String(description='Your password', required=True)
    
class LoginSchema(Schema):
    email = fields.String(description='Your email', required=True)
    password = fields.String(description='Your password', required=True)
