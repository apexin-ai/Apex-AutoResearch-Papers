# code aligned eval 15B script

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_aligned-eval-15B-script_20260514T083726_result.json`
- **Structured JSON:** [`98f841a29898db0076ae.json`](../../sessions/98/98f841a29898db0076ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已部署并通过语法检查：

- `/root/contamcal-irt-calibration/exp001/run_aligned_eval_15B.sh` — 包含 d000/d005/d100 三个 dosage，所有 checkpoint 和 lora_adapter 目录均已确认存在
- `/root/contamcal-irt-calibration/exp001/run_aligned_eval_3B.sh` — d000_s42 和 d100_s42 的 checkpoint 已存在，d005_s42 尚未训练，脚本会自动跳过（WARN + continue）

两个脚本均保持 `--mc-format aligned`，支持 `original|paraphrase|both` 模式。

---
