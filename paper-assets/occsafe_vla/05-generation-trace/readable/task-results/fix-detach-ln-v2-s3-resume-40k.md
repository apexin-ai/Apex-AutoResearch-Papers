# fix detach ln v2 s3 resume 40k

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_detach_ln_v2_s3_resume_40k_20260528T034604_result.json`
- **Structured JSON:** [`3bb1e0d42189c57c0cc0.json`](../../sessions/3b/3bb1e0d42189c57c0cc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练成功启动。

**结果汇总：**

| 项目 | 状态 |
|------|------|
| 40000_chkpt | 原始不完整（SIGHUP 中断了 safetensors 保存），已通过 35000 base + 40000 LoRA adapter 合并重建 |
| 训练 PID | 56822（GPU 3） |
| GPU 3 | 63000MiB / 97887MiB, 99% 利用率 |
| 起始 step | 40000（gradient_step_idx=0, log_step=40000） |
| 停止条件 | log_step == 50005, 即 ~10005 步 |
| 预计完成 | ~2.5h（约 14:25 UTC） |
| 日志 | `~/runs/occsafe_vla/detach_ln_v2_s3.log` |
| 首步 loss | action_loss=0.1299, occ_loss=0.0 |

注意：GPU 2 出现了两个新进程（PID 56474, 58736），不是本次操作产生的。GPU 0 的 detach_ln_v2_s2 (PID 47238) 正常运行。

---
