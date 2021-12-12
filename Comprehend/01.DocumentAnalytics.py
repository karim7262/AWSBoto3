#!pip install boto3
#!pip install awscli
#!aws configure
# AWS_ACCESS_KEY_ID:		AKIAWEF7VXIGWS7N6NXM
# AWS_SECRET_ACCESS_KEY: 	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
# Default region name [None]: us-east-1
# Default output format [None]: table

#!aws s3 ls s3://bkt0222mujahed/

import boto3
import json

comprehend=boto3.client(service_name="comprehend")
text=input("Enter Your Message to Start Analytics(NLP): ")
strLanguageResult=comprehend.detect_dominant_language(Text=text)
strEntityResult=comprehend.detect_entities(Text=text,LanguageCode="en")
strEntityResult=comprehend.detect_key_phrases(Text=text,LanguageCode="en")
strEntityResult=comprehend.detect_sentiment(Text=text,LanguageCode="en")

print("Detection Done")
jsonLanguageResult=json.dumps(strLanguageResult,sort_keys=True,indent=4)
print("JSON Conversion Done")
print(jsonLanguageResult)