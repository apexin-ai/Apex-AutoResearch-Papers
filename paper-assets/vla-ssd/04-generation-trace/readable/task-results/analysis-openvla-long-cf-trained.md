# analysis openvla long cf trained

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_openvla_long_cf_trained_20260521T224214_result.json`
- **Structured JSON:** [`5b77f3d5f38cb1ea9f8d.json`](../../sessions/5b/5b77f3d5f38cb1ea9f8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果: `openvla_long_cf_trained`

**状态**: 成功完成 (EXIT_CODE=0, 90.0 min)

### Counterfactual Sensitivity (Cohen's d, global)

| Rank | Condition | Cohen's d | Cross-task mean d | MSE mean | Token div |
|------|-----------|-----------|-------------------|----------|-----------|
| 1 | **shuffled** | 0.5646 | 0.5664 | 0.032518 | 0.999 |
| 2 | **wrong** | 0.5453 | 0.5452 | 0.030466 | 0.999 |
| 3 | **empty** | 0.5048 | 0.5063 | 0.026031 | 1.000 |
| 4 | **paraphrased** | 0.4486 | 0.4454 | 0.022493 | 0.957 |

### Ranking 对比

- **Hypothesized**: empty > wrong > shuffled > para
- **Observed**: shuffled > wrong > empty > para

Paraphrased 最低这一点与其他 suite 一致，但 shuffled 升至第一、empty 降至第三，与 Goal/Spatial/Object suite 的 ordering 不同。Top-3 条件间差距较小（d=0.50–0.56），paraphrased 明显低于其余三者。

### 注意事项
- Paraphrased 的 token_divergence=0.957 明显低于其他条件（~1.0），符合语义保留预期
- Per-task variance: paraphrased 的 CV=0.2516 最高，部分 task d 低至 0.28（LIVING_ROOM_SCENE5/6）
- 无 untrained 对照数据（遵守 C001: 不下 trained vs untrained 对比结论）

### 文件路径
- **log_path**: `~/runs/vla-ssd/openvla_long_cf_trained.log`
- **result_path**: `/root/autodl-tmp/vla-ssd/results/libero_long/counterfactual_combined.json`
- **checkpoint**: `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-oft-finetuned-libero-10`

---
