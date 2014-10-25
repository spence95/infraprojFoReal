from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from homepage import models as hmod
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django import forms

# Create your views here.
def index(request):

    context = { 'wilson': 'awesome' }
    return render(request, 'homepage/index.html', context)
    
def assets(request):
    
    context = { 'assets': hmod.Asset.objects.all().order_by('UID') }
    return render(request, 'homepage/assets.html', context)
    
def delete_asset(request, UIDP):
    
    f = hmod.Asset.objects.get(UID=UIDP)
    f.delete()
    return HttpResponseRedirect('/homepage/assets/')
    
def delete_location(request, UIDP):

    f = hmod.Location.objects.get(UID=UIDP)
    f.delete()
    return HttpResponseRedirect('/homepage/locations/')
    
def delete_manufacturer(request, UIDP):
    
    f = hmod.Manufacturer.objects.get(UID=UIDP)
    f.delete()
    return HttpResponseRedirect('/homepage/manufacturers/')
    
@csrf_exempt     
def edit_asset(request, UIDP):
    
    f = hmod.Asset.objects.get(UID=UIDP)

    form = AssetForm(initial={
        'UID': f.UID,
        'organizationalTag': f.organizationalTag,
        'manufacturerPartNumber': f.manufacturerPartNumber,
        'description': f.description,
        'maintenanceNotes': f.maintenanceNotes,
        'location': f.currentAssignedLocation.UID,
        'manufacturer': f.manufacturer.UID,
    })
    
    
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            
            f.currentlyActive = 'Yes'
            f.UID = form.cleaned_data['UID']
            f.organizationalTag = form.cleaned_data['organizationalTag']
            f.manufacturerPartNumber = form.cleaned_data['manufacturerPartNumber']
            f.description = form.cleaned_data['description']
            f.maintenanceNotes = form.cleaned_data['maintenanceNotes']
            
            loc = form.cleaned_data['location']
            location = hmod.Location.objects.get(UID=loc) 
            f.currentAssignedLocation = location
            
            man = form.cleaned_data['manufacturer']
            manufacturer = hmod.Manufacturer.objects.get(UID=man) 
            f.manufacturer = manufacturer

            f.save()
            
            
            return HttpResponseRedirect('/homepage/assets/')
    
    
    context = { 'form': form, } 
    
    return render(request, 'homepage/edit_asset.html', context )
    

@csrf_exempt    
def edit_location(request, UIDP):

    f = hmod.Location.objects.get(UID=UIDP)

    form = LocationForm(initial={
        'UID': f.UID,
        'name': f.name,
        'address': f.address,
        'phone': f.phone,
    })
       

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
                      
            f.UID = form.cleaned_data['UID']
            f.name = form.cleaned_data['name']
            f.address = form.cleaned_data['address']
            f.phone = form.cleaned_data['phone']
            
            f.save()
            return HttpResponseRedirect('/homepage/locations/')
    
    context = { 'form': form, } 
    
    return render(request, 'homepage/edit_location.html', context )
    
    
@csrf_exempt     
def edit_manufacturer(request, UIDP):
    
    f = hmod.Manufacturer.objects.get(UID=UIDP)

    form = ManufacturerForm(initial={
        'UID': f.UID,
        'name': f.name,
        'address': f.address,
        'phone': f.phone,
    })
    
    

    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
                      
            f.UID = form.cleaned_data['UID']
            f.name = form.cleaned_data['name']
            f.address = form.cleaned_data['address']
            f.phone = form.cleaned_data['phone']
            
            f.save()
            return HttpResponseRedirect('/homepage/manufacturers/')
    
    context = { 'form': form, } 
    
    return render(request, 'homepage/edit_manufacturer.html', context )
    
    
def locations(request):

    context = { 'locations': hmod.Location.objects.all().order_by('UID') }
    return render(request, 'homepage/locations.html', context)
    
def manufacturers(request):
            
    context = { 'manufacturers': hmod.Manufacturer.objects.all().order_by('UID') }
    return render(request, 'homepage/manufacturers.html', context)

