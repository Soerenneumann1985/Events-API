provider "aws" {
  region = "eu-central-1"
}

# 1. Der Bucket selbst
resource "aws_s3_bucket" "state" {
  bucket = "sn-bucket-state"   # weltweit eindeutig, z. B. mit deinem Kürzel und "tfstate"
}

# 2. Versionierung einschalten
resource "aws_s3_bucket_versioning" "state" {
  bucket = aws_s3_bucket.state.id

  versioning_configuration {
    status = "Enabled"
  }
}

# 3. Verschlüsselung
resource "aws_s3_bucket_server_side_encryption_configuration" "state" {
  bucket = aws_s3_bucket.state.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"   # Tipp: schau in deinem alten State nach, welcher Wert dort steht
    }
  }
}

# 4. Öffentlichen Zugriff komplett sperren
resource "aws_s3_bucket_public_access_block" "state" {
  bucket = aws_s3_bucket.state.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
