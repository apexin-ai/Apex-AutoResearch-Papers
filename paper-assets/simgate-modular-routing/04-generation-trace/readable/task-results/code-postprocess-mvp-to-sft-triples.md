# code postprocess mvp to sft triples

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_postprocess-mvp-to-sft-triples_20260513T184204_result.json`
- **Structured JSON:** [`44cc7b6a1cc0d34736ef.json`](../../sessions/44/44cc7b6a1cc0d34736ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| | episodes | det wins | internal wins | ties (丢弃) | SFT steps |
|---|---|---|---|---|---|
| melt | 20 | 8 | 0 | 12 | 240 |
| change-the-state-of-matter-of | 20 | 9 | 0 | 11 | 270 |
| chemistry-mix-paint-secondary-color | 20 | 8 | 0 | 12 | 240 |
| **合计** | **60** | **25** | **0** | **35** | **750** |

关键发现：
- **internal 没有赢过任何一个 episode**，所有非 tie 的 pair 都是 det 胜出
- tie rate 58.3%（35/60），主要来源是双方都 0 分或双方都 death（-100）
- 750 条 SFT triples 全部标记为 `deterministic`，这意味着训练出来的 router 会学到"永远选 det"——数据缺乏 internal 正样本

输出文件：
- `results/sft_data/sft_triples.jsonl`（750 行）
- `results/sft_data/collection_summary.json`

---
