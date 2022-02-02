
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class Account_activation_tocken_genrator(PasswordResetTokenGenerator):
    def _make_hash_values(self, user,timestamp):
        
        return (
            text_type(user.pk)+text_type(timestamp)+text_type(user.is_active)
        )
    
account_activation_token = Account_activation_tocken_genrator()