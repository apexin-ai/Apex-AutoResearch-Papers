import base64, sys, json, os
data = json.loads(sys.stdin.read())
for name, b64 in data.items():
    path = os.path.join('/root/spectral_optim_vision_geometry/paper', name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as f:
        f.write(base64.b64decode(b64))
    print(f'Wrote {name} ({os.path.getsize(path)} bytes)')
