# diagnose mvp occ s3 v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_occ_s3_v2_20260525T203037_result.json`
- **Structured JSON:** [`f6d9ec7568758cb02f0e.json`](../../sessions/f6/f6d9ec7568758cb02f0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结果

**根因**：`/root/autodl-tmp` 磁盘 100% 满（250G/250G，剩余 292K），导致 step 30000 checkpoint 保存时 tokenizer.json 写入失败（`No space left on device, os error 28`）。

**训练进度**：已完成 local step 30000（从 20K resume，即全局 50K），训练本身已跑完。崩溃发生在保存最终 checkpoint 阶段。

**Checkpoint 状态**：
- 30000_chkpt 目录已创建，但 **不完整**——`lora_adapter/` 为空目录，`tokenizer.json` 为 0 字节。此 checkpoint 不可用。
- 20000_chkpt 和 10000_chkpt 存在且应完整可用。

**GPU cuda:1 状态**：空闲（0 MiB / 97887 MiB, 0% util）。cuda:2、cuda:3 也空闲。仅 cuda:0 有任务在跑（62GB used, 99% util）。

## 建议

需要先清磁盘空间，然后从 20000_chkpt resume 重跑最后 10K steps：
1. 清理磁盘（删旧 checkpoint 或无用模型缓存释放空间）
2. 从 `mvp_occ_s3--20000_chkpt` resume，只需跑 step 20001→30000（约 2.5h）
3. 注意：约束 C002 禁止 cutoff/reverse_cutoff 实验用 resume，但 mvp_occ_s3 不是 cutoff 实验，可以 resume

---
