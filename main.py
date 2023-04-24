from datetime import datetime,date
import webbrowser
with open('outputFile.txt','w') as f:
    f.write(f'{datetime.now()}----{date.today()}')


