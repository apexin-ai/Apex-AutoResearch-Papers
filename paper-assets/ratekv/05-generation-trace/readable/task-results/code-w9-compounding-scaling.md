# code w9 compounding scaling

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w9_compounding_scaling_20260515T050328_result.json`
- **Structured JSON:** [`255bad28e66d9128af1a.json`](../../sessions/25/255bad28e66d9128af1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交。

- 脚本：服务器 `/root/ratekv/run_w9_compounding_scaling.py` 与本地 md5 一致（`3915cd83...`，7959 bytes），无需重传
- 依赖：`eval_ppl.py:24 patch_attention` / `eval_ppl.py:122 restore_attention` 均存在；`hires_profiles.json`、`calibration_hires.json` 已就位；Qwen 模型 4-shard safetensors 完整
- 作业：tmux session `w9_compounding_scaling`，PID 291410，GPU cuda:1（物理 GPU 1 → 脚本内 cuda:0），日志 `~/runs/ratekv/w9_compounding_scaling.log`

---
