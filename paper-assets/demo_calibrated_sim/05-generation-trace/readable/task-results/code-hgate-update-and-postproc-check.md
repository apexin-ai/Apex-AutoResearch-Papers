# code hgate update and postproc check

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hgate-update-and-postproc-check_20260512T125249_result.json`
- **Structured JSON:** [`33d4dfd5b7d80eb71ed2.json`](../../sessions/33/33d4dfd5b7d80eb71ed2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**任务 1 — `h_gate_evaluator.py` 修改总结：**
- **H1**：pass 条件改为仅 `politeness_rate >= 0.30`。question_rate 数据移入 `detail.secondary_metric` 嵌套字典，仍计算和报告但不影响 pass/fail。
- **H2**：pass 条件改为仅看 politeness 维度的 gap reduction >= 30%。question_rate gap reduction 移入每个 variant 的 `secondary_metric` 字典。
- **H3**：未修改。
- `__init__` 参数保持不变（`h1_question_rate_threshold` 保留，用于 secondary 报告）。

**任务 2 — `generate_synthetic_corpus.py` 检查结论：**
- import 正确引用 `behavioral_fingerprint` 模块的 `QuestionDetector`、`PolitenessDetector`、`BehavioralFingerprint`、`analyze_traces`。
- 所有检测调用均使用 `detector.detect(text)` → `tuple[bool, list[str]]`，与接口一致。
- 无硬编码 `?` 匹配。无需修改。

---
