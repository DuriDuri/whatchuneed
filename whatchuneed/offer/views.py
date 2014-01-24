from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import OfferForm
from django.http import HttpResponseRedirect
from twilio.rest import TwilioRestClient

account_sid = "AC5a3b3bd42351ca3b43bc281baf7a4f2d"
auth_token  = "747cba37eb310c39e44ea248e59d6eee"
client = TwilioRestClient(account_sid, auth_token)


def home(request):
    offer_form  = OfferForm(request.POST or None)
    if offer_form.is_valid():
        new_offer = offer_form.save(commit = False)
        new_offer.save()
        send = client.messages.create(to="+13013852733",  from_="+16015742587" , body= '\n Name: ' + new_offer.name
                                          + '\n @ '+ str(new_offer.phone)
                                          + '\n Wants: ' + str(new_offer.deliver_what)
                                          + '\n At: '+ str(new_offer.deliver_where)
                                          + '\n Offering: '+ str(new_offer.offer_for_delivery)
                                          + '\n Time Limit: '+ str(new_offer.length_of_offer))
        return HttpResponseRedirect('')

    return render_to_response('form.html', locals(), context_instance=RequestContext(request))

        
