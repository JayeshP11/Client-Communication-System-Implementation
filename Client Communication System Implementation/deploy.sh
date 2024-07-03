#!/bin/bash

# Deploy to AWS
aws s3 cp jira-workflow.py s3://my-bucket/jira-workflow.py
aws s3 cp github-api.py s3://my-bucket/github-api.py
aws s3 cp google-docs-api.py s3://my-bucket/google-docs-api.py

# Deploy to Google Cloud
gcloud storage cp jira-workflow.py gs://my-bucket/jira-workflow.py
gcloud storage cp github-api.py gs://my-bucket/github-api.py
gcloud storage cp google-docs-api.py gs://my-bucket/google-docs-api.py