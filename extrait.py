from os import system

sources = list(open("extrait.txt","r")) 

system("touch paragraphes.txt") # ==> ensemble des paragraphes
system("touch fileCleaned.txt") # ==> paragraphes.txt nettoyé
system("touch extraction.txt")  # ==> dictionnaire de paires bambaran french                            
                             
                       
   
def divParagraphe():
    """
    Extraction des paragraph 
    """
    global sources 
    paragraph = open("paragraphes.txt","w")  
    
    debut = 0
    fin = 0
    compter = 0
    for ligne in sources : 
        if ligne == "\n" or ligne == "\n\n" : 
            fin = compter
        if debut != fin  :
            paragraphe = str(sources[debut+1:fin]) + "\n"
            if len(sources[debut+1:fin]) > 2 : 
                paragraph.write(paragraphe[0:len(paragraphe)])
        debut = fin 
        compter+=1
    

def clean() : 
    
    """
    Suppression des paragraphes non traduit

    """


    FileCleaned = open("fileCleaned.txt","w")    
    paragraph = list(open("paragraphes.txt","r"))  
    

    for ph in paragraph : 
        
        
        if  any("\t" in term for term in eval(ph)): 
            FileCleaned.write(ph)
            


def extraction(): 
    """
    Extraction des paires
    """
    dictionnaire = dict()
    FileClean = list(open("fileCleaned.txt","r"))
    extraction = open("extraction.txt","w")
    x= 0
    for ph in FileClean[2:]:
        
        bambaran = ""
        french   = ""
        
        if any("\t" in i for i in eval(ph)) : 
            for sentence in eval(ph):
                if "\t" in sentence : 
                    x+=1
                    bambaran += sentence[0:sentence.index("\t")] + "\n"
                    index =  sentence[::-1].index("\t")
                    index = len(sentence)-index
                    french += sentence[index:]
                else : 
                    continue

            dictionnaire[bambaran] = french
    extraction.write(str(dictionnaire))



            
divParagraphe()
clean()                         
extraction()
    







