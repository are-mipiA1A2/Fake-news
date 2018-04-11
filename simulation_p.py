import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import random

#description d'un agent : nom:(opinion, deja_vu , force_de_persuasion , conviction)
#                         nom:(   op  , deja_vu ,       fp            ,     p     )

N_1dim = 25     #nb de membres du réseau sur une dimension
N = N_1dim**2  #nb de membres du réseau discussion physique
nb_om = 3      #nb d'organismes médiatiques
nb_malv = 6    #nb d'agents malveillants
steps = 100    #nb de pas de temps
seuil = 0.3    #seuil

#Initialisation d'un réseau d'humains :
Reseau_discu={str(k):(0,False,fp,0.5) for k in range(1,N+1) for fp in np.random.uniform(low=0.0, high=1.0,size=N)}
Noms_reseau_discu=[k for k in range(N)]

#Initialisation d'un réseau avec des agents malveillants :
def init_sys_avec_malv(n_1dim,nb_malv):
    
    Pop={str(k):(0,False,fp,0.5) for k in range(1,N+1) for fp in np.random.uniform(low=0.0, high=1.0,size=N)}
    L=np.random.choice(range(1,(n_1dim**2)+1), size=nb_malv, replace=False)
    for e in L:
        Pop[str(e)]=(1,True,0.9,0.8)
    
    return Pop

Pop_malv=init_sys_avec_malv(N_1dim,nb_malv)
print('Réseau avec malveillants : \n',Pop_malv)

#Initialisation d'un système avec organismes médiatiques:
List_om=np.random.choice(range(1,(N_1dim**2)+1), size=nb_om, replace=False)
print(List_om)

def init_ac_om(reseau,list_om):
    for (name,(op,deja,fp,p)) in reseau.items():
        if name in list_om:
            reseau['OM'+str(name)]=(0,False,np.random.uniform(low=0.7,high=1.0),0.5)
            del reseau[name]
    return reseau

Pop_ac_om=init_ac_om(Reseau_discu,List_om)
print('Population avec médias : \n',Pop_ac_om)
        
#Représentation des agents en 2 dimensions (sur une matrice) :
Agents=np.arange(1,N_1dim*N_1dim+1).reshape(N_1dim,N_1dim)
print('Agents :\n',Agents)

#Réseau à valeurs quelconques (au milieu de la simulation par exemple) pour faire des tests :
Test_reseau={str(k):(np.random.choice([0,1]),np.random.choice([False,True]),np.random.random_sample(),np.random.random_sample()) for k in range(1,N+1)}

#Matrice des opinions de départ :
def matrice_opinions(reseau,n_1dim):
    Op=np.zeros((n_1dim,n_1dim))
    i=0
    j=0
    for (nom,(op,deja_vu,persu,p)) in reseau.items():
        Op[i,j]=int(op)
        if j<(n_1dim-1):
            j=j+1
        elif j==(n_1dim-1):
            j=0
            i=i+1
    return Op

print(matrice_opinions(Pop_malv,N_1dim))

#Matrice des convictions de départ
def matrice_convic(reseau,n_1dim):
    C=np.zeros((n_1dim,n_1dim))
    i=0
    j=0
    for (nom,(opinion,deja_vu,persu,p)) in reseau.items():
        C[i,j]=p
        if j<(n_1dim-1):
            j=j+1
        elif j==(n_1dim-1):
            j=0
            i=i+1
    return C

print(matrice_convic(Pop_malv,N_1dim))




