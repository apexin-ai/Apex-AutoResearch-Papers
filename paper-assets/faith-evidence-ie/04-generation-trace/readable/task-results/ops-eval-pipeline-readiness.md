# ops eval pipeline readiness

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-pipeline-readiness_20260514T170347_result.json`
- **Structured JSON:** [`5783cbf593a66de73fd4.json`](../../sessions/57/5783cbf593a66de73fd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

## Eval Pipeline 就绪性报告

### 脚本状态
- `batch_eval.py`: ✅ 存在 (6378 bytes, 2025-05-14 23:56)
- `find_best_checkpoint.py`: ✅ 存在 (5239 bytes, 2025-05-14 23:57)

### batch_eval.py 参数
| 参数 | 必需 | 默认值 |
|------|------|--------|
| `--exp_dir` | ✅ | - |
| `--sft_adapter` | ✅ | - |
| `--output_dir` | ✅ | - |
| `--base_model` | | `/root/autodl-tmp/models/Qwen3-4B` |
| `--data_path` | | `/root/autodl-tmp/data/docred` |
| `--split` | | `dev` |
| `--batch_size` | | `16` |
| `--max_new_tokens` | | `1024` |
| `--quantize` | | `True` |
| `--resume` | | 跳过已有 metrics.json 的 checkpoint |
| `--checkpoints` | | 指定 step，逗号分隔 |

### Checkpoint 状态
| 实验 | 状态 | Checkpoints |
|------|------|-------------|
| ced_kl001 | 6 checkpoints | 10, 20, 30, 40, 50, 60 |
| extract_r4 | ❌ 目录空 | 训练尚未产出 checkpoint |
| flatnli_r5 | ❌ 目录空 | 训练尚未产出 checkpoint |

### SFT Baseline
- ✅ `/root/autodl-tmp/sft_eval_r3_results/` 存在 (metrics.json, predictions.json)
- SFT adapter: `/root/autodl-tmp/sft_output`

### 预备 Eval 命令

**ced_kl001 — 可立即执行：**

```bash
# 找 best checkpoint
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/freige
python -m freige.eval.find_best_checkpoint --exp_dir /root/autodl-tmp/grpo_ced_kl001 --sort_by total_reward --top_k 5

# best checkpoint eval（将 BEST_STEP 替换为上面输出的 step）
python -m freige.eval.batch_eval \
    --exp_dir /root/autodl-tmp/grpo_ced_kl001 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 \
    --checkpoints BEST_STEP \
    --quantize

# last checkpoint eval
python -m freige.eval.batch_eval \
    --exp_dir /root/autodl-tmp/grpo_ced_kl001 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --output_dir /root/autodl-tmp/eval_results/grpo_ced_kl001 \
    --checkpoints 60 \
    --quantize
```

**extract_r4 — 等待 checkpoint 产出后执行：**

```bash
python -m freige.eval.find_best_checkpoint --exp_dir /root/autodl-tmp/grpo_extract_r4 --sort_by total_reward --top_k 5

python -m freige.eval.batch_eval \
    --exp_dir /root/autodl-tmp/grpo_extract_r4 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --output_dir /root/autodl-tmp/eval_results/grpo_extract_r4 \
    --checkpoints BEST_STEP,LAST_STEP \
    --quantize
```

**flatnli_r5 — 等待 checkpoint 产出后执行：**

```bash
python -m freige.eval.find_best_checkpoint --exp_dir /root/autodl-tmp/grpo_flatnli_r5 --sort_by total_reward --top_k 5

python -m freige.eval.batch_eval \
    --exp_dir /root/autodl-tmp/grpo_flatnli_r5 \
    --sft_adapter /root/autodl-tmp/sft_output \
    --output_dir /root/autodl-tmp/eval_results/grpo_flatnli_r5 \
    --checkpoints BEST_STEP,LAST_STEP \
    --quantize
```

### 注意事项

1. **extract_r4 和 flatnli_r5 目录已创建但为空**——训练可能刚启动或尚未保存第一个 checkpoint，需确认训练进程是否在运行
2. **ced_kl001 已有 60 step**，`trainer_state.json` 存在于 checkpoint-60，`find_best_checkpoint` 可直接使用
3. **如果 best == last (step 60)**，只需跑一次 eval，不用重复
4. `batch_eval.py` 的 `--resume` 参数可跳过已评测的 checkpoint，适合中断后继续

---
