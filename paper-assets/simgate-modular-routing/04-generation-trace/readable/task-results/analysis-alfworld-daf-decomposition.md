# analysis alfworld daf decomposition

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alfworld-daf-decomposition_20260516T061925_result.json`
- **Structured JSON:** [`83d6d3a038d60ac8b92d.json`](../../sessions/83/83d6d3a038d60ac8b92d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果总结：

**Overall (N=135, 6 task types)**
- det SR: 27.41%, int SR: 2.96%, Δ_full = 0.2444, 95% CI [0.170, 0.326]
- **DAF = 1.0 (CI: [1.0, 1.0])**  — 因为 ALFWorld 是 binary outcome (0/1), 当 both succeed 时 Δ_non-failure 恒为 0，所以 DAF 在数学上恒等于 1.0。这是二值环境的必然结果，不像 ScienceWorld 有连续分数。
- Pearson r = 1.0 (p=0.000) — 同理，failure_diff ≡ delta（代数恒等式），不含额外信息。

**Per-task breakdown**

| Task type | n | det SR | int SR | Δ | Δ CI |
|---|---|---|---|---|---|
| pick_and_place | 32 | 56.3% | 0.0% | 0.563 | [0.375, 0.719] |
| look_at_obj_in_light | 13 | 38.5% | 15.4% | 0.231 | [0.0, 0.462] |
| pick_cool_then_place | 24 | 16.7% | 0.0% | 0.167 | [0.042, 0.333] |
| pick_clean_then_place | 27 | 18.5% | 3.7% | 0.148 | [0.0, 0.333] |
| pick_heat_then_place | 16 | 18.8% | 6.3% | 0.125 | [-0.125, 0.375] |
| pick_two_obj_and_place | 23 | 8.7% | 0.0% | 0.087 | [0.0, 0.217] |

**Label 验证**: det_preferred=35 (25.9%), internal_preferred=2 (1.5%), no_preference=98 (72.6%) — 与 registry 一致。

**关键发现**: DAF=1.0 是 binary-outcome 环境的 tautology。ALFWorld 的 DAF 分解不像 ScienceWorld 那样有分析价值——因为没有 partial scores，整个 det-internal gap 在数学上完全由 failure rate 差异解释。如果要做更有意义的 ALFWorld 分解，需要引入步数效率等连续指标作为 proxy score。

脚本和结果已保存：
- 脚本: `/root/autodl-tmp/simgate-modular-routing/scripts/alfworld_daf_analysis.py`
- JSON: `/root/autodl-tmp/simgate-modular-routing/artifacts/alfworld-daf/alfworld_daf_results.json`

---
