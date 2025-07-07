from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from .decorators import role_required
from django.db import connection
from django.db.models import Q
from django.conf import settings
from django.db.models import F
from django.db.models import Count
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
import requests
from .middleware import *
from .models import *
from .forms import *


# ==========================================  Super Admin Dashboard ===============================================
@role_required(['SUPERADMIN'])
def superadmin_dashboard(request):

    # Dashboard Total Count For Approve, Pending, Reject
    total_count = BarcodeScan.objects.count()
    approve_count = BarcodeScan.objects.filter(status='Approve').count()
    pending_count = BarcodeScan.objects.filter(status='pending').count()
    reject_count = BarcodeScan.objects.filter(status='Reject').count()

    # Akhil Bhartiya Dashboard Card Count
    akhilbhartiya_count = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='अखिल भारतीय').values('phone_number')).count()
    approvecount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='अअखिल भारतीय').values('phone_number'),status='Approve').count()
    pendingcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='अखिल भारतीय').values('phone_number'),status='pending').count()
    rejectcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='अखिल भारतीय').values('phone_number'),status='Reject').count()

    # क्षेत्र Dashboard Card Count
    chetracount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='क्षेत्र').values('phone_number')).count()
    chetrapprovecount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='क्षेत्र').values('phone_number'),status='Approve').count()
    chetrpendingcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='क्षेत्र').values('phone_number'),status='pending').count()
    chetrrejectcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='क्षेत्र').values('phone_number'),status='Reject').count()

    # प्रान्त Dashboard Card Count
    prantcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत').values('phone_number')).count()
    prantapprovecount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत').values('phone_number'),status='Approve').count()
    prantpendingcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत').values('phone_number'),status='pending').count()
    prantrejectcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत').values('phone_number'),status='Reject').count()

    # विभाग Dashboard Card Count
    vibhagcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग').values('phone_number')).count()
    vibhagapprovecount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग').values('phone_number'),status='Approve').count()
    vibhagpendingcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग').values('phone_number'),status='pending').count()
    vibhagrejectcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग').values('phone_number'),status='Reject').count()

    # जिला Dashboard Card Count
    jilacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला').values('phone_number')).count()
    jilaapprovecount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला').values('phone_number'),status='Approve').count()
    jilapendingcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला').values('phone_number'),status='pending').count()
    jilarejectcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला').values('phone_number'),status='Reject').count()

    # नगर Dashboard Card Count
    nagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर').values('phone_number')).count()
    nagarapprovecount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर').values('phone_number'),status='Approve').count()
    nagarpendingcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर').values('phone_number'),status='pending').count()
    nagarrejectcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर').values('phone_number'),status='Reject').count()

    # अन्य Dashboard Card Count
    anyacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai__isnull=True).values('phone_number')).count()
    anyaapprovecount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai__isnull=True).values('phone_number'),status='Approve').count()
    anyapendingcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai__isnull=True).values('phone_number'),status='pending').count()
    anyarejectcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai__isnull=True).values('phone_number'),status='Reject').count()

    # ---------------------------------------------------------------- Start Chart Data -----------------------------------------------------------
    # nagarcount Chart (Graph) the records
    nagarcount = RegisterSamautkarshRegistration.objects.values('nagar_address').distinct().count()
    # Fetch all RegisterSamautkarshRegistration data in Graph
    nagar = RegisterSamautkarshRegistration.objects.values('nagar_address').distinct()
    nagar_addresses = [entry['nagar_address'] for entry in nagar if entry['nagar_address']]

    # vibhagcount Chart (Graph) the records
    vibhagcount = RegisterSamautkarshRegistration.objects.values('nagar_address').distinct().count()
    # Fetch all RegisterSamautkarshRegistration data in Graph
    vibhag = RegisterSamautkarshRegistration.objects.values('nagar_address').distinct()
    nagar_addresses = [entry['nagar_address'] for entry in nagar if entry['nagar_address']]

    # --------------------------------------------------------------- End Chart Data ---------------------------------------------------------------

    # -------------------------------------------Start Total Register Count Dashboard Data ---------------------------------------------------------
    count = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='Prant',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id')).values('jila_id')).values('nagar_hindi')).values('phone_number'),nagar='बदरपुर').count()

    # ------------------------------------------- End Total Register Count Dashboard Data ---------------------------------------------------------

    vibhag_count = RegisterSamautkarshRegistration.objects.filter(ekai="विभाग").count()
    nagar_count = RegisterSamautkarshRegistration.objects.filter(ekai="nagar").count()
    prant_count = RegisterSamautkarshRegistration.objects.filter(ekai="प्रान्त").count()
    zilla_count = RegisterSamautkarshRegistration.objects.filter(ekai="jilla").count()

    # Chart DropDown all records
    vibhag = VibhagMaster.objects.all()
    nagar = NagarMaster.objects.all()
    prant = PrantMaster.objects.all()
    zilla = ZilaMaster.objects.all()

    # Fetch all RegisterSamautkarshRegistration data
    vibhag_chart = RegisterSamautkarshRegistration.objects.filter(ekai="vibhag")
    nagar_chart = RegisterSamautkarshRegistration.objects.filter(ekai="nagar")
    prant_chart = RegisterSamautkarshRegistration.objects.filter(ekai="prant")
    zilla_chart = RegisterSamautkarshRegistration.objects.filter(ekai="jilla")

    context = {'pages': 'Super Admin','vibhag_count': vibhag_count, 'nagar_count': nagar_count, 
        'prant_count': prant_count, 'zilla_count': zilla_count,
        'vibhag': vibhag, 'nagar': nagar, 'prant': prant, 'zilla': zilla,
        'vibhag_chart': vibhag_chart, 'nagar_chart': nagar_chart, 'prant_chart': prant_chart,
        'zilla_chart': zilla_chart, 'akhilbhartiya_count': akhilbhartiya_count, 'approvecount': approvecount, 'pendingcount': pendingcount, 'rejectcount': rejectcount, 'chetracount': chetracount, 'chetrapprovecount': chetrapprovecount, 'chetrpendingcount': chetrpendingcount, 'chetrrejectcount': chetrrejectcount, 'prantcount': prantcount, 'prantapprovecount': prantapprovecount, 'prantpendingcount': prantpendingcount, 'prantrejectcount': prantrejectcount, 'vibhagcount': vibhagcount, 'vibhagapprovecount': vibhagapprovecount, 'vibhagpendingcount': vibhagpendingcount, 'vibhagrejectcount': vibhagrejectcount, 'jilacount': jilacount, 'jilaapprovecount': jilaapprovecount, 'jilapendingcount': jilapendingcount, 'jilarejectcount': jilarejectcount, 'nagarcount': nagarcount, 'nagarapprovecount': nagarapprovecount, 'nagarpendingcount': nagarpendingcount, 'nagarrejectcount': nagarrejectcount, 'anyacount': anyacount, 'anyaapprovecount': anyaapprovecount, 'anyapendingcount': anyapendingcount, 'anyarejectcount': anyarejectcount, 'nagar_addresses': nagar_addresses, 'total_count': total_count, 'approve_count': approve_count, 'pending_count': pending_count, 'reject_count': reject_count}
    

    return render(request, 'superadmin_dashboard/superadmin_dashboard.html', context)


def superadmin_dashboard_totalregistercount(request):
    # Karawal Nagar (करावल नगर) Count
    karawalnagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='करावल नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    print(karawalnagarcount)
    # Brahmpuri (ब्रहमपुरी) Count
    brahmpurinagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='ब्रहमपुरी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Nand Nagari (नंद नगरी) Count
    nandnagaricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नंद नगरी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Rohtash Nagar (रोहताश नगर) Count
    rohtashnagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नंद नगरी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Sum of all individual counts for यमुना विहार
    yamunaviharsum_count = karawalnagarcount + brahmpurinagarcount + nandnagaricount + rohtashnagarcount
    
    # Shahdara (शाहदरा) Count
    shahdaracount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='शाहदरा').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Gandhi Nagar (गांधीनगर) Count
    gandhinagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='गांधीनगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Indraprastha (इन्द्रप्रस्थ) Count
    indraprasthacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='इन्द्रप्रस्थ').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Mayur Vihar (मयूर विहार) Count
    mayurviharcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मयूर विहार').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for पूर्वी
    purvisum_count = shahdaracount + gandhinagarcount + indraprasthacount + mayurviharcount 
    
    # Lajpat Nagar (लाजपत नगर) Count
    lajpatnagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='लाजपत नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    
    # Badarpur (बदरपुर) Count
    badarpurcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='बदरपुर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    
    # Kalka Jee (कालका जी) Count
    kalkajeecount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='कालका जी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for दक्षिण
    dakshinsum_count = lajpatnagarcount + badarpurcount + kalkajeecount

        
    # Ambedkar (अम्बेडकर) Count
    ambedkarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='अम्बेडकर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
        
    # Mihirawali (मिहिरावली) Count
    mihirawalicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मिहिरावली').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
        
    # Vasant (वसंत) Count
    vasantcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='वसंत').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for राम कृष्ण पुरम 
    ramkrishnapuramsum_count = ambedkarcount + mihirawalicount + vasantcount

            
    # Dawrka (द्वारका) Count
    dawrkacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='द्वारका').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
            
    # Nahargarh (नाहरगढ़) Count
    nahargarhcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नाहरगढ़').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
            
    # Uttam (उत्तम) Count
    uttamcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='उत्तम').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
            
    # Nangloi (नांगलोई) Count
    nangloicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नांगलोई').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for पश्चिमी   
    pashchimisum_count = dawrkacount + nahargarhcount + uttamcount + nangloicount
    
                
    # Tilak (तिलक) Count
    tilakcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='तिलक').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                
    # Janakpuri (जनकपुरी) Count
    janakpuricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='जनकपुरी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                
    # Moti Nagar (मोती नगर) Count
    motinagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मोती नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                
    # Saraswati Vihar (सरस्वती विहार) Count
    saraswativiharcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='सरस्वती विहार').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for केशवपुरम 
    keshavpuramsum_count = tilakcount + janakpuricount + motinagarcount + saraswativiharcount
              
    # Rohini (रोहिणी) Count
    rohinicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='रोहिणी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                    
    # Kan jhawala (कंझावला) Count
    kanjhawalacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='कंझावला').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                    
    # Narela (नरेला) Count
    narelacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नरेला').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                    
    # Burari (बुराड़ी) Count
    buraricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='बुराड़ी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for उत्तरी 
    uttarisum_count = rohinicount + kanjhawalacount + narelacount + buraricount
                  
    # Mukherjee Nagar (मुखर्जी नगर) Count
    mukherjeenagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मुखर्जी नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                  
    # Kamla Nagar (कमला नगर) Count
    kamlacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='कमला नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                  
    # Karol Bagh (करोल बाग़) Count
    karolbaghcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='करोल बाग़').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                  
    # Patel (पटेल) Count
    patelcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='प्रांत',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='पटेल').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for झंडेवालान
    jhandewalan_count = mukherjeenagarcount + kamlacount + karolbaghcount + patelcount
    total_register_prant_count = yamunaviharsum_count + purvisum_count + dakshinsum_count + ramkrishnapuramsum_count + pashchimisum_count + keshavpuramsum_count + uttarisum_count + jhandewalan_count

