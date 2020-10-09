from SimpleCovidAPI import sca

def data_return():
    return sca.cases(), sca.deaths()
