from Student import *
class Exercice:
    def __init__(self,path,author,title,subject,tag,prequesites):
        self.path = path
        self.author = author
        self.title = title
        self.subject = subject
        self.tag = tag
        self.prequesites = prequesites

    def getPath(self):
        return self.path
    
    def getAuthor(self):
        return self.author
    
    def getTag(self):
        return self.tag
    
    def getTitle(self):
        return self.title

    def getPrequesites(self):
        return self.prequesites
    
    def getSubject(self):
        return self.subject

    def similarTag(self,tags):
        #self.tag est le tag de l'exercice
        #tag est le tag qui s'adapte par rapport au mode
        for tag in tags.items():
            if tag[0] not in self.tag or (tag[0] in self.tag and (tag[1]-self.tag[tag[0]]>1 or tag[1]-self.tag[tag[0]]<-1)):
                return False
        return True


    def hasPrequesites(self,student):
        profil = student.profil
        if not self.prequesites:
           return True
        if profil.get(self.subject):
           subj = profil[self.subject]['skills']
           for p in self.prequesites.items():
              if not subj.get(p[0]):
                return False
              if subj[p[0]]<p[1]:
                return False
           return True
        return False
##############################################################################################################

    def hasPreForRev(self,student):
        """
        Vérifie si l'exercice rempli les conditions du mode révision
        Ici  :
        si le niveau de l'élève dans une notion correspond au niveau du prérequis de l'exercice :
            renvoi True
        Sinon renvoi False
        """
        profil = student.profil
        if not self.prequesites:
            return False
        if profil.get(self.subject):
            subj = profil[self.subject]['skills']
            for p in self.prequesites.items():
                if not subj.get(p[0]):
                    return False
                if round(subj[p[0]]) != p[1]:
                    return False
            return True
        return False
        
    def hasTagLevel(self,student,tags):
        for tag in tags.items():
            if(not((self.tag[tag[0]] <= tag[1]+2) and (self.tag[tag[0]] >= tag[1]))):
                return False
        return True

    def __str__(self):
        return "Path = "+self.path+" Author = "+self.author+" Title = "+self.title
