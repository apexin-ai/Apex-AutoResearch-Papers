# code gsm8k eval scripts prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k-eval-scripts-prep_20260520T052206_result.json`
- **Structured JSON:** [`f3b049ac8e0a7af8c2eb.json`](../../sessions/f3/f3b049ac8e0a7af8c2eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本创建完成。

### 产出汇总

**脚本路径：**
- `/root/contamcal-irt-calibration/scripts/gsm8k_s42/run_gsm8k_qwen14b_s42.sh`
- `/root/contamcal-irt-calibration/scripts/gsm8k_s42/run_gsm8k_gemma2_s42.sh`

**脚本结构（与参考模板一致）：**
- C009 evaluate.py md5 校验（hash: `001a9bc23f808c47d25ef9eaeecb81f1`）
- `CUDA_VISIBLE_DEVICES=0`（启动前按实际 GPU 修改）
- 离线模式 + HF_HOME 设置
- `run_eval` 函数自动检查 adapter 存在性，不存在则 SKIP
- Dosages: d000 + d100

**Checkpoint 状态（全部存在）：**

| Checkpoint | 路径 | 状态 |
|---|---|---|
| Qwen2.5-14B d000 s42 | `checkpoints/Qwen2.5-14B_d000_s42/lora_adapter/` | OK (May 18) |
| Qwen2.5-14B d100 s42 | `checkpoints/Qwen2.5-14B_d100_s42/lora_adapter/` | OK (May 19) |
| gemma-2-9b d000 s42 | `checkpoints/gemma-2-9b_d000_s42/lora_adapter/` | OK (May 19) |
| gemma-2-9b d100 s42 | `checkpoints/gemma-2-9b_d100_s42/lora_adapter/` | OK (May 19) |

**C006 验证：** 两个模型 lora_alpha=32，非废弃 checkpoint。

**基础模型路径：** `/root/autodl-tmp/models/Qwen2.5-14B`、`/root/autodl-tmp/models/gemma-2-9b`（均存在）。

**注意：** 任务路径给的是 `sft_output/`，实际 checkpoint 在 `checkpoints/.../lora_adapter/`，脚本已按实际路径编写。启动前需按 C001/C002/C004 确认目标 GPU 空闲并修改 `CUDA_VISIBLE_DEVICES`。

---
