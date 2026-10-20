# ops diagnose westd crashes

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_westd_crashes_20260518T181239_result.json`
- **Structured JSON:** [`54ef56bab78f4a8bc8db.json`](../../sessions/54/54ef56bab78f4a8bc8db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29022 诊断汇报

### 系统级
- **dmesg 不可用**（Operation not permitted，容器环境限制），无法确认 OOM/kill 事件
- **无 OOM 迹象**：当前所有进程运行正常

### GPU 状态

| GPU | 任务 | 显存 | 利用率 | 温度 | 状态 |
|-----|------|------|--------|------|------|
| **cuda:0** | grpo_cka_only_20_extended_300 (PID 11457) | 90.6G/97.9G | 99% | 84°C | **运行中，192/300 steps** (~64%)，ETA ~3.5h |
| **cuda:1** | eval_math500_grpo_standard_fair_v2 (PID 19616) | 16.8G/97.9G | 98% | 81°C | **运行中，23/500** (~5%)，01:52 启动 |
| **cuda:2** | eval_math500_sft_cka_only_v4 | 0G (已释出) | 100%* | 36°C | **运行中，85/500** (~17%)，Acc@50=30.0% |
| **cuda:3** | eval_math500_dense_unpruned | 0G (已释出) | 0% | 31°C | **已完成** ✅ |

*cuda:2 显示 100% util 但 0 mem 可能是 nvidia-smi 采样时差，进程仍在 tmux 中运行。

### 各实验详情

1. **cuda:0 — grpo_cka_only_20_extended_300**: 192/300 steps, ~55s/step, 预计还需约 3.5 小时完成
2. **cuda:1 — eval_math500_grpo_standard_fair_v2**: 刚启动（01:52），23/500，进度缓慢（~70s/it）
3. **cuda:2 — eval_math500_sft_cka_only_v4**: 85/500, Acc@50=30.0%，预计还需数小时
4. **cuda:3 — eval_math500_dense_unpruned**: **已完成** — **Accuracy = 73.6% (368/500)**, ±0.0197。Registry 已更新为 DONE/success

### 已完成结果 JSON
- `math500_dense_unpruned.json`: **accuracy=0.736** (368/500)
- `math500_grpo_unpruned.json`: **accuracy=0.690** (345/500)

### RASP GRPO fair checkpoint
**存在** — `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair/`，包含 model.safetensors (~12.3GB) + checkpoint-80/90/100。

---
