resource "aws_iam_role" "developer_role" {
  name = "developer-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect    = "Allow",
        Principal = {
          AWS = "arn:aws:iam::${var.account_id}:root"
        },
        Action    = "sts:AssumeRole",
        Condition = {
          StringEquals = {
            "aws:username" = ["kernel-memory-dump", "some-other-developer"]
          }
        }
      }
    ]
  })
}
