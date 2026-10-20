# audit table fewnerd source v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table_fewnerd_source_v2_20260518T035825_result.json`
- **Structured JSON:** [`972bc61c81c01997fba2.json`](../../sessions/97/972bc61c81c01997fba2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I've completed the exhaustive investigation. Here's the result.

## tab:fewnerd SciERC 行溯源

### SCIERC_REF 硬编码值来源：**无法追溯到任何单一实验/JSON**

各值逐一追踪结果：

| SCIERC_REF 值 | 可追溯性 | 最接近的实际计算值 |
|---|---|---|
| **greedy=0.614** | ❌ 无匹配 | exp_012_rerun_1024: 0.618 (n=551) 或 0.644 (n=529 gold-filtered) |
| **oracle=0.752** | ⚠️ 仅匹配 exp010 N=8 seed42 n=551 (0.7522)，但这是**不同实验** | exp_012_rerun_1024: 0.745 (n=551) 或 0.776 (n=529) |
| **headroom=13.8** | ✅ 与 greedy/oracle 内部一致 (0.752-0.614=0.138) | 但基础值本身不可追溯 |
| **lp_rho=0.205** | ✅ **唯一可确认来源**: exp_012_rerun_1024/report.json `ner_logprob_baseline.full.rho = 0.20517` | **确认为 max_tokens=1024** |
| **lp_delta=+0.42pp** | ❌ 无匹配 | exp_012_rerun_1024: +0.62pp (n=529) 或 +0.59pp (n=551) |

### 关键证据

- `exp_012_rerun_1024/comparison.json` 明确记录：512 版 logprob rho=0.1396，1024 版 rho=0.2052。**lp_rho=0.205 来自 1024 版无疑。**
- 512 版 LP delta = **-0.07pp**（负值），1024 版 = **+0.62pp**。+0.42pp 与两者都不匹配。
- `d112_table2_fix/corrected_table2.json` 给出经过验证的 seed42+123 平均值：greedy=0.645, oracle=0.778, LP delta=+0.20pp——也与 SCIERC_REF 不符。
- greedy=0.614 不匹配任何实验的任何过滤条件（n=551 全集 / n=529 gold-filtered / n=477 conditional）。
- 所有 JSON 中出现 `lp_delta: 0.42` 的文件（exp_020_pilot, exp_021_inference, exp_027_fewnerd_n16）都是 `analyze_fewnerd_results.py` 的输出，仅在回显 SCIERC_REF 常量。
- 无 git 历史可追溯 SCIERC_REF 被设置的 commit。

### 结论

```
tab:fewnerd SciERC 行是否受 max_tokens=512 污染: INCONCLUSIVE

判断依据:
- lp_rho=0.205 确认来自 1024 版本（不受 512 污染）
- greedy=0.614 和 lp_delta=+0.42pp 无法追溯到任何实验：
  - 512 版给出 LP Δ=-0.07pp（差距极大）
  - 1024 版给出 LP Δ=+0.62pp（方向正确但数值不符）
  - 两者都无法产生 greedy=0.614
- 这些值很可能是从某次已丢失的分析/控制台输出中手动摘录的，
  混合了不同实验/条件/计算方法的结果
- 核心问题不是 512 vs 1024 污染，而是 SCIERC_REF 所有值
 （除 lp_rho 外）均不可复现，属于硬编码 bug
```

**建议**：用 `exp_012_rerun_1024/samples.jsonl`（1024 版，seed42）重新计算所有值，根据论文使用的过滤条件（n=529 gold-filtered 或 n=551 全集）统一基准。

---
