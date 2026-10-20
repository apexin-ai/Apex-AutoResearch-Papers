# eval cwm4b mutation breakdown

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cwm4b-mutation-breakdown_20260516T022802_result.json`
- **Structured JSON:** [`b42560fe63c1b3176df4.json`](../../sessions/b4/b42560fe63c1b3176df4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果保存至 `artifacts/cwm4b_mutation_breakdown.json`。

**核心发现（CWM 4B s42）：**

| mutation_type | parse_rate | parseable acc | CLS 8B acc |
|---|---|---|---|
| gold | 43.5% | **23.5%** | 96.2% |
| operator_swap | 56.9% | **63.1%** | 81.4% |
| off_by_one | 4.4% | **0.0%** (n=8) | 86.9% |
| return_value | 48.8% | **27.0%** | 75.4% |
| boundary_removal | 30.6% | **59.2%** | 46.9% |
| **Overall** | **46.3%** | **42.9%** | — |

**关键洞察：**

1. **Parseable-only accuracy (42.9%) 远低于 overall (58.04%)**：因为 100% 的 unparseable 样本默认 pred=1 (pass)，在 pass-dominant 数据集 (73%) 上白捡准确率。
2. **Gold 类别灾难性低**：parseable 时仅 23.5% 正确（即模型倾向输出 "fail"）。CLS 8B 在 gold 上达 96.2%。
3. **Off-by-one 几乎完全不可解析**：95.6% unparseable，仅 8 个可解析样本且全错。
4. **CWM 的 "强项" 是 fail detection**：operator_swap fail-label acc=97.9%，但 pass-label 仅 34.5%——模型 parseable 时严重偏向预测 "fail"。
5. **两个 seed 一致**：seed123 parseable acc 也是 42.7%，模式相同。

这强力支持 "generation bottleneck" claim：CWM 4B 不仅有高 unparseable 率，其可解析预测的质量本身也远逊于 CLS。

---
