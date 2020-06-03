#webscrape_sb
from bs4 import BeautifulSoup


class team1:
    def __init__(self, first, last, ppg, threePct, fgPct, assists):
        self.first = first
        self.last = last
        self.ppg = ppg
        self.threePct = threePct
        self.fgPct = fgPct
        self.assists = assists  


class team2:
    def __init__(self, first,last,ppg, threePct, fgPct, assists):
        self.first = first
        self.last = last
        self.ppg = ppg
        self.threePct = threePct
        self.fgPct = fgPct
        self.assists = assists



p1 = team1('Kobe', 'Bryant', '42','65', '58', '7')
print(p1)
print(p1.first + ' ' + p1.last + ': Averages per game')
print('\t' 'PPG: ' + p1.ppg )
print('\t' '3pt accuracy: ' + p1.threePct + '%')
print('\t' 'FG accuracy: ' + p1.fgPct + '%')
print('\t' 'Assists: ' + p1.assists)

#check team2 class
p2 = team2('Dwight', 'Howard', '30','23', '79', '6')
print(p2)
print(p2.first + ' ' + p2.last + ': Averages per game')
print('\t' 'PPG: ' + p2.ppg )
print('\t' '3pt accuracy: ' + p2.threePct + '%')
print('\t' 'FG accuracy: ' + p2.fgPct + '%')
print('\t' 'Assists: ' + p2.assists)
