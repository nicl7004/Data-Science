
from pollster import Pollster
pollster = Pollster()

if __name__ == "__main__":
    for year in ['2012', '2016']:
        res = pollster.charts(topic='%i-president' % year)
        for chart in res:
            for poll in chart.polls():
                for question in poll.questions:
                    subpop_id = 0
                    for subpop in question['subpopulations']:
                        
