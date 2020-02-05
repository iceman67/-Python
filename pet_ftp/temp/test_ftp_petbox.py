import ftp_petbox

pftp =  ftp_petbox.FtpPetbox()
pftp.connect() 
files = pftp.flist()
for i,v in enumerate(files,1):
       print i,"->",v 

if i==0:
    for j in range(len(files)):
        pftp.download(j)                                                                         
if i>0 and i<=len(files):
    for j in range(len(files)):
        pftp.download(j-1)   
