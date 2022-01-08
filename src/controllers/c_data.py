import json

class DataController(object):
    def __init__(self):
        super(DataController, self).__init__()
        self.getData()
        try:
            self.sectionsTime = self.data['sectionsTime']
            self.shortBreakTime = self.data['shortBreakTime']
            self.longBreakTime = self.data['longBreakTime']
            self.amountSections = self.data['amountSections']
            self.alertSound = self.data['alertSound']
            self.notify = self.data['notify']
            self.darkTheme = self.data['darkTheme']
        except print(Exception):
            pass

    def getData(self):
        """Função que irá atualizar os dados salvos
        """        
        try:
            with open('data/data.json', 'r+') as file:
                self.data = json.load(file)
        except print(Exception):
            pass
    
    def setData(self):
        """Função que irá gravar os dados alterados
        """        
        with open('data/data.json', 'r+') as file:                
            self.data['sectionsTime'] = self.sectionsTime
            self.data['shortBreakTime'] = self.shortBreakTime
            self.data['longBreakTime'] = self.longBreakTime
            self.data['amountSections'] = self.amountSections
            self.data['alertSound'] = self.alertSound
            self.data['notify'] = self.notify
            self.data['darkTheme'] = self.darkTheme
            file.seek(0)
            try:
                json.dump(self.data, file, indent=4)
                file.truncate()
            except print(Exception):
                pass
        self.getData()