#   =============================================================== Start विभाग ==================================================                 
    # Karawal Nagar (करावल नगर) Count
    vibhagkarawalnagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='करावल नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Brahmapuri (ब्रहमपुरी) Count
    vibhagbrahmapuricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='ब्रहमपुरी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Nand Nagari (नंद नगरी) Count
    vibhagnandnagaricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नंद नगरी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Rohtash Nagar (रोहताश नगर) Count
    vibhagrohtashnagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='रोहताश नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for यमुना विहार (विभाग) 
    vibhagyamunaviharsum_count = vibhagkarawalnagarcount + vibhagbrahmapuricount + vibhagnandnagaricount + vibhagrohtashnagarcount

    
    # Shahadra (शाहदरा) Count
    vibhagshahadracount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='शाहदरा').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    
    # Gandhi Nagar (गांधीनगर) Count
    vibhagandhinagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='गांधीनगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    
    # Indraprastha (इन्द्रप्रस्थ) Count
    vibhagindraprasthacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='इन्द्रप्रस्थ').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    
    # Mayur Vihar (मयूर विहार) Count 
    vibhagmayurviharcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मयूर विहार').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for पूर्वी (विभाग)
    vibhagpurvisum_count = vibhagshahadracount + vibhagandhinagarcount + vibhagindraprasthacount + vibhagmayurviharcount
    
    # Lajpat Nagar दक्षिणी (लाजपत नगर) Count 
    vibhaglajpatnagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='लाजपत नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    
    # Badarpur दक्षिणी (बदरपुर) Count 
    vibhagbadarpurcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='बदरपुर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    
    # Kalkaji दक्षिणी ( कालका जी) Count 
    vibhagkalkajicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='कालका जी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for दक्षिणी (विभाग) राम कृष्ण पुरम
    vibhagdakshinsum_count = vibhaglajpatnagarcount + vibhagbadarpurcount + vibhagkalkajicount

        
    # Ambedkar राम कृष्ण पुरम ( अम्बेडकर ) Count 
    vibhagambedkarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='अम्बेडकर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
        
    # Mihirawali राम कृष्ण पुरम ( मिहिरावली ) Count 
    vibhagmihirawalicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मिहिरावली').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
        
    # Vasant राम कृष्ण पुरम ( वसंत ) Count 
    vibhagvasantcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='वसंत').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for राम कृष्ण पुरम (विभाग)
    vibhagramkrishnapuramsum_count = vibhagambedkarcount + vibhagmihirawalicount + vibhagvasantcount

            
    # Dwarka पश्चिमी ( द्वारका ) Count 
    vibhagdwarkacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='द्वारका').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
            
    # Nahargarh पश्चिमी ( नाहरगढ़ ) Count 
    vibhagnahargarhcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नाहरगढ़').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
            
    # Uttam पश्चिमी ( उत्तम ) Count 
    vibhaguttamcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='उत्तम').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
            
    # Nangloi पश्चिमी ( नांगलोई ) Count 
    vibhagnangloicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नांगलोई').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for पश्चिमी (विभाग)
    vibhagpashchimisum_count = vibhagdwarkacount + vibhagnahargarhcount + vibhaguttamcount + vibhagnangloicount
             
    # Tilak केशवपुरम ( तिलक ) Count 
    vibhagtilakcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='तिलक').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
             
    # Janakpuri केशवपुरम ( जनकपुरी ) Count 
    vibhagjanakpuricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='जनकपुरी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
             
    # Moti Nagar केशवपुरम ( मोती नगर ) Count 
    vibhagmotinagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मोती नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
             
    # Saraswati Vihar केशवपुरम ( सरस्वती विहार ) Count 
    vibhagsaraswativiharcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='सरस्वती विहार').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for केशवपुरम (विभाग)  
    vibhagkeshavpuramsum_count = vibhagtilakcount + vibhagjanakpuricount + vibhagmotinagarcount + vibhagsaraswativiharcount
               
    # Rohini उत्तरी ( रोहिणी ) Count 
    vibhagrohinicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='रोहिणी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
               
    # Kanjihawala उत्तरी ( कंझावला ) Count 
    vibhagkanjihawalacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='कंझावला').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
               
    # Narela उत्तरी ( नरेला ) Count 
    vibhagnarelacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नरेला').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
               
    # Burari उत्तरी ( बुराड़ी ) Count 
    vibhagburaricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='बुराड़ी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for उत्तरी (विभाग)  
    vibhaguttarisum_count = vibhagrohinicount + vibhagkanjihawalacount + vibhagnarelacount + vibhagburaricount
                   
    # Mukherjee Nagar झंडेवालान ( मुखर्जी नगर ) Count 
    vibhagmukherjeenagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मुखर्जी नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                   
    # Kamla Nagar झंडेवालान ( कमला नगर ) Count 
    vibhagkamlanagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='कमला नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                   
    # Karol Bagh झंडेवालान ( करोल बाग़ ) Count 
    vibhagkarolbaghcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='करोल बाग़').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                   
    # Patel झंडेवालान ( पटेल ) Count 
    vibhagpatelcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='विभाग',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='पटेल').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for झंडेवालान
    vibhagjhandewalan_count = vibhagmukherjeenagarcount + vibhagkamlanagarcount + vibhagkarolbaghcount + vibhagpatelcount
    total_register_vibhag_count = vibhagyamunaviharsum_count + vibhagpurvisum_count + vibhagdakshinsum_count + vibhagramkrishnapuramsum_count + vibhagpashchimisum_count + vibhagkeshavpuramsum_count + vibhaguttarisum_count + vibhagjhandewalan_count

#   ====================================================================== End विभाग ====================================================== 

#   ====================================================================== Start जिला ==================================================
               
    # Karawal Nagar यमुना विहार (  करावल नगर ) Count 
    jillakarawalnagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='करावल नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
               
    # Brahmapuri यमुना विहार ( ब्रहमपुरी ) Count 
    jillabrahmapuricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='ब्रहमपुरी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
               
    # Nand Nagari यमुना विहार ( नंद नगरी ) Count 
    jillanandnagaricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नंद नगरी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
               
    # Rohtash Nagar यमुना विहार ( रोहताश नगर ) Count 
    jillarohtashnagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='रोहताश नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for यमुना विहार (जिला)  शाहदरा
    jilayamunaviharsum_count = jillakarawalnagarcount + jillabrahmapuricount + jillanandnagaricount + jillarohtashnagarcount
                   
    # Shahadra पूर्वी ( शाहदरा ) Count 
    jillashahadracount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='शाहदरा').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                   
    # Gandhi Nagar पूर्वी ( गांधीनगर ) Count 
    jillagandhinagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='गांधीनगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                   
    # Gandhi Nagar पूर्वी ( इन्द्रप्रस्थ ) Count 
    jillaindraprasthacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='इन्द्रप्रस्थ').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                   
    # Mayur Vihar पूर्वी ( मयूर विहार ) Count 
    jillamayurviharcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मयूर विहार').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for पूर्वी (जिला)
    jilapurvisum_count = jillashahadracount + jillagandhinagarcount + jillaindraprasthacount + jillamayurviharcount
                    
    # Lajpat Nagar दक्षिणी ( लाजपत नगर ) Count 
    jillalajpatnagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='लाजपत नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                    
    # Badarpur दक्षिणी ( बदरपुर ) Count 
    jillabadarpurcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='लाजपत नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                    
    # Kalkaji दक्षिणी ( कालका जी ) Count 
    jillakalkajicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='कालका जी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for दक्षिणी (जिला) 
    jiladakshinsum_count = jillalajpatnagarcount + jillabadarpurcount + jillakalkajicount

    # Ambedkar राम कृष्ण पुरम ( अम्बेडकर ) Count 
    jillaambedkarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='अम्बेडकर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Mihirawali राम कृष्ण पुरम ( मिहिरावली ) Count 
    jillamihirawalicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मिहिरावली').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Vasant राम कृष्ण पुरम ( वसंत ) Count 
    jillavasantcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='वसंत').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for राम कृष्ण पुरम (जिला) 
    jilaramkrishnapuramsum_count = jillaambedkarcount + jillamihirawalicount + jillavasantcount
   
    # Dwarka पश्चिमी ( द्वारका ) Count 
    jilladwarkacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='द्वारका').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
   
    # Nahargarh राम कृष्ण पुरम ( नाहरगढ़ ) Count 
    jillanahargarhcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नाहरगढ़').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
   
    # Uttam राम कृष्ण पुरम ( उत्तम ) Count 
    jillauttamcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='उत्तम').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
   
    # Nangloi राम कृष्ण पुरम ( नांगलोई ) Count 
    jillanangloicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नांगलोई').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
   
    # sum of all individual counts for पश्चिमी (जिला)
    jilapashchimisum_count = jilladwarkacount + jillauttamcount + jillanangloicount
 
    # Tilak केशवपुरम ( तिलक ) Count 
    jillatilakcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='तिलक').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
 
    # Janakpuri केशवपुरम ( जनकपुरी ) Count 
    jillajanakpuricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='जनकपुरी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
 
    # Moti Nagar केशवपुरम ( मोती नगर ) Count 
    jillamotinagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मोती नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
 
    # Saraswati Vihar केशवपुरम ( सरस्वती विहार ) Count 
    jillasaraswativiharcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='सरस्वती विहार').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for केशवपुरम (जिला) 
    jilakeshavpuramsum_count = jillatilakcount + jillajanakpuricount + jillamotinagarcount + jillasaraswativiharcount
   
    # Rohini उत्तरी ( रोहिणी ) Count 
    jillasrohinicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='रोहिणी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Kanjihawala उत्तरी ( कंझावला ) Count 
    jillakanjihawalacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='कंझावला').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Narela उत्तरी ( नरेला ) Count 
    jillanarelacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नरेला').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Burari उत्तरी ( बुराड़ी ) Count 
    jillaburaricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='बुराड़ी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for उत्तरी (जिला) 
    jilauttarisum_count = jillasrohinicount + jillakanjihawalacount + jillanarelacount + jillaburaricount

    
    # Mukherjee Nagar झंडेवालान ( मुखर्जी नगर ) Count 
    jillamukherjeenagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मुखर्जी नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    
    # Kamla Nagar झंडेवालान ( कमला नगर ) Count 
    jillakamlanagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='कमला नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    
    # Karol Bagh झंडेवालान ( करोल बाग़ ) Count 
    jillakarolbaghcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='करोल बाग़').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    
    # Patel झंडेवालान ( पटेल ) Count 
    jillapatelcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='जिला',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='पटेल').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for झंडेवालान (जिला)
    jillajhandewalan_count = jillamukherjeenagarcount + jillakamlanagarcount + jillakarolbaghcount + jillapatelcount
    total_register_jila_count = jilayamunaviharsum_count + jilapurvisum_count + jiladakshinsum_count + jilaramkrishnapuramsum_count + jilapashchimisum_count + jilakeshavpuramsum_count + jilauttarisum_count + jillajhandewalan_count
