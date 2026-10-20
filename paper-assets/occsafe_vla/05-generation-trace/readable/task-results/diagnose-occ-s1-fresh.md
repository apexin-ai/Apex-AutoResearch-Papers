# diagnose occ s1 fresh

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_occ_s1_fresh_20260522T040304_result.json`
- **Structured JSON:** [`3f8e70fbecaf7c2c5863.json`](../../sessions/3f/3f8e70fbecaf7c2c5863.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：occ_s1_fresh

### 结论：训练已正常完成，EXIT_CODE=129 是误报

| 项目 | 详情 |
|------|------|
| **训练进度** | 50005/50005 (100%) |
| **最后指标** | step=50000, occ_loss=0.0089, action_loss=0.0496 |
| **最后 checkpoint** | `50000_chkpt` — 完整（4 个 safetensors 分片 + action_head + occ_head + proprio_projector + lora_adapter 全部保存） |
| **磁盘** | 200G/350G (58%)，充足 |
| **Traceback/OOM** | 无 |

### EXIT_CODE=129 根因

日志末尾明确打印了 `Max step 50005 reached! Stopping training...`，训练已跑完所有步数。之后 PyTorch 发出 `destroy_process_group() was not called before program exit` 警告，说明进程是在分布式清理阶段（而非训练阶段）收到 SIGHUP。

因为是 nohup 启动而非 tmux，SSH session 断开时发送的 SIGHUP 在进程退出清理期间被捕获，导致退出码为 129 而非 0。**训练本身无任何异常。**

### 行动建议

- **无需重跑。** 50000 checkpoint 是最终可用模型，最后 5 步（50001-50005）没有触发额外保存，loss 在该阶段已收敛。
- 后续实验建议用 `submit_training_job`（走 tmux），避免 nohup 的 SIGHUP 问题导致退出码误报。

---
