variable "aws_region" {
  default = "us-east-1"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "key_name" {
  description = "Name of your existing EC2 Key Pair"
}

variable "bucket_name" {
  description = "Globally unique name for the S3 bucket"
}

variable "my_ip" {
  description = "Your public IP with CIDR (e.g., 123.123.123.123/32)"
}
