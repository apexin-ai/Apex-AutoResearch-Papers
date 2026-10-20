# write s53 baseline narrative

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_s53-baseline-narrative_20260522T211425_result.json`
- **Structured JSON:** [`d4a63eab6f2d7e93c898.json`](../../sessions/d4/d4a63eab6f2d7e93c898.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三处修改已完成：

1. **Table 1** 新增两行 14B baseline 数据（0-shot 66.24%, 3-shot ICL 73.12%），分别插在对应方法组内 8B 和 DeepSeek 之间
2. **§5.3** 新增 `\paragraph{Baseline scaling.}` 段落（line 109），覆盖三个要点：
   - 3-shot 14B > 8B (+4.34pp)，scale 在 few-shot 有效
   - 0-shot 14B < 8B (-2.46pp)，措辞审慎归因于 instruction tuning 差异
   - 最优 baseline (73.12%) 仍低于 fine-tuned CLS 8B (89.94%) 16.82pp，scale 不能替代 fine-tuning

---
