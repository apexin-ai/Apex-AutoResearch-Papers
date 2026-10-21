# run fulldata groupkfold probe

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_fulldata_groupkfold_probe_20260521T034544_result.json`
- **Structured JSON:** [`9c1026bb8c1071ff4bad.json`](../../sessions/9c/9c1026bb8c1071ff4bad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

P0 任务完成。Artifact 已注册，实验 registry 已更新为 DONE(success)。

---

## Full-data GroupKFold Hidden State Probe 最终结果

| Dataset | Instances | Entities | GroupKFold AUROC | StratifiedKFold AUROC | Leakage Δ | 500-inst ref | vs MV(0.87) |
|---------|-----------|----------|------------------|-----------------------|-----------|-------------|-------------|
| **CoNLL** | 850 | 14,777 | **0.8824 ± 0.0001** | 0.9786 ± 0.0016 | +0.0962 | 0.885 | **> MV** |
| **FewNERD** | 1,698 | 41,096 | **0.6361 ± 0.0001** | 0.9802 ± 0.0002 | +0.3441 | 0.651 | < MV |
| **SciERC** | 539 | 13,188 | **0.6304 ± 0.0002** | 0.9763 ± 0.0002 | +0.3459 | 0.634 | < MV |

### 关键结论

1. **CoNLL hidden state probe (0.882) 超过 MV baseline (0.87)**，说明在 CoNLL 上模型内部表征比多次采样投票更能区分实体质量。

2. **FewNERD/SciERC probe (~0.63) 远高于随机（0.5）但低于 MV**，表明 hidden states 编码了部分质量信息，但不如 MV 聚合信号强。

3. **StratifiedKFold vs GroupKFold 泄露量化**：StratifiedKFold AUROC 全部 ~0.98，leakage delta 在 +0.096（CoNLL）到 +0.346（SciERC）。CoNLL 泄露最小（同一 instance 内实体相似度较低），FewNERD/SciERC 泄露严重——GroupKFold 是必要的。

4. **全量 vs 500-inst 子集一致**：CoNLL 0.882 vs 0.885，FewNERD 0.636 vs 0.651，SciERC 0.630 vs 0.634，差异 <0.02，子集结果具有代表性。

---
