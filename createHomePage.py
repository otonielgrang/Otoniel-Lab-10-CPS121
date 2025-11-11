import findTemperatureLive
import sentence
def createHomePageOld(emailuser):
    firstn, lastn = emailuser.split('.')
    with open(f'{firstn}.{lastn}.html','w') as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<head>\n")
        f.write("<html>\n")
        f.write("<head>\n")
        f.write("<title> CPS121 LAB 10 | Otoniel Matute</title>\n")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("<h1>Welcome to Otoniel's Home Page</h1>\n")
        f.write("<p>\n")
        f.write("My Name is Otoniel but you can call me oto. This is my home page.</p>\n")
        f.write("<p> \n")
        f.write("<img src='me.jpg'alt='Picture of me'/></p>\n")
        f.write("<p> I'm a computer science major trying to pike in Computational biology. I'm really curiouse and love to learn new things.</p>\n")
        f.write("</body>\n")
        f.write("</html>\n")
        f.write("\n")

def createHomePage(emailuser):
    firstn, lastn = emailuser.split('.')
    with open(f'{firstn}.{lastn}.html','w') as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<head>\n")
        f.write("<html>\n")
        f.write("<head>\n")
        f.write("<title> CPS121 LAB 10 | Otoniel Matute</title>\n")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("<h1>Welcome to Otoniel's Home Page</h1>\n")
        f.write("<p>\n")
        f.write("My Name is Otoniel but you can call me oto. This is my home page.</p>\n")
        f.write("<p> \n")
        f.write(createParagraph(temperatureP('01984')))
        f.write(createParagraph(temperatureP(input('Insert Zip code: '))))
        f.write("<img src='me.jpg'alt='Picture of me'/></p>\n")
        f.write("<p> I'm a computer science major trying to pike in Computational biology. I'm really curiouse and love to learn new things.</p>\n")
        f.write(createParagraph('Random Sentence:'))
        f.write(createParagraph(sentence.sentence()))
        f.write("</body>\n")
        f.write("</html>\n")
        f.write("\n")


def temperatureP(zip):
    temp = findTemperatureLive.findLoc(zip)
    sTemp = f"In {temp[0]} the {temp[1]}"
    return sTemp
def createDocType():
    return '<!DOCTYPE html>\n'

def startHTML():
    return '<html>\n\n'

def endHTML():
    return '</html>\n\n'
def startBody():
    return '<body>\n\n'

def endBody():
    return '</body>\n\n'

def createParagraph(string):
    string = f'<p>{string}</p>\n'
    return string
def createHead(string):
    string = '<head><title>'+string+'</title></head>\n\n'
    return string
def createHeading(string):
    string = '<h1>'+string+'</h1>\n'
    return string
def createLink(link,name):
    string = f'<a href="{link}">{name}]</a>'
    return string
def createImage(source,alt):
    string = f'<img src="{source}" alt="{alt}"/>'



if __name__ == '__main__':
    createHomePage('Otoniel.Matutev2')