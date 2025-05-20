import phonenumbers # type: ignore
from test import number

from phonenumbers import geocoder # type: ignore
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en")) # type: ignore

from phonenumbers import carrier # type: ignore
service_number = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(sevice_number,"en")) # type: ignore