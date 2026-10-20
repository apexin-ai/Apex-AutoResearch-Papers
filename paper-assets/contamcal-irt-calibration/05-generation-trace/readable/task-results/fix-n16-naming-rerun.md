# fix n16 naming rerun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_n16_naming_rerun_20260516T170011_result.json`
- **Structured JSON:** [`15696ddd764b45a55446.json`](../../sessions/15/15696ddd764b45a55446.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

**修复**：在 `run_pooled_rrf_irt.py` 中添加 `normalize_model_key()` + `resolve_rrf_key()`，解决 3 个命名不匹配：
1. `_s42_a32` vs `_a32_s42` 重排序（2 个）
2. `_s123` 缺 `_a32` 后缀回退（1 个）

**结果**（N=16 mmlu/arc, N=24 gsm8k）：

| Bench | Model | calMAE | ΔMAE | γ̂ | PPP |
|---|---|---|---|---|---|
| mmlu | vanilla_2pl | **0.0068** | +0.0087 | — | 0.349 |
| mmlu | 2pl_gamma | 0.0072 | +0.0083 | 0.70 (n.s.) | 0.193 |
| arc | vanilla_2pl | **0.0158** | +0.0180 | — | 0.035 |
| arc | 2pl_gamma | 0.0201 | +0.0136 | 0.73 (sig) | 0.003 |
| gsm8k | vanilla_2pl | 0.0063 | +0.1631 | — | 0.691 |
| gsm8k | 2pl_gamma | **0.0062** | +0.1632 | 0.06 (n.s.) | 0.541 |

所有收敛诊断正常（Rhat<1.01, ESS>1300, 0 divergences）。vanilla_2pl 在 mmlu/arc 上 calMAE 略优；gsm8k 两者等价。γ 仅在 arc 上显著。ARC 的 PPP 过低值得关注。

---
