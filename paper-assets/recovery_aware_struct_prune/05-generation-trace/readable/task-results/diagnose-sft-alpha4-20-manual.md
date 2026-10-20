# diagnose sft alpha4 20 manual

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sft_alpha4_20_manual_20260521T182335_result.json`
- **Structured JSON:** [`26c159a34fb245d17e38.json`](../../sessions/26/26c159a34fb245d17e38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 关键错误片段

```
RuntimeError: basic_ios::clear: iostream error
RuntimeError: [enforce fail at inline_container.cc:672] . unexpected pos 15735283264 vs 15735283164

File "/root/miniconda3/lib/python3.12/site-packages/transformers/trainer.py", line 3248, in _save_optimizer_and_scheduler
    torch.save(self.optimizer.state_dict(), os.path.join(output_dir, OPTIMIZER_NAME))
```

崩溃发生在 step 468/936 (epoch ~0.98)，保存 checkpoint 时写 optimizer state dict 失败。

### 失败根因

**数据盘 `/root/autodl-tmp/` 已 100% 满（619G/619G，剩余仅 4MB）。** Trainer 在 epoch 1 结束时尝试保存 checkpoint（optimizer state ~15GB），写入过程中磁盘空间耗尽，触发 iostream error。

### 当前状态

- 训练进程已退出（EXIT_CODE=1），无残留进程
- pruned model `/root/autodl-tmp/recovery_aware_struct_prune/pruned_alpha4_20/` 存在且完整（12.3GB）
- 根分区正常（17%），问题仅在数据盘
- GPU 上有 2 个 eval_math500 任务仍在运行（cuda:1 和 cuda:3）

### 修复方案

1. **清理数据盘空间** — 需要释放至少 ~30-40GB（模型 shards + optimizer state + 余量）。可清理的候选：
   - 旧的/不再需要的 checkpoint 目录
   - 已完成评估的临时文件
   - HuggingFace cache 中的重复文件
2. **重试实验** — 空间释放后可直接重新启动，模型和数据都在
3. **可选优化** — 训练配置中设置 `save_total_limit=1` 或 `save_strategy="epoch"` 减少 checkpoint 存储压力；或加 `--save_only_model` 跳过保存 optimizer state

是否需要我帮忙清理磁盘空间？

---
