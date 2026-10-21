# C4 数据 + GPT-2-medium 训练准备验证

**日期**: 2026-05-15  
**服务器**: westd-19828 (2× RTX PRO 6000 Blackwell 96GB)

---

## 检查结果

### 1. GPT-2-medium 模型缓存 ❌ 路径错误需修复

模型文件已下载（1.5GB, model.safetensors + tokenizer），但存放在**错误路径**：

| 路径 | 状态 |
|------|------|
| `/root/autodl-tmp/.hf_cache/models--gpt2-medium/` | ✅ 完整（1.5GB, blobs+snapshots+refs） |
| `/root/autodl-tmp/.hf_cache/hub/models--gpt2-medium/` | ❌ 空壳（4K, 仅 refs/main, 无 blobs/snapshots） |

**问题**: `.bashrc` 设置 `HF_HOME=/root/autodl-tmp/.hf_cache/`，transformers 会在 `$HF_HOME/hub/` 下查找模型。完整模型在 hub 外面（可能是用 `cache_dir=` 参数下载的），hub 内的是空壳。

**修复方法**（ssh_execute，1 步）：
```bash
rm -rf /root/autodl-tmp/.hf_cache/hub/models--gpt2-medium/
mv /root/autodl-tmp/.hf_cache/models--gpt2-medium/ /root/autodl-tmp/.hf_cache/hub/models--gpt2-medium/
```

### 2. C4 数据集 ✅ 就绪

`data/c4_5k/` 已由 `prepare_c4_v4.py` 准备完成（2026-05-15 16:51）：

| 分片 | 文件大小 | 预期条数 | 格式 |
|------|----------|----------|------|
| train | 10.7 MB (arrow) | 4500 | HF datasets, `text` 列 |
| eval | 1.2 MB (arrow) | 500 | HF datasets, `text` 列 |
| prompts | 195 KB (arrow) | ≤500 | HF datasets, `text` 列（64-word prefix） |

数据格式与 `iterative_train.py` 的 `load_from_disk()` + `text` 列完全匹配。

### 3. 训练脚本适配 ✅ 无需改动

`iterative_train.py` 参数检查：

| 参数 | 支持情况 | 说明 |
|------|----------|------|
| `--model_name gpt2-medium` | ✅ | 使用 `AutoModelForCausalLM`/`AutoTokenizer`，不绑定特定模型 |
| `--data_dir data/c4_5k` | ✅ | 加载 `data_dir/{train,eval,prompts}` |
| `--batch_size 32` | ✅ | argparse 参数，默认 4 |
| `--synthetic_ratio` | ✅ | 0.0-1.0 |
| `--dataset` | ✅ | 仅用于日志记录 |
| `--accumulate` | ✅ | 可选 |

GPT-2-medium (355M params) + bs=32 + max_length=512 + fp16 预估显存 ~12-15GB，RTX PRO 6000 96GB 充裕。

### 4. 现有实验参数参考

基于 `results/alpha_sweep/a025_s42/config.json`（Pythia-410m 基线）：
- steps_per_gen: 5000, lr: 5e-5, max_length: 512, gen_max_new_tokens: 256, top_p: 0.95

---

## 草拟提交命令

### gen_wiki_gpt2m_a100_s42（GPT-2-medium, WikiText, α=1.0, seed=42）

```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
CUDA_VISIBLE_DEVICES=0 python iterative_train.py \
  --model_name gpt2-medium \
  --data_dir data/wikitext103_5k \
  --dataset wikitext-103-v1 \
  --output_dir results/gen_wiki_gpt2m/a100_s42 \
  --synthetic_ratio 1.0 \
  --num_generations 10 \
  --steps_per_gen 5000 \
  --batch_size 32 \
  --seed 42
```

### gen_wiki_gpt2m_a025_s42（GPT-2-medium, WikiText, α=0.25, seed=42）

```bash
cd /root/autodl-tmp/distrib_canary_collapse && \
CUDA_VISIBLE_DEVICES=0 python iterative_train.py \
  --model_name gpt2-medium \
  --data_dir data/wikitext103_5k \
  --dataset wikitext-103-v1 \
  --output_dir results/gen_wiki_gpt2m/a025_s42 \
  --synthetic_ratio 0.25 \
  --num_generations 10 \
  --steps_per_gen 5000 \
  --batch_size 32 \
  --seed 42
```

---

## 提交前必须完成的准备步骤

1. **[必须] 修复 GPT-2-medium 缓存路径** — 将 `/root/autodl-tmp/.hf_cache/models--gpt2-medium/` 移入 `hub/` 目录
2. **[建议] 验证模型可加载** — 修复缓存后运行 `python -c "from transformers import AutoModelForCausalLM; m=AutoModelForCausalLM.from_pretrained('gpt2-medium'); print(sum(p.numel() for p in m.parameters()))"` 确认参数数 ~355M
3. **[确认] 等待 plan_006_s42 完成** — 当前两卡均被占用，需等实验释放 GPU
