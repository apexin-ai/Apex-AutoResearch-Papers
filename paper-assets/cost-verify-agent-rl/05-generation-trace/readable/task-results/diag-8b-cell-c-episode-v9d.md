# diag 8b cell c episode v9d

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_8b_cell_c_episode_v9d_20260520T022200_result.json`
- **Structured JSON:** [`78bd885ddc8c0a691379.json`](../../sessions/78/78bd885ddc8c0a691379.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论**：v9d 的训练本身完全成功（5 步，success 40.6%→81.25%），**不是 v9c 的 prompt overflow 问题**。崩溃发生在 step 4 后保存 checkpoint 时，`torch.save` 写 optimizer state dict 到 `/root/autodl-tmp` 时因磁盘几乎满（91%，仅剩 23GB）导致 zip 文件写入错误。

根因：`/root/autodl-tmp/checkpoints/` 积累了 174GB 旧 checkpoint（scienceworld_sft 108GB、qwen3_8b_sft_v1 31GB），挤占了空间。

修复：清理旧 checkpoint 释放 ~139GB，并考虑 `save_contents: ['model']`（不保存 optimizer）+ `save_freq: 10`（减少保存次数）后重跑。

报告已写入 `artifacts/8b_cell_c_episode_v9d/report/diag_v9d.md`。

---
