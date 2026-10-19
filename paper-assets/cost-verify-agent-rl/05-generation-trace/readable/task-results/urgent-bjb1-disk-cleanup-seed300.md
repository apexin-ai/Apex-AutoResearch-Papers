# urgent bjb1 disk cleanup seed300

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_bjb1_disk_cleanup_seed300_20260522T181558_result.json`
- **Structured JSON:** [`3cc2b6a1a9fdf5597159.json`](../../sessions/3c/3cc2b6a1a9fdf5597159.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**清理结果：**

| | 清理前 | 清理后 |
|---|---|---|
| 已用 | 243G | 222G |
| 可用 | 7.8G | **29G** |
| 使用率 | 97% | 89% |

**释放 ~21.2GB**，目标 ≥10GB 达成。

**删除内容：**
- `/root/autodl-tmp/checkpoints/exp029-seed300/`（21GB FSDP checkpoint）
- `/root/autodl-tmp/tmp/*`（244MB）
- `/tmp/ray` 30分钟以上的旧日志

**未删除 / 安全确认：**
- `qwen_exp029_seed300_step5_hf` → symlink 指向 `exp029_seed300_step5_hf`（独立 HF checkpoint，~4GB），完好 ✓
- PID 433097（ray::TaskRunner, 6.5GB RSS）存活 ✓ — **未 kill**，因为它就是 eval 进程本身

---
