from django.urls import path

from .views import DepositMoneyView, WithdrawMoneyView, TransactionRepostView, EnqueryView


app_name = 'transactions'


urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", TransactionRepostView.as_view(), name="transaction_report"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
    path("enquery/", EnqueryView.as_view(), name="enquery"),
]