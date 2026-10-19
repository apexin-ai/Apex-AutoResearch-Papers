# analysis v3 lora batch

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v3_lora_batch_20260516T200329_result.json`
- **Structured JSON:** [`4630041dc4c6a5149a85.json`](../../sessions/46/4630041dc4c6a5149a85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，报告已保存到 `artifacts/v3_training_analysis.md`。

关键结果：

| exp_id | initial_loss | final_loss | loss_ratio | status |
|--------|-------------|------------|------------|--------|
| physical_r16 | 1.8865 | **0.5876** | 3.21 | SUCCESS |
| spatial_r16 | 1.8081 | **0.6126** | 2.95 | SUCCESS |
| universal_r16 | 1.8050 | **0.6030** | 2.99 | SUCCESS |

3 个实验全部正常完成（EXIT_CODE=0，无 traceback），各 10000 steps，每个 ~170 min。Final adapter 各 15MB。

**与 Phase 1 的显著差异：** V3 final loss（0.59-0.61）比 Phase 1（~0.01）高约 50 倍。Loss 曲线从 ~1.8 稳定收敛到 ~0.6，后半段已趋平，说明不是收敛不充分——而是 V3 的 loss 计算方式或训练目标与 Phase 1 本质不同。

---
