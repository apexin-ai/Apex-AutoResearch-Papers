import os
import time
import json
import subprocess
import concurrent.futures

for k in ["http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY",
          "REQUESTS_CA_BUNDLE", "SSL_CERT_FILE"]:
    os.environ.pop(k, None)

MIRROR = "https://hf-mirror.com"
SAVE_DIR = os.environ.get("MODEL_DIR", "./models_1.3b")
CHUNK_SIZE = 100 * 1024 * 1024  # 100MB chunks
MAX_WORKERS = 8

MODELS = [
    "m-a-p/1.3B-100B-GatedDeltaNet-pure",
    "m-a-p/1.3B-100B-GatedDeltaNet-hybrid-24-1",
    "m-a-p/1.3B-100B-GatedDeltaNet-hybrid-12-1",
    "m-a-p/1.3B-100B-GatedDeltaNet-hybrid-6-1",
    "m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1",
    "m-a-p/1.3B-100B-HGRN2-pure",
    "m-a-p/1.3B-100B-HGRN2-hybrid-24-1",
    "m-a-p/1.3B-100B-HGRN2-hybrid-12-1",
    "m-a-p/1.3B-100B-HGRN2-hybrid-6-1",
    "m-a-p/1.3B-100B-HGRN2-hybrid-3-1",
    "m-a-p/1.3B-100B-RetNet-pure",
    "m-a-p/1.3B-100B-RetNet-hybrid-24-1",
    "m-a-p/1.3B-100B-RetNet-hybrid-12-1",
    "m-a-p/1.3B-100B-RetNet-hybrid-6-1",
    "m-a-p/1.3B-100B-RetNet-hybrid-3-1",
    "m-a-p/transformer_1.3B_baseline",
]


def curl_json(url):
    r = subprocess.run(["curl", "-s", "-f", url], capture_output=True, timeout=30)
    return json.loads(r.stdout)


def resolve_url(url):
    """Follow redirects, return the final URL and Content-Length."""
    r = subprocess.run(
        ["curl", "-sI", "-L", "-o", "/dev/null", "-w",
         "%{url_effective}\\n%{size_download}\\n%{content_type}",
         url],
        capture_output=True, timeout=30
    )
    final_url = r.stdout.decode().split('\n')[0].strip()

    # Get content-length from the final URL
    r2 = subprocess.run(["curl", "-sI", final_url], capture_output=True, timeout=30)
    for line in r2.stdout.decode().split('\n'):
        if line.lower().startswith('content-length:'):
            return final_url, int(line.split(':')[1].strip())
    return final_url, 0


def download_chunk(args):
    direct_url, start, end, output_path = args
    for attempt in range(3):
        try:
            subprocess.run(
                ["curl", "-s", "-f", "-r", f"{start}-{end}", "-o", output_path,
                 "--connect-timeout", "30", "--max-time", "300", direct_url],
                check=True, timeout=360
            )
            expected = end - start + 1
            actual = os.path.getsize(output_path)
            if actual == expected:
                return True
        except Exception:
            pass
        if attempt < 2:
            time.sleep(2)
    return False


def parallel_download_file(url, dest_path, desc=""):
    direct_url, file_size = resolve_url(url)
    
    if file_size == 0 or file_size < CHUNK_SIZE:
        subprocess.run(
            ["curl", "-s", "-f", "-L", "-o", dest_path, url],
            check=True, timeout=600
        )
        return True

    chunks = []
    for start in range(0, file_size, CHUNK_SIZE):
        end = min(start + CHUNK_SIZE - 1, file_size - 1)
        chunk_path = f"{dest_path}.part{start}"
        chunks.append((direct_url, start, end, chunk_path))

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(executor.map(download_chunk, chunks))

    if not all(results):
        for _, _, _, cp in chunks:
            try: os.remove(cp)
            except: pass
        return False

    with open(dest_path, 'wb') as out:
        for _, start, _, chunk_path in sorted(chunks, key=lambda x: x[1]):
            with open(chunk_path, 'rb') as inp:
                while True:
                    data = inp.read(8 * 1024 * 1024)
                    if not data:
                        break
                    out.write(data)
            os.remove(chunk_path)

    actual = os.path.getsize(dest_path)
    if actual != file_size:
        print(f"    SIZE MISMATCH {desc}: expected {file_size}, got {actual}", flush=True)
        os.remove(dest_path)
        return False
    return True


def download_model(model_id, local_dir):
    os.makedirs(local_dir, exist_ok=True)
    info = curl_json(f"{MIRROR}/api/models/{model_id}")
    files = [s["rfilename"] for s in info.get("siblings", [])]

    for fname in files:
        if fname == ".gitattributes":
            continue
        dest = os.path.join(local_dir, fname)
        if os.path.exists(dest):
            continue
        url = f"{MIRROR}/{model_id}/resolve/main/{fname}"

        t0 = time.time()
        ok = parallel_download_file(url, dest, desc=fname)
        dt = time.time() - t0
        size_mb = os.path.getsize(dest) / (1024 * 1024) if ok and os.path.exists(dest) else 0

        if ok:
            print(f"    {fname}: {size_mb:.0f}MB in {dt:.0f}s ({size_mb/max(dt,1):.1f} MB/s)", flush=True)
        else:
            print(f"    FAILED: {fname}", flush=True)
            return False
    return True


ok, skip, fail = 0, 0, 0
for i, model_id in enumerate(MODELS, 1):
    local_name = model_id.split("/")[-1]
    local_dir = os.path.join(SAVE_DIR, local_name)

    if os.path.exists(os.path.join(local_dir, "config.json")) and \
       any(f.endswith(".safetensors") for f in os.listdir(local_dir) if not f.startswith('.')):
        print(f"[{i}/16] SKIP (exists): {local_name}", flush=True)
        skip += 1
        continue

    print(f"[{i}/16] Downloading: {model_id}", flush=True)
    t0 = time.time()
    try:
        success = download_model(model_id, local_dir)
        dt = time.time() - t0
        if success:
            print(f"[{i}/16] OK: {local_name} ({dt:.0f}s)", flush=True)
            ok += 1
        else:
            print(f"[{i}/16] FAILED: {local_name}", flush=True)
            fail += 1
    except Exception as e:
        print(f"[{i}/16] FAILED: {local_name}: {e}", flush=True)
        fail += 1

print(f"\nSummary: {ok} downloaded, {skip} skipped, {fail} failed", flush=True)
print("Done.", flush=True)
