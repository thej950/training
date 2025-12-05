terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "4.53.0"
    }
  }
}

provider "azurerm" {
  # Configuration options
  subscription_id = "" # subscription id from azure
  client_id = "" # client id from app registration
  client_secret = "" # client secret from app registration
  tenant_id = "" # tenant id from azure
  features {}

}

resource "azurerm_resource_group" "main-rg1" {
  name     = "tf-rg1"
  location = var.region # Choose your desired Azure region

  tags = {
    name = var.mytag
  }
}

resource "azurerm_resource_group" "main-rg2" {
  name     = "tf-rg2"
  location = var.region

  tags = {
    name = var.mytag
  }
}