from wallet.models import Wallet


def get_user_wallets():
    user_wallets = Wallet.objects.all()
    return user_wallets
