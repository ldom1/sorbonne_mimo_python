variable "project_name" {
  description = "Name of the project"
}

variable "vpc_id" {
  description = "VPC ID"
}

variable "application_tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
}

# Security Group for EC2
resource "aws_security_group" "ec2_sg" {
  name        = "${var.project_name}-ec2-sg"
  description = "Allow HTTP and SSH traffic"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8889
    to_port     = 8889
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow access to JupyterLab"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(
    var.application_tags,
    { Name = "${var.project_name}-ec2-sg" }
  )
}

output "aws_security_group_id" {
  value = aws_security_group.ec2_sg.id
}
