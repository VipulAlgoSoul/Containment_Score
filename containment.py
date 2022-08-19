from Levenshtein import distance as lvdis
import numpy as np

def interest_zero(s1,s2):
    
    st1=set(s1)
    st2=set(s2)
    
    dc1={se:list(s1).count(se) for se in st1}
    dc2={se:list(s2).count(se) for se in st2}
    
#     print(dc1,dc2)
    
    int_st=st1.intersection(s2)
    intrst_zeros=sum([min(dc1[e],dc2[e]) for e in int_st])
#     print("the lev distance is {} , the interested zeros of shift is {}".format(lvdis(s1,s2),intrst_zeros))

    return intrst_zeros, dc1,dc2


def containment_score(str1,str2):
    
    str_list=[str1,str2]  
#     print(str_list)
    if len(str1)!=len(str2):
        s1 = str_list[[len(str1),len(str2)].index(max([len(str1),len(str2)]))]
        s2 = str_list[[len(str1),len(str2)].index(min([len(str1),len(str2)]))]
    else:
        s1=str1
        s2=str2
    int_zer,dcc1,dcc2=interest_zero(s1,s2)
#     print(int_zer,">>>>>>>>>")
    #shift
    dep_list=[]
    levd_lis=[]
    
    #accounting for 3 shift left and 3 shift right
    sar_1=np.array([ord(e) for e in s1])
    sar_2=np.array([ord(e) for e in s2])
    
    poss_shft=len(s1)-int_zer
    
    for i in range(-1*poss_shft,poss_shft+1):
#         print("\n",i)
        if i<0:
#             print(s2[-1*i::],s1[0:len(s2[-1*i::])])
            s1_p=sar_1[0:len(s2[-1*i::])]
            s2_p=sar_2[-1*i::]
            
            str1_p=s1[0:len(s2[-1*i::])]
            str2_p=s2[-1*i::]
            lev_D=lvdis(str1_p,str2_p)
            levd_lis.append(lev_D)
            
            num_zer=sum((s2_p-s1_p)==0)
            
#             num_zer=sum((sar_2[-1*i::]-sar_1[0:len(s2[-1*i::])])==0)
            
            dep_list.append(num_zer)
        if i==0:
#             print(">>>>>>>>>>>>>>>>>>>>")
#             print(s2[-1*i::],s1[0:len(s2[-1*i::])])
            s1_p=sar_1[0:len(s2[-1*i::])]
            s2_p=sar_2[-1*i::]
            
            str1_p=s1[0:len(s2[-1*i::])]
            str2_p=s2[-1*i::]
            lev_D=lvdis(str1_p,str2_p)
            levd_lis.append(lev_D)
            
            num_zer=sum((s2_p-s1_p)==0)

#             num_zer=sum((sar_2[-1*i::]-sar_1[0:len(s2[-1*i::])])==0)

            dep_list.append(num_zer)
            
#             print(s2,s1[len(s1)-len(s2[0::])::])
            s1_p=sar_1[len(s1)-len(s2)::]
            s2_p=sar_2
            
            str1_p=s1[len(s1)-len(s2)::]
            str2_p=s2
            lev_D=lvdis(str1_p,str2_p)
            levd_lis.append(lev_D)
            
            num_zer=sum((s2_p-s1_p)==0)

#             num_zer=sum((sar_2-sar_1[len(s1)-len(s2)::])==0)
            dep_list.append(num_zer)
            
        if i>0:
#             print(s2[0:-1*i],s1[len(s1)-len(s2[0:-1*i])::])
            s1_p=sar_1[len(s1)-len(s2[0:-1*i])::]
            s2_p=sar_2[0:-1*i]
            
            str1_p=s1[len(s1)-len(s2[0:-1*i])::]
            str2_p=s2[0:-1*i]
            lev_D=lvdis(str1_p,str2_p)
            levd_lis.append(lev_D)
            
            num_zer=sum((s2_p-s1_p)==0)
            dep_list.append(num_zer)

    print("the containment score for {} contained in {} is {}".format(s2,s1,max(dep_list)/len(s1)))
    
    return max(dep_list)/len(s1)


containment_score("pool","pooler")
