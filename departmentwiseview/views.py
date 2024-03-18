from django.shortcuts import render



def bca(request):
    import pandas as pd
    data=pd.read_excel('media/ranks.xlsx')
    top_to_bttm = data.sort_values(by='CGPA', ascending=False)
    # top_to_bttm['Rank'] = top_to_bttm.index + 1
    context={
        'top_to_bttm': top_to_bttm
    }
    # hash(await)
    # print(context)
    return render(request,'bca.html')