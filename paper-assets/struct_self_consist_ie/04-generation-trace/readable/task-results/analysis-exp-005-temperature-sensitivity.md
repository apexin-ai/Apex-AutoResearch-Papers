# analysis exp 005 temperature sensitivity

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_005_temperature_sensitivity_20260514T114116_result.json`
- **Structured JSON:** [`e542e0d323bfdd930fc4.json`](../../sessions/e5/e542e0d323bfdd930fc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-005 完成。产出在 `artifacts/exp005_temperature/`，已注册。

核心发现：

1. **SJ 对温度鲁棒**：NER ρ 变化仅 +0.005，RE 仅 -0.010。FK 对温度更敏感（NER +0.062, RE -0.095）。

2. **T=0.7 压缩可用范围**：oracle headroom 下降（NER -1.2pp, RE -3.6pp），diversity (1-SJ) 下降约 0.075。

3. **条件过滤 >> 温度调整**：RE SJ 的 full→cond lift (+0.07~+0.14) 远大于温度效应 (±0.01)。

4. **推荐 T=1.0 + conditional filtering**：保留更多 headroom 和多样性，信号质量几乎一致。

5. **数据缺口**：logprob/exact_match/voting_conf 只有 T=1.0 数据；T=0.7 无 tau/AUROC。

---
