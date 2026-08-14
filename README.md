# Event-Driven Auto-Remediation and Observability System on AWS

Capstone project: a fully event-driven DevOps pipeline on AWS that detects
configuration drift, fans events out to multiple consumers, auto-remediates
non-compliant resources, and provides full observability.

## Architecture

1. **AWS Config** detects a non-compliant security group (open SSH).
2. **EventBridge** captures the compliance-change event and fans it out to:
   - **SQS** (audit trail)
   - **Kinesis** (event streaming)
   - **Step Functions** (remediation workflow)
3. **Step Functions** invokes a **Lambda** to evaluate the finding, then
   triggers **Systems Manager Automation** to remediate the resource.
4. **CloudWatch** and **X-Ray** provide logs, metrics, and traces across
   the pipeline.

## Repo structure

- `cli-scripts/` — AWS CLI commands and IAM/bucket/Config JSON policies, one file per step
- `lambda/` — Lambda function source code
- `step-functions/` — Step Functions state machine definition
- `screenshots/` — Console evidence for each grading checkpoint

## Progress

- [x] Step 1: AWS Config enabled (recorder + delivery channel)
- [x] Step 2: Config rule for open SSH detection
- [x] Step 3: SQS queue
- [x] Step 4: Kinesis stream
- [ ] Step 5: Lambda evaluator
- [ ] Step 6: Step Functions workflow
- [ ] Step 7: EventBridge fan-out rule
- [ ] Step 8: CloudWatch + X-Ray monitoring
- [ ] Step 9: End-to-end test