# eval imm fullft dryrun westd

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_imm_fullft_dryrun_westd_20260516T200732_result.json`
- **Structured JSON:** [`1ea2fb3f35b8103abc0a.json`](../../sessions/1e/1ea2fb3f35b8103abc0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成，全部通过。

```
=== IMM FULLFT DRY-RUN REPORT ===
Status: PASS
Stage 1: ACIS grad=7/10 (trainable), Expert frozen=YES (0 with grad, expect 0)
Stage 2: Expert grad=155/155 (all trainable), ACIS frozen=YES (0 with grad, expect 0)
Loss: stage1 margin_loss=0.2998, stage2 action_loss=0.1209 (total=0.4201)
Error: None
```

关键确认项：
1. **Stage 1** — Expert params 0 有梯度（冻结 ✓），ACIS 7/10 有梯度 ✓
2. **Stage 2** — ACIS 0 有梯度（冻结 ✓），Expert 155/155 有梯度 ✓
3. **无 empty optimizer 报错** ✓
4. **Loss 合理**（非 NaN、非 0）✓
5. Checkpoint 已正确加载（step 50000）✓
6. Full FT 模式：trainable=99.8M/450M (22.2%) expert params ✓

Pipeline 验证通过，可以启动正式训练。

---
