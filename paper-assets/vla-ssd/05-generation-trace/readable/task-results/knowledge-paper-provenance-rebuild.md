# knowledge paper provenance rebuild

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_paper_provenance_rebuild_20260518T174151_result.json`
- **Structured JSON:** [`87ba4c27e36f69ed31ed.json`](../../sessions/87/87ba4c27e36f69ed31ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

映射完成。结果汇总：

**新增 13 条 tier1 claims（C430-C442），覆盖全部 8 个实验：**

| 实验 | Claims | 位置 |
|------|--------|------|
| `dose_response_curve` | C430 (数据), C431 (机制) | §4.3 + Discussion (4) |
| `counterfactual_instruction` | C432 (数据), C433 (机制) | §4.3 + Discussion (5) |
| `action_trajectory_analysis` | C434 (数据), C435 (机制) | §4.3 + Discussion (3) |
| `action_trajectory_control` | C436 (数据), C437 (机制+permutation) | §4.3 + Discussion per-head |
| `ablation_50demos_main` | C438 (数据), C439 (机制) | §4.3 + Discussion (2) |
| `random_subset_ablation` | C440 | §4.3 random subset |
| `permutation_test_I2` | C441 + C437(共享) | Appendix §A.8 |
| `threecond_multiseed_r2_v2` | C442 | §4.1 + §4.2 |

**覆盖率：69/74 → 74/74（100%）**，tier1 从 0 升至 18，tier2 从 69 降至 64。

**剩余 gap：无。** 2 条 tierX（无证据的定性 claim）不影响实验覆盖率。

---
