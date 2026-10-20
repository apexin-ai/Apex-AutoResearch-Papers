# ssh patch mean probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_patch-mean-probe_20260516T022703_result.json`
- **Structured JSON:** [`2bae298c8928af6332b8.json`](../../sessions/2b/2bae298c8928af6332b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Action Probe R²（超参完全一致）

| Model | feature_key | R² (mean) |
|-------|-----------|-----------|
| CLIP | cls_token | 0.587 |
| CLIP | **patch_mean** | **0.591** |
| DINO | cls_token | 0.634 |
| DINO | **patch_mean** | **0.631** |
| SigLIP projector | — | 0.630 |

patch_mean vs cls_token 差异不显著（CLIP: p=0.644, DINO: p=0.620）。

### DINO RSA 确认

**DINO RSA=0.388 用的是 `cls_token`**，但来自与 `rsa_clip.py` 不同的 RSA 方法论（rsa_results.json 中的框架）。用 rsa_clip.py **同一方法**重算：

| Model | feature_key | RSA |
|-------|-----------|-----|
| CLIP | cls_token | 0.506 |
| CLIP | patch_mean | 0.557 |
| DINO | cls_token | **0.692** |
| DINO | patch_mean | **0.631** |
| SigLIP projector | — | 0.615 |

### Table 1 公平对比表（同一 feature key = patch_mean，同一 RSA 方法）

| Model | feature_key | RSA | R² |
|-------|-----------|-----|-----|
| CLIP | patch_mean | 0.557 | 0.591 |
| DINO | patch_mean | 0.631 | 0.631 |
| SigLIP projector | — | 0.615 | 0.630 |

### 注意

DINO RSA 用 rsa_clip.py 同一方法重算后（0.631 patch_mean / 0.692 cls_token），**远高于**之前引用的 0.388。这意味着 Table 1 中的 DINO RSA 值需要更新，否则低估了 DINO 的 action-alignment 能力。建议确认论文中引用的 DINO RSA=0.388 是否应替换为 0.631（patch_mean，与 CLIP 同方法同 feature key）。

### Bootstrap 关键结论
- CLIP patch_mean 显著低于 DINO patch_mean（Δ=-0.040, p=0.0002）和 projector（Δ=-0.039, p<0.001）
- DINO patch_mean 与 projector 无显著差异（Δ=+0.001, p=0.911）

---
