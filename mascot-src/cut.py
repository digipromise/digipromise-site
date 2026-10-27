import numpy as np, sys
from PIL import Image, ImageFilter
from scipy import ndimage as nd
U='/root/.claude/uploads/bccd5e8c-39c9-57aa-8ce8-9f4a6170a2c0/'
SETS={'a':{'iris':'4afe1dc6','aura':'7e12ad75','nova':'9e9f140a','luna':'b1e2855a','lara':'83269b1a','stella':'51dfb0bd','lilia':'9d05259f'},
      'b':{'iris':'93b14b04','aura':'3707701d','nova':'530d4cf8','luna':'d8a0d34c','lara':'9b6ad4e8','stella':'ec198558','lilia':'cccc93da'}}
def cut(src,out,S=420):
    im=Image.open(U+src+'-image.jpg').convert('RGB'); a=np.asarray(im).astype(float)/255
    mx=a.max(2); mn=a.min(2); sat=(mx-mn)/(mx+1e-6)
    # background model: heavily blurred image of only bright, low-sat pixels
    bgmask=(sat<0.06)&(mx>0.85)
    h,w=mx.shape
    # estimate bg per column/row with large blur on bg pixels
    acc=nd.gaussian_filter(a*bgmask[...,None],(60,60,0)); wt=nd.gaussian_filter(bgmask.astype(float),60)[...,None]
    bg=acc/np.maximum(wt,1e-3)
    dist=np.sqrt(((a-bg)**2).sum(2))
    rough=(dist>0.10)|(sat>0.14)
    rough=nd.binary_opening(rough,iterations=2)
    lab,n=nd.label(rough); sizes=nd.sum(rough,lab,range(1,n+1)); keep=lab==(1+int(np.argmax(sizes)))
    keep=nd.binary_fill_holes(nd.binary_closing(keep,iterations=6))
    # cut away the floor shadow: rows below the ball where the mask is low-saturation and wide
    shadow=keep&(sat<0.10)&(mx<0.9)&(np.arange(h)[:,None]>h*0.6)
    keep=keep&~nd.binary_opening(shadow,iterations=3)
    keep=nd.binary_fill_holes(keep)
    # soft edge: alpha from dist near border
    soft=np.clip((dist-0.04)/0.10,0,1)
    edge=nd.binary_dilation(keep,iterations=3)&~nd.binary_erosion(keep,iterations=4)
    alpha=np.where(keep,1.0,0.0); alpha=np.where(edge,np.maximum(soft*nd.binary_dilation(keep,iterations=3),alpha*soft+0*alpha),alpha)
    alpha=nd.gaussian_filter(alpha,0.8)
    ys,xs=np.where(alpha>0.5); cy,cx=(ys.min()+ys.max())/2,(xs.min()+xs.max())/2; r=max(ys.max()-ys.min(),xs.max()-xs.min())/2*1.04
    rgba=np.dstack([a,alpha]); img=Image.fromarray((rgba*255).astype('uint8'),'RGBA')
    box=(int(cx-r),int(cy-r),int(cx+r),int(cy+r)); img=img.crop(box).resize((S,S),Image.LANCZOS)
    img.save(out,'WEBP',quality=86,method=6)
for s,m in SETS.items():
    for k,f in m.items():
        cut(f,f'{s}-{k}.webp'); print(s,k)
