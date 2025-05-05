from googlesearch.googlesearch import GoogleSearch as gs


def get_res(query=None , dt_from = None, dt_to= None):
    res = gs().search("Rare metal supply chain news")
    for i, result in enumerate(res.results):
        print(i, "; ", "Title : ", result.title, "Length: ", len(result.getText()))
        

get_res()
