# code submit olmo temp09

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_submit_olmo_temp09_20260514T182428_result.json`
- **Structured JSON:** [`9db9e5365ea15d2c7fa0.json`](../../sessions/9d/9db9e5365ea15d2c7fa0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 被 Pythia topk50 占用，无法提交 OLMo temp09。**

当前状态：
- **cuda:0**: PID 165810, 11614 MiB, tmux session `pythia_topk50_001`（Pythia topk50 实验正在运行）
- **cuda:1**: PID 166612, 7872 MiB，也被占用

其他先决条件均已就绪：
- 脚本 `run_pipeline_olmo_temp09.sh` 存在
- 数据 `depth_0.jsonl` 5000 条
- nucleus adapter (`olmo/lora_depth_0/`) 就绪
- Registry 中尚无 `olmo_temp09_001`，提交时需先创建

等 Pythia topk50 跑完释放 cuda:0 后即可提交。

---
