ph=[5.5,	9,	8.4,	9,	8.5,	8.5,	8.5,8.4,	8.3,	8.3,	8.3,	8.4,	8.3,	8.3		]
phnorm=[6.5,8.5,6.6,9,3,8,1,10,6,90,2,45,7,90]
timeline=[]
def qiymet(n):
    n=n-1
    timeline.append(ph[n:n+7])
def phyoxlama(n):
    n=n-1
    p=0
    phnetice=[]
    abc=timeline[n]
    for i in range(len(abc)):
        if phnorm[p]<= abc[i]<=phnorm[p+1]:
            phnetice.append(abc[i])
        else:
            phnetice.append('normadan kenar')
        p+=2
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
a=int(input())
qiymet(a)

print(timeline)
phyoxlama(a)
