# ops post restart check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart-check_20260524T040146_result.json`
- **Structured JSON:** [`ca3c10c17e1054c317b5.json`](../../sessions/ca/ca3c10c17e1054c317b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### exp_020 (GPT-2-medium r=0, cuda:0)
- **进程存活**: PID 853361 在跑
- **当前进度**: generation 0–7 已完成（共 8 代），正在跑 generation 8
- **GPU 0**: 52% 利用率，26431 / 97887 MiB 显存
- **日志**: 无 exp_020.log（可能直接写结果文件）
- **结果文件**: `phase1_gpt2m_pure_collapse_seed42_results.json`，最后更新 May 24 11:36

### exp_021 (GPT-2-medium real-data control, cuda:1)
- **进程存活**: PID 846794 在跑，已运行 1h16m
- **当前进度**: generation 0–1 已完成，正在跑 generation 2（日志全是 padding warning，说明在训练中）
- **GPU 1**: 100% 利用率，52858 / 97887 MiB 显存
- **结果文件**: `exp_021_gpt2m_realdata_control_seed42_results.json`，最后更新 May 24 11:50

### 结论
两个实验都在正常运行，服务器未重启。exp_020 进度较快（已到 gen 7），exp_021 刚完成 gen 1。

---
