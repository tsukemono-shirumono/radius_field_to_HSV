import numpy as np
import cv2
def makeImgHSV(thetas,vs=None,ss=None,norm=True):#S:色味,V:明るさ
    thetas=np.array(thetas)
    X,Y=thetas.shape

    if vs is None:
        vs=np.full((X,Y),255).astype(np.uint8)
    elif norm:
        vs=( (vs-np.min(vs))/(np.max(vs)-np.min(vs))*255 +0.5).astype(np.uint8)
    else:
        vs[vs>255]=255
        vs[vs<0]=0
        vs=(vs+0.5).astype(np.uint8)
    
    if ss is None:
        ss=np.full((X,Y),255).astype(np.uint8)
    else:
        ss[ss>255]=255
        ss[ss<0]=0
        ss=(ss+0.5).astype(np.uint8)
    
    thetas=( 179*( thetas%(2*math.pi) )/(2*math.pi)+0.5 ).astype(np.uint8)
    
    return cv2.cvtColor(np.stack([thetas,ss,vs],2), cv2.COLOR_HSV2BGR)
