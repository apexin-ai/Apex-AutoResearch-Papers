# analysis exp050b 049b final v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp050b-049b-final-v2_20260518T231314_result.json`
- **Structured JSON:** [`ce20486a091ee5a6f5ae.json`](../../sessions/ce/ce20486a091ee5a6f5ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总如下：

## 实验结果

| Experiment | Model | Dataset | n | SC | SICA | Delta | b | c | McNemar p | Sig |
|---|---|---|---|---|---|---|---|---|---|---|
| **exp-050b** | Mistral-7B + ICL Oracle | FOLIO-199 | 199 | 57.79% (115) | 54.27% (108) | **-3.52pp** | 6 | 13 | 0.167 | No |
| **exp-049b** | Mistral-7B | LogiQA-200 | 200 | 51.00% (102) | 51.50% (103) | **+0.50pp** | 6 | 5 | 1.000 | No |

### exp-050b 要点
- ICL 将 SC 从 vanilla 54.41% (exp-033) 提升到 57.79% (+3.38pp)，说明 ICL 对 SC 有效
- 但 SICA 反而低于 SC (54.27% < 57.79%)，delta 为负
- 解读：ICL 提高了单条 trace 质量从而增强 majority vote，但降低了 trace 间的 diversity，使 MaxSAT 加权失去 discriminative power

### exp-049b 要点
- Mistral FOLIO 上的 +4.90pp 优势未迁移到 LogiQA
- SC=51% 接近 4 选 1 随机水平，模型在 LogiQA 上能力不足
- 与 exp-038 (14B LogiQA delta=-0.50pp) 一致：SICA 在 LogiQA 上无论模型都无效

两个实验均为 **negative**，registry 已标记 DONE。

---
