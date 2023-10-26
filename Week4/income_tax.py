def reverse_income_tax(tax):
    assert(isinstance(tax,float)or isinstance(tax,int)),"Error in input please enter an float or int"
    results = 12500
    if tax > 0:
        if tax>37500*0.2:
            results+=37500
            tax-=37500*0.2
            if tax>100000*0.4:
                results+=100000
                tax-=100000*0.4
                if tax>0:
                    results+=tax/0.45
            else:
                results+=tax/0.4
        else:
            results+=tax/0.2
    return results
print(reverse_income_tax(35000))
