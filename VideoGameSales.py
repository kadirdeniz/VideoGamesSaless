"""
Created on Mon Mar 30 21:53:02 2020

@author: deniz
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

veriler = pd.read_csv('vgsales.csv')
veriler=veriler.dropna()
veriler=veriler.drop(columns=['Rank','Platform'])
nintendo=veriler[veriler['Publisher']=='Nintendo']
nintendo=nintendo.drop(columns=['Publisher'])
ninna=nintendo['NA_Sales']
ninna=ninna.sum()
nineu=nintendo['EU_Sales']
nineu=nineu.sum()
ninoth=nintendo['Other_Sales']
ninoth=ninoth.sum()
ninjp=nintendo['JP_Sales']
ninjp=ninjp.sum()
ningl=nintendo['Global_Sales']
ningl=ningl.sum()
ninsales=[ninna,nineu,ninjp,ninoth]
labels=['NA_Sales','EU_Sales','JP_Sales','Other_Sales']
explode=(0.1,0,0,0)
ax=plt.subplot()
ax.pie(ninsales,labels=labels,explode=explode, autopct='%1.1f%%',shadow=True, startangle=90)
plt.title('Nintendo Markasının Dünya Üzerindeki Pazar Payları')
plt.show()
ninnotendo=veriler[veriler['Publisher']!='Nintendo']
activision=veriler[veriler['Publisher']=='Activision']
activision=activision[activision['Year']>2010]

actshooter=activision[activision['Genre']=='Shooter']
actshooterna=actshooter['NA_Sales'].sum()
actshootereu=actshooter['EU_Sales'].sum()
actshooterjp=actshooter['JP_Sales'].sum()
actshootergl=actshooter['Global_Sales'].sum()


actaction=activision[activision['Genre']=='Action']
actactionna=actaction['NA_Sales'].sum()
actactioneu=actaction['EU_Sales'].sum()
actactionjp=actaction['JP_Sales'].sum()
actactiongl=actaction['Global_Sales'].sum()


actmisc=activision[activision['Genre']=='Misc']
actmiscna=actmisc['NA_Sales'].sum()
actmisceu=actmisc['EU_Sales'].sum()
actmiscjp=actmisc['JP_Sales'].sum()
actmiscgl=actmisc['Global_Sales'].sum()

actrole=activision[activision['Genre']=='Role-Playing']
actrolena=actrole['NA_Sales'].sum()
actroleeu=actrole['EU_Sales'].sum()
actrolejp=actrole['JP_Sales'].sum()
actrolegl=actrole['Global_Sales'].sum()

jplist=[actshooterjp,actactionjp,actmiscjp,actrolejp]
eulist=[actshootereu,actactioneu,actmisceu,actroleeu]
gllist=[actshootergl,actactiongl,actmiscgl,actrolegl]
nalist=[actshooterna,actactionna,actmiscna,actrolena]
ax2=plt.subplot()
width=0.20
x = np.arange(len(nalist))
ax2.bar(x-width*3/2, nalist, width, label='Shooter')
ax2.bar(x-width/2, eulist, width, label='Action')
ax2.bar(x+width/2, jplist, width, label='Mist')
ax2.bar(x+3*width/2, gllist, width, label='Role Play')
labels=['','','Shooting','','Action','','Misc','','Role Play']
plt.legend(['NA_Sales','EU_Sales','JP_Sales','Gl_Sales'])
ax2.set_xticklabels(labels)
plt.title('Verilere Göre En Çok Satılan Oyun Tipleri Ve Satıldığı Bölgeler')
plt.xlabel('Oyun Tipleri')
plt.show()
#Activision Oyun Sayısı
shootersayı=activision[activision['Genre']=='Shooter']
shootersayı=shootersayı['Genre'].count()
advsayı=activision[activision['Genre']=='Adventure']
advsayı=advsayı['Genre'].count()
miscsayı=activision[activision['Genre']=='Misc']
miscsayı=miscsayı['Genre'].count()
actsayı=activision[activision['Genre']=='Action']
actsayı=actsayı['Genre'].count()
platsayı=activision[activision['Genre']=='Platform']
platsayı=platsayı['Genre'].count()
racesayı=activision[activision['Genre']=='Racing']
racesayı=racesayı['Genre'].count()
rolesayı=activision[activision['Genre']=='Role-Playing']
rolesayı=rolesayı['Genre'].count()
simsayı=activision[activision['Genre']=='Simualation']
simsayı=simsayı['Genre'].count()
strasayı=activision[activision['Genre']=='Strategy']
strasayı=strasayı['Genre'].count()
sportsayı=activision[activision['Genre']=='Sports']
sportsayı=sportsayı['Genre'].count()
labels2=['Shooter','Adventure','Misc','Action','Platform','Racing','Role-Playing','Simualation','Strategy','Sports']
explode2=(0,0,0,0.1,0,0,0,0,0,0)
oyunsayı=[shootersayı,advsayı,miscsayı,actsayı,platsayı,racesayı,rolesayı,simsayı,strasayı,sportsayı]
ax3=plt.subplot()
ax3.pie(oyunsayı,labels=labels2,explode=explode2, autopct='%1.1f%%',shadow=True, startangle=90)
plt.title('Activision Markasının Yaptığı Oyunların Dağılımı')
plt.show()

#activisionshootervalues
ninsho=nintendo[nintendo['Genre']=='Action']
ninshona=ninsho['NA_Sales'].sum()
ninshoeu=ninsho['EU_Sales'].sum()
ninshojp=ninsho['JP_Sales'].sum()
ninshogl=ninsho['Global_Sales'].sum()
ninsholist=[ninshona,ninshoeu,ninshojp,ninshogl]

actsho=activision[activision['Genre']=='Action']
actshona=actsho['NA_Sales'].sum()
actshoeu=actsho['EU_Sales'].sum()
actshojp=actsho['JP_Sales'].sum()
actshogl=actsho['Global_Sales'].sum()
actsholist=[actshona,actshoeu,actshojp,actshogl]
ax4=plt.subplot()
ax4.bar(x-width/2,actsholist,width)
ax4.bar(x+width/2,ninsholist,width)
plt.title('Nintendo ve Activision Markalarının Action Oyunları Karşılaştırılmıştır.')
plt.legend(['Activision','Nintendo'])
plt.xlabel('Activision Markası %43 ile En Çok Action Oyunları ile Tanınmıştır Fakat Action Oyunlarında O Kadar Da Başarılı Olmadıkları Gözüküyor. ')




