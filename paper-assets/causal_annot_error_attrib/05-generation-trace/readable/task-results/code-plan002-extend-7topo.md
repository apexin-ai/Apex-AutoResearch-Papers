# code plan002 extend 7topo

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan002-extend-7topo_20260520T153526_result.json`
- **Structured JSON:** [`d114ffa6756e08cc4a3c.json`](../../sessions/d1/d114ffa6756e08cc4a3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。20 秒跑完 7 拓扑 × 3 个 K 值 = 21 组实验，GPU RTX 5090。

## K=3 回归测试

| Metric | plan_001 参考值 | 本次结果 | 匹配 |
|--------|---------------|---------|------|
| M-bias τ_sflip | 0% | 0.0% | ✓ |
| M-bias violation | 53.2% | 58.4% | ≈ (N_large 差异) |
| M-bias amplif | 10.4% | 8.9% | ≈ |
| IV 极端 | 是 | τ_sflip=52.6%, max_bias=10.9M | ✓ |
| Front-door violation | ≈100% | 100.0% | ✓ |
| Front-door amplif | ≈100% | 100.0% | ✓ |
| Front-door τ_sflip | 0% | 0.0% | ✓ |

## 完整 7 拓扑 × K={3,5,7} 对比表

| Topology | K | τ_spec_sflip | all_sflip | violation | amplif | WC_d90 |
|----------|---|-------------|-----------|-----------|--------|--------|
| confounding | 3 | 0.0% | 99.3% | 100.0% | 100.0% | 0.1615 |
| confounding | 5 | 0.0% | 100.0% | 100.0% | 100.0% | 0.1130 |
| confounding | 7 | 0.0% | 100.0% | 100.0% | 100.0% | 0.0920 |
| mediation | 3 | 0.0% | 83.8% | 100.0% | 100.0% | 0.1231 |
| mediation | 5 | 0.0% | 96.6% | 100.0% | 100.0% | 0.0847 |
| mediation | 7 | 0.0% | 100.0% | 100.0% | 100.0% | 0.0602 |
| collider | 3 | 0.0% | 66.6% | 100.0% | 100.0% | 0.0482 |
| collider | 5 | 0.0% | 95.5% | 100.0% | 100.0% | 0.0462 |
| collider | 7 | 0.0% | 99.2% | 100.0% | 100.0% | 0.0358 |
| exposure | 3 | 99.0% | 99.0% | 100.0% | 99.9% | 0.2532 |
| exposure | 5 | 100.0% | 100.0% | 100.0% | 99.8% | 0.2185 |
| exposure | 7 | 100.0% | 100.0% | 100.0% | 99.9% | 0.1942 |
| **mbias** | **3** | **0.0%** | 66.7% | 58.4% | 8.9% | 0.0106 |
| **mbias** | **5** | **0.0%** | 95.4% | 100.0% | 0.0% | 0.0155 |
| **mbias** | **7** | **0.0%** | 99.2% | 100.0% | 0.0% | 0.0132 |
| **iv** | **3** | **52.6%** | 52.6% | 100.0% | 100.0% | 0.3061 |
| **iv** | **5** | **51.4%** | 51.4% | 100.0% | 100.0% | 0.4376 |
| **iv** | **7** | **52.3%** | 52.3% | 100.0% | 100.0% | 0.3766 |
| **frontdoor** | **3** | **0.0%** | 83.6% | 100.0% | 100.0% | 0.1425 |
| **frontdoor** | **5** | **0.0%** | 96.7% | 100.0% | 100.0% | 0.1025 |
| **frontdoor** | **7** | **0.0%** | 99.3% | 100.0% | 100.0% | 0.0757 |

## 论文可 claim 的结论

**τ_specific_sign_flip 在 K={3,5,7} 下全部 STABLE**：
- **5/7 拓扑 (confounding, mediation, collider, mbias, frontdoor)**: τ_sign_flip = 0.0% across all K — misclassification never flips the treatment effect sign
- **IV**: ~52% sign flip (K-invariant) — Wald estimator is fragile regardless of K
- **Exposure**: ~100% sign flip — direct treatment effect estimand is structurally sensitive

输出文件：
- 脚本: `/home/sonny/causal_annot_error_attrib/plan_002_k57_extended_7topo.py`
- 日志: `/home/sonny/causal_annot_error_attrib/plan002_7topo_run.log`

---
