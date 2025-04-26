variable "aws_profile" {
  type    = string
  default = "default"
}

variable "region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-3"
}

variable "project_name" {
  description = "Project name"
  type        = string
  default     = "python-course-mimo"
}

variable "application_tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
  default = {
    creator = "Terraform"
    billing = "python-course-mimo"
    version = "ec2-deployment"
  }
}

# EC2 variables
variable "ami_id" {
  description = "AMI ID"
  type        = string
  default     = "ami-045a8ab02aadf4f88" # Ubuntu 24.04, amd64 noble image
}

variable "instance_type" {
  description = "Instance type"
  type        = string
  default     = "t2.xlarge"
}

variable "key_name" {
  description = "Key pair name"
  type        = string
  default     = "python-course-mimo"
}

# VPC variables
variable "aws_vpc_id" {
  description = "VPC ID"
  type        = string
  default     = "vpc-02b81a7b4e30aa658"
}

variable "aws_vpc_cidr_block" {
  description = "VPC CIDR block"
  type        = string
  default     = "172.31.48.0/20"
}

variable "aws_public_subnet_id" {
  description = "Public Subnet ID"
  type        = string
  default     = "subnet-02ef46a46293e66b9"
}

variable "aws_availability_zone" {
  description = "AWS Availability Zone"
  type        = string
  default     = "eu-west-3a"
}
