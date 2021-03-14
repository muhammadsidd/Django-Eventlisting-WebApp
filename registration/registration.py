from decimal import Decimal
from ngo.settings import SESSION_ID_REGISTRATION
from event.models import Event


class Registration(object):
    def __init__(self, request):
        self.session = request.session
        if not self.session.get(SESSION_ID_REGISTRATION):
            self.session[SESSION_ID_REGISTRATION] = {}
        self.session_registration_obj = self.session[SESSION_ID_REGISTRATION]

    def addnewAdult(self, event):
        event_id = str(event.id)
        if event_id not in self.session_registration_obj:
            self.session_registration_obj[str(event_id)] = {'quantity_Adult': 0, 'price_Adult': str(event.adult_price)}
        self.session_registration_obj[str(event_id)]['quantity_Adult'] += 1
        self.session[SESSION_ID_REGISTRATION] = self.session_registration_obj
        self.session.modified = True

    def addnewChild(self, event):
        event_id = str(event.id)
        if event_id not in self.session_registration_obj:
            self.session_registration_obj[str(event_id)] = {'quantity_Child': 0, 'price_Child': str(event.child_price)}
        self.session_registration_obj[str(event_id)]['quantity_Child'] += 1
        self.session[SESSION_ID_REGISTRATION] = self.session_registration_obj
        self.session.modified = True

    def removeAdult(self, event_id):
        if str(event_id) in self.session_registration_obj:
            self.session_registration_obj[str(event_id)]['quantity_Adult'] -= 1
            if self.session_registration_obj[str(event_id)]['quantity_Adult'] <= 0:
                del self.session_registration_obj[str(event_id)]
        self.session[SESSION_ID_REGISTRATION] = self.session_registration_obj
        self.session.modified = True

    def removeChild(self, event_id):
        if str(event_id) in self.session_registration_obj:
            self.session_registration_obj[str(event_id)]['quantity_Child'] -= 1
            if self.session_registration_obj[str(event_id)]['quantity_Child'] <= 0:
                del self.session_registration_obj[str(event_id)]
        self.session[SESSION_ID_REGISTRATION] = self.session_registration_obj
        self.session.modified = True

    def __iter__(self):
        event_ids = self.session_registration_obj.keys()
        events = Event.objects.filter(id__in=event_ids)
        for event in events:
            self.session_registration_obj[str(event.id)]['event'] = event
        for item in self.session_registration_obj.values():
            item['price_Adult'] = item['price_Adult']
            item['price_Child'] = item['price_Child']
            item['total_price'] = (Decimal(item['price_Adult']) * Decimal(item['quantity_Adult'])) + \
                                  (Decimal(item['price_Child']) * Decimal(item['quantity_Child']))
            yield item

    def clearSession(self):
        self.session_registration_obj = self.session[SESSION_ID_REGISTRATION] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(( (Decimal(item['price_Adult']) * Decimal(item['quantity_Adult'])) +
                     (Decimal(item['price_Child']) * Decimal(item['quantity_Child'])))
                   for item in self.session_registration_obj.values())

    def __len__(self):
        return sum(item['quantity_Adult'] + item['quantity_Child'] for item in self.session_registration_obj.values())


