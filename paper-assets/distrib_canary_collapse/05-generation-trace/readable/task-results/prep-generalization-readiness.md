# prep generalization readiness

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_generalization_readiness_20260515T113900_result.json`
- **Structured JSON:** [`215ed81ba300132f7d34.json`](../../sessions/21/215ed81ba300132f7d34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在写就绪报告。

---

## Generalization 实验就绪报告

### 检查结果

| 项目 | 状态 | 说明 |
|------|------|------|
| GPT-2-medium 模型缓存 | ⏳ 下载中 | HF cache 无完整权重。已启动 ModelScope 下载（~54%，预计 3-4 分钟完成），路径：`/root/autodl-tmp/.hf_cache/modelscope/AI-ModelScope/gpt2-medium/` |
| C4 数据 | ✅ | `/root/autodl-tmp/distrib_canary_collapse/data/c4_5k/` — train: 4500, eval: 500, prompts: 500（Arrow 格式） |
| WikiText 数据 | ✅ | `data/wikitext103` 和 `data/wikitext103_5k` 均存在 |
| 训练脚本兼容性 | ⚠️ 见下 | 支持所有基本参数，但 eval 和 train 绑定同一 data_dir |
| 磁盘空间 | ✅ | 99GB 可用（250GB 中用了 152GB） |
| GPU 可用性 | ✅ | cuda:0 空闲（0 MiB），cuda:1 被 alpha_sweep a075_s42 占用 |

### 脚本参数确认

| 参数 | 参数名 | 值 |
|------|--------|-----|
| 模型 | `--model_name` | `gpt2-medium` 或本地路径 |
| 数据 | `--data_dir` | `data/wikitext103_5k` |
| α (synthetic ratio) | `--synthetic_ratio` | `1.0` / `0.25` |
| Batch size | `--batch_size` | `32` |
| 代数 | `--num_generations` | `10` |
| 步数/代 | `--steps_per_gen` | `5000` |

### ⚠️ 需关注的问题

1. **plan_006_s42 已超时退出**（EXIT_CODE=124）：模型是 **Pythia-410m**（非 GPT-2-medium），完成 gen 0-18，gen 19 未完成。你说的 GPT-2-medium plan_006 似乎还未启动。

2. **脚本无独立 eval_dir**：`iterative_train.py` 的 eval_dataset 从 `--data_dir` 的 `eval/` 子目录加载，与训练数据绑定。如果 "generalization" 是指训练 WikiText + 评估 C4，需要修改脚本增加 `--eval_dir` 参数；如果只是换模型跑同样流程，则无需改。

3. **GPT-2-medium 加载方式**：ModelScope 下载完成后，`--model_name` 应传本地路径 `/root/autodl-tmp/.hf_cache/modelscope/AI-ModelScope/gpt2-medium/`，或者在启动命令中设置 `HF_ENDPOINT=https://hf-mirror.com` 让 transformers 从镜像站加载。

4. **僵尸进程**：PID 94952（dryrun a025_s43）占用 4098% CPU 但 0% GPU，看起来卡住了。建议 kill。

### 建议启动命令

等 ModelScope 下载完成后：

```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
export CUDA_VISIBLE_DEVICES=0 && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_HUB_DISABLE_XET=1 && \
export HF_ENDPOINT=https://hf-mirror.com && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
PYTHONUNBUFFERED=1 python -u iterative_train.py \
    --model_name /root/autodl-tmp/.hf_cache/modelscope/AI-ModelScope/gpt2-medium \
    --data_dir data/wikitext103_5k \
    --synthetic_ratio 1.0 \
    --num_generations 10 \
    --steps_per_gen 5000 \
    --batch_size 32 \
    --seed 42 \
    --output_dir results/gen_wiki_gpt2m_a100_s42
```

α=0.25 版本将 `--synthetic_ratio 0.25` 和 `--output_dir results/gen_wiki_gpt2m_a025_s42` 替换即可。

### 待确认

1. "generalization" 是指换模型验证 collapse 可复现，还是指 cross-domain eval（训练 WikiText 评估 C4）？后者需改脚本。
2. PID 94952 是否可以 kill？
3. plan_006_s42 gen 19 是否需要补完？

---
