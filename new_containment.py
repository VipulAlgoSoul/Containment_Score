from Levenshtein import distance as lvdis
import re



def get_score(predinp, gtinp):

    pred = re.sub('[^a-zA-Z0-9 \n\.]', ' ', predinp)
    gt = re.sub('[^a-zA-Z0-9 \n\.]', ' ', gtinp)

    pred_tu = tuple(pred.split())
    gt_tu = tuple(gt.split())
    #arrays
    if (len(gt_tu)==1) and (len(pred_tu)==1):
        pred_tu = tuple([*pred])
        gt_tu = tuple([*gt])


    slope_index=[]
    metrix = {i:[prd,[lvdis(prd,grd) for grd in gt_tu]] for i,prd in enumerate(pred_tu)}

    for ind, prdd in metrix.items():
        prd= prdd[1]
        minval = min(prd)
        if minval < len(prdd[0])/4:
            if prd.count(minval)>1:
                slope_index.append(tuple([inx for inx,v in enumerate(prd) if v==minval]))
            else:
                slope_index.append(prd.index(minval))

    master_path={"0":[]}
    try:
        for inddx in slope_index:

            if isinstance(inddx,tuple):
                ini_dic={}
                for indl in inddx:
                    for k in master_path.keys():
                        ini_dic[str(indl)+str(k)] = master_path[k].copy()
                        ini_dic[str(indl)+str(k)].append(indl)
                master_path =ini_dic

            else:
                for kyi in master_path.keys():
                    master_path[kyi].append(inddx)


        slope_consistency = {k:len(set([i-v[e+1] for e,i in enumerate(v[0:-1])])) for k,v in master_path.items()}
        minkey = min(slope_consistency, key=slope_consistency.get)
        score = len(master_path[minkey])/len(gt_tu)
    except: score =0

    return score

def Contain_Score(pred,gt):
    score1 = get_score(pred,gt)

    if score1>1:
        score1 = get_score(pred=gt,gt=pred)
    return score1

print(Contain_Score(pred="hi how are you ", gt="where is are you"))
