# Falcon3-7B GSM8K Eval Commands (cqa1-21977)

## 前提条件

- **d100_s42**: ✅ checkpoint 已就绪 (`/root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_d100_s42/lora_adapter/`, alpha=32)
- **d000_s42**: ❌ checkpoint 不在 cqa1 上，需先从源服务器传输
- **Base model**: ✅ `/root/autodl-tmp/.hf_cache/Falcon3-7B-Base`
- **GSM8K dataset**: ✅ 已缓存
- **evaluate.py md5**: `001a9bc23f808c47d25ef9eaeecb81f1`

## d100 GSM8K Eval（可直接启动）

```bash
#!/bin/bash
set -e

# AutoDL network proxy
source /etc/network_turbo 2>/dev/null || true

# C009: evaluate.py md5 verification
EXPECTED_MD5="001a9bc23f808c47d25ef9eaeecb81f1"
ACTUAL_MD5=$(md5sum /root/contamcal-irt-calibration/exp001/evaluate.py | cut -d' ' -f1)
if [ "$ACTUAL_MD5" != "$EXPECTED_MD5" ]; then
  echo "ERROR: evaluate.py md5 mismatch! Expected $EXPECTED_MD5, got $ACTUAL_MD5"
  exit 1
fi

# C004: explicit CUDA device — 根据 S4 完成后的空闲 GPU 修改
export CUDA_VISIBLE_DEVICES=0

# AutoDL env
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

EVAL_SCRIPT="/root/contamcal-irt-calibration/exp001/evaluate.py"
BASE_MODEL="/root/autodl-tmp/.hf_cache/Falcon3-7B-Base"
ADAPTER="/root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_d100_s42/lora_adapter"
RESULTS_DIR="/root/contamcal-irt-calibration/results/gsm8k"
OUT_DIR="${RESULTS_DIR}/falcon3_d100_s42"

mkdir -p "$OUT_DIR"

echo "=== $(date): Evaluating Falcon3-7B d100 s42 on GSM8K ==="
python3 "$EVAL_SCRIPT" \
    --model-path "$BASE_MODEL" \
    --adapter-path "$ADAPTER" \
    --benchmarks gsm8k \
    --batch-size 8 \
    --output-dir "$OUT_DIR" \
    --cache-dir "$HF_HOME"

touch "${OUT_DIR}/.done"
echo "=== $(date): DONE Falcon3-7B d100 s42 GSM8K ==="
```

## d000 GSM8K Eval（需先传输 checkpoint）

d000 checkpoint 不在 cqa1 上。传输完成后使用以下命令：

```bash
#!/bin/bash
set -e

source /etc/network_turbo 2>/dev/null || true

EXPECTED_MD5="001a9bc23f808c47d25ef9eaeecb81f1"
ACTUAL_MD5=$(md5sum /root/contamcal-irt-calibration/exp001/evaluate.py | cut -d' ' -f1)
if [ "$ACTUAL_MD5" != "$EXPECTED_MD5" ]; then
  echo "ERROR: evaluate.py md5 mismatch! Expected $EXPECTED_MD5, got $ACTUAL_MD5"
  exit 1
fi

export CUDA_VISIBLE_DEVICES=0
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

EVAL_SCRIPT="/root/contamcal-irt-calibration/exp001/evaluate.py"
BASE_MODEL="/root/autodl-tmp/.hf_cache/Falcon3-7B-Base"
ADAPTER="/root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_d000_s42/lora_adapter"
RESULTS_DIR="/root/contamcal-irt-calibration/results/gsm8k"
OUT_DIR="${RESULTS_DIR}/falcon3_d000_s42"

mkdir -p "$OUT_DIR"

echo "=== $(date): Evaluating Falcon3-7B d000 s42 on GSM8K ==="
python3 "$EVAL_SCRIPT" \
    --model-path "$BASE_MODEL" \
    --adapter-path "$ADAPTER" \
    --benchmarks gsm8k \
    --batch-size 8 \
    --output-dir "$OUT_DIR" \
    --cache-dir "$HF_HOME"

touch "${OUT_DIR}/.done"
echo "=== $(date): DONE Falcon3-7B d000 s42 GSM8K ==="
```

## 启动前 Checklist

1. `nvidia-smi` 确认目标 GPU 空闲（C001/C002）
2. `CUDA_VISIBLE_DEVICES` 设为空闲 GPU 编号（C004）
3. d000 checkpoint 需先从源服务器传输到 cqa1
4. 传输后验证：`cat /root/autodl-tmp/exp001/checkpoints/Falcon3-7B-Base_d000_s42/lora_adapter/adapter_config.json | grep lora_alpha`（C006: 必须 =32）

## 运行时间估算

- GSM8K test set: 1319 items
- 8-shot CoT, max_new_tokens=256, batch_size=8
- 7B model 单 GPU 预估: ~30-45 分钟/dosage
- d000 + d100 合计: ~60-90 分钟
