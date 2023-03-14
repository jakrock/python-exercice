class Node:
    def __init__(self,valeur):
        self.valeur=valeur
        self.enfant_gauche=None
        self.enfant_droite=None


    #inserer des nooued avec le language python
    def insert_gauche(self,v):
        if self.enfant_gauche ==None:
            self.enfant_gauche=Node(v)
        else:
            new_node=Node(v)
            new_node.enfant_gauche=self.enfant_gauche
            self.enfant_gauche=new_node 
   
    def insert_droite(self,v):
        if self.enfant_droite ==None:
            self.enfant_droite=Node(v)
        else:
            new_node=Node(v)
            new_node.enfant_droite=self.enfant_droite
            self.enfant_droite=new_node   
                     