class Stats():
    '''отслеживание статистики'''
    
    
    def __init__(self):
        '''инициализирует статистику'''
        self.reset_stats()
        self.rungame = True
        f = open('1.txt', 'r')
        self.high_score = int(f.readline())
        
    def reset_stats(self):
        '''статистика изменяющяяся во время игры'''
        self.gunsleft = 2
        self.score = 0
        