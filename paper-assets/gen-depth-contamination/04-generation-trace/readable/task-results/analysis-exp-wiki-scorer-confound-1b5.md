# analysis exp wiki scorer confound 1b5

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_wiki_scorer_confound_1b5_20260518T012012_result.json`
- **Structured JSON:** [`7d0b08a320fcc3ae6143.json`](../../sessions/7d/7d0b08a320fcc3ae6143.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 结果

**K\* = 1，Scorer confound confirmed for both Qwen scales。**

| Pair | AUC (Pythia scorer, 1.5B gen) | AUC (Pythia scorer, 7B gen) |
|------|------|------|
| 0v1 | **0.9729** | 0.9404 |
| 1v2 | 0.5994 | 0.587 |
| 2v3 | 0.533 | ~0.5 |
| 3v4 | 0.521 | ~0.5 |
| 4v5 | 0.507 | ~0.5 |

两个 scale 的 pattern 完全一致：Pythia 只能区分 depth 0 vs 1+，之后全部跌至随机水平。原始 Qwen-1.5B 自评 K\*=2 是 scorer artifact。

Registry 已更新：conclusion=negative, status=DONE。报告已注册为 artifact `art_20260518_4f91f8`。

---
