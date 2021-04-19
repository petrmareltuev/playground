from django.shortcuts import render, HttpResponse
from wallet.services.wallet_services import get_user_wallets


def test(request):
    user_wallets = get_user_wallets()
    context = {
        "user_wallets": user_wallets,
        "title": "Wallet"
    }

    return render(request, "wallet/user_wallets.html", context)
