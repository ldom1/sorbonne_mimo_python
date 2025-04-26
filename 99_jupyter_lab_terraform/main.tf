terraform {
  cloud {
    organization = "DomOrganization"
    workspaces {
      name = "PYTHON_COURSE_MIMO"
    }
  }
}

provider "aws" {
  region  = var.region
  profile = var.aws_profile
}

module "iam" {
  source             = "./iam"
  application_tags   = var.application_tags
  project_name       = var.project_name
}

module "vpc" {
  source           = "./vpc"
  application_tags = var.application_tags
  project_name     = var.project_name
  vpc_id           = var.aws_vpc_id
}

module "ec2" {
  source                     = "./ec2"
  application_tags           = var.application_tags
  project_name               = var.project_name
  ami_id                     = var.ami_id
  instance_type              = var.instance_type
  public_subnet_id           = var.aws_public_subnet_id
  key_name                   = var.key_name
  vpc_id                     = var.aws_vpc_id
  aws_iam_ec2_execution_role = module.iam.aws_iam_ec2_execution_role
  aws_security_group_id      = module.vpc.aws_security_group_id
  region                     = var.region
}


