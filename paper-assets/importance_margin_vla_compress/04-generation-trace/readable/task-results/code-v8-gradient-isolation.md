# code v8 gradient isolation

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v8-gradient-isolation_20260515T230802_result.json`
- **Structured JSON:** [`a8449d46df68e986580a.json`](../../sessions/a8/a8449d46df68e986580a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成报告

### 修改的文件

**1. `imm/smolvla_wrapper.py`** — 3 处改动：
- **L96**: `__init__` 中 pop `gradient_isolation` flag（默认 False，向后兼容）
- **L246-248**: `forward()` 中 ACIS 输入三重 detach：
  - `vis_tokens.detach()` — 阻断 margin_loss → SigLIP/connector 权重
  - `suffix_embs.detach()` — 阻断 margin_loss → action_in_proj/action_time_mlp LoRA 权重
  - `importance_scores = self.acis(suffix_for_acis, vis_for_acis)`
- **L252**: `importance_scores.detach()` 传给 `token_selector` — 阻断 action_loss → ACIS 权重

**2. `train.py`** — 1 处改动：
- **L318**: `wrap_with_imm` 中传递 `gradient_isolation` 到 `IMMSmolVLAWrapper`

**3. `configs/imm_anchor_v8.yaml`** — 新建：
- `gradient_isolation: true`, `lambda_margin: 0.5`, `delta: 0.3`, `grad_clip: 10.0`, `save_every: 2000`, `eval_every: 999999`, `total_steps: 30000`

### Gradient isolation 验证结果

| 检查项 | 结果 |
|--------|------|
| margin_loss → backbone LoRA (74 params) | **PASS** — blocked |
| action_loss → ACIS (10 params) | **PASS** — blocked |
| action_loss → backbone LoRA (sanity) | **PASS** — 梯度正常流通 |
| margin_loss → ACIS (sanity) | **PASS** — 梯度正常流通 |
| eval mode forward | **PASS** — 无 crash |

### Dry-run loss 值

- `action_loss = 0.276998`
- `margin_loss = 0.297578`
- `total_loss = 0.425787`（step=5000, lambda warmup 后）

### 启动命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp/importance_margin_vla_compress && \
source /etc/network_turbo && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && \
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && \
CUDA_VISIBLE_DEVICES=0,1 python train.py \
  --config configs/imm_anchor_v8.yaml \
  --wandb_run imm-anchor-v8-grad-isolation
```

---
