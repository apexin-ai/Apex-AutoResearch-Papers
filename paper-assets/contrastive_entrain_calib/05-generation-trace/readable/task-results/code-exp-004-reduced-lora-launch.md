# code exp 004 reduced lora launch

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-004-reduced-lora-launch_20260522T161557_result.json`
- **Structured JSON:** [`2465e5747ccdb5619453.json`](../../sessions/24/2465e5747ccdb5619453.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training confirmed running. Step 10 logged at 72s.

**汇报：**

- **脚本路径**: `/root/contrastive_entrain_calib/training/run_exp004_reduced_lora.py` (28034)
- **PID**: 30006 (tmux wrapper) / 30011 (python process on GPU 1)
- **Log**: `~/runs/contrastive_entrain_calib/exp-004-reduced-lora.log`
- **Output**: `/root/autodl-tmp/outputs/exp-004-reduced-lora/`

**Diff 确认（仅改 3 处，其他不变）**：
1. `lora_alpha`: `args.lora_rank * 2` (128) → `args.lora_rank` (64) ✓
2. `target_modules`: 7 个 → 4 个 `["q_proj", "k_proj", "v_proj", "o_proj"]` ✓
3. `output_dir`: → `/root/autodl-tmp/outputs/exp-004-reduced-lora` ✓

**其他参数不变确认**：
- `r=64`, `seed=42`, `lr=5e-5`, `lambda_l2=0.1`, `max_steps=8000`, `save_steps=500`, `grad_accum=16`, `warmup_steps=200`
- Loss: `sft_loss + 0.1 * l2_loss`（不变）
- Data: `calibration_v2_1_expanded.jsonl`（181 pairs，不变）

Step 10: sft=2.5445, l2=2.365277, total=2.7810

---
