# eval check 3 running evals

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check-3-running-evals_20260515T001247_result.json`
- **Structured JSON:** [`39415c71cd1ff4365e58.json`](../../sessions/39/39415c71cd1ff4365e58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 3 个 Eval 实验结果

| 实验 | 成功率 | 成功/总数 | vs Vanilla (65.3%) |
|------|--------|-----------|-------------------|
| **v4-taxei-seed123-eval** | **61.7%** | 29/47 | **-3.6pp** |
| **v4-taxei-fixed-inject10-eval** | **61.7%** | 29/47 | **-3.6pp** |
| **v4-taxei-fixed-inject25-eval** | **48.9%** | 23/47 | **-16.4pp** |

### Per-task breakdown

| Task Type | seed123 | inject10 | inject25 |
|-----------|---------|----------|----------|
| look_at_obj_in_light (6) | 83.3% | 83.3% | 66.7% |
| pick_and_place_simple (8) | 50.0% | 62.5% | 37.5% |
| pick_clean_then_place (11) | 63.6% | 45.5% | 45.5% |
| pick_cool_then_place (7) | 42.9% | 57.1% | 28.6% |
| pick_heat_then_place (8) | 75.0% | 75.0% | 62.5% |
| pick_two_obj_and_place (7) | 57.1% | 57.1% | 57.1% |

### Dose-response 曲线（fixed-size 训练集）

```
0% (vanilla):  65.3%
10% injection: 61.7%  (-3.6pp)
25% injection: 48.9%  (-16.4pp)
50% injection: 54.3%  (已有数据)
```

10% 注入对 clean eval 影响较小，25% 注入导致显著性能下降。seed123 的 TaxEI 模型与 seed=42 的结果一致（均 ~61.7%），说明 TaxEI 注入的性能影响跨 seed 稳定。

Registry 已全部更新为 DONE/success。

---
