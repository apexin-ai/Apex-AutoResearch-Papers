# code cwm cls checkpoint audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cwm-cls-checkpoint-audit_20260512T214719_result.json`
- **Structured JSON:** [`c86ffedf474e5989ef07.json`](../../sessions/c8/c86ffedf474e5989ef07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已获取全部信息。以下是分析报告。

---

## CWM vs CLS 配置对比

| 参数 | CWM (train_repo_cwm.py) | CLS (train_repo_verifier.py) |
|------|------------------------|------------------------------|
| save_strategy | `"steps"` (始终，不受 is_dryrun 影响) | `"epoch"` (正常) / `"no"` (dryrun) |
| save_steps | `args.save_steps` (CLI arg, default=100) | 无（epoch-based，不需要） |
| eval_strategy | `"steps"` (正常) / `"no"` (dryrun) | `"epoch"` (正常) / `"no"` (dryrun) |
| eval_steps | `args.save_steps` (与 save_steps 同步) | 无（epoch-based） |
| save_total_limit | 3 | 2 |
| output_dir (default) | `/root/autodl-tmp/checkpoints_repo_cwm/` | `checkpoints_repo_cls/` |
| load_best_model_at_end | `not is_dryrun` | `not is_dryrun` |
| metric_for_best_model | `"eval_loss"` (正常模式) | `"eval_loss"` (正常模式) |
| is_dryrun 判定 | `args.max_steps > 0` | `args.max_steps > 0` |
| resume_from_checkpoint | 有 CLI arg | 无 |
| batch_size default | 1 | 2 |
| grad_accumulation default | 32 | 4 |
| Trainer 子类 | WeightedCausalLMTrainer (仅覆盖 compute_loss) | WeightedCausalLMTrainer (仅覆盖 compute_loss) |
| TrainerCallback | 无自定义 | 无自定义 |

## Bug 定位

**CWM 当前代码没有明显的 save bug。** save_strategy="steps" 是无条件设置的（不像 CLS 在 dryrun 时变为 "no"），WeightedCausalLMTrainer 只覆盖了 compute_loss，没有干预 save 行为。

**CWM v1 零 checkpoint 的可能根因：**

1. **最可能：v1 启动时传了 `--max_steps N`（N>0），触发了 is_dryrun=True。** 虽然 save_strategy 仍为 "steps"，但 `eval_strategy="no"` + `load_best_model_at_end=True` 在旧版 Transformers 中可能导致 Trainer 初始化时报错或异常行为。当前代码中 `load_best_model_at_end = not is_dryrun`，在 dryrun 时为 False，应该没问题——**但如果 v1 运行时代码不同（例如 load_best_model_at_end 曾写死为 True），就会触发 Transformers 的校验冲突。**

2. **次可能：检查了错误的 checkpoint 目录。** CWM default output_dir 是 `/root/autodl-tmp/checkpoints_repo_cwm/`，如果 v1 启动时通过 CLI 指定了不同路径，检查默认路径自然为空。

3. **磁盘满。** AutoDL 根分区 30GB 容易满，但 output_dir 在 `/root/autodl-tmp/`（数据盘），不太可能。

## CLS v2 checkpoint 状态

**正常（符合预期）。**
- PID 2881844 存活，RSS 4.3GB，已运行 24m19s
- 当前 step 190/6633，epoch ≈ 0.07
- checkpoint 目录为空 —— **这是预期行为**，因为 save_strategy="epoch"，第一个 checkpoint 要等到 epoch 1 结束（step ~2211）
- 按 ~6.5s/step 估算，epoch 1 结束约需 14,337s ≈ 4h，即大约 3.5 小时后出第一个 checkpoint
- 日志中无 "saving" / "checkpoint" 字样，与 epoch-based 策略一致

## CWM v9 checkpoint 状态

**进程存活，尚未开始训练。**
- PID 95806 存活，RSS 4.5GB，已运行 3m58s
- 日志仍在数据加载阶段（已完成 tokenizer + data load + class weights 计算），正在预处理/加载模型
- checkpoint 目录为空 —— **预期行为**，还没跑到第一个 save_steps
- 预计数据预处理完成 + 模型加载后开始训练，save_steps=100 时第一个 checkpoint 在 step 100

---
