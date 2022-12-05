from scipy.stats import norm

if __name__ == "__main__":

    OD = 8  # optimistisch
    HD = 13  # mittel
    PD = 15  # pessimistisch

    verteilung = "beta"  # "gleich" oder "beta" oder "dreieck"

    if verteilung == "beta":
        MD = (OD + 4 * HD + PD) / 6
        VD = pow((PD - OD), 2) / 36

    elif verteilung == "gleich":
        MD = (OD + PD) / 2
        VD = pow((PD - OD), 2) / 12

    elif verteilung == "dreieck":
        MD = (OD + HD + PD) / 3
        VD = (pow(OD, 2) + pow(HD, 2) + pow(PD, 2) - OD * HD - OD * PD - HD * PD) / 18

    print(f"MD={MD}, VD={VD}")

    ############################################################################################

    norm.ppf(0.95)  # 95% Quantil der Standardnormalverteilung

    # wie hoch ist die Wahrscheinlichkeit, dass das Projekt höchstens 100 Tage dauert?
    print(norm.cdf( (100 - 98.17) / 3 ))  # ( 100 Tage - MT ) / sqrt(VT)
    # nach wie vielen Tagen ist das Projekt mit einer Wahrscheinlichkeit von 95 % beendet?
    print( norm.ppf(0.95) * 3 + 98.17 )  # 95% Quantil * sqrt(VT) + MT