def get_compensation(delay_hours, passenger_type):

    services=[]

    if delay_hours >=3:
        services.append("Food Coupon")

    if delay_hours >=5:
        services.append("Lounge Access")

    if delay_hours >=6:
        services.append("Hotel Stay")

    if passenger_type=="business":
        services.append("Priority Support")

    return {"services":services}