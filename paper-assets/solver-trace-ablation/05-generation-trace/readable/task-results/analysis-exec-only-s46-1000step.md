# analysis exec only s46 1000step

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exec-only-s46-1000step_20260522T043751_result.json`
- **Structured JSON:** [`f5003cb6f3fc73e8a6e1.json`](../../sessions/f5/f5003cb6f3fc73e8a6e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇报

| 项目 | 值 |
|------|-----|
| **训练完成** | 是，1000/1000 steps，2h15m |
| **W&B run ID** | 无（训练未配置 wandb） |
| **Checkpoint** | `/root/autodl-tmp/outputs/exec_only_s46_1000_k4` |
| **prove_rate** | **0.15** (15/100) |
| **mean_isr** | 0.084 (全样本), 0.5597 (proved-only) |
| **genuine_rate** | **86.7%** (13/15) |
| **CE (H1)** | 1 |
| **TS (H7)** | 1 |
| **PG (H8)** | 0 |
| **CI** | 0 |

**判断：negative（非收敛）**

prove_rate=15% < 30%，模型未能超越 base model 水平。与 s45 (PR=15%) 和 s52 (PR=14%) 呈现相同的 seed-dependent non-convergence 模式。不是 Goodhart collapse（那需要高 prove_rate + 低 genuine_rate），而是模型根本没学会有效证明。

这是 informative negative：即使训练到 1000 步、使用不同的 batch 配置 (4/accum=2)，exec-only 的收敛仍然高度依赖随机种子。Registry 已更新为 DONE/negative。

---
