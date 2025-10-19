# Learning Notes Serverless API – Full Infrastructure as Code (IaC) Deployment

## 🧭 Overview
This project demonstrates my complete learning journey with **AWS CloudFormation**, **Lambda**, **API Gateway**, **DynamoDB**, **S3**, and **CloudFront**.  
The objective was to design, build, and deploy a **serverless REST API** called **“Learning Notes API”** using 100% Infrastructure-as-Code principles.  
It aligns with the MSc DevOps (Level 9) outcomes, showcasing automation, scalability, observability, and secure cloud engineering practices.

---

## 🏗️ Architecture Overview
Client (Postman / cURL)
↓
API Gateway (REST)
↓
Lambda Function (Python)
↓
DynamoDB Table (LearningNotes)
↓
S3 Bucket + CloudFront (artifact hosting and CDN)


Each component is defined and deployed via modular CloudFormation stacks orchestrated by a master template.

---

## Work Completed So Far

### Phase 1 – Lambda Foundation
- Created a **CloudFormation template** for a simple Lambda function.
- Defined an **IAM Role** (`LambdaBasicExecutionRole`) with managed policy `AWSLambdaBasicExecutionRole`.
- Tested deployment using **AWS CLI** commands:
  ```
  aws cloudformation deploy --template-file infrastructure/lambda.yaml --stack-name lambda-stack --capabilities CAPABILITY_NAMED_IAM
Verified function creation and executed successful test invocation:


aws lambda list-functions
aws lambda invoke --function-name HelloLambda output.json

### Phase 2 – API Gateway Integration
- Added API Gateway REST API (HelloApi) integrated with the Lambda function.
- Created the /hello endpoint with a GET method using AWS_PROXY integration.
- Granted API Gateway invoke permissions to Lambda.
- Deployed stage prod and tested successfully:
-  curl https://<api-id>.execute-api.<region>.amazonaws.com/prod/hello

### Phase 3 – Learning Notes API Enhancement
- Designed a new API called Learning Notes API to store DevOps learnings.
- Implemented a DynamoDB table (LearningNotes) with partition key topic.
- Updated Lambda handler (/src/handler.py) to support:
- POST /note → add a learning note (topic, note, date)
- GET /note/{topic} → retrieve a specific note
- Added environment variable TABLE_NAME for dynamic configuration.
- Provided DynamoDB read/write permissions to the Lambda IAM role.
- Successfully validated both endpoints via Postman and CLI.


### Phase 4 – S3 Bucket & CloudFront Integration
- Added a versioned S3 bucket and CloudFront distribution using s3.yaml for secure artifact hosting.
- Enabled public access blocking and server-side encryption.
- Granted policies: CloudFrontFullAccess, AmazonS3FullAccess, AmazonDynamoDBFullAccess
-  Uploaded Lambda package and templates:
     a.  ```aws s3 cp build/handler.zip s3://<bucket-name>/lambda/lambda.zip```
     b.  ```aws s3 cp infrastructure/ s3://<bucket-name>/infra/ --recursive --exclude "" --include ".yaml" ```

### Phase 5 – Full Master Stack Deployment :

- ```aws cloudformation deploy --stack-name learning-notes-s3 --template-file infrastructure/s3.yaml --parameter-overrides BucketName=<bucket-name> ```
- Deployed Master Stack integrating all services:
- ```aws cloudformation deploy --stack-name learning-notes-master --template-file infrastructure/master-template.yaml --parameter-overrides S3Bucket=<bucket-name> S3Key=lambda/lambda.zip --capabilities CAPABILITY_NAMED_IAM ```
- Confirmed stack creation and fetched output values (API URL, DynamoDB table name, Lambda function name):
- aws cloudformation describe-stacks --stack-name learning-notes-master --query "Stacks[0].Outputs"


### Repository Structure
/infrastructure
  ├── s3.yaml               # Defines S3 bucket + CloudFront distribution
  ├── database.yaml         # Defines DynamoDB table
  ├── lambda.yaml           # Defines Lambda function + IAM role
  ├── api.yaml              # Defines API Gateway + integrations
  └── master-template.yaml  # Orchestrates all nested stacks
/src
  └── handler.py            # Lambda logic for POST/GET endpoints
/tests
  └── test_lambda.py        # Local unit tests using pytest
README.md
