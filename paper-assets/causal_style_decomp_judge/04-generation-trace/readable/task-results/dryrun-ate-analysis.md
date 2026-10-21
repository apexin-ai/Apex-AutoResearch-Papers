# dryrun ate analysis

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_dryrun_ate_analysis_20260520T112515_result.json`
- **Structured JSON:** [`2e230dc068d5f8984a26.json`](../../sessions/2e/2e230dc068d5f8984a26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry run 完成，结果汇总：

| 指标 | 数值 | 预期 | 状态 |
|------|------|------|------|
| **Raw ATE** | **+1.5000** | +1.5 | 精确匹配 |
| **Raw p-value** | ≈ 0 (3.99e-295) | p << 0.05 | 通过 |
| **Raw Cohen's d** | 2.78e+15（爆炸） | > 1.0 | 见下方说明 |
| **Rewrite bias** | +0.005 | ≈ 0 | 通过 |
| **Corrected ATE** | +1.4950 | ≈ 1.5 | 通过 |
| **Corrected p** | 1.17e-23 | p << 0.05 | 通过 |
| **Corrected Cohen's d** | +14.31 | > 1.0 | 通过 |
| **ate_bar.png** | 38K | 生成 | 通过 |
| **score_violin.png** | 61K | 生成 | 通过 |

**一个问题**：Raw Cohen's d 爆炸到 2.78e+15。原因是合成数据中 `score_formal - score_casual` 的 diff 恒为 1.5（零方差），`std(ddof=1)` ≈ 0 导致除法溢出。这是合成数据的特性（所有样本的 formal_bonus 完全相同），不是代码 bug。Corrected Cohen's d = 14.31 正常，因为 rewrite bias 引入了少量方差。

**修复记录**：ate_analysis.py 缺少 `from __future__ import annotations`，导致模块加载时 `pd.DataFrame` 类型注解触发 `NameError`。已在服务器和本地 artifacts 同步修复。

**有一个 warning**：seaborn 的 `palette` 参数在 v0.14 后需配合 `hue` 使用，不影响功能但可以后续修。

---
