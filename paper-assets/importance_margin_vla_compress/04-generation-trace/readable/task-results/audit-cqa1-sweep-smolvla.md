# audit cqa1 sweep smolvla

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cqa1-sweep-smolvla_20260521T150250_result.json`
- **Structured JSON:** [`78f4d5a0b8736277aae3.json`](../../sessions/78/78f4d5a0b8736277aae3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总如下：

---

## Part 1: X-VLA 实验状态

| 实验 | GPU | 状态 | SR | Episodes | Wilson CI 95% |
|------|-----|------|------|----------|---------------|
| `eval_xvla_l2norm_k03_object_seed44` | GPU0 | **RUNNING** (task 8/10, ep 8/50) | — | — | — |
| `eval_xvla_random_k085_object_seed42_v2` | GPU1 | **DONE** | **63.6%** | 500 | [59.3, 67.7] |
| `eval_xvla_random_k085_object_seed43` | GPU2 | **DONE** | **63.2%** | 500 | [58.9, 67.3] |
| `eval_xvla_random_k07_object_seed42_v2` | GPU3 | **DONE** | **65.2%** | 500 | [60.9, 69.3] |

- seed43 结果文件原在错误路径 `/root/eval_results/`，已移至正确位置
- l2norm_k0.3_seed44 预计还需 ~30-40 min 完成（剩余 task 8 剩 42 ep + task 9-10）

**空闲 GPU: GPU1, GPU2, GPU3**

---

## Part 2: SmolVLA 环境探测

**脚本**:
- `eval_random_prune_smolvla.py` — 支持参数: `--k_ratio`, `--episodes_per_task`, `--max_steps`, `--action_horizon`, `--output_name`, `--seed`。使用 `RandomPruner` + `true_removal` 方法，硬编码 checkpoint: `checkpoints/libero_full_ft/step_099999/checkpoint.pt`
- `eval_random_prune_smolvla_spatial.py` — spatial suite 版本
- `analyze_smolvla_importance_cv.py` — importance CV 分析
- `measure_smolvla_entropy_perlayer.py` / `_fixed.py` — 逐层 entropy 测量

**Checkpoints 已下载**:
- `smolvla_base` → `/root/autodl-tmp/.hf_cache/lerobot/smolvla_base`
- `smolvla_libero` → `/root/autodl-tmp/.hf_cache/hub/models--HuggingFaceVLA--smolvla_libero`
- `smolvla_libero_official` → `/root/autodl-tmp/.hf_cache/smolvla_libero_official`

**磁盘**: 75GB 可用 (250GB 用了 176GB, 71%)

**局限**: 现有 `eval_random_prune_smolvla.py` 只支持 random pruning（无 `--mode` 参数）。如需 Official Checkpoint Pruning Sweep 支持多种 mode（l2_norm, importance 等），需要新增或改造脚本。

---
