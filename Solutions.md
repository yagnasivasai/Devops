az group create \
    --name storage-resource-group \
    --location eastus

az storage account create \
    --name mystorageaccount \
    --resource-group storage-resource-group \
    --kind BlobStorage \
    --access-tier hot





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
aicommits config set OPENAI_KEY=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