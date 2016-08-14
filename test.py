from quicktry import quicktry
import os

workdir = os.path.join(os.getcwd(), 'tmp')
script = 'for i in range(10):\n\tprint("hello")'
stdin = None
language="python2"

script2="console.log('hello world');"
language2="nodejs"

output = quicktry.execute(workdir, script2, stdin, language2)
print(output)

print(quicktry.query_images())
