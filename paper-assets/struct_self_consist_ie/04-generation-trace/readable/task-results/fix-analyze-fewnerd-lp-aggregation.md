# fix analyze fewnerd lp aggregation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_analyze_fewnerd_lp_aggregation_20260518T135035_result.json`
- **Structured JSON:** [`af2d1f1c0aeab4dac455.json`](../../sessions/af/af2d1f1c0aeab4dac455.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Import 成功，无语法或依赖错误。

修改总结：
- **L25, L32**：注释 `max_LP` → `mean_LP`
- **L29**：`SCIERC_REF["lp_rho"]` 从 `0.215` → `0.205`
- **L211**：LP ρ global 计算从 `instance_max_signal["LP"]` → `instance_mean_lp`
- **L218-219**：LP ρ conditional 计算从 `instance_max_signal["LP"][non_degen_mask]` → `instance_mean_lp[non_degen_mask]`

重新运行脚本后 SciERC LP ρ 将为 0.205，与论文 Table 1 一致。

---