#Sélection d'un agent et de son voisinage pour établir un discussion
def selection_voisinage(Matrice,n_1dim):
    '''Sélection aléatoire des voisinages d'un individu
    '''
    L=[]                               #liste voisinage (pers susceptibles de discuter)
    Ldiscu=[]                          #liste discussion (pers qui vont discuter)
    size=np.random.choice(range(2,10)) #nb pers discussion
    
    ic=np.random.choice(range(n_1dim)) #ic,jc : indices de l'agent central
    jc=np.random.choice(range(n_1dim))
    a_central=Matrice[ic,jc]
    
    if ic>0 and ic<(n_1dim-1) and jc>0 and jc<(n_1dim-1):
        L=np.reshape(Matrice[ic-1 : ic+2 , jc-1 : jc+2] , 9)        
    elif ic==0 and jc>0 and jc<(n_1dim-1):          #a_central sur arête sup
        L=[(Matrice[ic,jc-1 : jc+2])
           ,(Matrice[ic+1,jc-1 : jc+2])
           ,(Matrice[n_1dim-1, jc-1 : jc+2])]
        L=np.reshape(L,9)
    elif ic==(n_1dim-1) and jc>0 and jc<(n_1dim-1): #a_central sur arête inf
        L=[(Matrice[ic,jc-1 : jc+2])
           ,(Matrice[ic-1,jc-1 : jc+2])
           ,(Matrice[0, jc-1 : jc+2])]
        L=np.reshape(L,9)        
    elif jc==0 and ic>0 and ic<(n_1dim-1):          #a_central sur arête gauche
        L=[(Matrice[ic-1 : ic+2,jc])
           ,(Matrice[ic-1 : ic+2,jc+1])
           ,(Matrice[ic-1 : ic+2,n_1dim-1])]
        L=np.reshape(L,9)        
    elif jc==(n_1dim-1) and ic>0 and ic<(n_1dim-1): #a_central sur arête droite
        L=[(Matrice[ic-1 : ic+2,jc])
           ,(Matrice[ic-1 : ic+2,jc-1])
           ,(Matrice[ic-1 : ic+2,0])]
        L=np.reshape(L,9)        
    elif a_central==1:                              #a_central sur coin sup/gauche
        L=[n_1dim,a_central,2,n_1dim*2,n_1dim+1,n_1dim+2,n_1dim*n_1dim,n_1dim*(n_1dim-1)+1,n_1dim*(n_1dim-1)+2]
        L=np.array(L)        
    elif a_central==n_1dim:                                                    #a_central sur coin sup/droit
        L=[n_1dim-1,a_central,1,n_1dim*2-1,n_1dim*2,n_1dim+1,n_1dim*n_1dim-1,n_1dim*n_1dim,n_1dim*(n_1dim-1)+1]
        L=np.array(L)
    elif a_central==n_1dim*(n_1dim-1)+1:            #a_central sur coin inf/gauche
        L=[n_1dim*(n_1dim-1),Matrice[ic-1,jc],Matrice[ic-1,jc+1]
          ,n_1dim*n_1dim,a_central,Matrice[ic,jc+1]
          ,1,2,n_1dim]
        L=np.array(L)        
    elif a_central==(n_1dim*n_1dim):                #a_central sur coin inf/droit
        L=[a_central-n_1dim-1,a_central-n_1dim,Matrice[ic-1,0]
          ,a_central-1,a_central,a_central-n_1dim+1
          ,1,n_1dim-1,n_1dim]
        L=np.array(L)
    
    Ldiscu=np.random.choice(L,size,replace=False)
             
    return Ldiscu

Population=np.arange(1,N_1dim*N_1dim+1).reshape(N_1dim,N_1dim)
List_discu=selection_voisinage(Population,N_1dim)
print('Population :\n',Population)
print('Liste des personnes qui vont discuter :',List_discu)


#Modification du paramètre p de x en fonction de la force de persuasion de y et vice versa :
def force_persu(x, y, reseau):
        
    opx,deja_vux,fpx,px=reseau[str(x)]
    opy,deja_vuy,fpy,py=reseau[str(y)]
    if fpx>fpy:
        py=py+fpy*(px-py)
    elif fpy>fpx:
        px=px+fpx*(py-px)
    
    reseau[str(x)]=(opx,True,fpx,px)
    reseau[str(y)]=(opy,True,fpy,py)
    
    return reseau


#Influence du voisinage :
    # si 2 personnes, force persu. Sinon, moyenne des p pondérée des fp; si abs(pi-moy)>seuil, pi=pi, sinon pi=moy
