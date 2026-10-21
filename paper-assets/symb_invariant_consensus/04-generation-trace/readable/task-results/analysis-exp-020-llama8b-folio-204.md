# analysis exp 020 llama8b folio 204

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-020-llama8b-folio-204_20260517T112831_result.json`
- **Structured JSON:** [`a6b9ef9ce9e1e39c733d.json`](../../sessions/a6/a6b9ef9ce9e1e39c733d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要
- SC accuracy: 63.2% (129/204)
- SICA accuracy: 60.8% (124/204)
- Delta: **-2.45 pp** (SICA 劣于 SC)
- p-value: 0.2668 (McNemar exact, two-sided); bootstrap one-sided p(SICA>=SC)=0.10
- Bootstrap 95% CI: [-5.88, +0.98] pp
- C0 / multi-candidate rate: 61.8% (126/204)
- Discordant pairs: 13 (SICA wins: 4, SC wins: 9)
- SICA win rate in discordant: 4/13 = 30.8%
- n: 204
- Extraction rate: 94.2%
- Answer extraction rate: 95.1%
- Contradiction rate: 6.2%
- Wall time: 131.7 min

## 与 exp-011 FOLIO 子集对比
- exp-011 FOLIO (n=30): SICA=70.0%, SC=60.0%, **+10.0 pp**
- exp-020 FOLIO (n=204): SICA=60.8%, SC=63.2%, **-2.45 pp**
- **方向不一致**。exp-011 的 +10pp 信号在 scale-up 后完全消失并反转。

## Conclusion
**negative** — SICA 在 LLaMA-3.1-8B + FOLIO 全量 204 题上不仅未达到统计显著，方向也反转为负。exp-011 中 FOLIO 子集 +10pp 的信号是小样本噪声（n=30 的随机波动）。Hypothesis 被拒绝。

## 关键发现
1. **Discordant pairs 极少**（仅 13/204 = 6.4%），说明 SICA 和 SC 在绝大多数题目上给出相同答案。SICA 的约束过滤机制几乎没有改变决策。
2. **在 discordant pairs 中 SICA 输多赢少**（4 wins vs 9 losses），说明约束过滤在改变决策时反而更多引入错误。
3. **C0 rate 61.8%** 意味着近 40% 的题目 SC 已经一致（unanimous），SICA 无操作空间。
4. **Both wrong = 71/204 (34.8%)**，模型基础推理能力是瓶颈，不是 aggregation 策略。
5. exp-011 FOLIO 的 +10pp 信号在 3.4x 数据量下消失，确认为 Type I error。

## Log 和 Checkpoint 路径
- log_path: `~/runs/symb_invariant_consensus/exp-020-llama8b-folio-204.log`
- results_path: `/root/symb_invariant_consensus/results/exp020_folio_200/exp020_results.json`
- checkpoint_path: 无（推理实验）

---
