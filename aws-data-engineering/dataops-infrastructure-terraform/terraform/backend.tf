# Configure the backend for Terraform using Local Backend
terraform {
  backend "local" {
    path = "/home/coder/.local/share/code-server/User/de-c2w3lab1-<AWS-ACCOUNT-ID>-us-east-1.state" # Path to the local state file
  }
}