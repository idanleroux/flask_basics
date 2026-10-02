from setup_users import demo_hash
from werkzeug.security import check_password_hash

print(check_password_hash(demo_hash, 'ClassDemo!2026'))
print(check_password_hash(demo_hash, 'wrong-password'))
