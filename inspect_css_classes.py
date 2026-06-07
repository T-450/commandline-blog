import re

with open('src/styles/global.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's write a script to find CSS blocks matching specific selectors
selectors = [
    r'\.blog-grid', r'\.blog-card', r'\.home-main', r'\.list-preview',
    r'\.list-header', r'\.view-grid', r'\.view-list'
]

for sel in selectors:
    print(f"=== Selector: {sel} ===")
    # Find all matches of selector followed by { ... }
    # Since CSS can be minified, let's look for the matching curly braces.
    pattern = re.compile(sel + r'[^{]*\{[^{}]*\}')
    for match in pattern.finditer(css):
        print(match.group())
    
    # Also look for nested or combined selectors
    pattern_comb = re.compile(sel + r'[^\{]*\{[^}]*\}')
    # Since there could be media queries, let's print lines matching the selector
    print("Lines containing selector:")
    for i, line in enumerate(css.splitlines()):
        if re.search(sel, line):
            # Print surrounding content or slice
            # To keep it readable:
            print(f"L{i+1}: {line[:120]}")
    print()
