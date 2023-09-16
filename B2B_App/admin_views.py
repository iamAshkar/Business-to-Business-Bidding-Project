from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from B2B_App import farmer_urls, farmer_views

from B2B_App.models import Auction, Farmer_Reg,fixed_auction, Product


class Indexview(TemplateView):
    template_name = 'admin/admin_index.html'


class Farmer_varify(TemplateView):
    template_name = 'admin/farmer_varify.html'

    def get_context_data(self, **kwargs):
        context = super(Farmer_varify, self).get_context_data(**kwargs)

        shop = Farmer_Reg.objects.filter(user__last_name='0', user__is_staff='0', user__is_active='1')

        context['shop'] = shop
        return context


class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '1'
        user.save()
        return render(request, 'admin/admin_index.html', {'message': " Account Approved"})


class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '1'
        user.is_active = '0'
        user.save()
        return render(request, 'admin/admin_index.html', {'message': "Account Removed"})


class Generate_complaints(TemplateView):
    template_name = 'admin/report.html'

    def post(self, request, *args, **kwargs):


        f = request.POST['f']
        t = request.POST['t']
        print(f)
        print(t)
        host = (fixed_auction.objects.filter(date__lte=f,status='Approved') | fixed_auction.objects.filter(
            date__lte=t,status='Approved'))

        return render(request, 'admin/report1.html', {'g':host})
    
class view_farmer(TemplateView):
    template_name = 'admin/view_farmer.html'

    def get_context_data(self, **kwargs):
        context = super(view_farmer, self).get_context_data(**kwargs)
        
        f = Farmer_Reg.objects.all()
        
        context['f'] = f
        return context


class Delete_farmer(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        try:
            id = request.GET['id']
            farmer = Farmer_Reg.objects.get(id=id)
            farmer.delete()
            message = "Farmer Removed"
        except Farmer_Reg.DoesNotExist:
            message = "Farmer Not Found"
        
        return render(request, 'admin/view_farmer.html', {'message': message})

class auction_view(TemplateView):
    template_name = 'admin/approve_auction.html'

    def get_context_data(self, **kwargs):

        context = super(auction_view,self).get_context_data(**kwargs)
        # id=self.request.GET['id']
        # view_fe = Farmer_Reg.objects.get(id=id)
        feed=Auction.objects.filter(admin_status="added")
        context['feed'] = feed
        return context

class auction_approve(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        act = Auction.objects.get(id=id)
        act.admin_status = 'approved'
        act.save()
        return render(request, 'admin/admin_index.html', {'message': " Auction Approved"})
    
class auction_reject(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        b = Auction.objects.get(pk=id)
        b.status='Rejected'
        b.save()
        return render(request,'admin/admin_index.html',{'message':" Removed"})
    
class booking(TemplateView):
    template_name ='admin/booking.html'

    def get_context_data(self, **kwargs):

        context = super(booking,self).get_context_data(**kwargs)

        feed=fixed_auction.objects.filter(payment="paid")
        context['feed'] = feed
        return context



class view_product(TemplateView):
    template_name = 'admin/view_product.html'
    def get_context_data(self, **kwargs):
        context = super(view_product,self).get_context_data(**kwargs)
        view_pr = Product.objects.all()
        context['view_pr'] = view_pr
        return context