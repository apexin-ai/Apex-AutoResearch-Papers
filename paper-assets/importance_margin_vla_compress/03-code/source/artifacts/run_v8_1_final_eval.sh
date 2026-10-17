#!/bin/bash
set -e
GPU=${1:-0}

cd /root/autodl-tmp/importance_margin_vla_compress
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo 2>/dev/null || true
export PYTHONUNBUFFERED=1
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export HF_HUB_DISABLE_XET=1

CKPT=checkpoints/imm_anchor_v8_1/latest
CONFIG=configs/imm_anchor_v8_1.yaml
VERSION=v8_1
BASELINE_LOSS=0.004077

if [ ! -d "$CKPT" ] && [ ! -f "$CKPT" ]; then
    echo "ERROR: Checkpoint not found: $CKPT"
    echo "Training may not be complete yet. Check: ls checkpoints/imm_anchor_v8_1/"
    exit 1
fi

mkdir -p eval_results

# Train-mode wrapper: use soft forward instead of hard binary mask
cat > /tmp/_eval_train_mode.py << 'WRAPPER'
import evaluate
_orig = evaluate.load_model_and_checkpoint
def _patched(*a, **kw):
    m, e = _orig(*a, **kw)
    m.train()
    return m, e
evaluate.load_model_and_checkpoint = _patched
evaluate.main()
WRAPPER

echo "=== Phase 1: Standard Eval (500 batches, train mode) ==="
CUDA_VISIBLE_DEVICES=$GPU python3 /tmp/_eval_train_mode.py \
  --checkpoint $CKPT --config $CONFIG \
  --gpu 0 --max_batches 500 --seed 42 \
  --output eval_results/eval_imm_${VERSION}_standard.json

echo "=== Phase 2: Bypass-ACIS Eval (500 batches, train mode) ==="
CUDA_VISIBLE_DEVICES=$GPU python3 /tmp/_eval_train_mode.py \
  --checkpoint $CKPT --config $CONFIG \
  --gpu 0 --max_batches 500 --seed 42 \
  --bypass_acis \
  --output eval_results/eval_imm_${VERSION}_bypass.json

echo "=== Phase 3: Extract ACIS-Prune JSON for Gate Analysis ==="
python3 << EXTRACT
import json

version = "$VERSION"
src = f"eval_results/eval_imm_{version}_standard.json"
dst = f"eval_results/eval_imm_{version}_acis_prune.json"

with open(src) as f:
    data = json.load(f)

out = {}
for k, v in data.items():
    if k.startswith("_"):
        out[k] = v
    elif "pruneTrue" in k:
        out[k.replace("pruneTrue", "pruneFalse")] = v
with open(dst, "w") as f:
    json.dump(out, f, indent=2)
print(f"Wrote {dst}")
EXTRACT

echo "=== Phase 4: Gate Analysis (G1-G4, baseline=$BASELINE_LOSS) ==="
python3 analyze_gate.py \
  --baseline eval_results/eval_baseline_v5_final.json \
  --imm eval_results/eval_imm_${VERSION}_standard.json \
  --acis-prune eval_results/eval_imm_${VERSION}_acis_prune.json \
  --bypass eval_results/eval_imm_${VERSION}_bypass.json \
  --output eval_results/gate_report_${VERSION}_final.json

echo ""
echo "=== Summary: All Conditions (clean action_loss) ==="
python3 << SUMMARY
import json

version = "$VERSION"
baseline = $BASELINE_LOSS

std = json.load(open(f"eval_results/eval_imm_{version}_standard.json"))
byp = json.load(open(f"eval_results/eval_imm_{version}_bypass.json"))

conditions = [
    ("standard (no prune)",  std, "eps0.0_pruneFalse"),
    ("ACIS+prune (50%)",     std, "eps0.0_pruneTrue"),
    ("bypass (no ACIS)",     byp, "eps0.0_pruneFalse"),
    ("random prune (50%)",   byp, "eps0.0_pruneTrue"),
]

print(f"{'Condition':<25} {'action_loss':>12} {'ratio vs bl':>12}")
print("-" * 51)
for name, data, key in conditions:
    loss = data.get(key, {}).get("action_loss")
    if loss is not None:
        print(f"{name:<25} {loss:>12.6f} {loss / baseline:>12.4f}")
    else:
        print(f"{name:<25} {'N/A':>12} {'N/A':>12}")
SUMMARY

echo ""
echo "=== DONE ==="
