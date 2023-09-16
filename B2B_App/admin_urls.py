from django.urls import path


from B2B_App.admin_views import Indexview, Farmer_varify, ApproveView, RejectView,Generate_complaints ,view_farmer ,Delete_farmer, auction_view, auction_approve, view_product, auction_reject,\
    booking

urlpatterns = [

    path('',Indexview.as_view()),
    path('Farmer_varify',Farmer_varify.as_view()),
    path('approve',ApproveView.as_view()),
    path('reject', RejectView.as_view()),
    path('Generate_complaints',Generate_complaints.as_view()),
    path('view_farmer',view_farmer.as_view()),
    path('Delete_farmer',Delete_farmer.as_view()),
    path('view_product',view_product.as_view()),
    path('auction_approve',auction_view.as_view()),
    path('auc_approve',auction_approve.as_view()),
    path('auction_reject',auction_reject.as_view()),
    path('booking',booking.as_view()),



]
def urls():
    return urlpatterns, 'admin','admin'