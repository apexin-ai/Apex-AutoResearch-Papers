# diagnose mvp occ s1 exit

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp_occ_s1_exit_20260520T235839_result.json`
- **Structured JSON:** [`bd6bc1a1413efa9a1ab1.json`](../../sessions/bd/bd6bc1a1413efa9a1ab1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息足够了。以下是排查结论。

---

## occ_s1 排查结果

### 退出原因：异常崩溃（Checkpoint 保存 I/O 错误）

**Crash 时间**：2026-05-21 07:57:05 UTC

**错误堆栈**：
```
finetune.py:1182 → save_training_checkpoint
finetune.py:700  → merged_vla.save_pretrained(checkpoint_dir)
safetensors_rust.SafetensorError: Error while serializing: I/O error: No such file or directory (os error 2)
```

训练在 **step 27500**（55%）时触发 checkpoint 保存，LoRA merge 后写入 safetensors 文件时目标目录不存在导致 crash。

### 关键数据

| 项目 | 状态 |
|------|------|
| 最后训练 step | ~27500 / 50005 (55%) |
| 最新可用 checkpoint | **7500_chkpt**（5000_chkpt 也存在） |
| 中间 checkpoints (10000-25000) | **已不存在**（日志显示 25000 曾成功保存，但目录已被删除） |
| occ_s0 (PID 27667) | 存活，运行 7h+ |
| occ_s2 (PID 29970) | 存活，运行 7h+ |
| GPU 1 (occ_s1 原用) | 空闲，0 MiB / 0% util |
| GPU 0, 2 | 正常 ~62GB / 99% util |
| 磁盘 /root/autodl-tmp | 240GB 可用，不是空间问题 |

### 分析

1. `save_freq` 被设为 2500 步（代码默认 10000，启动时覆盖），checkpoint 保存频繁
2. 每个 merged checkpoint ~15GB（4 个 safetensors shard），大量 checkpoint 会快速消耗磁盘
3. 中间 checkpoints (10000-25000) 已被删除（代码中**无自动清理逻辑**，可能是手动删除或外部脚本）
4. 27500 save 失败的 "No such file or directory" 很可能是外部清理进程在 `os.makedirs` 创建目录后、`safe_save_file` 写入前删除了目录
5. occ_s0/s2 不受影响 → 非系统级事件，是 occ_s1 独立的 checkpoint 保存失败

### 重启建议

从 7500_chkpt 恢复，损失约 20000 步训练进度。需要先确认：

1. **是谁/什么删除了中间 checkpoints？** 如果有外部清理 cron/脚本在跑，重启后同样会 crash
2. 建议增大 `save_freq`（如 5000 或 10000）减少 checkpoint 数量，或在代码中加 try-except 保护 checkpoint save 不要 crash 整个训练

如需立即重启，需要提供原始启动命令，我来拼 resume 命令。

---
