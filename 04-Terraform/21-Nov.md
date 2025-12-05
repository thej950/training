# Terraform Commands
 - terraform init 
 - terraform validate 
 - terraform plan
 - terraform apply 
 - terraform destroy 
 - terraform apply --auto-approve
 - terraform destroy --auto-approve
 - terraform destroy --target=azurerm_resource_group.example
 - terraform apply --target azurerm_resource_group.mygroup1 --var-file="stage.tfvars"
 - terraform apply --target azurerm_resource_group.mygroup1 --var-file="prod.tfvars"

# Pre-Rquiset
 - Install Terraform, Azure CLI(commands)
 - Create the App Registration (Service Principal Identity)
 - Create the Client Secret (The "Password")
 - Assign a Role (Grant Permissions)

# Configure Terraform


# Storage Account 
 
resource "azurerm_storage_account" "sa" {
  name                          = "terrasa098766"
  resource_group_name           = azurerm_resource_group.main-rg1.name
  location                      = azurerm_resource_group.main-rg1.location
  account_tier                  = "Standard"
  account_replication_type      = "LRS"
  public_network_access_enabled = false
}
output "sa" {
  value = azurerm_storage_account.sa.name
 
}
 
# Terraform locals & how storage account created add blob, containers, files 


resource "azurerm_storage_account" "sa" {
  name                          = "terrasa098766"
  resource_group_name           = azurerm_resource_group.example.name
  location                      = azurerm_resource_group.example.location
  account_tier                  = "Standard"
  account_replication_type      = "LRS"
  public_network_access_enabled = true
 
}
resource "azurerm_storage_container" "data" {
  name                  = "data"
  storage_account_name  = azurerm_storage_account.sa.name
  container_access_type = "private"
}
resource "azurerm_storage_blob" "sample" {
  name                   = "sample.txt"
  storage_account_name   = azurerm_storage_account.sa.name
  storage_container_name = azurerm_storage_container.data.name
  type                   = "Block"
  source                 = "sample.txt"
 
}
 
output "sa" {
  value = azurerm_storage_account.sa.name
 
}
 
# Dynamic blocks 



# Loop
 
resource "azurerm_resource_group" "rg1" {
  for_each = var.rgs
  name     = each.key
  location = each.value
}
 
 
variable "rgs" {
  type    = map(string)
  default = { "rg11" = "eastus", "rg12" = "westus", "rg13" = "centralindia" }
}
 
 # Sa count example
 
variable "sa_names" {
  type    = list(string)
  default = ["stor9841", "stor9842"]
}
 
resource "azurerm_storage_account" "sa1" {
  account_tier = "Standard"
  count        = length(var.sa_names)
 
  name                = var.sa_names[count.index]
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
 
  account_replication_type = "LRS"
}
 
 <!--  -->



resource "azurerm_virtual_network" "vnet" {
  name                = "example-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  dns_servers         = ["10.0.0.4", "10.0.0.5"]
}
resource "azurerm_subnet" "subnet1" {
  name                 = "example-subnet"
  resource_group_name  = azurerm_resource_group.example.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}
resource "azurerm_public_ip" "pip" {
  name                = "example-pip"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  allocation_method   = "Static"
}
resource "azurerm_network_interface" "nic1" {
  name                = "example-nic"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
 
  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.subnet1.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.pip.id
  }
}
resource "azurerm_virtual_machine" "vm1" {
  name                             = "example-vm"
  location                         = azurerm_resource_group.example.location
  resource_group_name              = azurerm_resource_group.example.name
  network_interface_ids            = [azurerm_network_interface.nic1.id]
  vm_size                          = "Standard_B1s"
  delete_os_disk_on_termination    = true
  delete_data_disks_on_termination = true
  storage_os_disk {
    name              = "example-os-disk"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }
  storage_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }
  os_profile {
    computer_name  = "hostname"
    admin_username = "adminuser"
    admin_password = "P@ssw0rd1234!"
  }
  os_profile_linux_config {
    disable_password_authentication = false
  }
  tags = {
    environment = "staging"
  }
}
 