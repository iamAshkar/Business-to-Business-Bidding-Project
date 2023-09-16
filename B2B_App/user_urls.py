from django.urls import path

from B2B_App.user_views import Indexview, Product_details, Add_Action, Status_Auc, Send_message, message_reply, Auction_view, Payment,\
    Make_Payment,booking

urlpatterns = [

    path('',Indexview.as_view()),
    path('Product_details',Product_details.as_view()),
    path('Add_Action',Add_Action.as_view()),
    path('Auction_Status',Status_Auc.as_view()),
    path('Send_message',Send_message.as_view()),
    path('message_reply',message_reply.as_view()),
    path('Auction_view',Auction_view.as_view()),
    path('Payment',Payment.as_view()),
    path('Make_Payment',Make_Payment.as_view()),
    path('booking',booking.as_view()),



]
def urls():
    return urlpatterns, 'user','user'