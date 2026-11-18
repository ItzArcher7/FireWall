from firewall_v1 import Text, Math, Security, Logger

print("Firewall V1:", "1.0.0")

print(Text.reverse("Firewall"))
print(Math.average([10, 20, 30]))

password = Security.hash_password("MyPassword123")
print(Security.verify_password("MyPassword123", password))

logger = Logger.get()
logger.info("Firewall V1 is running!")
