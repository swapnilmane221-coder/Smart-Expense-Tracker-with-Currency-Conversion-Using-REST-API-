from rest_framework.decorators import api_view
from rest_framework.response import Response

# Fixed exchange rates (all relative to 1 INR)
EXCHANGE_RATES = {
    "INR": 1,          # Base currency
    "USD": 0.012,      # US Dollar
    "EUR": 0.011,      # Euro
    "GBP": 0.0095,     # British Pound
    "JPY": 1.77,       # Japanese Yen
    "AUD": 0.018,      # Australian Dollar
    "CAD": 0.016,      # Canadian Dollar
    "CHF": 0.011,      # Swiss Franc
    "CNY": 0.088,      # Chinese Yuan
    "BRL": 0.066,      # Brazilian Real
    "RUB": 1.10,       # Russian Ruble
    "ZAR": 0.22,       # South African Rand
    "KRW": 16.0,       # South Korean Won
    "SGD": 0.016,      # Singapore Dollar
    "HKD": 0.093,      # Hong Kong Dollar
    "MXN": 0.20,       # Mexican Peso
    "NZD": 0.019,      # New Zealand Dollar
    "SEK": 0.13,       # Swedish Krona
    "NOK": 0.13,       # Norwegian Krone
    "DKK": 0.083,      # Danish Krone
    "PLN": 0.049,      # Polish Zloty
    "TRY": 0.35,       # Turkish Lira
    "THB": 0.42,       # Thai Baht
    "IDR": 184.0,      # Indonesian Rupiah
    "MYR": 0.057,      # Malaysian Ringgit
    "PHP": 0.67,       # Philippine Peso
    "VND": 293.0,      # Vietnamese Dong
    "AED": 0.044,      # UAE Dirham
    "SAR": 0.045,      # Saudi Riyal
    "EGP": 0.58,       # Egyptian Pound
    "NGN": 18.0,       # Nigerian Naira
    "PKR": 3.3,        # Pakistani Rupee
    "BDT": 1.3,        # Bangladeshi Taka
    "ILS": 0.044       # Israeli Shekel
}

@api_view(['GET'])
def convert_currency(request):
    """
    API Example: /api/convert/?amount=10&from=USD&to=EUR
    """
    try:
        amount = float(request.GET.get("amount", 0))
        from_currency = request.GET.get("from", "INR").upper()
        to_currency = request.GET.get("to", "USD").upper()

        # Validate currencies
        if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES:
            return Response({"error": "Invalid currency code"}, status=400)

        # Convert: source → INR → target
        in_inr = amount / EXCHANGE_RATES[from_currency]
        converted = in_inr * EXCHANGE_RATES[to_currency]

        return Response({
            "amount": amount,
            "from": from_currency,
            "to": to_currency,
            "converted_amount": round(converted, 2)
        })

    except Exception as e:
        return Response({"error": str(e)}, status=400)
