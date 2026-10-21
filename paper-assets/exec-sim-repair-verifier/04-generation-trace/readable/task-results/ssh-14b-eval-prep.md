# ssh 14b eval prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14b-eval-prep_20260523T073531_result.json`
- **Structured JSON:** [`8bc6df0dfb23aac2174b.json`](../../sessions/8b/8bc6df0dfb23aac2174b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。汇报如下：

---

## 探测结果

### 1. s42 CLS/CWM per-test prediction 文件

**CLS 14B s42 (bf16)**:
- 路径: `/root/autodl-tmp/eval_results/cls14b_func_s42_v2_bf16/eval_results_predictions.json`
- 格式: JSON list, 1890 条, 字段: `index`, `problem_id`, `label`, `prediction`, `correct`
- 精度: 89.21%

**CWM 14B s42**:
- 路径: `/root/autodl-tmp/eval_results/cwm14b_func_s42/eval_cwm_results_predictions.json`
- 格式: JSON dict (`metadata` + `predictions` list), 1890 条, 字段: `idx`, `problem_id`, `mutation_type`, `source`, `true_label`, `predicted_label`, `correct`, `raw_output`, `error_type`, `exact_match`

两个文件都存在，格式可直接用于 multi-seed 对比。

### 2. eval 脚本

| 任务 | 脚本 | 保存预测 |
|------|------|----------|
| CLS | `eval_verifier.py` | `--save_predictions` → `{output_stem}_predictions.json` |
| CWM | `eval_cwm_baseline.py` | `--save_predictions` → `{output}_predictions.json` |

两个脚本都用 `--checkpoint_dir` 指定 LoRA checkpoint，默认 bf16（不加 `--quantize_4bit` 即为 bf16）。

### 3. 4 个训练的当前状态

| 训练 | GPU | 进度 | 状态 |
|------|-----|------|------|
| cls14b-func-s123 | 0 | 1423/1434 (99%) | epoch 3, ~1min 到完成 |
| cls14b-func-s456 | 1 | 1425/1434 (99%) | epoch 3, ~1min 到完成 |
| cwm14b-func-s123 | 2 | epoch 2 eval 中 (27%) | eval 完后进 epoch 3 |
| cwm14b-func-s456 | 3 | epoch 2 eval 中 (54%) | eval 完后进 epoch 3 |

所有 4 个都已产出 checkpoint-478 (epoch 1) 和 checkpoint-956 (epoch 2)。预计全部完成时间：CLS ~立即，CWM 再 ~1.5h。

### 4. 新 seed eval 命令（训练完成后执行）

```bash
# CLS s123 eval
cd /home/sonny/exec-sim-repair-verifier && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 python3 eval_verifier.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/cls14b-func-s123/checkpoint-1434 \
  --model_name /dev/shm/Qwen3-14B \
  --output /root/autodl-tmp/eval_results/cls14b_func_s123/eval_results.json \
  --save_predictions --data_dir data/

# CLS s456 eval
CUDA_VISIBLE_DEVICES=1 python3 eval_verifier.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/cls14b-func-s456/checkpoint-1434 \
  --model_name /dev/shm/Qwen3-14B \
  --output /root/autodl-tmp/eval_results/cls14b_func_s456/eval_results.json \
  --save_predictions --data_dir data/

# CWM s123 eval
CUDA_VISIBLE_DEVICES=2 python3 eval_cwm_baseline.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/cwm14b-func-s123/checkpoint-1434 \
  --model_name /dev/shm/Qwen3-14B \
  --output /root/autodl-tmp/eval_results/cwm14b_func_s123/eval_cwm_results.json \
  --save_predictions --data_dir data/

# CWM s456 eval
CUDA_VISIBLE_DEVICES=3 python3 eval_cwm_baseline.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/cwm14b-func-s456/checkpoint-1434 \
  --model_name /dev/shm/Qwen3-14B \
  --output /root/autodl-tmp/eval_results/cwm14b_func_s456/eval_cwm_results.json \
  --save_predictions --data_dir data/
```

**注意**: checkpoint step 数字 1434 需要确认——如果 3 epochs × 478 steps = 1434，那最终 checkpoint 可能是 `checkpoint-1434`，也可能训练器只保存了中间 checkpoint 而最终模型在 output_dir 根目录。训练完成后先 `ls` 确认。

---
