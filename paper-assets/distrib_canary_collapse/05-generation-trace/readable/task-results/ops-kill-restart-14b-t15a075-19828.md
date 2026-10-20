# ops kill restart 14b t15a075 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-restart-14b-t15a075-19828_20260522T123031_result.json`
- **Structured JSON:** [`609c69131f92ff15038c.json`](../../sessions/60/609c69131f92ff15038c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**总结：**
- Zombie PID 791123 已 kill，清理了 5 个 orphan 下载进程
- 发现 pythia-1.4b-deduped 模型已存在于 `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b-deduped/`（t10_a050_v2 使用的直接路径），跳过下载
- 实验已在 tmux session `scale_14b_t15_a075` 重启，**PID 793171**，cuda:0 占用 10.3GB
- 正在运行 Generation 0 (baseline)
- Registry 已更新（model_name 改为 deduped，新 PID/log_path）

---
