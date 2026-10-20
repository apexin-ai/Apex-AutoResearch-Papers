# code pooled irt 2pl fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pooled_irt_2pl_fix_20260516T150336_result.json`
- **Structured JSON:** [`a6a4ad5f8d56d0c27c4d.json`](../../sessions/a6/a6a4ad5f8d56d0c27c4d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

**MMLU (2PL+γ, N=8)**: ✅ 通过 C008
- PPP=0.426（模型拟合良好），cal_mae=0.0023 < raw_mae=0.0078，校准改善 +0.0055
- γ=-0.259，95% CI 含 0 → MMLU 的 RRF exposure signal 对得分影响不显著

**ARC (2PL+γ, N=8)**: ❌ 未通过 C008
- PPP=0.002（拟合差），cal_mae=0.0362 > raw_mae=0.0088
- 但比 4PL+γ 明显好转（恶化从 -0.077 降到 -0.028）
- γ=1.307，95% CI=[0.37, 2.26] 排除 0 → exposure signal 显著，但模型仍无法将其正确转化为校准

ARC 的问题已不是过参数化（2PL 仅 2 个 item 参数），更可能是 N=8 下 item 参数估计精度不够，或 ARC 的 exposure-accuracy 关系非单调。

---