#   ====================================================================== End जिला ==================================================================================================


#   ====================================================================== Start नगर ==================================================================================================

    # Karawal Nagar यमुना विहार (  करावल नगर ) Count 
    nagarkarawalnagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='करावल नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
               
    # Brahmapuri यमुना विहार ( ब्रहमपुरी ) Count 
    nagarbrahmapuricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='ब्रहमपुरी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
               
    # Nand Nagari यमुना विहार ( नंद नगरी ) Count 
    nagarnandnagaricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नंद नगरी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
               
    # Rohtash Nagar यमुना विहार ( रोहताश नगर ) Count 
    nagarrohtashnagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='रोहताश नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for यमुना विहार (नगर)
    nagaryamunaviharsum_count = nagarkarawalnagarcount + nagarbrahmapuricount + nagarnandnagaricount + nagarrohtashnagarcount

    # Shahadra पूर्वी ( शाहदरा ) Count 
    nagarshahadracount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='शाहदरा').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                   
    # Gandhi Nagar पूर्वी ( गांधीनगर ) Count 
    jnagarandhinagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='गांधीनगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                   
    # Gandhi Nagar पूर्वी ( इन्द्रप्रस्थ ) Count 
    nagarindraprasthacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='इन्द्रप्रस्थ').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                   
    # Mayur Vihar पूर्वी ( मयूर विहार ) Count 
    nagarmayurviharcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मयूर विहार').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for पूर्वी (नगर)
    nagarpurvisum_count = nagarshahadracount + jnagarandhinagarcount + nagarindraprasthacount + nagarmayurviharcount

    # Lajpat Nagar दक्षिणी ( लाजपत नगर ) Count 
    nagarlajpatnagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='लाजपत नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                    
    # Badarpur दक्षिणी ( बदरपुर ) Count 
    nagarbadarpurcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='लाजपत नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
                    
    # Kalkaji दक्षिणी ( कालका जी ) Count 
    nagarkalkajicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='कालका जी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for दक्षिणी (नगर) 
    nagardakshinsum_count = nagarlajpatnagarcount + nagarbadarpurcount + nagarkalkajicount

    # Ambedkar राम कृष्ण पुरम ( अम्बेडकर ) Count 
    nagarambedkarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='अम्बेडकर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Mihirawali राम कृष्ण पुरम ( मिहिरावली ) Count 
    nagarmihirawalicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मिहिरावली').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Vasant राम कृष्ण पुरम ( वसंत ) Count 
    nagarvasantcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='वसंत').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for राम कृष्ण पुरम (नगर) 
    nagarramkrishnapuramsum_count = nagarambedkarcount + nagarmihirawalicount + nagarvasantcount

    # Dwarka पश्चिमी ( द्वारका ) Count 
    nagardwarkacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='द्वारका').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
   
    # Nahargarh राम कृष्ण पुरम ( नाहरगढ़ ) Count 
    nagarnahargarhcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नाहरगढ़').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
   
    # Uttam राम कृष्ण पुरम ( उत्तम ) Count 
    nagaruttamcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='उत्तम').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
   
    # Nangloi राम कृष्ण पुरम ( नांगलोई ) Count 
    nagarnangloicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नांगलोई').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
   
    # sum of all individual counts for पश्चिमी (नगर)
    nagarpashchimisum_count = nagardwarkacount + nagarnahargarhcount + nagaruttamcount + nagarnangloicount
 
    # Tilak केशवपुरम ( तिलक ) Count 
    nagartilakcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='तिलक').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
 
    # Janakpuri केशवपुरम ( जनकपुरी ) Count 
    nagarjanakpuricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='जनकपुरी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
 
    # Moti Nagar केशवपुरम ( मोती नगर ) Count 
    nagarmotinagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मोती नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
 
    # Saraswati Vihar केशवपुरम ( सरस्वती विहार ) Count 
    nagarsaraswativiharcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='सरस्वती विहार').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for केशवपुरम (नगर) 
    nagarkeshavpuramsum_count = nagartilakcount + nagarjanakpuricount + nagarmotinagarcount + nagarsaraswativiharcount
   
    # Rohini उत्तरी ( रोहिणी ) Count 
    nagarsrohinicount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='रोहिणी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Kanjihawala उत्तरी ( कंझावला ) Count 
    nagarkanjihawalacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='कंझावला').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Narela उत्तरी ( नरेला ) Count 
    nagarnarelacount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='नरेला').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # Burari उत्तरी ( बुराड़ी ) Count 
    nagarburaricount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='बुराड़ी').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for उत्तरी (नगर) 
    nagaruttarisum_count = nagarsrohinicount + nagarkanjihawalacount + nagarnarelacount + nagarburaricount

        
    # Mukherjee Nagar झंडेवालान ( मुखर्जी नगर ) Count 
    nagarmukherjeenagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='मुखर्जी नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    
    # Kamla Nagar झंडेवालान ( कमला नगर ) Count 
    nagarkamlanagarcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='कमला नगर').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    
    # Karol Bagh झंडेवालान ( करोल बाग़ ) Count 
    nagarkarolbaghcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='करोल बाग़').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()
    
    # Patel झंडेवालान ( पटेल ) Count 
    nagarpatelcount = BarcodeScan.objects.filter(phone_number__in=RegisterSamautkarshRegistration.objects.filter(ekai='नगर',nagar_address__in=NagarMaster.objects.filter(jila_id__in=ZilaMaster.objects.filter(vibhag_id__in=VibhagMaster.objects.filter(prant_id__in=PrantMaster.objects.all().values('prant_id')).values('vibhag_id'),jila_hindi='पटेल').values('jila_id')).values('nagar_hindi')).values('phone_number')).count()

    # sum of all individual counts for झंडेवालान (नगर)
    nagarjhandewalan_count = nagarmukherjeenagarcount + nagarkamlanagarcount + nagarkarolbaghcount + nagarpatelcount
    total_register_nagar_count = nagaryamunaviharsum_count + nagarpurvisum_count + nagardakshinsum_count + nagarramkrishnapuramsum_count + nagarpashchimisum_count + nagarkeshavpuramsum_count + nagaruttarisum_count + nagarjhandewalan_count
    #   ====================================================================== End नगर ==================================================================================================

    context = {
        'karawalnagarcount': karawalnagarcount,'brahmpurinagarcount': brahmpurinagarcount,'nandnagaricount': nandnagaricount,'rohtashnagarcount': rohtashnagarcount,'yamunaviharsum_count':yamunaviharsum_count,'shahdaracount': shahdaracount,'gandhinagarcount': gandhinagarcount,'indraprasthacount': indraprasthacount,'mayurviharcount':mayurviharcount,'purvisum_count': purvisum_count,'lajpatnagarcount': lajpatnagarcount,'badarpurcount': badarpurcount,'kalkajeecount': kalkajeecount,
        'dakshinsum_count': dakshinsum_count, 'ambedkarcount': ambedkarcount, 'mihirawalicount': mihirawalicount, 'vasantcount': vasantcount, 'ramkrishnapuramsum_count': ramkrishnapuramsum_count, 'dawrkacount': dawrkacount, 'nahargarhcount': nahargarhcount, 'uttamcount': uttamcount, 'nangloicount': nangloicount, 'pashchimisum_count': pashchimisum_count, 'tilakcount': tilakcount, 'janakpuricount': janakpuricount, 'motinagarcount': motinagarcount, 'saraswativiharcount': saraswativiharcount, 'keshavpuramsum_count': keshavpuramsum_count, 'rohinicount': rohinicount, 'kanjhawalacount': kanjhawalacount, 'narelacount': narelacount, 'buraricount': buraricount, 'uttarisum_count': uttarisum_count, 'mukherjeenagarcount': mukherjeenagarcount, 'kamlacount': kamlacount, 'karolbaghcount': karolbaghcount, 'patelcount': patelcount, 'jhandewalan_count': jhandewalan_count, 'vibhagkarawalnagarcount': vibhagkarawalnagarcount, 'vibhagbrahmapuricount': vibhagbrahmapuricount, 'vibhagnandnagaricount': vibhagnandnagaricount, 'vibhagrohtashnagarcount': vibhagrohtashnagarcount, 'vibhagyamunaviharsum_count': vibhagyamunaviharsum_count, 'vibhagshahadracount': vibhagshahadracount, 'vibhagandhinagarcount': vibhagandhinagarcount, 'vibhagindraprasthacount': vibhagindraprasthacount, 'vibhagmayurviharcount': vibhagmayurviharcount, 'vibhagpurvisum_count': vibhagpurvisum_count, 'vibhaglajpatnagarcount': vibhaglajpatnagarcount, 'vibhagbadarpurcount': vibhagbadarpurcount, 'vibhagkalkajicount': vibhagkalkajicount,    'vibhagdakshinsum_count': vibhagdakshinsum_count, 'vibhagambedkarcount': vibhagambedkarcount, 'vibhagmihirawalicount': vibhagmihirawalicount, 'vibhagvasantcount': vibhagvasantcount, 'vibhagramkrishnapuramsum_count': vibhagramkrishnapuramsum_count, 'vibhagdwarkacount': vibhagdwarkacount, 'vibhagnahargarhcount': vibhagnahargarhcount, 'vibhaguttamcount': vibhaguttamcount, 'vibhagnangloicount': vibhagnangloicount, 'vibhagpashchimisum_count': vibhagpashchimisum_count, 'vibhagtilakcount': vibhagtilakcount, 'vibhagjanakpuricount': vibhagjanakpuricount, 'vibhagmotinagarcount': vibhagmotinagarcount, 'vibhagsaraswativiharcount': vibhagsaraswativiharcount, 'vibhagkeshavpuramsum_count': vibhagkeshavpuramsum_count, 'vibhagrohinicount': vibhagrohinicount, 'vibhagkanjihawalacount': vibhagkanjihawalacount, 'vibhagnarelacount': vibhagnarelacount, 'vibhagburaricount':
        vibhagburaricount, 'vibhaguttarisum_count': vibhaguttarisum_count, 'vibhagmukherjeenagarcount': vibhagmukherjeenagarcount, 'vibhagkamlanagarcount': vibhagkamlanagarcount,
        'vibhagkarolbaghcount': vibhagkarolbaghcount, 'vibhagpatelcount': vibhagpatelcount, 'vibhagjhandewalan_count': vibhagjhandewalan_count, 'jillakarawalnagarcount': jillakarawalnagarcount, 'jillabrahmapuricount': jillabrahmapuricount, 'jillanandnagaricount': jillanandnagaricount, 'jillarohtashnagarcount': jillarohtashnagarcount, 'jilayamunaviharsum_count': jilayamunaviharsum_count, 'jillashahadracount': jillashahadracount, 'jillagandhinagarcount': jillagandhinagarcount, 'jillaindraprasthacount':
        jillaindraprasthacount, 'jillamayurviharcount': jillamayurviharcount, 'jilapurvisum_count': jilapurvisum_count, 'jillalajpatnagarcount': jillalajpatnagarcount, 'jillabadarpurcount': jillabadarpurcount, 'jillakalkajicount': jillakalkajicount, 'jiladakshinsum_count': jiladakshinsum_count, 'jillaambedkarcount': jillaambedkarcount,
        'jillamihirawalicount': jillamihirawalicount, 'jillavasantcount': jillavasantcount, 'jilaramkrishnapuramsum_count': jilaramkrishnapuramsum_count, 'jilladwarkacount': jilladwarkacount, 'jillanahargarhcount': jillanahargarhcount, 'jillauttamcount': jillauttamcount, 'jillanangloicount': jillanangloicount, 'jilapashchimisum_count': jilapashchimisum_count, 'jillatilakcount': jillatilakcount, 'jillajanakpuricount': jillajanakpuricount, 'jillamotinagarcount': jillamotinagarcount, 'jillasaraswativiharcount': jillasaraswativiharcount, 'jilakeshavpuramsum_count': jilakeshavpuramsum_count, 'jillasrohinicount': jillasrohinicount, 'jillakanjihawalacount': jillakanjihawalacount, 'jillanarelacount': jillanarelacount, 'jillaburaricount': jillaburaricount, 'jilauttarisum_count': jilauttarisum_count, 'jillamukherjeenagarcount': jillamukherjeenagarcount, 'jillakamlanagarcount': jillakamlanagarcount, 'jillakarolbaghcount': jillakarolbaghcount, 'jillapatelcount': jillapatelcount, 'jillajhandewalan_count': jillajhandewalan_count,
        'nagarkarawalnagarcount': nagarkarawalnagarcount, 'nagarbrahmapuricount': nagarbrahmapuricount, 'nagarnandnagaricount': nagarnandnagaricount, 'nagarrohtashnagarcount': nagarrohtashnagarcount, 'nagaryamunaviharsum_count': nagaryamunaviharsum_count, 'nagarshahadracount': nagarshahadracount, 'jnagarandhinagarcount': jnagarandhinagarcount, 'nagarindraprasthacount': nagarindraprasthacount, 'nagarmayurviharcount': nagarmayurviharcount, 'nagarpurvisum_count': nagarpurvisum_count, 'nagarlajpatnagarcount': nagarlajpatnagarcount, 'nagarbadarpurcount': nagarbadarpurcount, 'nagarkalkajicount': nagarkalkajicount, 'nagardakshinsum_count': nagardakshinsum_count, 'nagarambedkarcount': nagarambedkarcount, 'nagarmihirawalicount': nagarmihirawalicount, 'nagarvasantcount': nagarvasantcount, 'nagarramkrishnapuramsum_count': nagarramkrishnapuramsum_count, 'nagardwarkacount': nagardwarkacount, 'nagarnahargarhcount': nagarnahargarhcount, 'nagaruttamcount': nagaruttamcount, 'nagarnangloicount': nagarnangloicount, 'nagarpashchimisum_count': nagarpashchimisum_count, 'nagartilakcount': nagartilakcount, 'nagarjanakpuricount': nagarjanakpuricount, 'nagarmotinagarcount': nagarmotinagarcount, 'nagarsaraswativiharcount': nagarsaraswativiharcount, 'nagarkeshavpuramsum_count': nagarkeshavpuramsum_count, 'nagarsrohinicount': nagarsrohinicount, 'nagarkanjihawalacount': nagarkanjihawalacount, 'nagarnarelacount': nagarnarelacount, 'nagarburaricount': nagarburaricount, 'nagaruttarisum_count': nagaruttarisum_count, 'nagarmukherjeenagarcount': nagarmukherjeenagarcount, 'nagarkamlanagarcount': nagarkamlanagarcount, 'nagarkarolbaghcount': nagarkarolbaghcount, 'nagarpatelcount': nagarpatelcount, 'nagarjhandewalan_count': nagarjhandewalan_count, 'total_register_prant_count': total_register_prant_count, 'total_register_vibhag_count': total_register_vibhag_count, 'total_register_jila_count': total_register_jila_count, 'total_register_nagar_count': total_register_nagar_count
    }
    return render(request, 'superadmin_dashboard/totalregistercount.html', context)

