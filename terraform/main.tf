variable "region" {
  description = "The AWS region"
  default     = "us-west-2"
}

variable "bucket_name" {
  description = "The name of the S3 bucket"
}

variable "log_group_name" {
  description = "The name of the CloudWatch log group"
  default     = "sync-logs"
}

variable "log_stream_name" {
  description = "The name of the CloudWatch log stream"
  default     = "sync-requests"
}

provider "aws" {
  region = var.region
}

# S3 Bucket
resource "aws_s3_bucket" "sync_bucket" {
  bucket = var.bucket_name
  acl    = "private"
}

# CloudWatch Log Group
resource "aws_cloudwatch_log_group" "sync_log_group" {
  name = var.log_group_name
}

# CloudWatch Log Stream
resource "aws_cloudwatch_log_stream" "sync_log_stream" {
  name           = var.log_stream_name
  log_group_name = aws_cloudwatch_log_group.sync_log_group.name
}

# IAM Role
resource "aws_iam_role" "sync_role" {
  name = "sync-role"
  assume_role_policy = jsonencode({
    Statement = [
      {
        Action    = "sts:AssumeRole",
        Effect    = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        },
      },
    ],
    Version = "2012-10-17"
  })
}

# IAM Policy
resource "aws_iam_policy" "sync_policy" {
  name        = "sync-policy"
  description = "A policy that allows access to S3 bucket and CloudWatch logs"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action   = [
          "s3:ListBucket",
          "s3:GetObject",
          "s3:PutObject",
        ],
        Effect   = "Allow",
        Resource = [
          aws_s3_bucket.sync_bucket.arn,
          "${aws_s3_bucket.sync_bucket.arn}/*",
        ],
      },
      {
        Action   = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
        ],
        Effect   = "Allow",
        Resource = [
          aws_cloudwatch_log_group.sync_log_group.arn,
          "${aws_cloudwatch_log_group.sync_log_group.arn}:*",
        ],
      },
    ],
  })
}

# Attach IAM Policy to Role
resource "aws_iam_role_policy_attachment" "sync_policy_attachment" {
  role       = aws_iam_role.sync_role.name
  policy_arn = aws_iam_policy.sync_policy.arn
}

