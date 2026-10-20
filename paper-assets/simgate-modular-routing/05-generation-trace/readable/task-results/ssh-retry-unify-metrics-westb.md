# ssh retry unify metrics westb

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_retry-unify-metrics-westb_20260518T173813_result.json`
- **Structured JSON:** [`58972bc9ce1873131ee1.json`](../../sessions/58/58972bc9ce1873131ee1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 保存在 `/root/autodl-tmp/simgate-modular-routing/analysis/analysis/unified_dose_response_data.json`（因为脚本在 analysis/ 下运行，默认输出路径又是 `analysis/...`，导致嵌套了一层）。

---

## Retry Unified Dose-Response (final_dr, 分母=200)

| cutoff k | Deaths | DR | Wilson 95% CI |
|----------|--------|----|---------------|
| 1 | 96 | 48.0% | [41.2%, 54.9%] |
| 2 | 94 | 47.0% | [40.2%, 53.9%] |
| 3 | 87 | 43.5% | [36.8%, 50.4%] |
| 4 | 86 | 43.0% | [36.3%, 49.9%] |
| 5 | 87 | 43.5% | [36.8%, 50.4%] |

Trial length distribution: {1: 14, 2: 3, 3: 1, 4: 2, 5: 180} (20 episodes 因 early success 提前终止)

**Cross-validation:**
- cutoff=5 DR = 43.5% vs ground truth 43.5%: **PASS**
- cutoff=1 DR = 48.0% vs ground truth 48.0%: **PASS**

**JSON 输出路径:** `/root/autodl-tmp/simgate-modular-routing/analysis/analysis/unified_dose_response_data.json`

**注意:** 原脚本的 `compute_dose_response` 在 `k > len(trials)` 时跳过 episode（变动分母），不符合"分母固定 200"的要求。上面的正确 final_dr 是通过 `min(k, len(trials))` 取最后可用 trial 来计算的。原脚本输出的 cutoff=2..5 行分母分别是 186/183/182/180，仅供参考。

---
