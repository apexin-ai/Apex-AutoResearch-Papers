# diagnose full occ ln v2 s3

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full_occ_ln_v2_s3_20260528T040308_result.json`
- **Structured JSON:** [`9abd56acf9e821c92134.json`](../../sessions/9a/9abd56acf9e821c92134.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是诊断报告。

---

## 诊断报告（2026-05-28 12:05 北京时间）

**DDL: 20:00 北京时间，剩余 ~7h55m**

---

### 1. full_occ_ln_v2_s3 状态

**存活，但有严重问题。** PID 56474 在 westd-34685 GPU 2 上运行，GPU 利用率 80%，显存 62152MiB。

**发生了什么：** 训练到 step 40000 时保存了 checkpoint，之后 cron 重启了进程（用 `--resume True --resume_step 40000`）。第一次重启时加载 `proprio_projector--40000_checkpoint.pt` 从错误路径（`/root/autodl-tmp/models/openvla-7b/` 而非 checkpoint 目录）导致 `FileNotFoundError` 崩溃。之后再次重启成功，当前训练正常。

**关键问题：batch_idx 从 0 重新计数。** 进度条显示 608/50005，而不是 40608/50005。这意味着训练会跑完整 50005 步，需要 ~12.7h，**远超 DDL**。

**但好消息是：** 模型权重加载了 40000 checkpoint，action_loss=0.1016（低，符合预期）。虽然进度条显示 /50005，batch_idx=5000 时会保存 checkpoint（等效 45000 步），batch_idx=10000 时保存（等效 50000 步）。
- batch_idx 5000 checkpoint: ~1.1h 后（~13:10 北京时间）
- batch_idx 10000 checkpoint: ~2.4h 后（~14:25 北京时间）

**建议：** 等 batch_idx 10000 checkpoint 保存后（~14:25），手动 kill 进程。

---

### 2. 全部实验状态汇总

| 实验 | 服务器 | GPU | 状态 | 进度 | 预计完成 | 备注 |
|---|---|---|---|---|---|---|
| **detach_ln_v2_s2** | 34685 | 0 | 运行中 ✓ | 38826/50005 (78%) | ~14:50 | 正常，will finish |
| **vanilla_object_s0** | 34685 | 1 | **已挂 ❌** | ~25000/40005 | — | 保存 checkpoint 时崩溃 |
| **full_occ_ln_v2_s3** | 34685 | 2 | 运行中 ⚠️ | 608/50005 (重启) | 需手动 kill | batch_idx 重置 bug |
| **detach_ln_v2_s3** | 34685 | 3 | 运行中 ⚠️ | 624/50005 (重启) | 需手动 kill | batch_idx 重置 bug，同上 |
| **vanilla_object_s1** | 10894 | 0 | 运行中 ✓ | 38826/50005 (78%) | ~14:50 | 正常 |
| **detach_ln_v2_s4** | 10894 | 1 | 运行中 ✓ | 20255/50005 (40%) | ~19:40 | 紧但应能赶上 DDL |

westd-10894 GPU 2-3 空闲，westd-34685 GPU 1 空闲。

---

### 3. vanilla_object_s0 崩溃原因

**崩溃于 step ~25000 的 checkpoint 保存阶段**，不是 OOM，不是训练错误。

错误链：
```
finetune.py:1265 → save_training_checkpoint()
finetune.py:727  → AutoModelForVision2Seq.from_pretrained(path)
```
路径 `/root/autodl-tmp/checkpoints/vanilla_object_s0/...-10000_chkpt` **不存在**（可能被之前清理了），导致：
```
OSError: Incorrect path_or_model_id: '...--vanilla_object_s0--10000_chkpt'
```

这是 `save_training_checkpoint` 函数的 bug — 保存时引用了已删除的旧 checkpoint。

**Checkpoint 状况：**
- 15000_chkpt (07:03) ✓
- 20000_chkpt (08:27) ✓ ← 最后一个可靠的 checkpoint
- 25000_chkpt (09:51) ⚠️ 可能不完整（崩溃时正在保存）

**恢复方案：** 从 20000_chkpt 恢复，但需要先修复 `save_training_checkpoint` 中引用已删除 checkpoint 的 bug，否则会在下一个 save 点再次崩溃。

---

### 4. 磁盘空间

| 服务器 | 根分区 | 数据盘 |
|---|---|---|
| westd-34685 | 12G/30G (39%) | 15G/879G (2%) |
| westd-10894 | 15G/30G (48%) | 410G/879G (50%) |

磁盘空间充足，不是问题。

---

### 5. 紧急行动建议

1. **full_occ_ln_v2_s3 + detach_ln_v2_s3**：等到 ~14:25（batch_idx 10000 保存后），手动 kill。或者改代码修复 batch_idx resume 然后重启，但风险更大。
2. **vanilla_object_s0**：GPU 1 闲置中。如果需要这个实验的结果，需修复 `save_training_checkpoint` bug 后从 20000 checkpoint 恢复。剩余 20005 步 ≈ 5.1h，在 DDL 内。
3. **其他实验**：不需要干预。

---
