from django.urls import path

from B2B_App.farmer_views import Indexview, Add_Product, Auction_Amount, Auction_submit, view_product, Delete_product, \
    Fixed_Action, view_message, auction_reject, booking

urlpatterns = [

    path('',Indexview.as_view()),
    path('Add_Product',Add_Product.as_view()),
    path('Auction_Amount',Auction_Amount.as_view()),
    path('Auction_submit',Auction_submit.as_view()),
    path('view_product',view_product.as_view()),
    path('delete',Delete_product.as_view()),
    path('Fixed_Action',Fixed_Action.as_view()),
    path('view_message',view_message.as_view()),
    path('auction_reject',auction_reject.as_view()),
    path('booking',booking.as_view()),
    # path('Product_categ',Product_categ.as_view())

]
def urls():
    return urlpatterns, 'farmer','farmer'