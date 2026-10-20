# ssh esj probe qwen3 prep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_esj_probe_qwen3_prep_20260522T152951_result.json`
- **Structured JSON:** [`6115924d7310f41b2550.json`](../../sessions/61/6115924d7310f41b2550.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下。

---

## ESJ Probe on Qwen3-8B 准备工作汇总

### 1. ESJ 代码

**文件**: `/root/autodl-tmp/struct_self_consist_ie/code/run_esj.py` (~530 行)

**机制**: 对 N=8 samples 中每个 unique entity，用 finetuned 模型做 yes/no verification forward pass，取 P(yes) 作为 entity-level confidence。Prompt 模板：

```
In the following sentence, is "{entity_text}" a {entity_type} entity? Answer only yes or no.
Sentence: {sentence}
Answer:
```

通过 `apply_chat_template(enable_thinking=False)` 格式化，已适配 Qwen3。

**CLI 参数**:
```
--base_model_path  (required, 模型路径)
--adapter_path     (optional, LoRA adapter；merged 模型不需要)
--data_path        (required, samples.jsonl)
--output_dir       (required, 输出目录)
--max_instances    (default=0, 即全量)
--batch_size       (default=16)
```

Device 硬编码为 `"cuda"`，通过 `CUDA_VISIBLE_DEVICES` 选 GPU。

**无已有 ESJ 结果**（`esj_results.json` 搜索为空）。

### 2. Qwen3-8B Finetuned 模型（已 merged，可直接加载）

| 数据集 | Merged 模型路径 | 大小 |
|--------|----------------|------|
| CoNLL2003 | `checkpoints/qwen3-8b-conll2003-merged/` | ~16GB |
| SciERC | `checkpoints/qwen3-8b-scierc-merged-v2/` | ~16GB |
| FewNERD | `checkpoints/qwen3-8b-fewnerd-5epoch-merged/` | ~16GB |

都是 merged 模型，不需要 `--adapter_path`。

### 3. 可用数据（samples.jsonl）

| 数据集 | 路径 | 实例数 |
|--------|------|--------|
| SciERC | `output/scierc_mf4v2_seed42/samples.jsonl` | 551 |
| CoNLL | `output/conll_mf4v2_seed123/samples.jsonl` | 3,453 |
| FewNERD | `output/fewnerd_mf4v2_seed42/samples.jsonl` | 37,648 |

每个实例含 N=8 samples + gold + greedy + logprobs，格式完全匹配 `run_esj.py` 的输入要求。

### 4. 预估运行时长

每个实例平均 ~8-12 个 unique entities → 对应 verification prompts：
- SciERC: ~5K prompts → **~15-30s**
- CoNLL: ~25K prompts → **~1-2 min**
- FewNERD: ~300K prompts → **~12-25 min**

单 GPU 总计 **~15-30 分钟**（3 个 job 串行）。如果并行跑 3 张 GPU，**~25 分钟**搞定（由 FewNERD 瓶颈决定）。

### 5. GPU 可用性

autodl-5090: **cuda:0-3 全部空闲**（4× RTX 5090 32GB，0% utilization）。

**推荐**: 3 张 GPU 并行跑 3 个数据集（cuda:0=SciERC, cuda:1=CoNLL, cuda:2=FewNERD）。

### 6. 运行命令草案

```bash
cd /root/autodl-tmp/struct_self_consist_ie

# SciERC (cuda:0)
CUDA_VISIBLE_DEVICES=0 python code/run_esj.py \
  --base_model_path checkpoints/qwen3-8b-scierc-merged-v2 \
  --data_path output/scierc_mf4v2_seed42/samples.jsonl \
  --output_dir output/esj_qwen3_scierc_seed42 \
  --batch_size 32 &

# CoNLL (cuda:1)
CUDA_VISIBLE_DEVICES=1 python code/run_esj.py \
  --base_model_path checkpoints/qwen3-8b-conll2003-merged \
  --data_path output/conll_mf4v2_seed123/samples.jsonl \
  --output_dir output/esj_qwen3_conll_seed123 \
  --batch_size 32 &

# FewNERD (cuda:2)
CUDA_VISIBLE_DEVICES=2 python code/run_esj.py \
  --base_model_path checkpoints/qwen3-8b-fewnerd-5epoch-merged \
  --data_path output/fewnerd_mf4v2_seed42/samples.jsonl \
  --output_dir output/esj_qwen3_fewnerd_seed42 \
  --batch_size 32 &

wait
```

`batch_size=32` 可以用（5090 32GB 跑 8B bf16 forward-only 绰绰有余，prompt 很短）。

### 注意事项

- **CoNLL 没有 seed42 的 mf4v2 数据**，最近的是 seed123。如需 seed42 需先跑 inference。
- 3 个 job 同时加载 3 份 ~16GB 模型到 3 张 GPU，不存在显存冲突。
- 输出为 `esj_results.json`，包含 construction F1、entity-level AUROC/ρ、sample ranking 等完整指标。

---
