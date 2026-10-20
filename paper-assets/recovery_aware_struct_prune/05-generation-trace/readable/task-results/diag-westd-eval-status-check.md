# diag westd eval status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd-eval-status-check_20260515T183120_result.json`
- **Structured JSON:** [`25bc54045d3b67521d4a.json`](../../sessions/25/25bc54045d3b67521d4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 Eval 状态

| Eval | GPU | 进度 | 运行时间 | 预计剩余 | 20样本精度 |
|------|-----|------|---------|---------|-----------|
| sft_rasp_20_westd_n100 | cuda:0 | **32/100** (32%) | ~29 min | ~58 min | 0.0500 (1/20) |
| sft_standard_20_westd_n100 | cuda:1 | **33/100** (33%) | ~29 min | ~57 min | 0.0000 (0/20) |

**GPU 占用**: 两卡均 88% utilization, ~13GB memory

**tmux sessions**: 无（进程通过 nohup 启动，不在 tmux 内）

**结果文件**: 尚未生成

**预计完成时间**: ~02:59 UTC (服务器时间约 03:00)，即从现在起约 57 分钟。

**注意**: standard 模型在前 20 个样本上准确率为 0，rasp 也仅 5%。这些是 N=100 eval 的中间结果，最终结果需等全部完成后查看。

---
