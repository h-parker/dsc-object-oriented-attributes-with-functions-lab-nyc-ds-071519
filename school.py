class School:
    def __init__(self, name, roster={}):
        self.name = name
        self.roster = roster
        
        
    def add_student(self, name, grade): 
        if self.roster.get(grade)!= None: # if grade not None(thus exists)
            self.roster[grade].append(name) # add student to vals
        
        else: # otherwise
            self.roster[grade] = [name] # make new key, add student to list
        
        return
    
    
    def grade(self, grade):
        return self.roster[grade]
    
    
    def sort_roster(self):
        for grade in self.roster:
            self.roster[grade].sort()
        return self.roster