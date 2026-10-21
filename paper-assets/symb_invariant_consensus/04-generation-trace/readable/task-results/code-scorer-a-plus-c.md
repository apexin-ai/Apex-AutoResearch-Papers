# code scorer a plus c

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scorer-a-plus-c_20260515T163255_result.json`
- **Structured JSON:** [`dc8aaa60038844b9a42d.json`](../../sessions/dc/dc8aaa60038844b9a42d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结如下：

---

### 1. scorer.py 改动摘要

- `__init__` 新增 `alpha=0.5` 和 `fallback_threshold=0.2` 参数
- `score()` 计算 `satisfied_ratio = n_satisfied / n_total`：
  - **NORMAL 模式** (ratio ≥ 0.2): `score = Σw(satisfied∩traces) - α·Σw(excluded∩traces)`
  - **FALLBACK 模式** (ratio < 0.2): `score = -Σw(excluded∩traces)` （最少矛盾者胜）
- 添加 INFO 级 logging，记录模式选择和关键参数
- `select_answer()` 不变，兼容负分（fallback 场景）
- 向后兼容：`InvariantScorer()` 用默认参数即走 A+C 逻辑；pipeline.py 零改动

### 2. P5 原始 vs 新评分对比

| | OLD (仅正信号) | NEW (A+C) |
|---|---|---|
| "80" | 0.0 | **-3.0** (最小负暴露) |
| "120" | 4.0 | -28.0 |
| "100" | 0.0 | -19.0 |
| 选中答案 | 120 (错误) | **80** (正确) |

Fallback 模式在 satisfied_ratio=0.048 时启动，利用 40 个 excluded 约束的负信号成功区分候选。

### 3. 回归测试结果

全 6 个测试通过：
- P1 (unanimous): 24.0 → 24.0 ✓
- P4 (high sat ratio): 13.0 → 12.0 (微调，答案不变) ✓
- P5 (low sat ratio): fallback 正确选出最少矛盾候选 ✓
- Synthetic multi-candidate: C > B > A 排序正确 ✓
- Zero constraints 边界情况 ✓

### 4. rescore_all.py 设计

- `--input` 模式：从 summary-level JSON 分析哪些题会受 A+C 影响（当前 v2 数据 3/7 题受影响，1 题进入 FALLBACK）
- `--full` 模式：从包含 constraint source_traces 的完整结果 JSON 重建 MaxSATResult 并真正重打分
- v3 跑完后，若 pipeline 输出包含 `maxsat_detail` 和 `traces`，直接 `python rescore_all.py --full -i results/aime30_v3.json`

### 5. source_traces 映射

验证了 trace_idx 在 TraceGenerator 和 ConstraintDeduplicator 中一致（都用顺序索引 0..K-1）。P5 的 `score=0.0` 不是 mapping bug——2 个 satisfied 约束确实来自未产出答案 "80" 的 trace。A+C 通过利用 excluded 约束解决了这个信号缺失问题。aime2024_II_07 的 `score=0.0` 同理（1 个 satisfied、0 个 excluded，但 source_traces 与唯一候选 trace 不重叠）。

---
