from aws_cdk import core as cdk
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

import base64
from .app_stage import MyWidgetServiceStack


class CdkPipelineWithApiStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        encoded_secret = 'Z2hwX1JSRVRJekdEd0c1OERnTk5ldDVvNlJVR05aVFpWRjREamIyVw=='
        base64_bytes = encoded_secret.encode('ascii')
        decoded_secret = base64.b64decode(base64_bytes)
        original_secret = decoded_secret.decode('ascii')

        # source = CodePipelineSource.git_hub("SumanOjha/cdk-pipeline-with-api", "master", authentication=core.SecretValue.plain_text(original_secret))
        source = CodePipelineSource.connection(
                        "SumanOjha/cdk-pipeline-with-api", "master",
                        connection_arn="arn:aws:codestar-connections:us-east-1:357568851775:connection/d1007f96-8a03-4a89-b62c-411c8e8b6fdd")
        pipeline =  CodePipeline(self, "Pipeline", 
                        pipeline_name="Pipeline-with-REST-API",
                        synth=ShellStep("Synth", 
                            input=source,
                            commands=[  "python -m venv .venv",
                                        "python -m pip install -r requirements.txt",
                                        "npm config set unsafe-perm true",
                                        "npx cdk synth",
                                        # "npx cdk deploy"
                            ]
                        )
                    )
        stage = pipeline.add_stage(
                        MyWidgetServiceStack(self, "SumanTesting",
                            # env = cdk.Environment(account="357568851775", region="ap-southeast-2"))
                            env = kwargs['env'])
                )
        # This is a test change
