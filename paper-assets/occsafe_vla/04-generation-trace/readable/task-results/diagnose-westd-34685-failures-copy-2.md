# diagnose westd 34685 failures

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd-34685-failures_20260522T072817_result.json`
- **Structured JSON:** [`4cb01348f425ab6caad6.json`](../../sessions/4c/4cb01348f425ab6caad6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因：数据盘 `/root/autodl-tmp` 磁盘空间耗尽

```
/dev/md127    350G  350G  300K  100%  /root/autodl-tmp
```

三个实验在几乎同一时刻触发 checkpoint 保存，全部因 `No space left on device (os error 28)` 失败。

### 各实验错误详情

| 实验 | 崩溃时刻 | 崩溃点 | 错误 |
|------|---------|--------|------|
| depth_s0 | 15:24:39 UTC | 保存 step 15000 merged checkpoint | `safetensors_rust.SafetensorError: I/O error: No space left on device` |
| depth_s1 | 15:24:38 UTC | 保存 step 15000 merged checkpoint | 同上 |
| cutoff_s1 | 15:24:37 UTC | 保存 step 2500 merged checkpoint | 同上 |

三者崩溃栈完全一致：`finetune.py:1254 → save_training_checkpoint → merged_vla.save_pretrained → safe_save_file`

### 磁盘占用明细

| 目录 | 大小 |
|------|------|
| occ_s1_fresh | **149G** |
| depth_s1 | 80G |
| depth_s0 | 76G |
| cutoff_s0 | 15G |
| cutoff_s1 | 11G |
| 其他日志 | ~10M |
| **合计** | ~331G / 350G |

`occ_s1_fresh` 独占 149G，是最大的空间消耗者。

### cutoff_s0 状态

仍在运行（GPU 0, step ~2837/50005, ~1.08 it/s），但**即将在 step 5000 保存 checkpoint 时同样崩溃**，因为磁盘仍然满。预计约 33 分钟后触发。

### 能否直接重启

**不能。** 磁盘满的问题不解决，重启后三个实验还是会在第一个 checkpoint 处崩溃。需要先清理空间：

1. **最有效**：如果 `occ_s1_fresh`（149G）的旧 checkpoint 不再需要，清理它可以立刻释放大量空间
2. depth_s0/depth_s1 各有 6 个 checkpoint（每个 ~13G），可以只保留最新的，删掉旧的
3. **紧急**：cutoff_s0 大约 33 分钟后也会撞上同样的问题，需要尽快清理

---
