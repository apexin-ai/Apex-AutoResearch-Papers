# diag perlayer kl k16 eval final

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_perlayer_kl_k16_eval_final_20260523T051709_result.json`
- **Structured JSON:** [`efb29e958f072da38868.json`](../../sessions/ef/efb29e958f072da38868.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。总结：

**三次失败的根因都是 nohup 环境隔离问题：**

| 次数 | EXIT_CODE | 根因 |
|------|-----------|------|
| v3_eval | 1 | 网络不可达，未设离线模式 |
| eval_v2 | 1 | 设了 `HF_DATASETS_OFFLINE=1` 但没设 `HF_HOME`，找不到缓存 |
| eval_final | 127 | nohup shell 没有 conda，`python` 不在 PATH |

**当前状态：第4次尝试 eval_final2 (PID 114997) 正在运行**，已修复全部三个问题，arc_challenge 正在跑（~32%），预计 30-60 分钟完成。

K=8 eval 日志未在 `~/runs/` 下找到，无法直接对比命令结构——K=8 可能在交互式 shell 中直接运行的。

---
