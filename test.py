from quicktry import quicktry
import os

#parameters for all 
workdir = os.path.join(os.getcwd(), 'tmp')
stdin = None

#python 2 test parameters
language="python2"
script = 'for i in range(10):\n\tprint("hello")'

#python 3 test parameters
language="python3"
script_python3  = 'for i in range(10):\n\tprint("hello")'
output_python3 = quicktry.execute(workdir, script_python3, stdin, "python3")
print (output_python3)

#nodejs test parameters
script_nodejs="console.log('hello world');"
output_nodejs = quicktry.execute(workdir, script_nodejs, stdin, "nodejs")
print(output_nodejs)

#go test parameters
script_go='package main; import "fmt"; func main() { fmt.Println("Hello World") }'
output_go = quicktry.execute(workdir,script_go, stdin, "go")
print (output_go)

#java test parameters
script_java='System.out.println("Hello World")'
output_java = quicktry.execute(workdir,script_java, stdin, "java")
print (output_java)





print(quicktry.query_images())
