ph=[8.5,8.5,8.4,8.4,8.5,8.5,8.5,8.4,8.3,8.3,8.3,8.4,8.3,8.3,0 ,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.6,8.6,8.6,8.6,8.6,8.5,8.6,8.5,8.4,8.2,8.4,7.9,8.1,7.8,7.9,8.2,8.4,7.9,7.8,7.7,7.9,0,8.7,8.2,8.6,8.2,7.9,8.1,7.8,8.4,8.3,8.6,8.3,8.4,8.3]
phnorm=[6.5,8.5]
iyi=[]
dadi=[]
rengpt=[]
rengbicr=[]
bulaniq=[]
bulaniqnorm=2.6
codluq=[]
codluq_norm=7 #7-den az
elek20=[]
hidrokar=[]
hidrokar_norm=[]
hidrogen=[]
aluminium=[]
nh4=[]
nh4_norm=0.5
arsen=[]
demir=[]
ag=[]
hidrosulfid=[]
hidrisulfid=[]
cloride=[]
clorfree=[]
clorfree_norm=[0.3,0.5]
cloradd=[]
xlorationu=[]
xlorationu_norm=350 #350-den az
kalium=[]
kalsium=[]
manqan=[]
mis=[]
molibden=[]
maqnezium=[]
natrium=[]
nikel=[]
nitratlar=[]
nitrat_norm=45
nitrit=[]
nitrit_norm=3.3
polifosfat=[]
polifosfat_norm=3.5
stronsium=[]
zn=[]
sulfats=[]
sianids=[]
timeline=[]
dates=["Yanvar 2018", "Fevral 2018", "Mart 2018", "Aprel 2018","May 2018","Iyun 2018","Iyul 2018","Sentyabr 2018","Oktyabr 2018"]
essential=[]
def qiymet(n):
  essential.append(dates[n-1])
  n=7*(n-1)
  timeline.append(ph[n:n+7])
def phyoxlama(n):                
    n=n-1
    phnetice=[]
    abc=timeline[n]
    for i in range(len(abc)):
        if abc[i]==0:
            phnetice.append('teyin olunmayib')
        else:
            if phnorm[0]<= abc[i]<=phnorm[1]:
                phnetice.append(abc[i])
            else:
                phnetice.append('normadan kenar')
    print(phnetice)
    if 'normadan kenar' in phnetice:
        a=input('Menteqelere melumat gonderilsinmi?')
        a=a.lower()
        if a=='yes' or a=='he' or a=='beli':
            while 'normadan kenar' in phnetice:
                print("Melumat gonderilir")
                if phnetice.index('normadan kenar')==0:
                    print('Taxtakorpu')
                    phnetice[0]='temir'
                elif phnetice.index('normadan kenar')==1:
                    print("Su goturucu qurgunun adi")
                    phnetice[1]='temir'
                elif phnetice.index('normadan kenar')==2:
                    print("Cenub nasos stansiyasinin yani")
                    phnetice[2]='temir'
                elif phnetice.index('normadan kenar')==3:
                    print("Cenub-qerb dambasi")
                    phnetice[3]='temir'
                elif phnetice.index('normadan kenar')==4:
                    print("Cenub dambasi")
                    phnetice[4]='temir'
                elif phnetice.index('normadan kenar')==5:
                    print("Simal serq dambasi")
                    phnetice[5]='temir'
                elif phnetice.index('normadan kenar')==6:
                    print("meliorasiya")
                    phnetice[6]='temir'
        else:
            print('Neticede filan filan xestelikler olacaq')
        print(phnetice)
    else:
        print("Her sey qaydasindadir")
print("Ph üzrə: "+str(len(dates))+ " zaman")
for i in range(int(input())):
    b=int(input())
    qiymet(b)
print(essential)
a=int(input())
phyoxlama(a)
