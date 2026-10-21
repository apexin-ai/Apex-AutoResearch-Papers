# ops gpt2m submit readiness

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpt2m-submit-readiness_20260515T115323_result.json`
- **Structured JSON:** [`6af6e2cdda6e5b101f37.json`](../../sessions/6a/6af6e2cdda6e5b101f37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕。汇总如下：

---

## 检查结果

| # | 检查项 | 状态 | 详情 |
|---|--------|------|------|
| 1 | 模型权重 | **通过** | `model.safetensors` 1.5GB，symlink 到 HF cache，config.json/tokenizer.json/vocab.json/merges.txt 均存在 |
| 2 | 模型可加载 | **通过** | params=354,823,168（~355M，GPT-2-medium 正确） |
| 3 | 训练数据 | **通过** | `data/wikitext103_5k/` 含 train/eval/prompts 三个 split，Arrow 格式 |
| 4 | 训练脚本 | **通过** | `iterative_train.py` 存在，--help 正常输出 |
| 5 | 环境 | **通过** | torch=2.10.0+cu128, cuda=True, gpus=2, transformers=4.57.6 |
| 6 | GPU | **通过** | 2× NVIDIA RTX PRO 6000 Blackwell (96GB each) |

**注意**：conda 环境需要先 source 激活，`python3` 不在默认 PATH 中。

---

## 提交命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp/distrib_canary_collapse && \
nohup python3 iterative_train.py \
  --model_name /root/autodl-tmp/models/gpt2-medium \
  --data_dir /root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k \
  --dataset wikitext103_5k \
  --synthetic_ratio 1.0 \
  --num_generations 10 \
  --steps_per_gen 5000 \
  --batch_size 32 \
  --seed 42 \
  --output_dir results/gpt2m_wiki/a100_s42 \
  > results/gpt2m_wiki/a100_s42/train.log 2>&1 &
```

**风险点**：
- 输出目录 `results/gpt2m_wiki/a100_s42` 需先创建，否则 nohup 重定向会失败（可在命令前加 `mkdir -p results/gpt2m_wiki/a100_s42`）
- batch_size=32 对 GPT-2-medium (355M) + 96GB 显存绰绰有余，无需调整
- 脚本默认只用单 GPU（无 `--gpu` 参数），如需指定 GPU 可用 `CUDA_VISIBLE_DEVICES=0` 前缀
- `--accumulate` 未加，使用默认行为（仅用最新一代合成数据）——确认是否符合实验设计

---
