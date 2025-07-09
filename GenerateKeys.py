from Cryptodome.PublicKey import RSA

pair_keys = RSA.generate(1024)
private_key = pair_keys.export_key()
public_key = pair_keys.public_key().export_key()
print(private_key)
print(public_key)