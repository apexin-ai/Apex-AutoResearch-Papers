# eval aeff only direct

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_aeff_only_direct_20260523T200509_result.json`
- **Structured JSON:** [`acdcf923987008821005.json`](../../sessions/ac/acdcf923987008821005.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

```
seed42:  holdout_ppl = 17.750, holdout_loss = 2.8763
seed123: holdout_ppl = 17.733, holdout_loss = 2.8755
2-seed mean = 17.742 ± 0.009

对比:
- α_eff-only (n_min=1):       17.742 ± 0.009
- Dual-constrained (n_min=2): 17.674 ± 0.007
- Uniform:                    17.694 ± 0.008
```

α_eff-only 比 dual-constrained 差 0.068 PPL，也比 uniform 差 0.048 PPL。移除 ESS 约束后性能下降，说明 ESS 约束有独立贡献——仅靠 α_eff 信号不足以有效加权，支持双约束设计的必要性。

---
