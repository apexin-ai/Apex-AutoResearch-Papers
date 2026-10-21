import os
import sys
import time
import shutil
from modelscope import snapshot_download

MODELS = [
    "m-a-p/340M-20B-GatedDeltaNet-pure-baseline",
    "m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1",
    "m-a-p/340M-20B-GatedDeltaNet-hybrid-12-1",
    "m-a-p/340M-20B-GatedDeltaNet-hybrid-6-1",
    "m-a-p/340M-20B-GatedDeltaNet-hybrid-3-1",
    "m-a-p/340M-20B-HGRN2-pure-baseline",
    "m-a-p/340M-20B-HGRN2-hybrid-24-1",
    "m-a-p/340M-20B-HGRN2-hybrid-12-1",
    "m-a-p/340M-20B-HGRN2-hybrid-6-1",
    "m-a-p/340M-20B-HGRN2-hybrid-3-1",
    "m-a-p/340M-20B-RetNet-pure",
    "m-a-p/340M-20B-RetNet-hybrid-24-1",
    "m-a-p/340M-20B-RetNet-hybrid-12-1",
    "m-a-p/340M-20B-RetNet-hybrid-6-1",
    "m-a-p/340M-20B-RetNet-hybrid-3-1",
    "m-a-p/transformer_340M_baseline",
]

BASE_DIR = os.environ.get("MODEL_DIR", "./models")
CACHE_DIR = os.environ.get("CACHE_DIR", "./.ms_cache")
results = []

for i, repo_id in enumerate(MODELS):
    model_name = repo_id.split("/")[1]
    target_dir = os.path.join(BASE_DIR, model_name)

    # skip if already complete
    if os.path.exists(os.path.join(target_dir, "config.json")) and \
       any(f.endswith(".safetensors") for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f))):
        print(f"[{i+1}/{len(MODELS)}] SKIP: {model_name}", flush=True)
        results.append((model_name, "OK", 0))
        continue

    print(f"[{i+1}/{len(MODELS)}] Downloading: {repo_id}", flush=True)
    t0 = time.time()
    try:
        cache_path = snapshot_download(repo_id, cache_dir=CACHE_DIR)
        elapsed = time.time() - t0

        # Copy files to target dir
        os.makedirs(target_dir, exist_ok=True)
        for f in os.listdir(cache_path):
            src = os.path.join(cache_path, f)
            dst = os.path.join(target_dir, f)
            if os.path.isfile(src):
                if not os.path.exists(dst):
                    shutil.copy2(src, dst)

        has_config = os.path.exists(os.path.join(target_dir, "config.json"))
        has_st = any(f.endswith(".safetensors") for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f)))
        status = "OK" if (has_config and has_st) else "INCOMPLETE"
        print(f"  {status} ({elapsed:.0f}s)", flush=True)
        results.append((model_name, status, elapsed))
    except Exception as e:
        elapsed = time.time() - t0
        print(f"  FAILED: {e}", flush=True)
        results.append((model_name, f"FAILED: {e}", elapsed))

# cleanup cache to save disk
shutil.rmtree(CACHE_DIR, ignore_errors=True)

print("\n" + "="*60, flush=True)
print("SUMMARY", flush=True)
print("="*60, flush=True)
ok = fail = 0
for name, status, elapsed in results:
    tag = "OK" if status == "OK" else "FAIL"
    print(f"  [{tag:4s}] {name} ({elapsed:.0f}s)", flush=True)
    if status == "OK": ok += 1
    else: fail += 1
print(f"\n{ok} OK, {fail} failed", flush=True)
print("DONE", flush=True)
