# diag sft sweep failures westd

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_sft_sweep_failures_westd_20260520T013204_result.json`
- **Structured JSON:** [`ab362d28d7c489b34c3f.json`](../../sessions/ab/ab362d28d7c489b34c3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：根分区 30GB 磁盘满（`/root/.cache/huggingface` 占 20GB）。两个 sweep 各完成 d000-d050 后，HF datasets cache 填满根分区，d100 均失败。

**具体情况**：
- **Qwen2.5-14B d100**：在 `datasets.map()` 阶段 ENOSPC，训练未开始
- **gemma-2-9b d100**：训练跑到 21%（step 888/4159）后崩溃，无 checkpoint 保存
- 两个模型的 d000/d005/d025/d050 均正常完成

**额外发现**：两个脚本缺 `set -e`，Python 崩溃后 shell 报 `exit code=0`（假成功），这是 cron 报 "no sentinel/W&B" 而非 "exit code non-zero" 的原因。

报告已写到 `artifacts/diag_sft_sweep_failures_westd.md`。重试前需清理根分区 cache 并设置 `HF_HOME` 到数据盘。

---