@role_required(['SUPERADMIN'])
def superadmin_dashboard_totalothercount(request):
    context = {}
    return render(request, 'superadmin_dashboard/totalothercount.html', context) 
# ========================================== Start Super Admin Dashboard nagar_chart_data Views===================================================

# Chart-1 data for nagar
@role_required(['SUPERADMIN'])
def vibhag_chart_data(request):
    selected_vibhag = request.GET.get('vibhag', None)

    vibhag_data = (
        RegisterSamautkarshRegistration.objects.filter(
            ekai='विभाग',
            vibhag__in=VibhagMaster.objects.values_list('vibhag_hindi', flat=True),
            phone_number__in=BarcodeScan.objects.values_list('phone_number', flat=True)
        ).count()
    )

    # If a specific nagar is selected, filter the data
    if selected_vibhag:
        vibhag_data = vibhag_data.filter(vibhag=selected_vibhag)

    labels = [entry['vibhag'] for entry in vibhag_data]
    data = [entry['count'] for entry in vibhag_data]

    return JsonResponse({'labels': labels, 'data': data})


# Chart-2 data for nagar
@role_required(['SUPERADMIN'])
def nagar_chart_data(request):
    selected_nagar = request.GET.get('nagar', None)

    nagar_data = (
        RegisterSamautkarshRegistration.objects
        .values('nagar_address')
        .annotate(count=Count('nagar_address'))
        .order_by('-count')
    )

    # If a specific nagar is selected, filter the data
    if selected_nagar:
        nagar_data = nagar_data.filter(nagar_address=selected_nagar)

    labels = [entry['nagar_address'] for entry in nagar_data]
    data = [entry['count'] for entry in nagar_data]

    return JsonResponse({'labels': labels, 'data': data})

# =============================================== End Super Admin Dashboard nagar_chart_data Views ================================================

