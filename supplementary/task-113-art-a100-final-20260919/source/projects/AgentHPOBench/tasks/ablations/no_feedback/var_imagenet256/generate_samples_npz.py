import os
import sys
import time
import zipfile
from pathlib import Path

import numpy as np
import torch

setattr(torch.nn.Linear, "reset_parameters", lambda self: None)
setattr(torch.nn.LayerNorm, "reset_parameters", lambda self: None)

ROOT = Path(".")
REPO = ROOT / "repositories/VAR"
CKPT = ROOT / "data/paper_exact/var_imagenet256/checkpoints"
OUT_DIR = ROOT / "data/paper_exact/var_imagenet256/samples"
OUT_DIR.mkdir(parents=True, exist_ok=True)

NPY = OUT_DIR / "var_d16_cfg1.5_topk900_topp0.96_50k.npy"
NPZ = OUT_DIR / "var_d16_cfg1.5_topk900_topp0.96_50k.npz"
STATUS = OUT_DIR / "var_d16_cfg1.5_topk900_topp0.96_50k.progress"

os.chdir(REPO)
sys.path.insert(0, str(REPO))
from models import build_vae_var  # noqa: E402

MODEL_DEPTH = 16
PATCH_NUMS = (1, 2, 3, 4, 5, 6, 8, 10, 13, 16)
SAMPLES_PER_CLASS = int(os.environ.get("VAR_SAMPLES_PER_CLASS", "50"))
NUM_CLASSES = int(os.environ.get("VAR_NUM_CLASSES", "1000"))
CFG = float(os.environ.get("VAR_CFG", "1.5"))
TOP_K = int(os.environ.get("VAR_TOP_K", "900"))
TOP_P = float(os.environ.get("VAR_TOP_P", "0.96"))
BASE_SEED = int(os.environ.get("VAR_BASE_SEED", "0"))

torch.backends.cudnn.allow_tf32 = True
torch.backends.cuda.matmul.allow_tf32 = True
torch.set_float32_matmul_precision("high")

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"device={device} samples={NUM_CLASSES * SAMPLES_PER_CLASS}", flush=True)

vae, var = build_vae_var(
    V=4096,
    Cvae=32,
    ch=160,
    share_quant_resi=4,
    device=device,
    patch_nums=PATCH_NUMS,
    num_classes=1000,
    depth=MODEL_DEPTH,
    shared_aln=False,
)
vae.load_state_dict(torch.load(CKPT / "vae_ch160v4096z32.pth", map_location="cpu"), strict=True)
var.load_state_dict(torch.load(CKPT / "var_d16.pth", map_location="cpu"), strict=True)
vae.eval()
var.eval()
for param in vae.parameters():
    param.requires_grad_(False)
for param in var.parameters():
    param.requires_grad_(False)

shape = (NUM_CLASSES * SAMPLES_PER_CLASS, 256, 256, 3)
arr = np.lib.format.open_memmap(NPY, mode="w+", dtype=np.uint8, shape=shape)
start_time = time.time()

with torch.inference_mode():
    for cls in range(NUM_CLASSES):
        labels = torch.full((SAMPLES_PER_CLASS,), cls, dtype=torch.long, device=device)
        with torch.autocast("cuda", enabled=(device == "cuda"), dtype=torch.float16, cache_enabled=True):
            recon = var.autoregressive_infer_cfg(
                B=SAMPLES_PER_CLASS,
                label_B=labels,
                cfg=CFG,
                top_k=TOP_K,
                top_p=TOP_P,
                g_seed=BASE_SEED + cls,
                more_smooth=False,
            )
        images = recon.permute(0, 2, 3, 1).mul(255).clamp_(0, 255).to(torch.uint8).cpu().numpy()
        lo = cls * SAMPLES_PER_CLASS
        hi = lo + SAMPLES_PER_CLASS
        arr[lo:hi] = images
        if cls % 10 == 0 or cls == NUM_CLASSES - 1:
            arr.flush()
            elapsed = time.time() - start_time
            message = f"class={cls + 1}/{NUM_CLASSES} samples={hi}/{shape[0]} elapsed_sec={elapsed:.1f}"
            STATUS.write_text(message + "\n")
            print(message, flush=True)

arr.flush()
print(f"npy_done={NPY} size={NPY.stat().st_size}", flush=True)

if NPZ.exists():
    NPZ.unlink()
with zipfile.ZipFile(NPZ, "w", compression=zipfile.ZIP_STORED, allowZip64=True) as zf:
    zf.write(NPY, arcname="arr_0.npy")
print(f"npz_done={NPZ} size={NPZ.stat().st_size}", flush=True)
