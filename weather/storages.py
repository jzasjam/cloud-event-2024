from storages.backends.azure_storage import AzureStorage
class AzureMediaStorage(AzureStorage):
    account_name = 'shucloudevent2024'
    account_key = 'MMdKLLXg7bNrMwD4oN3xR8mxAgP5+BMSNRidqA5DHp9YDz9onNnlOcgXhNLawlUIvp+Z9H8wznok+AStZ8eu6Q=='
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
	account_name = 'shucloudevent2024'
	account_key = 'MMdKLLXg7bNrMwD4oN3xR8mxAgP5+BMSNRidqA5DHp9YDz9onNnlOcgXhNLawlUIvp+Z9H8wznok+AStZ8eu6Q=='
	azure_container = 'static'
	expiration_secs = None
