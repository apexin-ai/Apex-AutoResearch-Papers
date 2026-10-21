# fix hidden probe f1 bug

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_hidden_probe_f1_bug_20260518T111410_result.json`
- **Structured JSON:** [`9273b9aedb40af48d215.json`](../../sessions/92/9273b9aedb40af48d215.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果：

## Text-based F1, Gold-filtered 529 instances, 5-fold CV × 3 seeds

| Method | Dim | Spearman ρ | Selection F1 | Gap Closure |
|--------|-----|-----------|-------------|-------------|
| Greedy | -- | -- | 0.6099 | -- |
| LP | 1 | 0.2214 | 0.6087 | -0.7% |
| Hidden Linear | 4096 | 0.2327±0.0212 | 0.6199±0.0043 | 6.3% |
| Hidden MLP | 4096 | 0.4535±0.0081 | 0.6348±0.0043 | 15.6% |
| Oracle | -- | -- | 0.7692 | 100% |

## 修复内容

1. `extract_hidden_states.py` entity_set: `(start,end,type)` → `(text,type)`
2. `hidden_state_probe.py`: 从 JSONL 重算 text-based F1 labels（替代加载旧的 span-based labels.pt）
3. 删除 DeBERTa hardcoded 数字
4. 结果保存至 `results_textbased_goldfiltered.json`

## 关键发现

**匹配方式差异影响极小**：text-based greedy F1 = 0.6099, span-based = 0.6094，差异仅 0.05pp。

**真正的 bug 是 labels 不一致**：labels.pt（span-based from extract_hidden_states.py）与 selection F1 计算（text-based in hidden_state_probe.py）用了不同匹配方式。修复后 MLP gap closure 从 13.9% 提升到 **15.6%**。

**Greedy F1 = 0.609 vs 论文 0.644-0.645 的差异不是匹配方式问题**，而是不同实验数据源（exp_012_logprob vs exp_016_rerun_1024）。exp_012 的 greedy 输出与 exp_016 的不同（可能不同模型 checkpoint 或不同推理参数）。

---
