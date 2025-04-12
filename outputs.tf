output "ec2_public_ip" {
  value = aws_instance.web.public_ip
}

output "s3_website_url" {
  value = aws_s3_bucket.static_site.website_endpoint
}
