# DeepSeek CLS Repo: s42 v4 vs s123 训练配置对比

## 结论

**不可以直接合并为双 seed 报告。** 虽然训练超参数完全一致（仅 seed 不同），但 checkpoint 选择点不同：v4 是 epoch 2（中途停止），s123 是 3 epochs 完成后的 best checkpoint。3.6pp 的差距（71.29% vs 74.93%）很可能反映的是训练进度差异，而非 seed variance。

## 训练配置对比

| 参数 | s42 v4 | s123 | v5 (s42 retrain) |
|------|--------|------|-------------------|
| 训练脚本 | train_unified.py | train_unified.py | train_unified.py |
| base model | deepseek-coder-6.7b-instruct | deepseek-coder-6.7b-instruct | deepseek-coder-6.7b-instruct |
| train data | swebench_train.jsonl | swebench_train.jsonl | swebench_train.jsonl |
| raw train samples | 70748 | 70748 | 70748 |
| **preprocessing** | **truncate（保留全部 70748）** | **truncate（保留全部 70748）** | **drop（剩 67343）** |
| truncated/dropped | 3405 truncated (4.8%) | 3405 truncated (4.8%) | 3405 dropped (4.8%) |
| train max_seq_length | 2048 (default) | 2048 (default) | 2048 (default) |
| lr | 2e-4 | 2e-4 | 2e-4 |
| lr_scheduler | linear | linear | linear |
| warmup_ratio | 0.1 | 0.1 | 0.1 |
| epochs (planned) | 3 | 3 | 3 |
| **epochs (actual)** | **~2 (stopped at step 4422)** | **3 (completed)** | **3 (completed)** |
| total_steps | 6633 | 6633 | 6315 |
| batch_size | 2 | 2 | 2 |
| grad_accumulation | 16 | 16 | 16 |
| effective batch | 32 | 32 | 32 |
| seed | 42 | 123 | 42 |
| bf16 | true | true | true |
| weight_decay | 0.0 | 0.0 | 0.0 |
| max_grad_norm | 1.0 | 1.0 | 1.0 |

## LoRA 配置（三者完全一致）

| 参数 | 值 |
|------|-----|
| rank (r) | 16 |
| alpha | 32 |
| dropout | 0.05 |
| target_modules | q_proj, k_proj, v_proj, o_proj |
| bias | none |
| task_type | CAUSAL_LM |

## Eval 配置

| 参数 | s42 v4 | s123 |
|------|--------|------|
| eval checkpoint | checkpoint-4422 (epoch 2) | best/ (epoch 3 后保存) |
| eval seq_length | 8192 | 8192 |
| test data | swebench_test.jsonl (9784) | swebench_test.jsonl (9784) |
| **Accuracy** | **71.29%** | **74.93%** |
| F1 macro | 44.39% | 53.94% |
| unparseable | 247 | 133 |

## 问题分析

### 为什么不能直接合并

1. **训练进度不同**: v4 只跑了 2/3 epochs（step 4422/6633），s123 完成了 3 epochs。这不是公平的 seed 对比。
2. **Checkpoint 选择策略不同**: v4 用的是中途 checkpoint，s123 用的是训练完成后 Trainer 自动保存的 best。
3. **性能差距过大**: 3.6pp 的差距更可能归因于 epoch 数差异，而非随机种子变化。

### v5 也不是完美替代

v5（s42 重训）虽然完成了 3 epochs，但 preprocessing 从 truncate 改为 drop，导致训练数据量从 70748 降到 67343（步数 6633→6315）。这意味着 v5 和 s123 的训练数据分布不同。

### 建议

- **方案 A**: 等 v5 完成后，用 v5 结果和 s123 结果做双 seed 报告，在论文中标注 preprocessing 有微小差异（truncate vs drop）。如果 v5 和 s123 的结果接近（差距 < 2pp），这个差异可以忽略。
- **方案 B**: 用 s123 的 checkpoint-4422（与 v4 同步点）重新 eval，得到一个 epoch 2 的 s123 结果，与 v4 做公平对比。但 epoch 2 的模型性能明显不如 epoch 3，报告价值有限。
- **方案 C**: 用与 s123 完全相同的代码版本（truncate 逻辑）重跑 s42 全 3 epochs。最干净但需要额外训练。

## 数据来源

- v4 training log: `/root/runs/exec-sim-repair-verifier/deepseek-cls-repo-v4.log`
- s123 training log: `/root/runs/exec-sim-repair-verifier/deepseek-cls-repo-s123.log`
- v5 training log: `/root/runs/deepseek-cls-repo-v5.log`
- v4 checkpoint: `/root/autodl-tmp/checkpoints_deepseek_cls_repo_v4/checkpoint-4422/`
- s123 checkpoint: `/root/autodl-tmp/checkpoints_deepseek_cls_repo_s123/best/`
- v5 checkpoint: `/root/autodl-tmp/checkpoints_deepseek_cls_repo_v5/`
- Eval results: `/root/autodl-tmp/eval_results/deepseek_cls_repo_{v4,s123}_8192.{json,log}`
