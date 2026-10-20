# ops kill llama verify dpo003

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-llama-verify-dpo003_20260512T182700_result.json`
- **Structured JSON:** [`ad8716bd4f43ab97b7b3.json`](../../sessions/ad/ad8716bd4f43ab97b7b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕。

## 报告

**1. llama-bcp-001 进程：已清理**
- 未找到任何 vllm/8002/Meta-Llama/run_mvp_experiment 相关进程，llama-bcp-001 已不在运行。

**2. dpo-003 训练：健康**
- PID 299960（bash wrapper）→ PID 299965（python train_dpo_v3.py），运行 ~3 分钟
- 进度：34/1173 steps（~3%），预计剩余 ~1.5h
- Loss：从 ~0.695 下降到 ~0.67-0.68，趋势正常
- rewards/margins 逐步增大（从负值到 ~0.03-0.05），DPO 训练在学习区分 chosen/rejected
- rewards/accuracies 在 0.5-1.0 之间波动，开始分离

**3. GPU 占用状态**

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| cuda:2 | 23031/24564 MiB | 100% | PID 299965 — dpo-003（仅此一个） |
| cuda:3 | 23201/24564 MiB | 96% | PID 276055 — dpo-002 |

cuda:2 干净，仅 dpo-003 占用，无残留进程。

---
