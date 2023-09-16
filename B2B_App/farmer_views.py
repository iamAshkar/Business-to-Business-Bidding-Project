from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View

from B2B_App.models import Product, Farmer_Reg, Auction, fixed_auction, chat


class Indexview(TemplateView):
    template_name = 'farmer/farmer_index.html'


class Add_Product(TemplateView):
    template_name = 'farmer/add_product.html'



    def post(self, request,*args,**kwargs):



        farmer = Farmer_Reg.objects.get(user_id=self.request.user.id)
        name = request.POST['name']

        price = request.POST['price']
        quantity=request.POST['qty']
        desc = request.POST['desc']
        a_date = request.POST['a_date']
        d_date = request.POST['d_date']

        image = request.FILES['image']
        fii = FileSystemStorage()
        filesss = fii.save(image.name, image)

        se = Product()
        se.farmer = farmer
        se.name = name
        se.auction_date=a_date
        se.delivery_date=d_date

        se.quantity=quantity
        se.image=filesss
        se.price = price
        se.desc = desc

        se.save()

        return render(request, 'farmer/farmer_index.html', {'message': "Product Added"})


class Auction_Amount(TemplateView):
    template_name = 'farmer/view_auction_amount.html'

    def get_context_data(self, **kwargs):

        context = super(Auction_Amount,self).get_context_data(**kwargs)

        view_fe = Farmer_Reg.objects.get(user_id=self.request.user.id)
        feed=Auction.objects.filter(farmer_id=view_fe.id, admin_status="approved", status="added")
        context['feed'] = feed
        return context

    def post(self, request, *args, **kwargs):
        search =request.POST['search']
        feed = Auction.objects.filter(product_name__icontains=search,status='added').order_by('price')
        return render(request, 'farmer/search.html', {'feed': feed})


class Auction_submit(TemplateView):
    template_name = 'farmer/view_auction_amount.html'
    def post(self, request, *args, **kwargs):

        id = request.POST['id']
        name = request.POST['name']
        cus_price = request.POST['cus_price']

        price = request.POST['price']
        d_date = request.POST['d_date']
        cu_name = request.POST['cu_name']
        f_name = request.POST['f_name']

        id2 = request.POST['id2']

        action = request.POST['action']
        if Auction.objects.filter(product_id=id2,status='confirm'):
            print("fvvfsff")
            return render(request, 'farmer/farmer_index.html', {'message': "Already Added"})
        else:
            act = Auction.objects.get(id=id)

            # act.complaint=complaint
            act.message = action

            act.status = 'confirm'
            act.save()
            a = fixed_auction()
            a.price = price
            a.product_name = name
            a.date = d_date
            a.message=action
            a.customer_id = cu_name
            a.farmer_id=f_name
            a.Auction_price=cus_price
            a.status='Approved'
            a.payment='added'
            a.save()

            return render(request, 'farmer/farmer_index.html', {'message': "Price Confirmed"})
        
class auction_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        b = Auction.objects.get(pk=id)
        b.status='Rejected'
        b.save()
        return render(request,'farmer/farmer_index.html',{'message':" Removed"})

class view_product(TemplateView):
    template_name = 'farmer/view_product.html'


    def get_context_data(self, **kwargs):

        context = super(view_product,self).get_context_data(**kwargs)
        f = Farmer_Reg.objects.get(user_id=self.request.user.id)
        view_pr = Product.objects.filter(farmer_id=f.id)
        context['view_pr'] = view_pr
        return context

class Delete_product(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Product.objects.get(id=id).delete()

        return render(request,'farmer/View_product.html',{'message':"Product Removed"})


class Fixed_Action(TemplateView):
    template_name = 'farmer/fixed_action.html'


    def get_context_data(self, **kwargs):

        context = super(Fixed_Action,self).get_context_data(**kwargs)
        f = Farmer_Reg.objects.get(user_id=self.request.user.id)
        view_pr = fixed_auction.objects.filter(farmer_id=f.id)

        context['view_pr'] = view_pr
        return context


class view_message(TemplateView):
    template_name = 'farmer/view_message.html'


    def get_context_data(self, **kwargs):

        context = super(view_message,self).get_context_data(**kwargs)
        f = Farmer_Reg.objects.get(user_id=self.request.user.id)
        view_pr = chat.objects.filter(farmer_id=f.id)

        context['view_pr'] = view_pr
        return context

    def post(self, request, *args, **kwargs):
        # complaint = actions.objects.get(user_id=self.request.id)
        id = request.POST['id']
        action = request.POST['reply']
        act = chat.objects.get(id=id)
        # act.complaint=complaint
        act.reply = action

        act.status = 'replied'
        act.save()

        return render(request, 'farmer/farmer_index.html', {'message': "Replied"})
    
    
class booking(TemplateView):
    template_name ='farmer/booking.html'

    def get_context_data(self, **kwargs):

        context = super(booking,self).get_context_data(**kwargs)

        cus = Farmer_Reg.objects.get(user_id=self.request.user.id)
        feed=fixed_auction.objects.filter(farmer_id=cus.id, payment="paid")
        context['feed'] = feed
        return context