# ops check cka only 30 retry

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_cka_only_30_retry_20260517T230840_result.json`
- **Structured JSON:** [`6fcb12d759c03ce8d2db.json`](../../sessions/6f/6fcb12d759c03ce8d2db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**PID 59403 状态：存活，是原始 eval 进程（重试后的新实例）**

- PID 59403 是 wrapper bash 进程，启动时间 05:59 (UTC)
- 子进程 PID 59408 是实际的 `python src/eval_gsm8k.py` 进程，CPU 106%，已运行 ~74 分钟

**日志进度：**
- 模型加载成功（Non-uniform MLP, intermediate_size range [8128, 18944]）
- GSM8K 数据集加载成功（网络不可达，使用了 HF 缓存）
- 评估进度：**49/200 samples (24.5%)**，速度 ~47-95s/sample
- 日志中有一条 "Terminated" 字样出现在 sample 35 附近，但进程没有退出，之后速度加快（从 95s 降到 ~48s/it），可能是 GPU 竞争消除后加速

**结果文件：**
- `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_cka_only_30.json` 尚未产出（评估未完成时不会写文件）

**模型目录 (`pruned_cka_only_30/`)：完整**
- config.json, generation_config.json, model.safetensors, tokenizer.json, tokenizer_config.json

**预估完成时间：**
- 剩余 151 samples × ~48s/sample ≈ 120 分钟（~2 小时后完成）
- 预计 UTC 08:10 左右产出结果文件

**结论：eval 正在正常运行中，无需干预。Registry 显示 DONE/failed 是旧状态，当前是成功重试后的新进程。**

---
