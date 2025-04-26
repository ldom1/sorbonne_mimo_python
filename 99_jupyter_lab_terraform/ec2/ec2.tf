variable "project_name" {
  description = "Name of the project"
}

variable "ami_id" {
  description = "AMI ID"
}

variable "instance_type" {
  description = "Instance type"
}

variable "public_subnet_id" {
  description = "Public Subnet ID"
}

variable "key_name" {
  description = "Key pair name"
}

variable "vpc_id" {
  description = "VPC ID"
}

variable "application_tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
}

variable "aws_iam_ec2_execution_role" {
  description = "IAM Instance Profile Name"
}

variable "aws_security_group_id" {
  description = "Security Group id"
}

variable "region" {
  description = "AWS Region"
}


# Elastic IP
resource "aws_eip" "ec2_fixed_ip" {
  tags = {
    Name = "${var.project_name}-eip"
  }
}

# EC2 Instance
resource "aws_instance" "docker_ec2" {
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = var.public_subnet_id
  key_name      = var.key_name

  tags = merge(
    var.application_tags,
    { Name = "${var.project_name}-docker-ec2" }
  )

  associate_public_ip_address = true

  security_groups = [var.aws_security_group_id]

  iam_instance_profile = aws_iam_instance_profile.ec2_instance_profile.name

  # User data for setup
  user_data = <<-EOT
    #!/bin/bash

    # Update and install dependencies
    sudo apt update
    sudo apt install -y docker.io

    # Start and enable Docker
    sudo systemctl start docker
    sudo systemctl enable docker

    # Pull and run Docker image
    sudo docker run --rm -p 8889:8888 quay.io/jupyter/base-notebook start-notebook.py --NotebookApp.token='mimo_2025' -p 8889:8888 -e JUPYTER_TOKEN='mimo_2025' --ServerApp.allow_password_change=False
  EOT
}

resource "null_resource" "associate_eip" {

  # Attach Elastic IP
  provisioner "local-exec" {
    command = "aws ec2 associate-address --instance-id ${aws_instance.docker_ec2.id} --allocation-id ${aws_eip.ec2_fixed_ip.id} --region ${var.region}"
  }

  depends_on = [aws_instance.docker_ec2, aws_eip.ec2_fixed_ip]
}


# Instance Profile for EC2
resource "aws_iam_instance_profile" "ec2_instance_profile" {
  name = "${var.project_name}-ec2-instance-profile"
  role = var.aws_iam_ec2_execution_role
}

# Output: the public ip of the EC2 instance
output "ec2_instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.docker_ec2.public_ip
}