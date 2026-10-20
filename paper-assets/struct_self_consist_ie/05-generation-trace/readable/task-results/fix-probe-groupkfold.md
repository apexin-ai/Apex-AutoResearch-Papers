# fix probe groupkfold

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_probe_groupkfold_20260521T030809_result.json`
- **Structured JSON:** [`c5ad6979f260637f9902.json`](../../sessions/c5/c5ad6979f260637f9902.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| Dataset | StratifiedKFold (leaky) | GroupKFold (corrected) | Delta | Probe > MV (0.87)? |
|---------|------------------------|----------------------|-------|---------------------|
| **CoNLL** | 0.980 | **0.885** | -0.095 | **YES** |
| **FewNERD** | 0.987 | **0.651** | -0.336 | **NO** |
| **SciERC** | 0.977 | **0.634** | -0.342 | **NO** |

### 关键发现

1. **泄露确认**：fewnerd/scierc 的原始高 AUROC (0.97-0.99) 主要来自 instance 信息泄露，修正后暴跌 0.33-0.34
2. **CoNLL 仍成立**：GroupKFold AUROC = 0.885 > MV (0.87)，probe > MV 的结论在 conll 上仍然成立
3. **fewnerd/scierc 重新定位**：修正后 AUROC 0.63-0.65，处于 ESJ (0.51) 和 MV (0.87) 之间，表明 hidden states 中有部分质量信息但远不如 MV
4. **与 LODO 一致**：LODO 近随机 (0.559) 与 GroupKFold 的较低 AUROC 一致——跨 instance 泛化能力弱

### 对论文的影响

原来的叙事 "probe AUROC >> MV → info exists but prompt interface fails" 只对 CoNLL 成立。需要修改论文中的 probe 讨论：
- CoNLL: 仍支持 representation-level 信号 > MV
- FewNERD/SciERC: hidden states 中有部分信号，但远低于 MV，说明 multi-sample 投票捕获的信号不仅仅来自单次推理的 representation

代码和结果保存在 `output/entity_probe_auroc_groupkfold/`，registry 已更新。

---
