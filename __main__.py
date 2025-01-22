import pulumi
from pulumi_azure_native import storage

# Tagging
tags = {
  "BusinessStructure": "BEES Platform - CloudDevOps",
  "Creator": "Brasil, Rodrigo B",
  "ValueStream": "BEES Platform - CloudDevOps",
  "teamName": "Platform Engineering"
}

pulumi_config = pulumi.Config()
storage_account_name = pulumi_config.require("name")

# Create an Azure Resource Group
#resource_group = resources.ResourceGroup("pulumipoc", tags=tags)

# Use existing Resource Group
resource_group_name = "pulumipoc165c8889"

# Create an Azure resource (Storage Account)
account = storage.StorageAccount(
    resource_name=storage_account_name,
    resource_group_name=resource_group_name,
    sku={
        "name": storage.SkuName.STANDARD_LRS,
    },
    kind=storage.Kind.STORAGE_V2,
    tags=tags,
)

# Export the primary endpoint URL of the storage account
pulumi.export("primary_storage_endpoint", account.primary_endpoints.blob)
