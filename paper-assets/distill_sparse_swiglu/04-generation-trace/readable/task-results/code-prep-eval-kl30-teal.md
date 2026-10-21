# code prep eval kl30 teal

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-eval-kl30-teal_20260516T052024_result.json`
- **Structured JSON:** [`c3e3b9ce31b83ec8818a.json`](../../sessions/c3/c3e3b9ce31b83ec8818a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切确认完毕。

**汇总：**

| 项 | 状态 |
|---|---|
| evaluate.py | `/root/distill_sparse_swiglu/src/evaluate.py` |
| checkpoint | `/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt` (32 layers, 76M params, 加载正常) |
| 模型 | `/root/autodl-tmp/models/llama-3.1-8b` (4 shards, OK) |
| wikitext-2 缓存 | `/root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-2-raw-v1` (需 `HF_HOME` 指向) |
| `--sparsity_target` 默认值 | **0.5** — 必须显式传 `0.3` |
| GPU | cuda:0 空闲 (97GB free)，cuda:1 在用 (91GB used)。用 `--gpu 0` |
| 显存需求 | LLaMA-3.1-8B bf16 ≈ 16GB + predictor ~150MB + eval buffer ≈ 总 ~20GB，单卡 97GB 绰绰有余 |
| 预估运行时间 | 200 samples × seq_len 2048，单卡推理约 15-25 分钟 |

### 完整提交命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && export HF_HOME=/root/autodl-tmp/.hf_cache && CUDA_VISIBLE_DEVICES=0 nohup python src/evaluate.py \
  --model_name_or_path /root/autodl-tmp/models/llama-3.1-8b \
  --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt \
  --gpu 0 \
  --seq_len 2048 \
  --sparsity_target 0.3 \
  --skip_c4 \
  > logs/eval_kl30_teal_30pct.log 2>&1 &
```

**关键点：**
- `--sparsity_target 0.3` — 显式指定，避免落入默认 0.5 的陷阱
- `CUDA_VISIBLE_DEVICES=0` — 只用 cuda:0（约束 C001），`--gpu 0` 对应映射后的设备
- `HF_HOME=/root/autodl-tmp/.hf_cache` — 指向 wikitext-2 缓存位置
- `--skip_c4` — 只评 wikitext-2（任务只需 TEAL PPL）
- `nohup` + 日志重定向 — 约束 C002
- 日志写到 `logs/eval_kl30_teal_30pct.log`，用 `tail -f` 监控

---
