from django.urls import path

from departmentwiseview import views
urlpatterns = [
    path('OVERALL',views.OVERALL,name='OVERALL'),
    path('BCAIT/'  ,views.BCAIT    ,name='BCAIT'),
    path('BSC(PHY)/',views.BSC_PHY,name='BSC(PHY)'),
    path('BSC(CHE)/',views.BSC_CHE,name='BSC(CHE)'),
    path('BSC(MAT)/',views.BSC_MAT,name='BSC(MAT)'),
    path('BSC(BOT)/',views.BSC_BOT,name='BSC(BOT)'),
    path('BSC(ZOO)/',views.BSC_ZOO,name='BSC(ZOO)'),
]