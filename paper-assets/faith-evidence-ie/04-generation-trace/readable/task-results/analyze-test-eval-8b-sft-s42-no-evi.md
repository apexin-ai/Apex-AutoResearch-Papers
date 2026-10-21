# analyze test eval 8b sft s42 no evi

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_test_eval_8b_sft_s42_no_evi_20260522T060522_result.json`
- **Structured JSON:** [`6a954a4b850b74c2112a.json`](../../sessions/6a/6a954a4b850b74c2112a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## 8B Test Evidence Tax (s42)

| Metric | with_evi | no_evi | Δ |
|--------|----------|--------|---|
| **ign_f1** | 0.3106 | 0.2935 | **-1.71pp** |
| precision | 0.4543 | 0.4336 | -2.07pp |
| recall | 0.2359 | 0.2218 | -1.41pp |
| format_ok_rate | 0.996 | 0.998 | +0.2pp |
| truncated | 410/500 | 399/500 | -11 docs |

**Test evidence tax = -1.71pp**（负值 = evidence 有帮助）

### Dev→Test 一致性

- Dev fair_tax: **+0.04pp**（几乎 neutral，极微 evidence hurts）
- Test tax: **-1.71pp**（evidence helps）
- **方向不一致**：dev 说 neutral，test 说 evidence 帮助了 ~1.7pp。

不过两者绝对值都很小（<2pp），在 test set noise margin 内。综合看，8B 模型的 evidence tax 基本是 **neutral to slightly negative**（evidence 不 hurt，甚至可能略有帮助）。

值得注意：no_evi truncation 更少（399 vs 410），说明不输出 evidence 字段确实节省了 token budget，但并未转化为更多有效预测——反而 recall 更低（0.2218 vs 0.2359），说明 evidence prompting 的 chain-of-thought 效应对召回有一定正向作用。

---
