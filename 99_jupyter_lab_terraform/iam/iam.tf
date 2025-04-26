variable "project_name" {
  description = "Project name"
}

variable "application_tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
}


# IAM Role for EC2
resource "aws_iam_role" "ec2_execution_role" {
  name = "${var.project_name}-ec2-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })

  tags = merge(
    var.application_tags,
    { Name = "${var.project_name}-EC2-Execution-Role" }
  )
}

output "aws_iam_ec2_execution_role" {
  value = aws_iam_role.ec2_execution_role.name
}
