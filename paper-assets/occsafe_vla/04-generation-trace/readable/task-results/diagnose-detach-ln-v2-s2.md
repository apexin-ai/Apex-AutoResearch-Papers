# diagnose detach ln v2 s2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_detach_ln_v2_s2_20260528T091041_result.json`
- **Structured JSON:** [`4795f730547df2b0e95b.json`](../../sessions/47/4795f730547df2b0e95b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 训练实际已成功完成，EXIT_CODE=1 是误报

**直接原因**: EXIT_CODE=1 来自 PyTorch distributed 清理问题：
```
[rank0]:[W528 17:08:28] WARNING: destroy_process_group() was not called before program exit
```
这是一个 cleanup warning，不是训练错误。

**根因分析**: 

日志开头显示本次 run 从 25000_chkpt 恢复：
```
Fine-tuning OpenVLA Model `.../detach_ln_v2_s2--25000_chkpt`
```

训练从全局 step 25000 开始，又跑了 ~25006 iterations，全局步数达到 ~50006 ≥ max_steps(50005)，触发正常停止。进度条显示 50% (25006/50005) 是因为它显示的是当前 run 的 batch_idx 而非全局步数——**这是预期行为**。

**完成证据**:
- `50000_chkpt` 已保存 (May 28 17:09)
- `45000_chkpt` 已保存 (May 28 15:51)
- 日志末尾：`Max step 50005 reached! Stopping training...`
- 无 OOM / CUDA error / Python traceback

**Checkpoint 列表**:
| Checkpoint | 时间 |
|---|---|
| 25000_chkpt_backup | May 28 10:15 |
| 25000_chkpt | May 28 14:16 (重新保存) |
| 45000_chkpt | May 28 15:51 |
| **50000_chkpt** | **May 28 17:09** |

### 结论

- **不需要重启** — 训练已完成全部 50000 步，最终 checkpoint 已保存
- **反复 retry 的原因**: job manager 把 EXIT_CODE=1 当失败处理，但实际是 torch distributed 的 cleanup warning 导致的非零退出码
- **GPU cuda:0 状态**: 有一个进程 PID 179444 占用 ~16.7GB，不是本实验（已结束），可能是其他实验或残留进程
- **磁盘空间**: 正常，根分区 39%，数据盘 2%

**下一步**: 直接用 `50000_chkpt` 进行评估即可，无需再跑训练。如需修复 exit code 问题防止未来误报，可在训练脚本末尾加 `dist.destroy_process_group()` 调用。

---
