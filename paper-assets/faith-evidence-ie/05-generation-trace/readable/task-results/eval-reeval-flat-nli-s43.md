# eval reeval flat nli s43

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_reeval_flat_nli_s43_20260515T220105_result.json`
- **Structured JSON:** [`6de2bfccbcf4f7dd2f3b.json`](../../sessions/6d/6de2bfccbcf4f7dd2f3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**C001 约束阻塞：所有 GPU 显存占用都远超 2GB，无法提交 eval。**

当前 GPU 状态：
| GPU | 占用 | 进程 |
|-----|------|------|
| 0 | 14597 MiB | seed44 训练 |
| 1 | 16716 MiB | plan_011 step eval |
| 2 | 15158 MiB | seed45 训练 |
| 3 | 31134 MiB | 两个进程 |

已确认的修复命令（准备就绪，等 GPU 空闲即可提交）：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUNBUFFERED=1 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507 --base_model /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_path /root/autodl-tmp/data/docred --split dev --batch_size 16 --max_new_tokens 1024 --seed 43 --output_dir /root/autodl-tmp/eval_results/rsft_flat_nli_s43_reeval --no-quantize"
```

修复点：添加了 `--sft_adapter /root/autodl-tmp/sft_output`，使用具体 checkpoint 路径 `checkpoint-507`。

选项：
1. 等某个训练完成后提交到空闲 GPU
2. 你指定一个可以中断的进程，腾出 GPU

---
