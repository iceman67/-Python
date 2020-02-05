from ftplib import FTP

class ftp_petbox:
  host='petbox.kr'
  username='triniti'
  password='u#CMs37RcWJb'
  ftp=None
  attempts=0
  files=None

  def connect(self):
     self.ftp = FTP()
     self.ftp.connect(self.host)
     self.ftp.login(user=self.username, passwd=self.password)
     self.attempts += 1

  def flist(self):
     self.files = self.ftp.nlst()
     return self.files

  def download(self, j):
    print "file name=>",self.files[j]      
    fhandle = open(self.files[j], 'wb')
    self.ftp.retrbinary('RETR ' + self.files[j], fhandle.write)
    fhandle.close()


if __name__ == '__main__': 
   pftp =  ftp_petbox()
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
