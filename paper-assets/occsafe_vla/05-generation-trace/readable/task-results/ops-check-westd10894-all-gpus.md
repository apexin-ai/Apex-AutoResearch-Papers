# ops check westd10894 all gpus

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_westd10894_all_gpus_20260523T135815_result.json`
- **Structured JSON:** [`bb12e11a373181a06791.json`](../../sessions/bb/bb12e11a373181a06791.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**根因：数据盘 `/root/autodl-tmp` 250G 100% 满。全部 4 个实验在保存 checkpoint 时因 `No space left on device (errno 28)` 崩溃。**

---

```
exp_id: detach_ln_s0
状态: 崩溃
崩溃时间: 2026-05-23 21:54:29
错误: OSError: [Errno 28] No space left on device (保存 30K checkpoint 时 tokenizer.model 写入失败)
最终 step: ~30000 (30K checkpoint 损坏，仅有 tokenizer 文件，无 model shards)
最后完好 checkpoint: 20K (4/4 model shards + action_head + occ_head + proprio_projector)
50K checkpoint: 无
eval 提交: 否(未完成训练)
```

```
exp_id: detach_ln_s1
状态: 崩溃
崩溃时间: 2026-05-23 21:55:35
错误: ChildFailedError (磁盘满，30K checkpoint 目录未创建)
最终 step: ~30000 (20K 后又跑了 ~2.5h)
最后完好 checkpoint: 20K (4/4 model shards 完整)
50K checkpoint: 无
eval 提交: 否(未完成训练)
```

```
exp_id: detach_ln_s2
状态: 崩溃
崩溃时间: 2026-05-23 19:20:54
错误: safetensors_rust.SafetensorError: I/O error: No space left on device (保存 20K checkpoint 序列化失败)
最终 step: ~20000 (20K checkpoint 损坏，仅 2/4 model shards)
最后完好 checkpoint: 10K (4/4 model shards 完整)
50K checkpoint: 无
eval 提交: 否(未完成训练)
```

```
exp_id: cutoff_s2_v2
状态: 崩溃
崩溃时间: 2026-05-23 20:29:15
错误: Exception: No space left on device (保存 10K checkpoint 失败)
最终 step: 10000 (10K checkpoint 损坏，仅 532K tokenizer 文件，lora_adapter 目录为空)
最后完好 checkpoint: 无 (仅有初始权重目录)
50K checkpoint: 无
eval 提交: 否(未完成训练)
```

---

### 磁盘占用分析

| 目录 | 大小 | 备注 |
|------|------|------|
| cutoff_s2 (旧实验) | 74G | 最大占用 |
| detach_ln_s0 | 30G | 含损坏 30K |
| detach_ln_s1 | 30G | |
| detach_ln_s2 | 21G | 含损坏 20K |
| ablation_occ_detach_s2 | 15G | 旧实验 |
| ablation_random_occ_s2 | 15G | 旧实验 |
| depth_s2 | 15G | 旧实验 |
| depth_s3 | 15G | 旧实验 |
| cutoff_s2_v2 | 540K | 损坏 |

**旧实验 (cutoff_s2 + ablation × 2 + depth × 2) 占 134G。** 清理这些 + 损坏 checkpoint 可腾出 ~140G 空间，足够恢复训练。等你指令。

---
