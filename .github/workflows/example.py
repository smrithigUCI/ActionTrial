def main():
  print("Hello from GitHub");
  with open('.github/workflows/outputFile1.txt') as f:
        contents = f.readlines();
        contents = str(contents);
        print('reading file content');
        print('contents->',contents);
        if contents == '':
          print("found file empty");

if __name__=='__main__':
  main()
