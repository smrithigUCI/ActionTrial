from datetime import date
def main():
  print("Hello from GitHub");
  with open('.github/workflows/outputFile1.txt') as f:
        contents = f.readlines();
        contents = str(contents);
        contents = contents.rstrip();
        print('reading file content');
        print('contents->',contents);
        print('date.today()->',date.today());
        if contents == '':
          print("found file empty");
        if (date.today()==contents):
          print("today's date is->",contents);

if __name__=='__main__':
  main()
