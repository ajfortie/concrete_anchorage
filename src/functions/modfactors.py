"""This module will return concrete anchorage modification
factors based on anchorage input."""

#Concrete Breakout Cracking Factor per ACI318-19 §17.6.2.5.1
def psi_c_n(condition,anc_type,kc=17):

    if (condition == "Uncracked" and anc_type == "CIP"):
        psi = 1.25
    elif (condition == "Uncracked" and anc_type != "CIP"):
        if kc == 17:
            psi = 1.4
        else:
            psi = 1.0
    else:
        psi = 1.0
    
    return psi

#Concrete Breakout Edge Effect Factor per ACI 319-19 §17.6.2.4.1
def psi_ed_n(ca1,heff):
    if ca1 >= 1.5*heff:
        psi = 1.0
    else:
        psi = 0.7+0.3*(ca1/(1.5*heff))
    
    return psi

#Concrete Breakout Splitting Factor per ACI318-19 §17.6.2.6.1
