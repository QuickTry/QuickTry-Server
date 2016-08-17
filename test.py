from quicktry import quicktry
import os
import yaml

with open('languages.yml') as f:
    config = yaml.load(f)

qt = quicktry.QuickTry(config['languages'])

#parameters for all 
workdir = os.path.join(os.getcwd(), 'tmp')
stdin = None

#python 2 test parameters
script = 'for i in range(10):\n\tprint("hello")'
output = qt.execute("python2", script, stdin, workdir)
print(output)

#python 3 test parameters
script = 'for i in range(10):\n\tprint("hello")'
output = qt.execute("python3", script, stdin, workdir)
print(output)

#nodejs test parameters
script = "console.log('hello world');"
output = qt.execute("nodejs", script, stdin, workdir)
print(output)

#go test parameters
script = 'package main; import "fmt"; func main() { fmt.Println("Hello ' \
         'World") }'
output = qt.execute("go", script, stdin, workdir)
print (output)

print(qt.query_images())
print(qt.get_languages())