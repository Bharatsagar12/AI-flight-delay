def get_compensation(delay_hours, passenger_type):

    response={"services":[]}

    if delay_hours < 1:
        pass

    elif delay_hours <3:
        response["services"].append("Food Coupon")

    elif delay_hours <6:
        response["services"].extend(
            ["Food Coupon","Lounge Access"]
        )

    else:
        response["services"].extend(
            ["Food Coupon","Lounge Access","Hotel Stay"]
        )

    if passenger_type=="business":
        response["services"].append(
            "Priority Support"
        )

    return response