# ======================================================= Start Sub-Admin Dashboard Views =========================================================
@role_required(['SUBADMIN'])
def sub_admin_dashboard(request):
    mobile = request.session.get('mobile')
    role_sublevel = Admin.objects.filter(mobile=mobile)
    role_sublevel = list(role_sublevel)
    role_sublevel=role_sublevel[0]
    mappings={}

    # Fetch all records from the database
    if role_sublevel.role_level == 'Vibhag':
        raw_data=['Jila','Nagar','Mandal','Basti','Upbasti']
        mappings['role_level']=raw_data
        raw_data = list(ZilaMaster.objects.select_related("vibhag_id").filter(vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("jila_hindi", flat=True))
        mappings['Jila']=raw_data

        raw_data = list(NagarMaster.objects.select_related("jila_id__vibhag_id").filter(jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("nagar_hindi", flat=True))
        mappings['Nagar']=raw_data
        raw_data = list(MandalMaster.objects.select_related("nagar_id__jila_id__vibhag_id").filter(nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("mandal_hindi", flat=True))
        mappings['Mandal']=raw_data
        raw_data = list(BastiMaster.objects.select_related("mandal_id__nagar_id__jila_id__vibhag_id").filter(mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("basti_hindi", flat=True))
        mappings['Basti']=raw_data
        raw_data = list(UpbastiMaster.objects.select_related("basti_id__mandal_id__nagar_id__jila_id__vibhag_id").filter(basti_id__mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("upbasti_hindi", flat=True))
        mappings['Upbasti']=raw_data

        sql_query = f"SELECT register_id,register_samautkarsh_registration.name,register_samautkarsh_registration.phone_number,gender,prant_hindi,vibhag_hindi,jila_hindi,register_samautkarsh_registration.nagar,register_samautkarsh_registration.dayitv,status,register_samautkarsh_registration.ekai,referral_code,user_type,vividhsangathan FROM register_samautkarsh_registration  INNER JOIN nagar_master ON register_samautkarsh_registration.nagar = nagar_master.nagar_hindi INNER JOIN zila_master ON nagar_master.jila_id = zila_master.jila_id INNER JOIN vibhag_master ON zila_master.vibhag_id = vibhag_master.vibhag_id INNER JOIN prant_master ON vibhag_master.prant_id = prant_master.prant_id inner join barcode_scan on register_samautkarsh_registration.phone_number=barcode_scan.phone_number WHERE vibhag_master.vibhag_hindi = '{role_sublevel.role_sublevel}' ORDER BY FIELD(status, 'pending', 'Approve', 'Reject'), register_samautkarsh_registration.ekai DESC;"
    # AND register_samautkarsh_registration.ekai in ('Vibhag','jila','nagar''mandal','basti','upbasti')
    if role_sublevel.role_level == 'Prant':
        raw_data=['Vibhag','Jila','Nagar','Mandal','Basti','Upbasti']
        mappings['role_level']=raw_data
        raw_data = list(VibhagMaster.objects.select_related("prant_id").filter(prant_id__prant_hindi=role_sublevel.role_sublevel).values_list("vibhag_hindi", flat=True))
        mappings['Vibhag']=raw_data
        raw_data = list(ZilaMaster.objects.select_related("vibhag_id").filter(vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("jila_hindi", flat=True))
        mappings['Jila']=raw_data
        raw_data = list(NagarMaster.objects.select_related("jila_id__vibhag_id").filter(jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("nagar_hindi", flat=True))
        mappings['Nagar']=raw_data
        raw_data = list(MandalMaster.objects.select_related("nagar_id__jila_id__vibhag_id").filter(nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("mandal_hindi", flat=True))
        mappings['Mandal']=raw_data
        raw_data = list(BastiMaster.objects.select_related("mandal_id__nagar_id__jila_id__vibhag_id").filter(mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("basti_hindi", flat=True))
        mappings['Basti']=raw_data
        raw_data = list(UpbastiMaster.objects.select_related("basti_id__mandal_id__nagar_id__jila_id__vibhag_id").filter(basti_id__mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("upbasti_hindi", flat=True))
        mappings['Upbasti']=raw_data#print("superadmin_userRole:", mappings)
        sql_query = f"SELECT register_id,register_samautkarsh_registration.name,register_samautkarsh_registration.phone_number,gender,prant_hindi,vibhag_hindi,jila_hindi,register_samautkarsh_registration.nagar,register_samautkarsh_registration.dayitv,status,register_samautkarsh_registration.ekai,referral_code,user_type,vividhsangathan FROM register_samautkarsh_registration INNER JOIN nagar_master ON register_samautkarsh_registration.nagar = nagar_master.nagar_hindi INNER JOIN zila_master ON nagar_master.jila_id = zila_master.jila_id INNER JOIN vibhag_master ON zila_master.vibhag_id = vibhag_master.vibhag_id INNER JOIN prant_master ON vibhag_master.prant_id = prant_master.prant_id inner join barcode_scan on register_samautkarsh_registration.phone_number=barcode_scan.phone_number WHERE prant_master.prant_hindi = '{role_sublevel.role_sublevel}'  ORDER BY FIELD(status, 'pending', 'Approve', 'Reject'), register_samautkarsh_registration.ekai DESC"
    if role_sublevel.role_level == 'Jila':
        raw_data=['Nagar','Mandal','Basti','Upbasti']
        mappings['role_level']=raw_data
        raw_data = list(NagarMaster.objects.select_related("jila_id__vibhag_id").filter(jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("nagar_hindi", flat=True))
        mappings['Nagar']=raw_data

        raw_data = list(MandalMaster.objects.select_related("nagar_id__jila_id__vibhag_id").filter(nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("mandal_hindi", flat=True))
        mappings['Mandal']=raw_data
        raw_data = list(BastiMaster.objects.select_related("mandal_id__nagar_id__jila_id__vibhag_id").filter(mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("basti_hindi", flat=True))
        mappings['Basti']=raw_data
        raw_data = list(UpbastiMaster.objects.select_related("basti_id__mandal_id__nagar_id__jila_id__vibhag_id").filter(basti_id__mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("upbasti_hindi", flat=True))
        mappings['Upbasti']=raw_data

        sql_query = f"SELECT register_id,register_samautkarsh_registration.name,register_samautkarsh_registration.phone_number,gender,prant_hindi,vibhag_hindi,jila_hindi,nagar_address,register_samautkarsh_registration.dayitv,status,register_samautkarsh_registration.ekai,referral_code,user_type,vividhsangathan FROM register_samautkarsh_registration  INNER JOIN nagar_master ON register_samautkarsh_registration.nagar_address = nagar_master.nagar_hindi INNER JOIN zila_master ON nagar_master.jila_id = zila_master.jila_id INNER JOIN vibhag_master ON zila_master.vibhag_id = vibhag_master.vibhag_id INNER JOIN prant_master ON vibhag_master.prant_id = prant_master.prant_id inner join barcode_scan on register_samautkarsh_registration.phone_number=barcode_scan.phone_number WHERE zila_master.jila_hindi = '{role_sublevel.role_sublevel}'  ORDER BY FIELD(status, 'pending', 'Approve', 'Reject'), register_samautkarsh_registration.ekai DESC"
    if role_sublevel.role_level == 'Nagar':
        raw_data=['Mandal','Basti','Upbasti']
        mappings['role_level']=raw_data
        raw_data = list(MandalMaster.objects.select_related("nagar_id__jila_id__vibhag_id").filter(nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("mandal_hindi", flat=True))
        mappings['Mandal']=raw_data
        raw_data = list(BastiMaster.objects.select_related("mandal_id__nagar_id__jila_id__vibhag_id").filter(mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("basti_hindi", flat=True))
        mappings['Basti']=raw_data
        raw_data = list(UpbastiMaster.objects.select_related("basti_id__mandal_id__nagar_id__jila_id__vibhag_id").filter(basti_id__mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("upbasti_hindi", flat=True))
        mappings['Upbasti']=raw_data
        
        sql_query = f"SELECT register_id,register_samautkarsh_registration.name,register_samautkarsh_registration.phone_number,gender,prant_hindi,vibhag_hindi,jila_hindi,nagar_address,register_samautkarsh_registration.dayitv,status,register_samautkarsh_registration.ekai,referral_code,user_type,vividhsangathan FROM register_samautkarsh_registration  INNER JOIN nagar_master ON register_samautkarsh_registration.nagar_address = nagar_master.nagar_hindi INNER JOIN zila_master ON nagar_master.jila_id = zila_master.jila_id INNER JOIN vibhag_master ON zila_master.vibhag_id = vibhag_master.vibhag_id INNER JOIN prant_master ON vibhag_master.prant_id = prant_master.prant_id inner join barcode_scan on register_samautkarsh_registration.phone_number=barcode_scan.phone_number WHERE nagar_master.nagar_hindi = '{role_sublevel.role_sublevel}' ORDER BY FIELD(status, 'pending', 'Approve', 'Reject'), register_samautkarsh_registration.ekai DESC"
    
    if role_sublevel.role_level == 'Mandal':
        raw_data=['Basti','Upbasti']
        mappings['role_level']=raw_data
        mappings['Basti']=raw_data
        raw_data = list(UpbastiMaster.objects.select_related("basti_id__mandal_id__nagar_id__jila_id__vibhag_id").filter(basti_id__mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("upbasti_hindi", flat=True))
        mappings['Upbasti']=raw_data

        sql_query = f"SELECT register_id,register_samautkarsh_registration.name,register_samautkarsh_registration.phone_number,gender,prant_hindi,vibhag_hindi,jila_hindi,nagar_address,register_samautkarsh_registration.dayitv,status,register_samautkarsh_registration.ekai,referral_code,user_type,vividhsangathan FROM register_samautkarsh_registration  INNER JOIN nagar_master ON register_samautkarsh_registration.nagar_address = nagar_master.nagar_hindi INNER JOIN zila_master ON nagar_master.jila_id = zila_master.jila_id INNER JOIN vibhag_master ON zila_master.vibhag_id = vibhag_master.vibhag_id INNER JOIN prant_master ON vibhag_master.prant_id = prant_master.prant_id inner join barcode_scan on register_samautkarsh_registration.phone_number=barcode_scan.phone_number WHERE nagar_master.nagar_hindi = '{role_sublevel.role_sublevel}' ORDER BY FIELD(status, 'pending', 'Approve', 'Reject'), register_samautkarsh_registration.ekai DESC"

    if role_sublevel.role_level == 'Basti':
        raw_data=['Upbasti']
        mappings['role_level']=raw_data
        raw_data = list(UpbastiMaster.objects.select_related("basti_id__mandal_id__nagar_id__jila_id__vibhag_id").filter(basti_id__mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("upbasti_hindi", flat=True))
        mappings['Upbasti']=raw_data

        sql_query = f"SELECT register_id,register_samautkarsh_registration.name,register_samautkarsh_registration.phone_number,gender,prant_hindi,vibhag_hindi,jila_hindi,nagar_address,register_samautkarsh_registration.dayitv,status,register_samautkarsh_registration.ekai,referral_code,user_type,vividhsangathan FROM register_samautkarsh_registration  INNER JOIN nagar_master ON register_samautkarsh_registration.nagar_address = nagar_master.nagar_hindi INNER JOIN zila_master ON nagar_master.jila_id = zila_master.jila_id INNER JOIN vibhag_master ON zila_master.vibhag_id = vibhag_master.vibhag_id INNER JOIN prant_master ON vibhag_master.prant_id = prant_master.prant_id inner join barcode_scan on register_samautkarsh_registration.phone_number=barcode_scan.phone_number WHERE nagar_master.nagar_hindi = '{role_sublevel.role_sublevel}' ORDER BY FIELD(status, 'pending', 'Approve', 'Reject'), register_samautkarsh_registration.ekai DESC"

    if role_sublevel.role_level == 'Upbasti':
        raw_data=['']
        mappings['role_level']=raw_data
        raw_data = []
        mappings['Upbasti']=raw_data

        sql_query = f"SELECT register_id,register_samautkarsh_registration.name,register_samautkarsh_registration.phone_number,gender,prant_hindi,vibhag_hindi,jila_hindi,nagar_address,register_samautkarsh_registration.dayitv,status,register_samautkarsh_registration.ekai,referral_code,user_type,vividhsangathan FROM register_samautkarsh_registration  INNER JOIN nagar_master ON register_samautkarsh_registration.nagar_address = nagar_master.nagar_hindi INNER JOIN zila_master ON nagar_master.jila_id = zila_master.jila_id INNER JOIN vibhag_master ON zila_master.vibhag_id = vibhag_master.vibhag_id INNER JOIN prant_master ON vibhag_master.prant_id = prant_master.prant_id inner join barcode_scan on register_samautkarsh_registration.phone_number=barcode_scan.phone_number WHERE nagar_master.nagar_hindi = '{role_sublevel.role_sublevel}' ORDER BY FIELD(status, 'pending', 'Approve', 'Reject'), register_samautkarsh_registration.ekai DESC"

    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        results = cursor.fetchall()

    # Status counts (can be outside pagination)
    total_count = len(results)
    pending_count = len([r for r in results if str(r[9]).lower() == 'pending'])
    approve_count = len([r for r in results if 'Approve' in r])
    reject_count = len([r for r in results if 'Reject' in r])

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(results, 15)  # Show 15 records per page

    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    print(results)

    referral_code = RegisterSamautkarshRegistration.objects.values_list('referral_code', flat=True).distinct()
    mappings['referral_code'] = list(referral_code)
    raw_data = DayitvMaster.objects.select_related("ekai_id").values_list("dayitv_name", "ekai_id__ekai_name")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    result['Nagar'] = result.pop('nagar')
    result['Prant'] = result.pop('prant')
    result['Vibhag'] = result.pop('vibhag')
    result['Jila'] = result.pop('jila')

    mappings['dayitvaMapping'] = result

    #jilaToNagar extraction
    raw_data = NagarMaster.objects.select_related("jila_id").values_list("nagar_hindi", "jila_id__jila_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['jilaToNagar'] = result

    #VibhagToJila extraction
    raw_data = ZilaMaster.objects.select_related("vibhag_id").values_list("jila_hindi", "vibhag_id__vibhag_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['vibhagToJila'] = result

    #prantToVibhag extraction
    raw_data = VibhagMaster.objects.select_related("prant_id").values_list("vibhag_hindi", "prant_id__prant_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['prantToVibhag'] = result
    role_defined=request.session.get("role_level")
    role_sublevel=request.session.get('role_sublevel')

    if request.method == "POST":
        # Handle POST request (update status)
        register_id = request.POST.get('register_id')  # Get the ID of the record to update
        new_status = request.POST.get('status')  # Get the new status (अनिर्णीत, स्वीकृत, अस्वीकार)
   
        # Find the corresponding BarcodeScan record
        register_scan = RegisterSamautkarshRegistration.objects.get(register_id=register_id)
        #print(register_scan)
        mobile = register_scan.phone_number
        barcode_scan = BarcodeScan.objects.get(phone_number = mobile)
        #print(barcode_scan)

        # Update the status
        barcode_scan.status = new_status
        barcode_scan.Approving_person=request.session["mobile"]
        image_path = barcode_scan.qrcode
        barcode_scan.save()
        if new_status=='Approve':
            url = "http://sms.messageindia.in/v2/sendSMS"
                    # API parameters
            params = {
                    "username": "utkarshbharatresearch",  # Your API username
                    "message": f"Namaste ji, Your Reg. has been completed. Get the QR Code from https://samutkarsh.in/ Team Samurkarsh Bharat",  # Message content
                    "sendername": "SBRPLW",  # Sender name (approved by provider)
                    "smstype": "TRANS",  # Transactional or promotional
                    "numbers": mobile,  # Mobile numbers (comma-separated)
                    "apikey": "9fcec71f-f3ee-4b7c-8099-ee8cbc06478b",  # Your API key
                    "peid": "1701173858154413324",  # PE ID from provider
                    "templateid": "1707173883044603731"  # Template ID from provider
                    }
                    # Sending the GET request
            response = requests.get(url, params=params)
            url = "http://148.251.129.118/wapp/api/send"

            # API key and message details
            params = {
                "apikey": "747f01ec1e574d74bb6f557c6d304692",  # Your API key
                "mobile": mobile,  # Comma-separated mobile numbers
                "msg": "❍❍❍❖❖ केशवकुंज दर्शन ❖❖❍❍❍\n\n⊰᯽⊱┈─╌❊ ⚜️ ❊╌─┈⊰᯽⊱\n\nआपका नाम कार्यक्रम हेतु पंजीकृत हुआ है। केशवकुंज दर्शन हेतु आप सादर आमंत्रित हैं।\n\nसुरक्षा कारणों से आपकी सुविधा हेतु कार्यक्रम में प्रवेश अनुमति हेतु QR कोड संलग्न है।\n\nकृपया ध्यान दें ..!!\n\n👉 आपके जिले/विभाग के लिए जो दिन निश्चित हुआ है, उसी दिन आपका आना अपेक्षित है।\n\n👉 प्रवेश द्वार पर QR Code दिखाना आवश्यक है।\n\n👉 कृपया अपना पहचान पत्र अपने साथ अवश्य लाएं\n\nविशेष :- कार्यक्रम स्थल पर सुविधा पूर्वक पहुंचने के लिए कृपया Metro का प्रयोग कर झंडेवालान मेट्रो स्टेशन पर उतरें।\n\nनिवेदक\n\nश्री केशव स्मारक समिति, दिल्ली\n\n", "img1": "https://samutkarsh.in/static/QRCodes/{}.jpg".format(mobile)
            }
            # Sending the GET request
            response = requests.get(url, params=params)
        else:
            pass

        # Return a JSON response for success
        return JsonResponse({'success': True, 'message': 'Status updated successfully.'})
    
    context = {"mappings": mappings,'registrations': results,'role_defined': role_defined,'role_sublevel': role_sublevel, 'total_count': total_count, 'approve_count': approve_count, 'pending_count': pending_count, 'reject_count': reject_count, 'page_obj': results, 'is_paginated': results.has_other_pages(),}
    return render(request, 'sub_admin_dashboard/sub_admin_dashboard.html', context)

# =============================================== End Sub-Admin Dashboard Views ================================================

# Logout Function
def user_logout(request):
    # Flush the session
    request.session.flush()
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


# -------------------------------------------------End User Registration and Login Views -------------------------------------------------

# ------------------------------------------------Start Super Admin Dashboard Views ------------------------------------------------------

# SuperAdmin User Role Assignment
@role_required(['SUPERADMIN', 'SUBADMIN'])
def superadmin_userRole(request):
    # Get approving person's mobile from session
    approving_mobile = request.session.get("mobile")
    if not approving_mobile:
        messages.error(request, "Session expired. Please login again.")
        return redirect('login')

    # Prepare dropdown mappings
    mappings = {
        'role_level': ['Prant', 'Vibhag', 'Jila', 'Nagar', 'Mandal', 'Basti', 'Upbasti'],
        'Prant': list(PrantMaster.objects.values_list("prant_hindi", flat=True)),
        'Vibhag': list(VibhagMaster.objects.values_list("vibhag_hindi", flat=True)),
        'Jila': list(ZilaMaster.objects.values_list("jila_hindi", flat=True)),
        'Nagar': list(NagarMaster.objects.values_list("nagar_hindi", flat=True)),
        'Mandal': list(MandalMaster.objects.values_list("mandal_hindi", flat=True)),
        'Basti': list(BastiMaster.objects.values_list("basti_hindi", flat=True)),
        'Upbasti': list(UpbastiMaster.objects.values_list("upbasti_hindi", flat=True))
    }

    # Get roles approved by current user
    admin_roles = Admin.objects.exclude(mobile=approving_mobile).order_by('-id')
    # Get scanner roles approved by current user
    scanner_roles = ScannerApprovals.objects.exclude(phone_number=approving_mobile).order_by('-scanner_id')

    # Search functionality
    user_info = None
    registration_info = None
    phone_number = request.GET.get('phone_number', '').strip()
    is_scanner = request.GET.get('is_scanner', False)

    if phone_number:
        try:
            registration_info = RegisterSamautkarshRegistration.objects.filter(phone_number=phone_number).first()
            
            if is_scanner:
                user_info = ScannerApprovals.objects.filter(phone_number=phone_number).first()
            else:
                user_info = registration_info
            
            if not registration_info:
                messages.warning(request, f"No registration found with phone number: {phone_number}")
            elif not user_info and is_scanner:
                messages.info(request, f"No scanner record found, will create new one")
        except Exception as e:
            messages.error(request, f"Search error: {str(e)}")

        # Role assignment
    if request.method == "POST":
        try:
            post_phone = request.POST.get('phone_number') or request.POST.get('mobile')

            # Check if user is trying to assign role to themselves
            if post_phone == approving_mobile:
                messages.error(request, "You cannot assign roles to yourself!")
                return redirect('core:superadmin_userRole')
            
            role_type = request.POST.get('role_type')
            
            if role_type == 'scanner':
                scanner_name = request.POST.get('scanner_name')
                
                obj, created = ScannerApprovals.objects.update_or_create(
                    phone_number=post_phone,
                    defaults={
                        'scanner_name': scanner_name,
                        'role': 'scanner',
                        'updated_at': timezone.now(),
                        'person_approving': approving_mobile
                    }
                )
                msg = 'Scanner created successfully.' if created else 'Scanner updated successfully.'
                
            else:
                # Create both admin and scanner roles
                name = request.POST.get('name')
                name = request.POST.get('scanner_name')
                role = request.POST.get('role')
                role_level = request.POST.get('role_level')
                role_sublevel = request.POST.get('role_sublevel')

                # print(f"POST data: {request.POST}")

                # Create/update admin role
                admin_obj, admin_created = Admin.objects.update_or_create(
                    mobile=post_phone,
                    defaults={
                        'name': name,
                        'role': role,
                        'role_level': role_level,
                        'role_sublevel': role_sublevel,
                        'person_approving': approving_mobile
                    }
                )
                # print(f"Creating admin role with: name={name}, role={role}, level={role_level}, sublevel={role_sublevel}")
                # Create corresponding scanner role
                scanner_obj, scanner_created = ScannerApprovals.objects.update_or_create(
                    phone_number=post_phone,
                    defaults={
                        'scanner_name': name,  # Use admin name as scanner name
                        'role': 'scanner',
                        'updated_at': timezone.now(),
                        'person_approving': approving_mobile,
                        'admin_role': role,  # Store admin role reference
                        'admin_level': role_level  # Store admin level
                    }
                )
                
                print(f"Creating scanner role with: name={name}, phone={post_phone}")
                msg = 'Admin and Scanner roles created successfully.' if admin_created else 'Admin and Scanner roles updated successfully.'
            
            messages.success(request, msg)
            return redirect('core:superadmin_dashboard')
            
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')

    context = {
        'user_info': user_info,
        'registration_info': registration_info,
        'searched_phone': phone_number,
        'is_scanner': is_scanner,
        'mappings': mappings,
        'admin_roles': admin_roles,
        'scanner_roles': scanner_roles,
        'approving_person': approving_mobile
    }
    return render(request, 'superadmin_dashboard/ekai_sidebar/superadmin_add_user.html', context)


# SUPERADMIN Delete views
@role_required(['SUPERADMIN', 'ADMIN'])
def delete_admin_role(request, role_id):
    # role = get_object_or_404(Admin, id=role_id, person_approving=request.session.get("mobile"))
    if request.method == "POST":
        role = get_object_or_404(Admin, id=role_id)
        role.delete()
        messages.success(request, "Admin role deleted successfully")
    return redirect('core:superadmin_userRole')

@role_required(['SUPERADMIN', 'ADMIN'])
def delete_scanner_role(request, scanner_id):
    # scanner = get_object_or_404(ScannerApprovals, scanner_id=scanner_id, person_approving=request.session.get("mobile"))
    if request.method == "POST":
        scanner = get_object_or_404(ScannerApprovals, scanner_id=scanner_id)
        scanner.delete()
        messages.success(request, "Scanner role deleted successfully")
    return redirect('core:superadmin_userRole')


@role_required(['SUPERADMIN', 'ADMIN', 'SUBADMIN'])
def subadmin_userRole(request):
    # Fetch all records from the database
    mappings={}
    raw_data=['Prant','Vibhag','Jila','Nagar','Mandal','Basti','Upbasti']
    mappings['role_level']=raw_data
    raw_data = list(PrantMaster.objects.values_list("prant_hindi", flat=True))
    mappings['Prant']=raw_data
    raw_data = list(VibhagMaster.objects.values_list("vibhag_hindi", flat=True))
    mappings['Vibhag']=raw_data
    raw_data = list(ZilaMaster.objects.values_list("jila_hindi", flat=True))
    mappings['Jila']=raw_data
    raw_data = list(NagarMaster.objects.values_list("nagar_hindi", flat=True))
    mappings['Nagar']=raw_data
    raw_data = list(MandalMaster.objects.values_list("mandal_hindi", flat=True))
    mappings['Mandal']=raw_data
    raw_data = list(BastiMaster.objects.values_list("basti_hindi", flat=True))
    mappings['Basti']=raw_data
    raw_data = list(UpbastiMaster.objects.values_list("upbasti_hindi", flat=True))
    mappings['Upbasti']=raw_data
    mobile = request.session.get('mobile')
    role_sublevel = Admin.objects.filter(mobile=mobile)
    role_sublevel = list(role_sublevel)
    role_sublevel=role_sublevel[0]
    mappings={}
    #mappings={}
    # Fetch all records from the database
    if role_sublevel.role_level == 'Vibhag':
        raw_data=['Jila','Nagar','Mandal','Basti','Upbasti']
        mappings['role_level']=raw_data
        raw_data = list(ZilaMaster.objects.select_related("vibhag_id").filter(vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("jila_hindi", flat=True))
        mappings['Jila']=raw_data
        # print(raw_data)
        # print(mappings['Jila'])
        raw_data = list(NagarMaster.objects.select_related("jila_id__vibhag_id").filter(jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("nagar_hindi", flat=True))
        mappings['Nagar']=raw_data
        raw_data = list(MandalMaster.objects.select_related("nagar_id__jila_id__vibhag_id").filter(nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("mandal_hindi", flat=True))
        mappings['Mandal']=raw_data
        raw_data = list(BastiMaster.objects.select_related("mandal_id__nagar_id__jila_id__vibhag_id").filter(mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("basti_hindi", flat=True))
        mappings['Basti']=raw_data
        raw_data = list(UpbastiMaster.objects.select_related("basti_id__mandal_id__nagar_id__jila_id__vibhag_id").filter(basti_id__mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("upbasti_hindi", flat=True))
        mappings['Upbasti']=raw_data
        #print("superadmin_userRole:", mappings)
       
    if role_sublevel.role_level == 'Prant':
        raw_data=['Vibhag','Jila','Nagar','Mandal','Basti','Upbasti']
        mappings['role_level']=raw_data
        raw_data = list(VibhagMaster.objects.select_related("prant_id").filter(prant_id__prant_hindi=role_sublevel.role_sublevel).values_list("vibhag_hindi", flat=True))
        mappings['Vibhag']=raw_data
        raw_data = list(ZilaMaster.objects.select_related("vibhag_id").filter(vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("jila_hindi", flat=True))
        mappings['Jila']=raw_data
        raw_data = list(NagarMaster.objects.select_related("jila_id__vibhag_id").filter(jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("nagar_hindi", flat=True))
        mappings['Nagar']=raw_data
        raw_data = list(MandalMaster.objects.select_related("nagar_id__jila_id__vibhag_id").filter(nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("mandal_hindi", flat=True))
        mappings['Mandal']=raw_data
        raw_data = list(BastiMaster.objects.select_related("mandal_id__nagar_id__jila_id__vibhag_id").filter(mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("basti_hindi", flat=True))
        mappings['Basti']=raw_data
        raw_data = list(UpbastiMaster.objects.select_related("basti_id__mandal_id__nagar_id__jila_id__vibhag_id").filter(basti_id__mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("upbasti_hindi", flat=True))
        mappings['Upbasti']=raw_data#print("superadmin_userRole:", mappings)
       
    if role_sublevel.role_level == 'Jila':
        raw_data=['Nagar','Mandal','Basti','Upbasti']
        mappings['role_level']=raw_data
        raw_data = list(NagarMaster.objects.select_related("jila_id__vibhag_id").filter(jila_id__jila_hindi=role_sublevel.role_sublevel).values_list("nagar_hindi", flat=True))
        #raw_data = list(NagarMaster.objects.select_related("jila_id__vibhag_id").filter(jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("nagar_hindi", flat=True))
        mappings['Nagar']=raw_data
        #raw_data = list(MandalMaster.objects.select_related("nagar_id__jila_id__vibhag_id").filter(nagar_id__jila_id__jila_name=role_sublevel.role_sublevel).values_list("mandal_hindi", flat=True))
        raw_data = list(MandalMaster.objects.filter(nagar_id__jila_id__jila_hindi=role_sublevel.role_sublevel).values_list('mandal_hindi', flat=True))
        mappings['Mandal']=raw_data
        raw_data =  list(BastiMaster.objects.filter(mandal_id__nagar_id__jila_id__jila_hindi=role_sublevel.role_sublevel).values_list('basti_hindi', flat=True))
        mappings['Basti']=raw_data
        raw_data =  list(UpbastiMaster.objects.filter(basti_id__mandal_id__nagar_id__jila_id__jila_hindi=role_sublevel.role_sublevel).values_list('upbasti_hindi', flat=True))
        mappings['Upbasti']=raw_data
        #print("superadmin_userRole:", mappings)
        
    if role_sublevel.role_level == 'Nagar':
        raw_data=['Mandal','Basti','Upbasti']
        mappings['role_level']=raw_data
        raw_data = list(MandalMaster.objects.select_related("nagar_id__jila_id__vibhag_id").filter(nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("mandal_hindi", flat=True))
        mappings['Mandal']=raw_data
        raw_data = list(BastiMaster.objects.select_related("mandal_id__nagar_id__jila_id__vibhag_id").filter(mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("basti_hindi", flat=True))
        mappings['Basti']=raw_data
        raw_data = list(UpbastiMaster.objects.select_related("basti_id__mandal_id__nagar_id__jila_id__vibhag_id").filter(basti_id__mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("upbasti_hindi", flat=True))
        mappings['Upbasti']=raw_data#print("superadmin_userRole:", mappings)
        
    if role_sublevel.role_level == 'Mandal':
        raw_data=['Basti','Upbasti']
        mappings['role_level']=raw_data
        mappings['Basti']=raw_data
        raw_data = list(UpbastiMaster.objects.select_related("basti_id__mandal_id__nagar_id__jila_id__vibhag_id").filter(basti_id__mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("upbasti_hindi", flat=True))
        mappings['Upbasti']=raw_data#print("superadmin_userRole:", mappings)
        #print("superadmin_userRole:", mappings)
        
    if role_sublevel.role_level == 'Basti':
        raw_data=['Upbasti']
        mappings['role_level']=raw_data
        raw_data = list(UpbastiMaster.objects.select_related("basti_id__mandal_id__nagar_id__jila_id__vibhag_id").filter(basti_id__mandal_id__nagar_id__jila_id__vibhag_id__vibhag_hindi=role_sublevel.role_sublevel).values_list("upbasti_hindi", flat=True))
        mappings['Upbasti']=raw_data#print("superadmin_userRole:", mappings)
        #print("superadmin_userRole:", mappings)
        
    if role_sublevel.role_level == 'Upbasti':
        raw_data=['']
        mappings['role_level']=raw_data
        raw_data = []
        mappings['Upbasti']=raw_data

 # Get approving person's mobile from session
    approving_mobile = request.session.get("mobile")
    if not approving_mobile:
        messages.error(request, "Session expired. Please login again.")
        return redirect('login')

    # Prepare dropdown mappings
    mapping = {
        'role_level': ['Prant', 'Vibhag', 'Jila', 'Nagar', 'Mandal', 'Basti', 'Upbasti'],
        'Prant': list(PrantMaster.objects.values_list("prant_hindi", flat=True)),
        'Vibhag': list(VibhagMaster.objects.values_list("vibhag_hindi", flat=True)),
        'Jila': list(ZilaMaster.objects.values_list("jila_hindi", flat=True)),
        'Nagar': list(NagarMaster.objects.values_list("nagar_hindi", flat=True)),
        'Mandal': list(MandalMaster.objects.values_list("mandal_hindi", flat=True)),
        'Basti': list(BastiMaster.objects.values_list("basti_hindi", flat=True)),
        'Upbasti': list(UpbastiMaster.objects.values_list("upbasti_hindi", flat=True))
    }

    # Get roles approved by current user
    admin_roles = Admin.objects.filter(person_approving=approving_mobile).order_by('-id')
    scanner_roles = ScannerApprovals.objects.filter(person_approving=approving_mobile).order_by('-updated_at')

    # Search functionality
    user_info = None
    registration_info = None
    phone_number = request.GET.get('phone_number', '').strip()
    is_scanner = request.GET.get('is_scanner', False)

    if phone_number:
        try:
            registration_info = RegisterSamautkarshRegistration.objects.filter(
                phone_number=phone_number
            ).first()
            
            if is_scanner:
                user_info = ScannerApprovals.objects.filter(
                    phone_number=phone_number
                ).first()
            else:
                user_info = registration_info
            
            if not registration_info:
                messages.warning(request, f"No registration found with phone number: {phone_number}")
            elif not user_info and is_scanner:
                messages.info(request, f"No scanner record found, will create new one")
        except Exception as e:
            messages.error(request, f"Search error: {str(e)}")

    # Role assignment
    if request.method == "POST":
        try:
            post_phone = request.POST.get('phone_number') or request.POST.get('mobile')
            role_type = request.POST.get('role_type')
            
            if role_type == 'scanner':
                scanner_name = request.POST.get('scanner_name')
                
                obj, created = ScannerApprovals.objects.update_or_create(
                    phone_number=post_phone,
                    defaults={
                        'scanner_name': scanner_name,
                        'role': 'scanner',
                        'updated_at': timezone.now(),
                        'person_approving': approving_mobile
                    }
                )
                msg = 'Scanner created successfully.' if created else 'Scanner updated successfully.'
                
            else:
                role = request.POST.get('role')
                role_level = request.POST.get('role_level')
                role_sublevel = request.POST.get('role_sublevel')

                obj, created = Admin.objects.update_or_create(
                    mobile=post_phone,
                    defaults={
                        'role': role,
                        'role_level': role_level,
                        'role_sublevel': role_sublevel,
                        'person_approving': approving_mobile
                    }
                )
                msg = 'Admin role created successfully.' if created else 'Admin role updated successfully.'
            
            messages.success(request, msg)
            return redirect('core:subadmin_userRole')
            
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')

    context = {
        'user_info': user_info,
        'registration_info': registration_info,
        'searched_phone': phone_number,
        'is_scanner': is_scanner,
        'mapping': mapping,
        'admin_roles': admin_roles,
        'scanner_roles': scanner_roles,
        'approving_person': approving_mobile,
        "mappings":mappings
    }


    return render(request, 'sub_admin_dashboard/subadmin_add_user.html', context)



# SubADMIN Delete views
@role_required(['SUBADMIN', 'ADMIN'])
def delete_subadmin_role(request, role_id):
    role = get_object_or_404(Admin, id=role_id, person_approving=request.session.get("mobile"))
    if request.method == "POST":
        role.delete()
        messages.success(request, "Admin role deleted successfully")
    return redirect('core:subadmin_userRole')

@role_required(['SUBADMIN', 'ADMIN'])
def delete_subscanner_role(request, scanner_id):
    scanner = get_object_or_404(ScannerApprovals, scanner_id=scanner_id, person_approving=request.session.get("mobile"))
    if request.method == "POST":
        scanner.delete()
        messages.success(request, "Scanner role deleted successfully")
    return redirect('core:subadmin_userRole')

# -------------------------------------------------Start Permission Denied View -------------------------------------------------
# Permission Denied View (for unauthorized access)
def permission_denied_view(request):
    return render(request, '403.html')

# -------------------------------------------------End Permission Denied View -------------------------------------------------
@role_required(['ADMIN', 'SUPERADMIN'])
def admin(request):
    # Fetch all records from the database  
    # total_count = BarcodeScan.objects.count()
    # approve_count = BarcodeScan.objects.filter(status='Approve').count()
    # pending_count = BarcodeScan.objects.filter(status='pending').count()
    # reject_count = BarcodeScan.objects.filter(status='Reject').count() 

    sql_query = """
    SELECT register_id,register_samautkarsh_registration.name,register_samautkarsh_registration.phone_number,gender,prant_hindi,vibhag_hindi,jila_hindi,register_samautkarsh_registration.nagar,register_samautkarsh_registration.dayitv,status,register_samautkarsh_registration.ekai,referral_code,user_type,vividhsangathan FROM register_samautkarsh_registration INNER JOIN nagar_master ON register_samautkarsh_registration.nagar = nagar_master.nagar_hindi INNER JOIN zila_master ON nagar_master.jila_id = zila_master.jila_id INNER JOIN vibhag_master ON zila_master.vibhag_id = vibhag_master.vibhag_id INNER JOIN prant_master ON vibhag_master.prant_id = prant_master.prant_id inner join barcode_scan on register_samautkarsh_registration.phone_number=barcode_scan.phone_number ORDER BY FIELD(status, 'pending', 'Approve', 'Reject');
    """

    with connection.cursor() as cursor:
        cursor.execute(sql_query)  # Pass the parameter safely using parameterized query
        results = cursor.fetchall()

    # Status counts (can be outside pagination)
    total_count = len(results)
    pending_count = len([r for r in results if str(r[9]).lower() == 'pending'])
    approve_count = len([r for r in results if 'Approve' in r])
    reject_count = len([r for r in results if 'Reject' in r])

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(results, 10)  # Show 10 records per page

    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    # print(results)
    mappings={}

    referral_code = RegisterSamautkarshRegistration.objects.values_list('referral_code', flat=True).distinct()
    mappings['referral_code'] = list(referral_code)
    raw_data = DayitvMaster.objects.select_related("ekai_id").values_list("dayitv_name", "ekai_id__ekai_name")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
        #print(result)
        #print(category)
    result['Nagar'] = result.pop('nagar')
    result['Prant'] = result.pop('prant')
    result['Vibhag'] = result.pop('vibhag')
    result['Jila'] = result.pop('jila')

    mappings['dayitvaMapping'] = result

    #jilaToNagar extraction
    raw_data = NagarMaster.objects.select_related("jila_id").values_list("nagar_hindi", "jila_id__jila_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['jilaToNagar'] = result

    #VibhagToJila extraction
    raw_data = ZilaMaster.objects.select_related("vibhag_id").values_list("jila_hindi", "vibhag_id__vibhag_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['vibhagToJila'] = result

    #prantToVibhag extraction
    raw_data = VibhagMaster.objects.select_related("prant_id").values_list("vibhag_hindi", "prant_id__prant_hindi")
    result = {}
    # Iterate over the data to group by categories
    for item, category in raw_data:
        category = category.lower()  # Convert category to lowercase
        if category not in result:
            result[category] = []  # Initialize a list for the category if it doesn't exist
        result[category].append(item)  # Append the item to the appropriate category list
    mappings['prantToVibhag'] = result
    role_defined=request.session.get("role_level")
    role_sublevel=request.session.get('role_sublevel')

    if request.method == "POST":
        # Handle POST request (update status)
        register_id = request.POST.get('register_id')  # Get the ID of the record to update
        new_status = request.POST.get('status')  # Get the new status (अनिर्णीत, स्वीकृत, अस्वीकार)
   
        # Find the corresponding BarcodeScan record
        register_scan = RegisterSamautkarshRegistration.objects.get(register_id=register_id)
        # print(register_scan)
        mobile = register_scan.phone_number
        barcode_scan = BarcodeScan.objects.get(phone_number = mobile)
        # print(barcode_scan)

        # Update the status
        barcode_scan.status = new_status
        barcode_scan.Approving_person=request.session["mobile"]
        image_path = barcode_scan.qrcode
        barcode_scan.save()
        if new_status=='Approve':
            url = "http://sms.messageindia.in/v2/sendSMS"
                    # API parameters
            params = {
                        "username": "utkarshbharatresearch",  # Your API username
                        "message": f"Namaste ji, Your Reg. has been completed. Get the QR Code from https://samutkarsh.in/ Team Samurkarsh Bharat",  # Message content
                        "sendername": "SBRPLW",  # Sender name (approved by provider)
                        "smstype": "TRANS",  # Transactional or promotional
                        "numbers": mobile,  # Mobile numbers (comma-separated)
                        "apikey": "9fcec71f-f3ee-4b7c-8099-ee8cbc06478b",  # Your API key
                        "peid": "1701173858154413324",  # PE ID from provider
                        "templateid": "1707173883044603731"  # Template ID from provider
                    }

                    # Sending the GET request
            response = requests.get(url, params=params)
            url = "http://148.251.129.118/wapp/api/send"

            # API key and message details
            params = {
                "apikey": "747f01ec1e574d74bb6f557c6d304692",  # Your API key
                "mobile": mobile,  # Comma-separated mobile numbers
                "msg": "❍❍❍❖❖ केशवकुंज दर्शन ❖❖❍❍❍\n\n'⊰᯽⊱┈─╌❊ ⚜️ ❊╌─┈⊰᯽⊱'\n\nआपका नाम कार्यक्रम हेतु पंजीकृत हुआ है। केशवकुंज दर्शन हेतु आप सादर आमंत्रित हैं।\n\nसुरक्षा कारणों से आपकी सुविधा हेतु कार्यक्रम में प्रवेश अनुमति हेतु QR कोड संलग्न है।\n\nकृपया ध्यान दें ..!! \n\n👉 आपके जिले/विभाग के लिए जो दिन निश्चित हुआ है, उसी दिन आपका आना अपेक्षित है।\n\n👉 प्रवेश द्वार पर QR Code दिखाना आवश्यक है।\n\n👉कृपया अपना पहचान पत्र अपने साथ अवश्य लाएं\n\nविशेष :- कार्यक्रम स्थल पर सुविधा पूर्वक पहुंचने के लिए कृपया Metro का प्रयोग कर झंडेवालान मेट्रो स्टेशन पर उतरें।\n\nनिवेदक\n\nश्री केशव स्मारक समिति, दिल्ली", "img1": "https://samutkarsh.in/static/QRCodes/{}.jpg".format(mobile)
            }
            # Sending the GET request
            response = requests.get(url, params=params)
        else:
            pass
        # Return a JSON response for success
        return JsonResponse({'success': True, 'message': 'Status updated successfully.'})
    
    return render(request, 'admin.html',{"mappings":mappings,'registrations':results,'role_defined':role_defined,'role_sublevel':role_sublevel, 'total_count': total_count, 'approve_count': approve_count, 'pending_count': pending_count, 'reject_count': reject_count, 'page_obj': results, 'is_paginated': results.has_other_pages(),})
