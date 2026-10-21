# check cls home checkpoint provenance

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cls-home-checkpoint-provenance_20260514T063058_result.json`
- **Structured JSON:** [`1bc494cea2e2e12a72c7.json`](../../sessions/1b/1bc494cea2e2e12a72c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部关键信息已收集。logging_dir 显示 home 训练于 May 12 14:58:01 启动。以下是完整报告。

---

## 调查报告：checkpoints_repo_cls_home/ 中 3 个 checkpoint 的来源

### 1. 文件时间戳

| Checkpoint | 时间戳 | Global Step | Epoch |
|---|---|---|---|
| checkpoint-200 | May 12 15:34 | 200 | 0.090 |
| checkpoint-2400 | May 12 22:15 | 2400 | 1.085 |
| checkpoint-2600 | May 12 22:51 | 2600 | 1.176 |

### 2. 来源推断

**这 3 个 checkpoint 来自同一次连续训练**，依据：
- log_history 在每个 checkpoint 中累积（后者包含前者的全部训练日志，且数值完全一致）
- logging_dir 中的时间戳表明训练于 **May 12 14:58:01** 启动
- run_name = `repo-cls-qwen3-4b-lora-home`
- `save_total_limit=3`，所以只保留了 3 个 checkpoint（checkpoint-200 作为 best_model 被保留，checkpoint-2400 和 checkpoint-2600 是最近的两个）
- 训练在 step 2600 后被中止或仍在运行时被 kill（max_steps=6633 远未完成）

**与 registry 记录的关系**：registry 的 `repo-level-cls-home` 被记录为 May 12 kill（687 秒，零 checkpoint）。这次训练显然是另一次独立运行——它从 14:58 运行到至少 22:51（近 8 小时），且 `report_to=[]`（未接入 wandb），说明不是通过标准实验管理流程启动的。

### 3. 环境版本

| | home (这3个) | seed123 | v5 |
|---|---|---|---|
| PEFT | **0.19.1** | **0.19.1** | **0.14.0** |
| transformers | 4.57.6 (当前环境) | 4.57.6 (当前环境) | wandb 记录 5.8.0，但 training_args schema 与 home 完全一致(132 key)，存疑 |
| 当前服务器环境 | transformers==4.57.6, peft==0.19.1 | | |

### 4. 训练超参差异（关键）

| 参数 | home (这3个) | seed123 | v5 |
|---|---|---|---|
| **learning_rate** | **0.0002** | 5e-05 | 5e-05 |
| **warmup_ratio** | **0.1** | 0.05 | 0.05 |
| **weight_decay** | **0.0** | — | 0.01 |
| seed | 42 | 123 | 42 |
| save_total_limit | 3 | — | 5 |
| report_to | [] (无) | — | wandb |

lr 是 seed123/v5 的 **4 倍**，warmup 是 **2 倍**，且无 weight_decay。

### 5. LoRA 配置

三者完全相同：r=16, alpha=32, dropout=0.05, target=q/k/v/o_proj, base_model=Qwen/Qwen3-4B, task=CAUSAL_LM。权重格式上是兼容的。

### 6. 结论

**这 3 个 home checkpoint 不能与 seed123/v5 的 val sweep 结果混用。**

原因：
- **超参完全不同**（4x lr, 2x warmup, 无 weight_decay），混用会比较不同超参配置的效果而非训练进度/epoch 的效果，在科学上无效
- 来自一次**未注册、未追踪**的独立训练运行，无法溯源完整训练过程
- 训练未完成（2600/6633 steps），且因 `save_total_limit=3` 已丢失中间 checkpoint

建议处理方式：视为废弃的探索性训练残留，不纳入 val sweep。如需这个 output_dir 用于新训练，应先清理这 3 个 checkpoint。

---
