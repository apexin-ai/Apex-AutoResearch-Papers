# ops check vanilla 2pl and stale

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_vanilla_2pl_and_stale_20260517T193031_result.json`
- **Structured JSON:** [`4c952244254200916b57.json`](../../sessions/4c/4c952244254200916b57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完毕，报告已写入 `artifacts/report_vanilla_2pl_check.md`。

**总结：**

| 实验 | 状态 | 说明 |
|------|------|------|
| exp_006_mmlu_vanilla_2pl_fullitems | **已完成** | 4 chains 全部采样完毕（898MB chains 保存在 `/root/autodl-tmp/exp006/vanilla_2pl_fullitems_chains/`），但 log 中无 Python 后处理输出，需手动用 chains 做 tau 提取 |
| exp_002_signals_3B_d000_s123_cuda2 | **已完成** | 2026-05-16 22:05 结束，6/9 成功 + 2 跳过 + 1 失败，mmlu/arc/gsm8k 三组信号均已产出并 merge |

注意事项：vanilla_2pl chains 1/2 的 CSV 大小（184/162MB）明显小于 chains 3/4（296MB），可能存在 divergent transitions，后续使用前建议检查 Rhat 和 n_eff。

---
