# knowledge update paper framing

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_update_paper_framing_20260514T233712_result.json`
- **Structured JSON:** [`5430ff08bdbea625dfbb.json`](../../sessions/54/5430ff08bdbea625dfbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已更新 paper_framing.md，主要变更：

1. **Claim 1**: EM 取代 voting 成为 AUROC 最强信号 (0.749 vs 旧 voting 0.728)；voting_conf 仍领先 ρ (0.379)；logprob 从 0.559→0.578。所有 evidence 表格替换为 1024-token 数据，缺失的 τ/cond ρ 标注"待补"。

2. **Claim 2**: NER 方向反转——logprob 0.6501 微超 greedy 0.6439 (+0.6pp，标注待 bootstrap)；RE 方向完全反转——greedy 0.4042 > logprob 0.3948。correlation-selection gap 叙事更强。

3. **R3b**: 从"voting vs SJ"改为"EM beats all on AUROC — why present SJ/voting_conf?"，补充 EM 在 ρ 上反而最弱 (0.295) 的互补论证。

4. **R11**: Ensemble AUROC 从 0.735 降至 0.666，不再有 ensemble 优势（EM 单信号 0.749 反而更高），解释调整为特征冗余。

5. **Headline result / Story spine**: 所有引用数字同步更新。

---
