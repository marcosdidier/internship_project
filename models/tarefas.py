class Task:
    _id_counter_ = 1

    STATUS = ["Pendente", "Em andamento", "Concluído"]

    def __init__(self, title:str, desc:str, user):
        self.id = Task._id_counter_
        self.title = title
        self.desc = desc
        
