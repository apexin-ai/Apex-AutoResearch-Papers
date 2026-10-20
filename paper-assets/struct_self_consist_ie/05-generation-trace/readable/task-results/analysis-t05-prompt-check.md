# analysis t05 prompt check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_t05_prompt_check_20260518T172500_result.json`
- **Structured JSON:** [`ca321dd1ce9815a06a05.json`](../../sessions/ca/ca321dd1ce9815a06a05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：exp_026_t05 使用了 joint NER+RE prompt，不是 NER-only。**

关键发现：
- 两个实验（exp_026_t05 和 exp_012_rerun_1024）都使用 `use_train_format=True`，对应 `_TRAIN_ALIGNED_TEMPLATE`，指令为 "Extract all structured information (entities and relations)"
- 模型实际输出了 entities + relations（已从 samples.jsonl 验证）
- **两者 prompt 完全一致**，区别仅在于 eval 阶段：T=0.5 只评了 NER，T=1.0 评了 NER+RE

是否需要重跑取决于目标：
- 若目标是 T=0.5 vs T=1.0 公平对比 → **不需要重跑**（prompt 已一致）
- 若目标是纯 NER-only 推理（排除 RE 对 NER 的干扰）→ 需要用 `--use_train_format false --subtask ner` 重跑，且 T=1.0 baseline 也需同步重跑

报告已写入 `artifacts/t05_check/t05_prompt_check.md`。

---
