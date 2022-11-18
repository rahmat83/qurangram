import re
class Harfjar:
    minn='من'
    inna='إن'
    fi='في'
    aala='على'
    hatta='حتى'
    illa='إلى'
    lan='لن'
    izzan='إذن'
    kay='كى' 
    illla="إلا" 
    lam="لم"
    maa="ما"
    zalika="ذلك"
    kalla="كلا"
    iza="إذا"
    iz="إذ"
    anna='أن'
class Huruf:
    alif,ba,ta,sa,ja,ha,kho,da,zal,ro,zai,sin,shim,sod,do='ابتثجحخدذرزسشصض'
    tho,zo,ain,ghin,fa,kof,kaf,lam,minn,nun,haa,ya="طظعغفقكلمنهي"
    hamzah='ء'
    wau='و'
class Quransearch:
    #receive content
    def __init__ (self,select,content,display):
        self.select=select
        self.content=content 
        self.display=display   
        self.p1=fr'\d.*'
        self.count=0
        self.surah=None
    def selectsec(self):
        if self.select=='w':
            sec=self.compile(self.p1,self.content)
        else:
            p2=self.surahselection(self.select)
            sec=self.compile(p2,self.content)
            self.surah=sec
        return (sec)
    def compile(self,p,con):
        sec=""
        x=re.compile(p)
        match=x.finditer(con)
        for i in match:
            sec+="\n"+i.group() 
        return sec
    def split(self,x):
        wau="ﻭ"
        strp=""
        for i in x:
            if x[i][1]==1:                
                strp+=fr'\b\و?{x[i][0]}\s.*'
            elif x[i][1]==2:
                g=[i for i in x[i][0]]
                s2=""
                for i in g:
                    s2+=i+'\w*'
                s3=fr'\b.*{s2}\b.*'                
                strp+=s3
        return strp
    def opentaskel(self):
        with open('quran-simple-min.txt',mode='r',encoding='utf-8') as f:
            content=f.read()        
        return content    
    def surahnumbering(self,x):
        x=re.sub(r'\s+', '', x)
        s=re.split(r'\B',x)    
        op = ""
        i = 0
        while i < len(s):
            op += fr'[{s[i]}]'        
            i = i + 1     
        return op
    def surahselection(self,x):
        s=self.surahnumbering(x)
        p=fr'\b{s}[|]\d.*'# surah selection pattern
        return p
    def searchpattern(self,x):
        z=self.selectsec()#this is how the section is passed
        strp=fr'\d.*'+self.split(x)+".*"
        print("This is the pattern selected",strp)
        ui=re.compile(strp)
        matches=ui.finditer(z)
        k=1
        r=1
        j=[]
        xt=[]
        wt=[]
        for i in matches:
            vf = r'\d*\|\d*'
            uf = re.compile(vf)
            r = uf.match(i.group())
            
            j.append(r.group())
            if self.display == 'r':
                xt.append(i.group())
            k += 1
        count = 0
        for i in j:
            f = re.sub(r'\D', "\|", j[count])
            rt = r'\b' + f + r'\b'
            lo = re.compile(rt + '.*')
            y = lo.search(self.opentaskel())            
            if self.display == 't':
                wt.append(y.group())
            count += 1
        return xt,wt
        
    def specayah(self,s,v):        
        regx=fr'\W{self.numiter(s)}\|{self.numiter(v)}\W.*'
        print(regx)
        ayah=re.compile(regx)
        rt=ayah.findall(self.content)
        print(rt)   
    def numiter(self,s):
        x=re.sub(r'\s+', '', s)       
        r=""
        for i in re.split(r'\B',x):
            r+=fr'[{i}]'
        return r  


