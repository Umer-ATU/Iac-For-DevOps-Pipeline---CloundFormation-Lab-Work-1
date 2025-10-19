# Lambda Learning Project Progress

## Overview
This project demonstrates my learning progress with **AWS Lambda**, **API Gateway**, and **CloudFormation**.  
The goal is to deploy a simple Lambda function (`HelloLambda`) using CloudFormation, expose it through a RESTful API Gateway endpoint, test it via AWS CLI, and understand IAM role and policy requirements in a real Infrastructure-as-Code (IaC) workflow.

---

## Work Completed So Far

### Phase 1 – Lambda Foundation
- Created a **CloudFormation template** for a simple Lambda function.
- Defined an **IAM Role** (`LambdaBasicExecutionRole`) with the managed policy `AWSLambdaBasicExecutionRole`.
- Tested deployment via **AWS CLI**:
  - Created the stack using `--capabilities CAPABILITY_NAMED_IAM`.
  - Verified Lambda function exists using `aws lambda list-functions`.
  - Invoked the function successfully using `aws lambda invoke`.

### Phase 2 – API Gateway Integration
- Added **API Gateway REST API** (`HelloApi`) connected to the Lambda function.
- Created a new resource `/hello` and defined a `GET` method.
- Integrated Lambda with **AWS_PROXY** mode for full event forwarding.
- Added **Lambda invoke permissions** for API Gateway.
- Added **API deployment stage** (`prod`) and exposed endpoint via Outputs.
- Tested endpoint using:
  ```bash
  curl https://<api-id>.execute-api.<region>.amazonaws.com/prod/hello
