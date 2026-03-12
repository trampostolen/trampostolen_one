# 1. AWS Access Key (Классический паттерн: 20 символов, начинается с AKIA)
aws_key = "AKIAIMNO7YBX3TOA7SRA"
aws_secret = "8u9S6unI+0u68SwnZ/WSpYm80u68SwnZ/WSpYm80"

# 2. GitHub Personal Access Token (Современный формат ghp_)
github_token = "ghp_n7S3p0rtantSecretTokenForTesting12345"

# 3. Приватный ключ SSH (Поиск по заголовкам файла)
ssh_key = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA75h7... (тут обычно длинный хеш)
-----END RSA PRIVATE KEY-----
"""

# 4. Строка подключения к базе данных (Generic Secret)
db_url = "postgresql://admin:password123@localhost:5432/mydb"

# 5. Google API Key
google_api = "AIzaSyA-1234567890abcdefghijklmnopqrstuv"
