from quicktry import quicktry
import os

workdir = os.path.join(os.getcwd(), 'tmp')
script = 'for i in range(10):\n\tprint("hello")'
stdin = None
language="python2"

script2="console.log('hello world');"
language2="nodejs"

script_go='package main; import "fmt"; func main() { fmt.Println("Hello World") }'

script_java='System.out.println("Hello World")'

output = quicktry.execute(workdir, script2, stdin, language2)
print(output)

output_go = quicktry.execute(workdir,script_go, stdin, "go")
print (output_go)

output_java = quicktry.execute(workdir,script_java, stdin, "java")
print (output_java)

print(quicktry.query_images())
