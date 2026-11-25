# 1. Der Bucket für die Avatare
resource "aws_s3_bucket" "avatars" {
  bucket = "sn-grocerymate-avatars"

  tags = {
    Name        = "sn-grocerymate-avatars"
    Environment = "Dev"
  }
}

# 2. Versionierung einschalten
resource "aws_s3_bucket_versioning" "avatars" {
  bucket = aws_s3_bucket.avatars.id

  versioning_configuration {
    status = "Enabled"
  }
}

# 3. Öffentlichen Zugriff komplett sperren
resource "aws_s3_bucket_public_access_block" "avatars" {
  bucket = aws_s3_bucket.avatars.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
