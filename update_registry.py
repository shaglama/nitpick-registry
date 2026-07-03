import json
import os

registry_path = '/home/randy/Workspace/REPOS/nitpick-registry/registry.json'

with open(registry_path, 'r') as f:
    data = json.load(f)

new_packages = [
    {
        "name": "nsemver",
        "version": "1.0.0",
        "description": "Native Semantic Versioning parsing for Nitpick.",
        "url": "https://ai-lp.org/nsemver-1.0.0.npkpkg",
        "keywords": ["utility", "version", "semver"]
    },
    {
        "name": "nlog",
        "version": "1.0.0",
        "description": "Native structured logging for Nitpick.",
        "url": "https://ai-lp.org/nlog-1.0.0.npkpkg",
        "keywords": ["utility", "log", "logging"]
    }
]

# Remove existing nsemver/nlog if any
data['packages'] = [p for p in data['packages'] if p['name'] not in ['nsemver', 'nlog']]

# Add new packages
data['packages'].extend(new_packages)

with open(registry_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Registry updated with nsemver and nlog")
