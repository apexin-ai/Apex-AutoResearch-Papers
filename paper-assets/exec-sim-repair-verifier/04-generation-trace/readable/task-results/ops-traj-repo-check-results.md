# ops traj repo check results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_traj-repo-check-results_20260516T151617_result.json`
- **Structured JSON:** [`464b3fb97daa00024369.json`](../../sessions/46/464b3fb97daa00024369.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总报告：

---

## DeepSeek Repo-Level TRAJ 结果

### 训练概况
- 模型: deepseek-coder-6.7b-instruct + LoRA
- 数据: 386 train / 43 val / 48 test
- 3 epochs, 147 steps, best checkpoint @ step 98 (epoch 2)
- Loss 曲线正常：train_loss 0.42→0.12, eval_loss 0.16→0.11→0.13（epoch 3 轻微过拟合）

### Test Accuracy

| Seed | Accuracy | Eval Loss (best) |
|------|----------|-----------------|
| 42   | 77.1%    | 0.1110          |
| 123  | 77.1%    | 0.1147          |
| **Mean** | **77.1% ± 0.0%** | |

### 对比

| Method | Accuracy | Gap |
|--------|----------|-----|
| Func-level TRAJ (DeepSeek) | 84.16 ± 1.30% | baseline |
| Repo-level CLS (Qwen 14B) | 84–86% | ~same as func TRAJ |
| **Repo-level TRAJ (DeepSeek)** | **77.1 ± 0.0%** | **-7.1pp** |

### 问题分析

1. **高 unparseable 率 (8/48 = 16.7%)**：模型生成了非结构化文本而非 "resolved"/"unresolved"，fallback 到多数类（resolved），严重损害 unresolved recall (54.5%)
2. **严重的类别偏斜**：resolved recall 96.2% vs unresolved recall 54.5%，模型过度预测 resolved
3. **两个 seed 结果完全一致**：说明模型行为非常确定性，unparseable 的 8 条样本在两个 seed 下都是相同的（可能是这些输入序列太长被截断，导致生成垃圾）
4. **数据量太少（386条）不是主因**：loss 曲线正常收敛，eval_loss 低（~0.11），问题出在 inference 端的 seq_length 截断和格式遵从

### 结论

Repo-level TRAJ 用 DeepSeek 6.7B 效果显著不如 func-level TRAJ（-7pp），主要瓶颈是 repo-level diff 更长导致 2048 token 截断后模型无法正确生成格式化输出。需要增加 max_seq_length 或换更长上下文的模型。

---
