terraform {
  backend "s3" {
    bucket       = "sn-bucket-state"                  # Name deines neuen Tresor-Buckets
    key          = "infrastructure/terraform.tfstate" # Wo im Tresor soll das Notizbuch liegen?
    region       = "eu-central-1"
    encrypt      = true # Ja/Nein: verschlüsselt speichern?
    use_lockfile = true # Ja/Nein: Sperre, damit nicht zwei gleichzeitig schreiben
  }
}


provider "aws" {
  region = "eu-central-1"
}

resource "aws_s3_bucket" "grocerymate_bucket" {
  bucket = "sn100-bucket-soeren"
  tags = {
    Projekt = "Events-API"
  }
}
