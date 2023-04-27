from datetime import date
def main():
  print("Hello from GitHub");
  with open('.github/workflows/outputFile1.txt') as f:
        contents = f.readlines();
        contents = str(contents);
        print('reading file content');
        print('contents->',contents);
        c1=str(date.today())
        print("date.today()->",c1);
        c1=c1+"\"+"n";
        print("c1-now->",c1);
        if contents == '':
          print("found file empty");
        if (date.today()==c1):
          print("today's date is->",contents);

if __name__=='__main__':
  main()
