from aws_cdk import core as cdk
from aws_cdk import core

from .api_lamdba_stack import MyLambdaStack

class MyWidgetServiceStack(cdk.Stage):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        lambdaStack = MyLambdaStack(self, "LambdaStack")  # self -> scope (Stage Construct), "LambdaStack" --> construct_id


        