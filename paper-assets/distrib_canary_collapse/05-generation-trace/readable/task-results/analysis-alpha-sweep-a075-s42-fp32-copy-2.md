# analysis alpha sweep a075 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a075_s42_fp32_20260519T114254_result.json`
- **Structured JSON:** [`e4dce6df1071c699c784.json`](../../sessions/e4/e4dce6df1071c699c784.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新 partial metrics。

续跑命令（等 GPU 空出后执行）:

```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
export HF_ENDPOINT=https://hf-mirror.com && \
export HF_HUB_DISABLE_XET=1 && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export TRANSFORMERS_OFFLINE=1 && \
export HF_HUB_OFFLINE=1 && \
CUDA_VISIBLE_DEVICES=5 python -u iterative_train.py \
  --model_name EleutherAI/pythia-410m \
  --seed 42 --data_dir data/wikitext103_5k \
  --synthetic_ratio 0.75 --num_generations 10 \
  --steps_per_gen 5000 --start_gen 4 \
  --output_dir results/alpha_sweep/a075_s42_fp32 \
  --batch_size 4 --max_length 512 --lr 5e-5 \
  --gen_max_new_tokens 256 --gen_batch_size 16 \
  --top_p 0.95 --optim adamw_torch
```

**总结**: α=0.75 fp32 仅完成 4/10 gen。Drift 幅度在 gen_3 已超过 α=0.50/0.60 的 10-gen 终值（entropy -35% vs -16%/-23%, ppl +88% vs +17%/+69%），定性确认 high regime。但 T=4 致 PermG/TY/MMCT 全部不可用，无法出 conclusion。需从 gen_4 续跑（加 `TRANSFORMERS_OFFLINE=1` 修复 HF config 加载问题），完成后重新分析。

---
