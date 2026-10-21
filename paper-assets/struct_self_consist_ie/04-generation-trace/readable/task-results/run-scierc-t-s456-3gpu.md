# run scierc t s456 3gpu

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_scierc_t_s456_3gpu_20260521T032250_result.json`
- **Structured JSON:** [`9ecfb1e686b1a86bad87.json`](../../sessions/9e/9ecfb1e686b1a86bad87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部正常运行：

| Exp ID | Server | GPU | VRAM | 状态 |
|--------|--------|-----|------|------|
| exp_scierc_t05_s456 | autodl-5090-b | cuda:2 | 30306 MiB | 处理中 ~192/4408 prompts |
| exp_scierc_t08_s456 | autodl-5090-b | cuda:3 | 30290 MiB | 处理中 ~96/4408 prompts |
| exp_scierc_t12_s456 | autodl-5090-c | cuda:1 | 30307 MiB | 处理中 ~168/4408 prompts |

551 instances × 8 samples = 4408 prompts，当前吞吐 ~1800-2700 toks/s，预计 7-10 分钟完成。

注意：5090-c 无 tmux，T=1.2 实验用 nohup 启动（PID=272106），进程正常但无 tmux session 管理。

---
