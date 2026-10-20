# code plan019 multiseed prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan019_multiseed_prep_20260520T054528_result.json`
- **Structured JSON:** [`92fc0e774c019d8cc052.json`](../../sessions/92/92fc0e774c019d8cc052.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

| 脚本 | 路径 | seed | output-dir |
|------|------|------|------------|
| TG s123 | `scripts/launch_tg_s123.sh` | 123 | `runs/phase2_tg_s123_v7` |
| LoRA-only s123 | `scripts/launch_lora_s123.sh` | 123 | `runs/phase2_lora_only_s123` |

依赖验证通过：`train_phase2.py`、`data/ultrachat_8k`、模型路径均存在。GPU 空闲后在项目根目录执行 `bash scripts/launch_tg_s123.sh` 和 `bash scripts/launch_lora_s123.sh` 即可启动。

---
