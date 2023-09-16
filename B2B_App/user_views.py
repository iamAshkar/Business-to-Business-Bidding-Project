from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView

from B2B_App.models import Product, Farmer_Reg, Auction, Customer_Reg, fixed_auction, chat


class Indexview(TemplateView):
    template_name = 'user/product.html'

    def get_context_data(self, **kwargs):
        context = super(Indexview,self).get_context_data(**kwargs)
        view_pp = Product.objects.all()
        context['view_pp'] = view_pp
        return context

class Product_details(TemplateView):
    template_name = 'user/product_details.html'

    def get_context_data(self, **kwargs):
        id =self.request.GET['id']

        context = super(Product_details, self).get_context_data(**kwargs)

        single_view = Product.objects.get(id=id)
        shop = Product.objects.get(id=id)


        context['single_view'] = single_view

        return context


class Add_Action(TemplateView):
    template_name ='user/product_details.html'

    def dispatch(self, request, *args, **kwargs):
        pid = request.POST['id']
        id2 = request.POST['id2']
        qunty = request.POST['price']

        cust = Customer_Reg.objects.get(user_id=self.request.user.id)
        product=Product.objects.get(pk=pid)
        # if Auction.objects.filter(product_id=product,customer_id=cust):
        #     print("fvvfsff")
        #     return render(request, 'user/product.html', {'message': "Already Added"})
        # else:
        shop = Product.objects.get(pk=pid)

        shopp = Farmer_Reg.objects.get(id=shop.farmer_id)
        ca = Auction()
        ca.customer = cust
        ca.product_name=id2
        ca.farmer_id = shopp.id
        ca.product = product
        ca.price = qunty
        ca.status = 'added'
        ca.admin_status = 'added'
        ca.save()
        return render(request, 'user/product.html', {'message': " price added"})


class Status_Auc(TemplateView):
    template_name ='user/My_Auction_Status.html'

    def get_context_data(self, **kwargs):

        context = super(Status_Auc,self).get_context_data(**kwargs)

        cus = Customer_Reg.objects.get(user_id=self.request.user.id)
        feed=fixed_auction.objects.filter(customer_id=cus.id, payment="Added")
        context['feed'] = feed
        return context

class Send_message(TemplateView):
    template_name = 'user/chat.html'

    def get_context_data(self, **kwargs):
        context = super(Send_message, self).get_context_data(**kwargs)
        id = self.request.GET['id']

        replay = Product.objects.get(id=id)

        context['repl'] = replay
        return context

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)

        product = request.POST['product']
        pro = Product.objects.get(id=product)
        message = request.POST['message']
        fe = chat()
        fe.user = user
        fe.farmer_id=pro.farmer_id
        fe.product_id=product
        fe.message = message
        fe.status='added'
        fe.save()
        return render(request, 'user/product.html', {'message': "Message Send "})

class message_reply(TemplateView):
    template_name = 'user/view_message_reply.html'

    def get_context_data(self, **kwargs):
        context = super(message_reply,self).get_context_data(**kwargs)
        usid = self.request.user.id
        replay = chat.objects.filter(user_id=usid,status='replied')

        context['replay'] = replay
        return context


class Auction_view(TemplateView):
    template_name = 'user/view_auction_amount.html'
    def get_context_data(self, **kwargs):

        context = super(Auction_view,self).get_context_data(**kwargs)
        feed=Auction.objects.filter(admin_status="approved", status="added")
        context['feed'] = feed
        return context
    
class Payment(TemplateView):
    template_name= 'user/payment.html'
    def get_context_data(self, **kwargs):

        context = super(Payment,self).get_context_data(**kwargs)
        feed=Auction.objects.filter(admin_status="approved", status="added")
        context['feed'] = feed
        return context

class Make_Payment(TemplateView):
    template_name= 'user/payment.html'
    def dispatch(self,request,*args,**kwargs):

        pid = self.request.user.id
        cus = Customer_Reg.objects.get(user_id=self.request.user.id)
        ch=fixed_auction.objects.filter(customer_id=cus.id)
        
        print(ch)
        for i in ch:
            i.payment='paid'
            i.save()
        return render(request,'user/user_index.html',{'message':" payment Successfull, Check Booking Details"})
    

class booking(TemplateView):
    template_name ='user/booking.html'

    def get_context_data(self, **kwargs):

        context = super(booking,self).get_context_data(**kwargs)

        cus = Customer_Reg.objects.get(user_id=self.request.user.id)
        feed=fixed_auction.objects.filter(customer_id=cus.id, payment="paid")
        context['feed'] = feed
        return context