def influ_voisinage(list_discu,reseau,seuil):
    
    P=[]   #liste des convictions des membres de la discussion
    F=[]   #liste des forces de persuasion des membres de la discussion
    N=[]   #liste des noms des membres de la discussion
    i=0
    
    for k in list_discu:
        op_k,deja_k,fp_k,p_k=reseau[str(k)]
        N.append(int(k))
        P.append(p_k)
        F.append(fp_k)
            
    if len(N)==2:
        reseau=force_persu(N[0],N[1],reseau)
    else:
        for a in N:
            op_a,deja_a,fp_a,p_a=reseau[str(a)]
            other_p=P[0:a]+P[a+1:len(P)]
            other_fp=F[0:a]+F[a+1:len(F)]            
            moy=np.average(other_p,weights=other_fp)
            if abs(p_a-moy)<seuil:
                p_a=moy
            reseau[str(a)]=(op_a,True,fp_a,p_a)
    
            
    return reseau

print(influ_voisinage(List_discu,Test_reseau,seuil))


#Sélection d'un agent et de son voisinage pour établir un discussion
def selection_voisinage(Matrice,n_1dim):
    '''Sélection aléatoire des voisinages d'un individu
    '''
    L=[]                               #liste voisinage (pers susceptibles de discuter)
    Ldiscu=[]                          #liste discussion (pers qui vont discuter)
    size=np.random.choice(range(2,10)) #nb pers discussion
    
    ic=np.random.choice(range(n_1dim)) #ic,jc : indices de l'agent central
    jc=np.random.choice(range(n_1dim))
    a_central=Matrice[ic,jc]
    
    if ic>0 and ic<(n_1dim-1) and jc>0 and jc<(n_1dim-1):
        L=np.reshape(Matrice[ic-1 : ic+2 , jc-1 : jc+2] , 9)        
    elif ic==0 and jc>0 and jc<(n_1dim-1):          #a_central sur arête sup
        L=[(Matrice[ic,jc-1 : jc+2])
           ,(Matrice[ic+1,jc-1 : jc+2])
           ,(Matrice[n_1dim-1, jc-1 : jc+2])]
        L=np.reshape(L,9)
    elif ic==(n_1dim-1) and jc>0 and jc<(n_1dim-1): #a_central sur arête inf
        L=[(Matrice[ic,jc-1 : jc+2])
           ,(Matrice[ic-1,jc-1 : jc+2])
           ,(Matrice[0, jc-1 : jc+2])]
        L=np.reshape(L,9)        
    elif jc==0 and ic>0 and ic<(n_1dim-1):          #a_central sur arête gauche
        L=[(Matrice[ic-1 : ic+2,jc])
           ,(Matrice[ic-1 : ic+2,jc+1])
           ,(Matrice[ic-1 : ic+2,n_1dim-1])]
        L=np.reshape(L,9)        
    elif jc==(n_1dim-1) and ic>0 and ic<(n_1dim-1): #a_central sur arête droite
        L=[(Matrice[ic-1 : ic+2,jc])
           ,(Matrice[ic-1 : ic+2,jc-1])
           ,(Matrice[ic-1 : ic+2,0])]
        L=np.reshape(L,9)        
    elif a_central==1:                              #a_central sur coin sup/gauche
        L=[n_1dim,a_central,2,n_1dim*2,n_1dim+1,n_1dim+2,n_1dim*n_1dim,n_1dim*(n_1dim-1)+1,n_1dim*(n_1dim-1)+2]
        L=np.array(L)        
    elif a_central==n_1dim:                                                    #a_central sur coin sup/droit
        L=[n_1dim-1,a_central,1,n_1dim*2-1,n_1dim*2,n_1dim+1,n_1dim*n_1dim-1,n_1dim*n_1dim,n_1dim*(n_1dim-1)+1]
        L=np.array(L)
    elif a_central==n_1dim*(n_1dim-1)+1:            #a_central sur coin inf/gauche
        L=[n_1dim*(n_1dim-1),Matrice[ic-1,jc],Matrice[ic-1,jc+1]
          ,n_1dim*n_1dim,a_central,Matrice[ic,jc+1]
          ,1,2,n_1dim]
        L=np.array(L)        
    elif a_central==(n_1dim*n_1dim):                #a_central sur coin inf/droit
        L=[a_central-n_1dim-1,a_central-n_1dim,Matrice[ic-1,0]
          ,a_central-1,a_central,a_central-n_1dim+1
          ,1,n_1dim-1,n_1dim]
        L=np.array(L)
    
    Ldiscu=np.random.choice(L,size,replace=False)
             
    return Ldiscu

