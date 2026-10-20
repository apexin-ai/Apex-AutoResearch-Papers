# verify vota v4 gpu1 launch

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_vota-v4-gpu1-launch_20260514T222145_result.json`
- **Structured JSON:** [`2133f8855bb708259172.json`](../../sessions/21/2133f8855bb708259172.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态
- **cuda:0**: 75,623 MiB / 97,887 MiB，GPU-Util 100%，PID 835089 (python)
- **cuda:1**: 41,077 MiB / 97,887 MiB，GPU-Util 100%，PID 836281 (python)

## vota_seed42_v4 启动确认
- **PID 836276**: 存活（ELAPSED 00:40，wrapper shell）
- **实际训练 PID**: 836281（在 cuda:1 上占 41 GB 显存）
- **tmux session**: 无法通过 ssh_read_only 检查（tmux 不在白名单中）
- **日志**: 数据加载完成（Train: 4720, Eval: 1190），模型加载完成，tokenization 完成，已输出 `Starting training...` 并显示 `0%| | 0/444`
- **结论**: **启动成功**，训练已开始，正在第 0 step

## no_trace_seed42_v4 状态
- **PID 835084**: 存活（ELAPSED 09:35）
- **进度**: step 197/444（44%），~2.6s/it，已运行 9 分 24 秒

---
