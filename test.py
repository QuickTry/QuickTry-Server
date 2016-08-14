from quicktry import quicktry
import os

workdir = os.path.join(os.getcwd(), 'tmp')
script = 'for i in range(10):\n\tprint("hello")'
stdin = None
language="python2"

script2="console.log('hello world');"
language2="nodejs"

script_go='package main; import "fmt"; func main() { fmt.Println("Hello World") }'

output = quicktry.execute(workdir, script2, stdin, language2)
print(output)

output_go = quicktry.execute(workdir,script_go, stdin, "go")
print (output_go)

print(quicktry.query_images())
