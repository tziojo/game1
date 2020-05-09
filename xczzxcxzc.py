#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

nikes=int(input('Στις πόσες νίκες θέλεις να παίξεις;'))
c=0;
computer=0;
you=0;
r=True
while (computer < nikes) and (you < nikes) and (r==True) :
    c += 1
    print('Ξεκινάει o γύρος:' , c , 'το score είναι:', you ,'-' , computer ,'............')
    x=input('πέτρα,ψαλίδι ή χαρτί;')
    while x!= 'πέτρα' and x!='χαρτί' and x!='ψαλίδι' and x!= 'exit':
         x=input('Λάθος γράψε πέτρα,ψαλίδι,χαρτί ή exit για έξοδο')
    if x == 'πέτρα':
            x=1;
    elif x == 'ψαλίδι':
            x=2;
    elif x == 'χαρτί':
            x=3;
    else:
        r=False
    k=random.randint(1,3)
    if (x==1):
        if(k==1):
            print('Ισοπαλία είχατε πέτρα και οι δύο')
        elif(k==3):
            print('Έχασες είχε ψαλίδι :(')
            computer += 1
        else:
            print('Μπράβο!Κερδισες,είχε ψαλίδι')
            you += 1
    elif (x==2):
        if(k==2):
            print('Ισοπαλία είχατε ψαλίδι και οι δύο')
        elif(k==1):
            print('Έχασες είχε πέτρα :(')
            computer += 1
        else:
            print('Μπράβο!Κερδισες,είχε χαρτί')
            you += 1
    elif (x==3):
        if(k==3):
            print('Ισοπαλία είχατε χαρτί και οι δύο')
        elif(k==2):
            print('Έχασες είχε ψαλίδι :(')
            computer += 1
        else:
            print('Μπράβο!Κερδισες,είχε χαρτί')
            you += 1
    else:
        print('Πατήσατε έξοδο!............')
if computer < you :
    print('Μπράβο κέρδισες!!!!', you , '-',computer)
elif you < computer :
    print('Δυστυχως έχασες',you ,'-', computer )
else :
    print('Σταμάτησες το παιχνίδι και είναι ισοπαλία ')


# In[ ]:





# In[ ]:




