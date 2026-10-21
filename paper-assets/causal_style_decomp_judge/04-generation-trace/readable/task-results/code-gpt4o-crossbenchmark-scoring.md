# code gpt4o crossbenchmark scoring

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpt4o_crossbenchmark_scoring_20260521T082621_result.json`
- **Structured JSON:** [`6d292fc6b036e1590319.json`](../../sessions/6d/6d292fc6b036e1590319.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

```
## AlpacaEval × GPT-4o
Pairs: 86
BT: P(formal)=72.7% [66.3%, 78.5%], p=< 0.0001
Likert: ATE=0.128, p=0.1704, d=0.148, tie_rate=66.3%
Blindspot: Yes
GEE: Style OR=4.91 p=< 0.0001, Orig OR=1.99 p=0.0356

## MT-Bench × GPT-4o
Pairs: 73
BT: P(formal)=69.2% [62.3%, 75.3%], p=< 0.0001
Likert: ATE=0.164, p=0.0163, d=0.167, tie_rate=69.9%
Blindspot: Yes
GEE: Style OR=2.28 p=0.1055, Orig OR=6.24 p=0.0005
```

两个 benchmark 都确认 GPT-4o 存在 formality blindspot（BT 显著偏好 formal）。

AlpacaEval 上 GEE 风格效应极强（OR=4.91, p<0.0001），原创偏好也显著（OR=1.99, p=0.036）。Likert ATE 不显著（p=0.17），高 tie rate 66.3% 说明 Likert 灵敏度不够。

MT-Bench 上 GEE 原创效应很强（OR=6.24, p=0.0005），但风格效应不显著（OR=2.28, p=0.106）——说明 MT-Bench 上 GPT-4o 更多是偏好"原始"文本而非纯粹的 formal 风格。Likert 在 MT-Bench 上反而显著（ATE=0.164, p=0.016），但效应量小（d=0.167）。

输出文件已保存：
- `data/pairwise_results_alpacaeval_gpt4o.jsonl`
- `data/scored_alpacaeval_gpt4o.jsonl`
- `data/pairwise_results_mtbench_gpt4o.jsonl`
- `data/scored_mtbench_gpt4o.jsonl`

---
