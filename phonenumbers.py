# phone_info.py
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def phone_metadata(number_str, lang="en"):
    # number_str example: "9774126761" or "9815552671"
    try:
        pn = phonenumbers.parse(number_str, None)
    except phonenumbers.NumberParseException as e:
        return {"error": str(e)}

    valid = phonenumbers.is_valid_number(pn)
    region = phonenumbers.region_code_for_number(pn)
    description = geocoder.description_for_number(pn, lang) 
    carrier_name = carrier.name_for_number(pn, lang)         
    tz = timezone.time_zones_for_number(pn)                 

    return {
        "valid": valid,
        "region_code": region,
        "description": description,
        "carrier": carrier_name,
        "timezones": tz
    }

if __name__ == "__main__":
    number = input("Enter phone number (with country code, e.g. +1...): ").strip()
    info = phone_metadata(number)
    print(info)
