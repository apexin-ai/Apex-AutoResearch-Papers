# diagnose 10894 failures

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_10894_failures_20260526T182259_result.json`
- **Structured JSON:** [`048267eca35d310c3367.json`](../../sessions/04/048267eca35d310c3367.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全貌清晰了。当前四张 GPU 都已加载，三个实验已成功重启并在训练中。

---

## 诊断报告

### 根因：自动重试机制传了不存在的参数

三个实验在 02:08 的重试中，命令行被添加了 `--resume_from_checkpoint` 参数：

```
finetune.py: error: unrecognized arguments: --resume_from_checkpoint 
  /root/autodl-tmp/checkpoints/&lt;name>/openvla-7b+...--&lt;name>--20000_chkpt
```

**两个问题叠加**：
1. `finetune.py` 不认识 `--resume_from_checkpoint`（正确参数是 `--resume` + `--resume_step`）
2. 引用的 `20000_chkpt` 目录根本不存在（这三个实验从未跑到过 20000 步）

这导致 argparse 直接报错 exitcode=2，torchrun 包装后变成 EXIT_CODE=1。

### 训练进度

| 实验 | 最远步数 | 有 checkpoint？ |
|------|---------|-----------------|
| full_occ_ln_v2_s0 | ~275 | 无（仅 dataset_statistics.json） |
| full_occ_ln_v2_s1 | ~276 | 无 |
| detach_ln_v2_s0 | ~275 | 无 |

三个实验都从未达到首个 save_freq（10000 步），无可恢复的 checkpoint。

### 当前状态（02:25 重启后）

三个实验已于 02:25 被正确重启（不带错误参数），当前正在训练：

| GPU | 实验 | 显存占用 | GPU Util |
|-----|------|---------|----------|
| 0 | reverse_cutoff_s2_v2（其他实验） | 62203/97887 MiB | 43% |
| 1 | full_occ_ln_v2_s0 | 62203/97887 MiB | 99% |
| 2 | full_occ_ln_v2_s1 | 63013/97887 MiB | 99% |
| 3 | detach_ln_v2_s0 | 62203/97887 MiB | 99% |

磁盘空间充足（根分区 48%，autodl-tmp 51%）。

### 结论

- **不需要修复，已自行恢复**。02:25 的重启没有携带错误参数，三个实验已从头开始训练。
- **退出文件有 bug**：`/tmp/agent-ml-exit/*.exit` 中的时间戳格式 `%Y-%m-%dT%H:%M:%SZ` 未被正确展开（date 命令格式串可能未被正确引用）。
- **建议关注**：这三个实验需要跑 50005 步，按 ~1.08 it/s 约需 ~12.9 小时，预计完成时间约 May 27 15:25 UTC，在 DDL（May 28 12:00 UTC）之前。

---
