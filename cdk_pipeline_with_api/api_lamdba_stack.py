from aws_cdk import core as cdk


from . import widget_service

class MyLambdaStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
    
        # Call the labmda function
        # The code that defines your stack goes here
        widget_service.WidgetService(self, "Widgets")  # Passing 'scope' and 'id' for construct