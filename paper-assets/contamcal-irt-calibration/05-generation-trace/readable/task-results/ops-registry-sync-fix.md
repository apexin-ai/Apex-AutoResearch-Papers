# ops registry sync fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry_sync_fix_20260514T011534_result.json`
- **Structured JSON:** [`83b5abfed2fac486dcf7.json`](../../sessions/83/83b5abfed2fac486dcf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 项全部完成，报告如下：

---

### 1. exp_001_sft_d100_15B_v2 ✅
- **PID 251924** 确认在跑，GPU 0，10044 MiB 显存占用
- **command** 正确：`--batch-size 1 --grad-accum 16`（非 batch-size 2）
- **日志** `exp_001_sft_d100_15B_v2.log` 已存在（9982 bytes），无需修复
- **registry** 已在项目 registry 创建：PREPARING → QUEUED → RUNNING，spec 含 pid=251924、正确 command、log_path、checkpoint_path，parent=exp_001_sft_d100_15B

### 2. 旧日志确认 ✅
- `exp_001_sft_d100_15B.log`：55 行，末尾为 `torch.OutOfMemoryError: CUDA out of memory`（model.to(device) 时 OOM，GPU 0 被 PID 248703 占 20.07 GiB）
- 属于失败的 v1，已保留不删除

### 3. exp_001_eval_15B_d000_s123 ✅
- **PID 250600** 确认在跑，CUDA_VISIBLE_DEVICES=5（GPU 5，子进程 PID 250610 占 5820 MiB）
- **registry** 已从 PREPARING → QUEUED → RUNNING
- spec 已更新：pid=250600, gpu=cuda:5, model_name=Qwen2.5-1.5B, seed=123, checkpoint_source=exp_001_sft_0pct_15B_s123, eval_data=mmlu,gsm8k,arc_challenge,humaneval

---
