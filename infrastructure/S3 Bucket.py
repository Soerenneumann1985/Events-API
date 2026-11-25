import aws_cdk as cdk
from aws_cdk import aws_s3 as s3

class GrocerymateInfraStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        s3.Bucket(
            self,
            "GroceryMateBucket",
            bucket_name="grocerymate-user-avatars",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
        )