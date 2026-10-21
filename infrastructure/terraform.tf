provider "aws" {
  region = "eu-central-1"
}

resource "aws_s3_bucket" "grocerymate_bucket" {
  bucket = "sn100-bucket-soeren"
}
