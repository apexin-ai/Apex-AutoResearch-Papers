# diagnose eval mlp adapter seed43 done

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_mlp_adapter_seed43_done_20260519T134657_result.json`
- **Structured JSON:** [`b8b43751541ca9a52022.json`](../../sessions/b8/b8b43751541ca9a52022.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

## 报告

**eval_mlp_adapter_seed43** — 已完成，状态正常退出。

| 指标 | 值 |
|------|-----|
| Overall SR | **64.6%** (323/500) |
| Wilson 95% CI | [60.3%, 68.7%] |

**Per-task SR:**

| Task | SR |
|------|-----|
| T0 alphabet_soup | 74% |
| T1 cream_cheese | 74% |
| T2 salad_dressing | 66% |
| T3 bbq_sauce | 44% |
| T4 ketchup | 56% |
| T5 tomato_sauce | 64% |
| T6 butter | **86%** |
| T7 milk | 58% |
| T8 chocolate_pudding | 72% |
| T9 orange_juice | 52% |

**Conclusion: negative** — 原假设"MLP显著低于cross-attention"再次被拒。Seed 43 (64.6%) 与 seed 42 (65.2%) 高度一致（差 0.6pp），且两者 CI 几乎完全重叠，MLP adapter 结果稳健。

对比 cross-attention M=32 三seed均值 61.2±1.4%，MLP adapter 两seed均值 64.9% 甚至略高，进一步说明在 LIBERO-Object 上 cross-attention 机制相比 MLP+avg-pool 无显著优势。

**Registry 已更新**: metrics、conclusion=negative、status=DONE。westd-27271 cuda:0 现已释放，可用于 eval_mlp_adapter_seed44。

---