@csrf_exempt     
def new_asset(request):
    
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            
            f = hmod.Asset()
            f.currentlyActive = 'Yes'
            f.UID = form.cleaned_data['UID']
            f.organizationalTag = form.cleaned_data['organizationalTag']
            f.manufacturerPartNumber = form.cleaned_data['manufacturerPartNumber']
            f.description = form.cleaned_data['description']
            f.maintenanceNotes = form.cleaned_data['maintenanceNotes']
            
            loc = form.cleaned_data['location']
            location = hmod.Location.objects.get(UID=loc) 
            f.currentAssignedLocation = location
            
            man = form.cleaned_data['manufacturer']
            manufacturer = hmod.Manufacturer.objects.get(UID=man) 
            f.manufacturer = manufacturer

            f.save()
            
            
            return HttpResponseRedirect('/homepage/assets/')
    
    form = AssetForm()
    
    context = { 'form': form, } 
    
    return render(request, 'homepage/new_asset.html', context )
    
    
@csrf_exempt    
def new_location(request):
    
    
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            
            f = hmod.Location()
            f.currentlyActive = 'Yes'
            f.UID = form.cleaned_data['UID']
            f.name = form.cleaned_data['name']
            f.address = form.cleaned_data['address']
            f.phone = form.cleaned_data['phone']

            f.save()          
            
            return HttpResponseRedirect('/homepage/locations/')
    
    form = LocationForm()

    
    context = { 'form': form, } 
    
    return render(request, 'homepage/new_location.html', context )
    
    
@csrf_exempt   
def new_manufacturer(request):
    
    if request.method == 'POST':
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            
            f = hmod.Manufacturer()
            f.currentlyActive = 'Yes'
            f.UID = form.cleaned_data['UID']
            f.name = form.cleaned_data['name']
            f.address = form.cleaned_data['address']
            f.phone = form.cleaned_data['phone']

            f.save()          
            
            return HttpResponseRedirect('/homepage/manufacturers/')
    
    form = ManufacturerForm()

    
    context = { 'form': form, } 
    
    return render(request, 'homepage/new_manufacturer.html', context )
    


def getLocations():
    l = hmod.Location.objects.all()
    locationChoices = []
    count = 1
    tup1 = ()
    listy = list()
    for loc in l:
        tup1 = (loc.UID, str(str(loc.UID) + " " + str(loc.name)))
        listy.append(tup1)
        count += 1
    locationChoices = listy
    return locationChoices
    
def getManufacturers():
    m = hmod.Manufacturer.objects.all()
    manufacturerChoices = []
    count = 1
    tup1 = ()
    listy = list()
    for man in m:
        tup1 = (man.UID, str(str(man.UID) + " " + str(man.name)))
        listy.append(tup1)
        count += 1
    manufacturerChoices = listy
    return manufacturerChoices

class AssetForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(AssetForm, self).__init__(*args, **kwargs)
        self.fields['location'] = forms.ChoiceField(choices=getLocations(), required=True, label="Current Assigned Location",)
        self.fields['manufacturer'] = forms.ChoiceField(choices=getManufacturers(), required=True, label="Manufacturer",)
    
    UID = forms.CharField(required=True, label="Asset ID", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    organizationalTag = forms.CharField(required=True, label="Organizational Tag", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    manufacturerPartNumber = forms.CharField(required=True, label="Manufacturer Part Number", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    description = forms.CharField(required=True, label="Description", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    maintenanceNotes = forms.CharField(required=True, label="Maintenance Notes", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))

    
    
class LocationForm(forms.Form):
    
    UID = forms.CharField(required=True, label="Store ID", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    name = forms.CharField(required=True, label="Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    address = forms.CharField(required=True, label="Address", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    phone = forms.CharField(required=True, label="Phone", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    
class ManufacturerForm(forms.Form):
    
    UID = forms.CharField(required=True, label="Manufacturer ID", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    name = forms.CharField(required=True, label="Name", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    address = forms.CharField(required=True, label="Address", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    phone = forms.CharField(required=True, label="Phone", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '',}))
    