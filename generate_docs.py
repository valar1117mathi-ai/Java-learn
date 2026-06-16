import os
import re

root_dir = '/home/dev/Projects/java/Java-learn'
directories = [
    'Array problems',
    'Linkdin_List',
    'non-linear-data',
    'pattern',
    'Queue_DSA',
    'Recursiveprogramming',
    'Searching_Algo',
    'Sorting',
    'stack'
]

output_file = os.path.join(root_dir, 'operations.md')

mermaid_template = """```mermaid
graph TD
    A[Start Operation] --> B[Execute %s]
    B --> C[End Operation]
```"""

with open(output_file, 'w') as f:
    f.write("# Java Operations Documentation\n\n")
    
    for d in directories:
        dir_path = os.path.join(root_dir, d)
        if not os.path.exists(dir_path):
            continue
            
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.java'):
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, root_dir)
                    
                    # Read file and extract methods
                    with open(filepath, 'r') as jf:
                        content = jf.read()
                        
                    # Find simple method signatures: public/private/protected [static] returnType methodName(...)
                    methods = re.findall(r'(?:public|private|protected)\s+(?:static\s+)?(?:[\w<>,\[\]]+\s+)+(\w+)\s*\(', content)
                    methods = [m for m in set(methods) if m != 'main' and m != file.split('.')[0]]
                    
                    if methods:
                        f.write(f"@[{root_dir}]\n\n")
                        f.write(f"### {rel_path}\n\n")
                        for m in methods:
                            f.write(f"#### Operation: `{m}`\n\n")
                            f.write(mermaid_template % m)
                            f.write("\n\n")

print("Generated operations.md")
