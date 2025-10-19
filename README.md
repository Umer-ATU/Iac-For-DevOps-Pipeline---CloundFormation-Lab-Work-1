# Lambda Learning Project Progress

## Overview
This project demonstrates my learning progress with AWS Lambda and CloudFormation.  
The goal was to deploy a simple Lambda function (`HelloLambda`) using CloudFormation, test it via AWS CLI, and understand IAM role and policy requirements.

## Work Completed So Far
- Created a CloudFormation template for a simple Lambda function.
- Defined an IAM Role (`LambdaBasicExecutionRole`) with managed policy `AWSLambdaBasicExecutionRole`.
- Tested deployment via CLI:
  - Created the stack with proper capabilities (`CAPABILITY_NAMED_IAM`).
  - Verified Lambda function exists using `aws lambda list-functions`.
  - Invoked the function successfully using `aws lambda invoke`.

## Errors Encountered and Solutions

1. **Error:** Using a User ARN for Lambda Role  
   - **Message:** `'arn:aws:iam::919586551133:user/Umer-01-IAM' does not match role ARN pattern`  
   - **Solution:** Created a proper IAM Role and attached the managed policy.  

2. **Error:** Stack creation failed due to missing IAM capability  
   - **Message:** `InsufficientCapabilitiesException: Requires capabilities: [CAPABILITY_NAMED_IAM]`  
   - **Solution:** Added `--capabilities CAPABILITY_NAMED_IAM` flag during stack creation.  

3. **Error:** Lambda function not found / list-functions returns empty  
   - **Cause:** Stack rolled back due to IAM permission issues  
   - **Solution:** Verified user has IAM permissions to create roles, deleted failed stack, recreated stack successfully.  

## Next Steps
- Continue extending the Lambda project with additional functions and integrations.
- Prepare final assignment submission with full documentation and tested deployment.

## Branching Strategy
- Current progress: `feature/lambda-learning-progress`  
- Final submission: `submission/final-assignment`
