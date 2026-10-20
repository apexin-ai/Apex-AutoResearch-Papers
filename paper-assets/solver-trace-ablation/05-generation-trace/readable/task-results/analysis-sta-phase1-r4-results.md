# analysis sta phase1 r4 results

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sta-phase1-r4-results_20260513T204651_result.json`
- **Structured JSON:** [`0cdb5ac9b9d425166226.json`](../../sessions/0c/0cdb5ac9b9d425166226.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结：

## 结论：NEGATIVE — `fast_isr_fol` 设计缺陷导致实验无效

**指标对比**：

| 指标 | Baseline | exec-only | exec-sta |
|------|----------|-----------|----------|
| prove_rate | 0.120 | 0.151 | 0.158 |
| mean_isr | 0.064 | 0.148 | 0.153 |
| last-20 MA | — | 0.200 | 0.213 |

**根因**：`fast_isr_fol()` 只做 tautology check，返回 {0.0, 1.0} 二值。由于模型不产生 tautology，ISR 恒等于 prove_rate，两组实验收到**完全相同的 reward 信号**（前 20 步数据逐步一致）。

**MVP 评估**：
- ✅ #4 accuracy 无退化（+3-4pp 提升）
- ⚠️ #1 Solver 可靠但 ISR 退化为二值
- ❌ #2 ISR 区分度无法评估
- ❌ #3 两组无分离（last-20 差异 0.013，纯噪声）

**正面**：训练管线验证通过，GRPO 100 步稳定运行，prove_rate 有提升。

**修复方向**：需将 `fast_isr_fol` 替换为连续 ISR 信号（随机采样单个 premise ablation，或直接用 `run_sta` 完整版），然后重跑。

---