Population=np.arange(1,N_1dim*N_1dim+1).reshape(N_1dim,N_1dim)
List_discu=selection_voisinage(Population,N_1dim)
print('Population :\n',Population)
print('Liste des personnes qui vont discuter :',List_discu)


def simulation_op(reseau,n_1dim,mat_pop,names,steps,seuil):
    """retourne la matrice des OPINIONS de la population après un certain nb d'étapes"""
    
    M=matrice_opinions(reseau,n_1dim)
    results=[]
    results.append(M.copy())
    
    for simu in range(steps):
        i=np.random.choice(names)
        List_discu=selection_voisinage(mat_pop,n_1dim)
        Res_p_changé=influ_voisinage(List_discu,reseau,seuil)
        for c in Res_p_changé:
            op,deja,fp,p=Res_p_changé[c]
            if p>0.5 and op==0:
                op=1
                Res_p_changé[c]=(op,deja,fp,p)
            elif p<0.5 and op==1:
                op=0
                Res_p_changé[c]=(op,deja,fp,p)
        Op=[]
        P=[]
        for e in Res_p_changé:
            op,deja,fp,p=Res_p_changé[e]
            Op.append(op)
            P.append(p)
        Op_final=np.reshape(Op, (n_1dim,n_1dim))
        P_final=np.reshape(P, (n_1dim,n_1dim))
        results.append(Op_final.copy())
        
    return results

simulation_op(init_sys_avec_malv(N_1dim,nb_malv),N_1dim,Population,Noms_reseau_discu,steps,seuil)


def simulation_p(reseau,n_1dim,mat_pop,names,steps,seuil):
    """retourne la matrice des CONVICTIONS de la population après un certain nb d'étapes"""
    
    M=matrice_convic(reseau,n_1dim)
    results=[]
    results.append(M.copy())
    
    for simu in range(steps):
        i=np.random.choice(names)
        List_discu=selection_voisinage(mat_pop,n_1dim)
        Res_p_changé=influ_voisinage(List_discu,reseau,seuil)
        for c in Res_p_changé:
            op,deja,fp,p=Res_p_changé[c]
            if p>0.5 and op==0:
                op=1
                Res_p_changé[c]=(op,deja,fp,p)
            elif p<0.5 and op==1:
                op=0
                Res_p_changé[c]=(op,deja,fp,p)
        Op=[]
        P=[]
        for e in Res_p_changé:
            op,deja,fp,p=Res_p_changé[e]
            Op.append(op)
            P.append(p)
        Op_final=np.reshape(Op, (n_1dim,n_1dim))
        P_final=np.reshape(P, (n_1dim,n_1dim))
        results.append(P_final.copy())
        
    return results

simulation_p(init_sys_avec_malv(N_1dim,nb_malv),N_1dim,Population,Noms_reseau_discu,steps,seuil)


#ANIMATION

import matplotlib.animation as animation
import matplotlib.pyplot as plt
from IPython.core.display import HTML


fig=plt.figure()

Simulation_p=simulation_p(init_sys_avec_malv(N_1dim,nb_malv),N_1dim,Population,Noms_reseau_discu,1000,seuil)

#Affichage des opinions de départ

im=plt.imshow(Simulation_p[0],cmap='bwr',vmin=0,vmax=1)


def updatefig(i):
    im.set_array(Simulation_p[i+1])
    return im,

ani = animation.FuncAnimation(fig, updatefig, frames=range(1000), interval=50, blit=False)
HTML(ani.to_html5_video())
# Pour sauvegarder la vidéo dans un fichier externe
ani.save('simu_p.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
