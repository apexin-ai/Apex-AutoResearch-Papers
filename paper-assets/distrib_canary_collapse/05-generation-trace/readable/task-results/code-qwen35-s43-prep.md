# code qwen35 s43 prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen35_s43_prep_20260519T171116_result.json`
- **Structured JSON:** [`f6250676bd852ca4f615.json`](../../sessions/f6/f6250676bd852ca4f615.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

### 环境验证

| 项目 | 状态 |
|------|------|
| 模型 `/root/autodl-tmp/models/Qwen3.5-0.8B-Base/` | ✅ 存在（safetensors, 752M params） |
| 代码 `iterative_train.py` | ✅ 存在 |
| 数据 `data/wikitext103_5k/` | ✅ 存在（train/eval/prompts） |
| 磁盘 `/root/autodl-tmp/` | ✅ 175G 可用（51% 已用） |

### Dry-run

✅ 通过。模型 CPU 加载成功，752M params，tokenizer vocab 248077。

### 训练命令（完整可复制）

基于 s42_v2 的 `config.json` 精确复刻，仅改 seed 和 output_dir：

```bash
bash -c "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 PYTHONUNBUFFERED=1 python -u iterative_train.py --model_name /root/autodl-tmp/models/Qwen3.5-0.8B-Base --data_dir data/wikitext103_5k --synthetic_ratio 1.0 --num_generations 10 --steps_per_gen 5000 --seed 43 --batch_size 4 --max_length 512 --lr 5e-5 --gen_max_new_tokens 256 --gen_batch_size 16 --top_p 0.95 --optim adamw_torch --output_dir results/generalize/qwen35_08b_wiki_a100_s43_fp32"
```

注：`CUDA_VISIBLE_DEVICES=1` 与 s42 一致（s42 registry 记录 gpu=cuda:1）。

### Registry

- exp_id: `qwen35_08b_wiki_a100_s43_fp32`
- status: PREPARING
- parent: `qwen35_08b_wiki_a100_s42_v2`
- hypothesis 已填写

### 预估

- GPU 时间：~12.8h（与 s42_v2 的 wall_clock 46094s / gpu_hours 12.8 一致）
- 磁盘需求：~5-8G（10 gen checkpoints），当前 175G 可用，充足

### 潜在问题

- `torch_dtype` 已 deprecated，transformers 5.8.1 改用 `dtype`，但 s42_v2 日志显示 iterative_train.py 已有 explicit cast（`Casting model from torch.bfloat16 to torch.float32`），无需额外处理
- flash-linear-attention 未装（warning），不影响正确性，只影响速度，s42 也是同样状态

---
