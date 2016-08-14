from quicktry import quicktry
import os

workdir = os.path.join(os.getcwd(), 'tmp')
script = 'for i in range(10):\n\tprint("hello")'
stdin = None
language="python27"

output = quicktry.execute(workdir, script, stdin, language)
print(output)

print(quicktry.query_images())
