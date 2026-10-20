# exec eval gsm8k sft alpha4 20 v3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_eval_gsm8k_sft_alpha4_20_v3_20260521T222555_result.json`
- **Structured JSON:** [`35e8208654e16b2fd231.json`](../../sessions/35/35e8208654e16b2fd231.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功，eval 正在运行。

## 汇总

### 1. 新 PID
- **Python 进程 PID: 425497**（bash wrapper PID: 425492）

### 2. 启动验证
- 进程存活，GPU 0 占用 **12620 MiB**
- 正在评估 1319 个 GSM8K 样本，速度 ~2.61s/it
- 预估总时间：~57 分钟

### 3. VRAM 排查
当前 VRAM **12620 MiB**（约 12.3GB），远低于之前报告的 29GB。之前 29GB 可能是因为：
- 前两次跑的脚本参数不同（之前用 `--max_samples` 且 output_path 在 autodl-tmp 下）
- 可能当时有其他进程共用 GPU 0
- 或者之前是 float32 加载（当前正确以 bf16 加载）

模型配置对比（**sft_alpha4_20** vs **sft_cka_only_20**）：
- 架构完全相同：Qwen2ForCausalLM, hidden=3584, heads=28, layers=28, kv_heads=4
- 两者都是非均匀剪枝模型，`per_layer_intermediate_size` 分布略有不同但范围一致 [8128, 18944]
- 模型文件大小 12GB（bf16），VRAM 占用 12.6GB 正常

**当前运行正常，无 VRAM 异常。**

---
