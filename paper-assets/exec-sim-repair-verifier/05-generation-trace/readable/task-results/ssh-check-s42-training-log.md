# ssh check s42 training log

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-s42-training-log_20260520T070452_result.json`
- **Structured JSON:** [`5ab8e3f1979ecc8a0da0.json`](../../sessions/5a/5ab8e3f1979ecc8a0da0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是所有命令结果汇总：

---

### 1. s42 训练日志文件

找到的 deepseek-cwm 相关日志：
```
/root/runs/exec-sim-repair-verifier/deepseek-cwm-func.log
/root/runs/exec-sim-repair-verifier/deepseek-cwm-func-s123.log
/root/runs/exec-sim-repair-verifier/deepseek-cwm-repo.log          ← s42 训练日志
/root/runs/exec-sim-repair-verifier/deepseek-cwm-repo-s123.log
/root/runs/exec-sim-repair-verifier/deepseek-cwm-repo-s42-seq4096-eval.log
/root/runs/exec-sim-repair-verifier/deepseek-cwm-repo-s123-train.log
/root/runs/exec-sim-repair-verifier/deepseek-cwm-repo-s123-eval.log
/root/runs/exec-sim-repair-verifier/deepseek-cwm-repo-s456-train.log
/root/runs/exec-sim-repair-verifier/deepseek-cwm-repo-s123-train-v2.log
```

### 2. training_args.bin（best/ 和 checkpoint-13266 内容一致）

```
seed = 42
output_dir = /root/autodl-tmp/checkpoints_deepseek_cwm_repo/
run_name = deepseek-cwm-repo-s42
num_train_epochs = 3
per_device_train_batch_size = 2
per_device_eval_batch_size = 2
gradient_accumulation_steps = 8
learning_rate = 0.0002
lr_scheduler_type = linear
warmup_ratio = 0.1
weight_decay = 0.0
bf16 = True
fp16 = False
gradient_checkpointing = True
logging_steps = 50
eval_strategy = epoch
save_strategy = epoch
save_total_limit = 2
load_best_model_at_end = True
metric_for_best_model = eval_loss
optim = adamw_torch_fused
max_steps = -1
max_grad_norm = 1.0
dataloader_num_workers = 4
report_to = []
```

### 3. deepseek-cwm-repo.log 前30行（启动信息）

```
2026-05-16 16:04:54,196 INFO Model: /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct → family=deepseek
2026-05-16 16:04:54,196 INFO Task: cwm, Run name: deepseek-cwm-repo-s42
2026-05-16 16:04:54,196 INFO Loading tokenizer: /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct
2026-05-16 16:04:54,271 INFO Chat template kwargs: {}
2026-05-16 16:04:54,275 INFO Sample formatted prompt (first 300 chars):
<｜begin▁of▁sentence｜>You are a code execution simulator. Given a code snippet and a test case, predict the execution result.### Instruction:
## Code
def f(): return 1

## Test
assert f() == 1

What is the execution result?
### Response:
PASS: test completed successfully
<|EOT|>

2026-05-16 16:04:54,275 INFO Train file: data/swebench_full/swebench_train.jsonl
2026-05-16 16:04:54,275 INFO Val file: data/swebench_full/swebench_val.jsonl
2026-05-16 16:04:56,171 INFO Loaded train=70748, val=9335
Token indices sequence length is longer than the specified maximum sequence length for this model (21612 > 16384). Running this sequence through the model will result in indexing errors
2026-05-16 16:13:29,967 INFO train: 6700/70748 truncated (9.5%)
2026-05-16 16:15:25,214 INFO val: 2679/9335 truncated (28.7%)
2026-05-16 16:15:27,829 INFO Loading model: /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct
2026-05-16 16:15:27,832 INFO Attention: sdpa
2026-05-16 16:15:27,908 INFO LoRA target modules: ['q_proj', 'k_proj', 'v_proj', 'o_proj']
2026-05-16 16:15:35,036 INFO Starting training...
trainable params: 16,777,216 || all params: 6,757,289,984 || trainable%: 0.2483
```

### 4. 训练结束信息（log 尾部）

```
100%|██████████| 13266/13266 [31:17:59<00:00, 8.49s/it]
2026-05-17 23:33:35,291 INFO Best model saved to /root/autodl-tmp/checkpoints_deepseek_cwm_repo/best
{'eval_loss': nan, 'eval_runtime': 1423.15, 'eval_samples_per_second': 6.559, 'epoch': 3.0}
{'train_runtime': 112679.88, 'train_samples_per_second': 1.884, 'train_steps_per_second': 0.118, 'train_loss': 0.021031, 'epoch': 3.0}
```

### 5. train_repo_cwm.py

文件存在（12016 bytes, May 14），但 **s42 训练不是用它跑的**。该脚本头部标注 "Qwen3 LoRA fine-tuning"，且其默认超参（lr=5e-5, batch=1, grad_accum=32, weight_decay=0.01, save_strategy=steps）与 training_args.bin 记录的超参全部不匹配。

### 6. 实际训练脚本：train_unified.py

日志里 `family=deepseek` 和 `Task: cwm` 格式匹配 `train_unified.py`。该脚本的默认超参与 training_args.bin 完全一致：
```
--lr 2e-4  (= 0.0002 ✓)
--batch_size 2 ✓
--grad_accumulation 16  (training_args 记录为 8，可能命令行覆盖了)
--epochs 3 ✓
--warmup_ratio 0.1 ✓
--lora_rank 16 ✓
--lora_alpha 32 ✓
--seed 42 ✓
```

日志中 grep 不到 "train_unified" 或 "train_repo_cwm" 字样（脚本没有 log 自身文件名）。

### 7. 关键结论

- **训练脚本**: `train_unified.py`（非 train_repo_cwm.py）
- **数据**: `data/swebench_full/swebench_train.jsonl` — **train=70748 行, val=9335 行**
- **train 截断**: 6700/70748 (9.5%), val 截断: 2679/9335 (28.7%)
- **总训练 steps**: 13266 (= 70748 / (2×8) × 3 epochs, 说明 grad_accumulation 实际=8)
- **训练时间**: 2026-05-16 16:15 → 2026-05-17 23:33, 约 31.3 小时

---
