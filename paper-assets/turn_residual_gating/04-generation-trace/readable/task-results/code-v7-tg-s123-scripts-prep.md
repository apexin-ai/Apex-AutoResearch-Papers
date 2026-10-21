# code v7 tg s123 scripts prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v7_tg_s123_scripts_prep_20260521T095152_result.json`
- **Structured JSON:** [`0fddd058b56c67ce55d5.json`](../../sessions/0f/0fddd058b56c67ce55d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both scripts pass syntax check.

---

## 汇报

### 1. v7 s42 原始训练配置

| Param | Value |
|---|---|
| script | `train_phase2.py` |
| gate-type | threadgate |
| gar-loss-mode | mse_target |
| gar-target | 0.5 |
| lambda-gar | 1.0 |
| lambda-gate-div | 1.0 |
| min-gate-std | 0.05 |
| init-bias | 1.5 |
| gate-lr-multiplier | 10 |
| max-seq-len | 2048 |
| seed | 42 |
| epochs | 3 |
| data-dir | data/ultrachat_8k |
| lr / batch-size / grad-accum | defaults in train_phase2.py |

### 2. s123 vs s42 diff

仅两处变更：
- `--seed 42` → `--seed 123`
- `--output-dir .../phase2_tg_s42_v7` → `--output-dir .../phase2_tg_s123_v7`

额外加了 `CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1`（原 s42 command 也有，只是没写进旧脚本）。

### 3. Eval 脚本结构

**4 conditions** (guarded):
- Base — 无 checkpoint
- LoRA-only s123 — `runs/phase2_lora_only_s123/`（guard: 不存在则 skip）
- TG v7 s123 — `runs/phase2_tg_s123_v7/`（auto-detect highest epoch）
- v8b-SS s123 — `checkpoints/tg_v8b_ss_s123/`（guard: 不存在则 skip）

**Each condition**: GAR-ours + GAR-Dongre, 共 2 variants

**Two modes**: TF (heldout data) + AR (built-in model-gen)

最多 16 eval runs（LoRA-only 或 v8b-SS 不存在则自动跳过）。

### 4. 使用命令

```bash
# 训练
bash scripts/launch_v7_tg_s123.sh

# Eval（训练完成后）
bash scripts/eval_v7_tg_s123.sh
```

---
