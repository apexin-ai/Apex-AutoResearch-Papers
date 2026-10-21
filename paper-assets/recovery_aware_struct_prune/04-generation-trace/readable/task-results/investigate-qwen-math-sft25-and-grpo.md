# investigate qwen math sft25 and grpo

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_qwen_math_sft25_and_grpo_20260516T120641_result.json`
- **Structured JSON:** [`0f4721102e31aeb8c1d9.json`](../../sessions/0f/0f4721102e31aeb8c1d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。汇总报告如下：

---

## westd-11672 实验状态报告

### 1. sft_qwen_math_rasp_25 — ✅ 已完成

| 项目 | 详情 |
|------|------|
| 状态 | **训练完成，exit 0** |
| Sentinel | `sft_rasp_25.exit` → `0|2026-05-16T05:57:33Z` |
| Checkpoint | `/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25/model.safetensors` (11.5GB) |
| 训练详情 | 2 epochs, 1870 steps, final train_loss=0.8498, runtime=1635s (~27min) |
| 最终 loss | 0.7365 (epoch 2.0) |
| Eval | 已在运行 (pid 6140, cuda:2, 4分钟前启动，200 samples GSM8K) |

**Cron 误报原因**：sentinel 文件名是 `sft_rasp_25.exit`，而非 Cron 期望的 `sft_qwen_math_rasp_25.exit`。

---

### 2. sft_qwen_math_standard_25 — ✅ 已完成（第二次运行）

| 项目 | 详情 |
|------|------|
| 状态 | **首次被 SIGTERM 杀死 (exit 143)，已被重跑并成功完成** |
| 首次 Sentinel | `sft_standard_25.exit` → `143|2026-05-16T06:17:03Z`（killed at step 724/1870, 38%） |
| Checkpoint | `/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25/model.safetensors` (11.5GB, mtime 19:52 +0800) |
| 证据 | checkpoint 含 `training_args.bin`（仅训练完成时写入），时间戳晚于 kill 时间 |
| Eval | 已在运行 (pid 6220, cuda:3, 4分钟前启动，200 samples GSM8K) |

**注意**：`sft_standard_25.log` 仍记录的是首次被杀的运行，第二次成功运行的日志可能被覆盖或写到别处。

---

### 3. grpo_rasp_qwen_math — 🔄 运行中 (step 0/100)

| 项目 | 详情 |
|------|------|
| 进程 | pid 5033, **存活**, elapsed ~10min |
| GPU | cuda:0 |
| 模型 | sft_qwen_math_rasp_20 (20% sparsity) |
| 进度 | 0/100 steps（正在生成第一批 completions，max_completion_length=1024） |
| W&B | run `1yl4wuij` (grpo_rasp_qwen_math) |
| 参数 | beta=0.04, dapo loss, temp=0.4, rep_penalty=1.15, adamw_bnb_8bit |

---

### 4. grpo_standard_qwen_math — 🔄 运行中 (step 0/100)

| 项目 | 详情 |
|------|------|
| 进程 | pid 5111, **存活**, elapsed ~10min |
| GPU | cuda:1 |
| 模型 | sft_qwen_math_standard_20 (20% sparsity) |
| 进度 | 0/100 steps（正在生成第一批 completions） |
| W&B | run `k4grawvk` (grpo_standard_qwen_math) |
| 参数 | 同上 |

---

### GPU 分配总览

| GPU | 任务 | 状态 |
|-----|------|------|
| cuda:0 | grpo_rasp_qwen_math | 运行中 |
| cuda:1 | grpo_standard_qwen_math | 运行中 |
| cuda:2 | eval_sft_qwen_math_rasp_25 | 运行中 |
| cuda:3 | eval_sft_qwen_math_standard_25 | 运行中 |

### 关键结论

1. **SFT 两个实验均已完成**，checkpoint 完整。Cron 误报是因为 sentinel 文件名不匹配（`sft_rasp_25` vs 期望的 `sft_qwen_math_rasp_25`）。
2. **GRPO 刚启动约 10 分钟**（非用户描述的"已运行多小时"），进程是新的。GRPO 第一个 step 生成 1024 token completions 预计需要 20-40 分钟，当前 0/100 是正常的。
3. Eval 也在并行运行，4 张 GPU 全部占用。

---
