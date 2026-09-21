def fertilizer_advice(n, p, k):

    if n < 50:
        return "Nitrogen-rich fertilizer (Urea)"

    elif p < 40:
        return "Phosphorus-rich fertilizer (DAP)"

    elif k < 40:
        return "Potassium-rich fertilizer (MOP)"

    elif n < 50:
        return "Zinc fertilizer (zinc sulfate)"

    else:
        return "No additional fertilizer required"