# ssh dgec sj construction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_dgec-sj-construction_20260520T083925_result.json`
- **Structured JSON:** [`00c76104c38fd9bf20a7.json`](../../sessions/00/00c76104c38fd9bf20a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

17 个 config 全部完成，M030 验证全部通过。

| Config | Dataset | Model | Regime | Greedy F1 | SJ F1 | Δpp | p-value | Sig |
|---|---|---|---|---|---|---|---|---|
| scierc/72b/zs | SciERC | 72B | ZS | 0.399 | 0.419 | **+2.0** | 0.001 | **+** |
| scierc/72b/fs | SciERC | 72B | FS | 0.462 | 0.463 | +0.2 | 0.369 | n.s. |
| conll/72b/zs | CoNLL | 72B | ZS | 0.712 | 0.706 | −0.6 | 0.999 | **−** |
| conll/72b/fs | CoNLL | 72B | FS | 0.745 | 0.743 | −0.2 | 0.873 | n.s. |
| fewnerd/72b/zs | FewNERD | 72B | ZS | 0.628 | 0.625 | −0.3 | 1.000 | **−** |
| fewnerd/72b/fs | FewNERD | 72B | FS | 0.619 | 0.619 | +0.0 | 0.415 | n.s. |
| fewnerd/7b/ft/s42 | FewNERD | 7B | FT | 0.785 | 0.776 | −0.9 | 1.000 | **−** |
| fewnerd/7b/ft/s123 | FewNERD | 7B | FT | 0.785 | 0.781 | −0.4 | 1.000 | **−** |
| fewnerd/7b/ft/s456 | FewNERD | 7B | FT | 0.783 | 0.779 | −0.3 | 1.000 | **−** |
| conll/7b/ft/s123 | CoNLL | 7B | FT | 0.907 | 0.906 | −0.1 | 0.750 | n.s. |
| conll/7b/ft/s456 | CoNLL | 7B | FT | 0.908 | 0.903 | −0.4 | 0.989 | **−** |
| conll/7b/ft/s789* | CoNLL | 7B | FT | 0.907 | 0.906 | −0.1 | 0.650 | n.s. |
| scierc/7b/ft/s456 | SciERC | 7B | FT | 0.645 | 0.639 | −0.6 | 0.805 | n.s. |
| scierc/7b/ft/s789 | SciERC | 7B | FT | 0.643 | 0.634 | −0.9 | 0.882 | n.s. |
| wnut17/7b/ft/s42 | WNUT17 | 7B | FT | 0.452 | 0.441 | −1.2 | 0.978 | **−** |
| wnut17/7b/ft/s123 | WNUT17 | 7B | FT | 0.452 | 0.455 | +0.3 | 0.217 | n.s. |
| wnut17/7b/ft/s456 | WNUT17 | 7B | FT | 0.453 | 0.457 | +0.4 | 0.172 | n.s. |

*s789 uses N=16 samples

**Summary**: 1 significant positive / 7 significant negative / 9 not significant

SJ 作为 construction 权重**整体不如 greedy baseline**——仅 SciERC 72B ZS（最低精度、最低退化率的 config）获得显著正向提升。FewNERD 7B FT 的 3 个 seed 一致显著下降（−0.3 到 −0.9pp），说明 SJ 信号作为 construction 权重时反而引入噪声。这与 VC 实验对照可以明确回答：**并非任何"更强 QE 信号"都有效**。

---
