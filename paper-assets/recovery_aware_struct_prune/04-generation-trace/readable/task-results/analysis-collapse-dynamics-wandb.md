# analysis collapse dynamics wandb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collapse_dynamics_wandb_20260516T014849_result.json`
- **Structured JSON:** [`cd6981e3670a4650c6d3.json`](../../sessions/cd/cd6981e3670a4650c6d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存。核心发现与之前的理解有重要修正：

**Standard v8 的 step 60 "collapse" 是暂时的** — grad_norm 从 2.094 暴跌到 0.013，但到 step 90 完全恢复（grad_norm=2.14, reward=0.065, frac_zero_std=0.475）。这不是简单的"更慢的 collapse"，而是**质性不同的动态**：Standard 有自我修复能力，RASP 没有。

**三种 collapse 模式各不相同**：

| 模型 | 模式 | Onset | 可逆？ |
|------|------|-------|--------|
| RASP | 熵死亡 (entropy=0.054, grad=0.007) | ≤step 10 | 不可逆 |
| Standard | 瞬态 grad cliff | step 60 | **step 90 恢复** |
| Unpruned | reward-mode collapse (entropy=1.24 但 reward=0) | ~step 80 | 不可逆 |

这实际上**加强了 Claim 2** — 不同剪枝方法产生的不仅是不同 collapse 速度（6x差异），而是完全不同的失败签名和恢复能力。

**数据缺口**：
- RASP v9 只有 step 10 数据（run 可能卡住），steps 20/30 未获取
- Standard v8 缺 steps 70/80（step 60→90 之间的恢复轨迹）
- 需要 SSH 到服务器读 trainer_state.json 补全

报告路径：`artifacts/grpo_collapse_dynamics_analysis.md`

---
