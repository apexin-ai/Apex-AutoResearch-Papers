# analysis eval pi05 random k03 long seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_random_k03_long_seed42_postfix_20260524T162012_result.json`
- **Structured JSON:** [`cf08650f197fbf6db362.json`](../../sessions/cf/cf08650f197fbf6db362.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个服务器都有完整日志，实验均已正常结束。

## 实验结果

- **exp_id**: eval_pi05_random_k03_long_seed42_postfix
- **Overall SR**: 30.0% (cqa1-33015) / 29.6% (westd-38929)，两次运行高度一致，取均值 **29.8%**

### Per-task SR

| Task | Description | SR (cqa1) | SR (westd) |
|------|-------------|-----------|------------|
| T0 | put both the alphabet soup and the tomat... | 34% | 36% |
| T1 | put both the cream cheese box and the bu... | 12% | 8% |
| T2 | turn on the stove and put the moka pot o... | 62% | 64% |
| T3 | put the black bowl in the bottom drawer | 78% | 76% |
| T4 | put the white mug on the left plate and... | 18% | 30% |
| T5 | pick up the book and place it in the bac... | 32% | 20% |
| T6 | put the white mug on the plate and put t... | 6% | 6% |
| T7 | put both the alphabet soup and the cream... | 20% | 22% |
| T8 | put both moka pots on the stove | 10% | 8% |
| T9 | put the yellow and white mug in the micr... | 28% | 26% |

- **Conclusion**: success（实验正常完成，无错误）
- **结果文件**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.30_libero_10_seed42.json`

### Long Random Disruption Curve 完整数据

| k | SR | 备注 |
|------|-------|------|
| 0.95 | 63.2% | |
| 0.90 | 32.0% | |
| 0.85 | 45.2% | |
| 0.70 | 65.8% | |
| 0.50 | 46.8% | |
| **0.30** | **29.8%** | ← 本实验 |

### 关键发现

1. **k=0.3 是 Long suite 的最低点**，29.8% 低于所有其他 k 值，符合"极端 pruning 应导致最大性能下降"的预期。
2. **跨 suite 对比 k=0.3**：Long (29.8%) < Spatial (43.4%) < Goal (52.8%) < Object (32.2%)。Long 和 Object 在极端 pruning 下最脆弱。
3. **Long 的 disruption curve 整体呈非单调**（k=0.70 最高 65.8%，k=0.30 最低 29.8%），与其他 suite 的 random pruning 表现类似——random pruning 没有稳定的单调递减关系。
4. **任务方差极大**：T3（黑碗放抽屉）在 k=0.3 仍有 77%，而 T6/T8 降到 6-10%，说明 Long 任务中复杂多步任务对 token 数量更敏感。

---
