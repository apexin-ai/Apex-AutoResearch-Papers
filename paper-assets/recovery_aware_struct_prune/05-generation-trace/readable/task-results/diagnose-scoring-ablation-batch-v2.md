# diagnose scoring ablation batch v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scoring_ablation_batch_v2_20260517T102338_result.json`
- **Structured JSON:** [`bf53c8e0d8c9dd2e4d56.json`](../../sessions/bf/bf53c8e0d8c9dd2e4d56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。让我总结发现并确认最终状态。

**诊断结果：**

1. **scoring_ablation_batch_v2** 只跑到 magnitude eval 60/200 就被 `Terminated`（仅 107 行日志），从未到达 gradient 阶段。
2. **gradient SFT 失败**发生在单独的 pipeline（`ablation_log.txt`），在 step 935/1870 因 `No space left on device (os error 28)` 中断。
3. **gradient_sft_v3** 也失败了（CUDA OOM at step 0），但 `sft_gradient_20` 目录确实有成功的模型（May 17 18:02），eval_gradient_postsft.json 显示 acc=0.615，说明有另一次成功重试。
4. **磁盘当前状态**：`/dev/md0` 49% (6.9T/14T)，根分区 29% (8.6G/30G)，已经不满了。
5. **没有 batch_v2 产生的 gradient_sft 中间 checkpoint**可清理（batch 从未到 gradient 阶段）。
6. 发现 2 个**可清理的冗余 checkpoint 目录**（共 23G）：
   - `sft_standard_25/checkpoint-1870` (11G)
   - `sft_rasp_rlvr_20/checkpoint-1870` (12G)

这两个 checkpoint 目录是训练中间保存点，对应的最终模型已经保存在父目录。要清理它们来释放 23G 空间吗？

无论如何，先输出诊断结果：

```json
{
  "root_cause": "gradient SFT (独立 pipeline, 非 batch_v2) 在 step 935/1870 保存 checkpoint 时因 autodl-tmp 磁盘满 (No space left on device, os error 28) 失败。batch_v2 本身仅执行到 magnitude eval 60/200 时被 Terminated，从未到达 gradient 阶段。",
  "error_type": "resource",
  "disk_before": "/dev/md0 6.9T/14T (49%), root 8.6G/30G (29%) — 磁盘已恢复，当时满但现已有空间",
  "disk_after": "未执行清理 — 无 batch_v2 产生的 gradient_sft checkpoint 可删除。可选清理: 2个冗余 checkpoint-1870 目录共 23G",
  "fix_steps": [
    "确认 batch_v2 未产生 gradient_sft checkpoint（batch 在 magnitude eval 就终止了）",
    "确认 sft_gradient_20 已有成功模型 (acc=0.615)，不应删除",
    "可选：删除 sft_standard_25/checkpoint-1870 (11G) + sft_rasp_rlvr_20/checkpoint-1870 (12G) 释放 23G"
  ],
  "can_retry": true,
  "retry_notes": "1) 磁盘当前充足 (49%)，可直接重跑 batch。2) batch 脚本需按顺序跑 4 个方法，gradient 和 random 已有独立结果（pruned_gradient_20, sft_gradient_20, pruned_random_20），可修改脚本跳过已完成的方法。3) magnitude 阶段需修复 eval shape mismatch（v2 已加 --skip_attention 解决）但 magnitude 的 pruned 模型和 SFT 都未完成。4) cka_only 也未开始。5) 建议先删除 23G 冗余 checkpoint 预留空间。"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "gradient SFT (独立 pipeline, 非 batch_v2) 在 step 935/1870 保存 checkpoint 时因 autodl-tmp 磁盘满 (No space left on device, os error 28) 失败。batch_v2 本身仅执行到 magnitude eval 60/200 时被 Terminated，从未到达 gradient 阶段。",
    "error_type": "resource",
    "disk_before": "/dev/md0 6.9T/14T (49%), root 8.6G/30G (29%) — 磁盘已恢复，当时满但现已有空间",
    "disk_after": "未执行清理 — 无 batch_v2 产生的 gradient_sft checkpoint 可删除。可选清理: 2个冗余 checkpoint-1870 目录共 23G",
    "fix_steps": [
      "确认 batch_v2 未产生 gradient_sft checkpoint（batch 在 magnitude eval 就终止了）",
      "确认 sft_gradient_20 已有成功模型 (acc=0.615)，不应删除",
      "可选：删除 sft_standard_25/checkpoint-1870 (11G) + sft_rasp_rlvr_20/checkpoint-1870 (12G) 释放 23G"
    ],
    "can_retry": true,
    "retry_notes": "1) 磁盘当前充足 (49%)，可直接重跑 batch。2) batch 脚本需按顺序跑 4 个方法，gradient 和 random 已有独立结果（pruned_gradient_20, sft_gradient_20, pruned_random_20），可修改脚本跳过已完成的方法。3) magnitude 阶段需修复 eval shape mismatch（v2 已加 --skip_attention 解决）但 magnitude 的 pruned 模型和 SFT 都未完成。4) cka_only 也未开始。5) 建议先删除 23G 冗余 checkpoint 预留空间。"
  }
}
```

</details>

---
