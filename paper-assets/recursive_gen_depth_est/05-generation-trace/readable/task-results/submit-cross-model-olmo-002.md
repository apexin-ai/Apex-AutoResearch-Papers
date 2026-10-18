# submit cross model olmo 002

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_cross_model_olmo_002_20260514T163144_result.json`
- **Structured JSON:** [`1f36c64bcd2bafc8fb9a.json`](../../sessions/1f/1f36c64bcd2bafc8fb9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`cross_model_olmo_002` 已提交并标记为 RUNNING。

**汇总：**
- 服务器：`autodl-rtx6000`（即 westb-52439）
- GPU：cuda:0，显存 20.2/97.9 GB
- tmux session：`olmo_002`，PID 150550
- 日志：`/root/autodl-tmp/recursive_gen_depth_est/logs/pipeline_olmo_002.log`
- Depth-0 LoRA finetune 正在训练中（939 steps，~2.5 it/s，预计 ~6 min）
- 注册表已更新为 RUNNING

注意：cuda:0 上有 `pythia_temp09` 的 `extract_features.py` 残留进程（7.8 GB），但 96GB 显存足够容纳两个进程，不影响训练。

---
