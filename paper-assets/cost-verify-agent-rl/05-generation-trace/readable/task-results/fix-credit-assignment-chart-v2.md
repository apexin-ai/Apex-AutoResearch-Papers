# fix credit assignment chart v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_credit_assignment_chart_v2_20260517T011244_result.json`
- **Structured JSON:** [`cb0aa1a602c34c7ab409.json`](../../sessions/cb/cb0aa1a602c34c7ab409.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

## 产出

**图表已修正并重新生成**:
- `/root/cost-verify-agent-rl/analysis/figures/credit_assignment.pdf` (53KB)
- `/root/cost-verify-agent-rl/analysis/figures/credit_assignment.png` (187KB)

修改内容:
1. **图 1 (左)**: 标题改为 "Analogy: Reward Visibility under Discounted MDP"，添加脚注说明 GRPO 不使用 γ discount
2. **图 2 (右)**: 替换为 Causal Dilution 组合模型 — P(window contains ≥1 critical point) = 1 - C(T-K,h)/C(T,h)，T=35, K=4
   - exp028c (h=2): P=0.22 — 只有 22% 的窗口包含关键决策点
   - exp029 (h=T): P=1.00 — 全窗口必然覆盖
   - Causal dilution ratio: 4.58x
3. **整体标题**: "Credit Assignment: Why Context Window Size Matters for Episode-Level RL"

---

## 方案 1 数据可行性报告

**Per-step rollout 数据现状**:

| 数据源 | 路径 | 格式 | 内容 |
|--------|------|------|------|
| wandb tables | `/root/autodl-tmp/wandb/wandb/run-20260517_041330-7a59sudo/files/media/table/rollout/` | `.table.json` | 每 step 的 per-group reward matrix (16 groups × 8 rows)，只有最终 reward (0/10)，无 per-step action 数据 |
| tmp rollout dirs | `/root/autodl-tmp/tmp/tmp*/rollout/` | `.table.json` | 同上格式 |
| trajectory_tracker | verl 内置 | `.pth` (HDFS) | 需设 `VERL_ENABLE_TRACKER=1`，当前未启用 |
| exp029 checkpoints | `/root/autodl-tmp/checkpoints/exp029/global_step_{5,10}/` | model weights only | 无 rollout 日志 |

**结论**: 当前**无可用的 per-step trajectory 数据**。wandb 表只记录了 episode-level reward (0 or 10)，没有保存中间 step 的 action/observation。要实现方案 1（真实 per-step credit assignment 分析），需要下次训练时启用 `VERL_ENABLE_TRACKER=1` 或在 RAGEN 的 rollout loop 中添加 trajectory dump 逻辑。

---
