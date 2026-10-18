# exp accum discovery

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_accum_discovery_20260521T070711_result.json`
- **Structured JSON:** [`625b81eee8532ace8cfb.json`](../../sessions/62/625b81eee8532ace8cfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Discovery 完成。以下是汇报。

---

## Accumulation 实验 Discovery 报告

### 1. 已有 Pipeline 分析

**核心脚本**: `scripts/accumulation_pipeline_gpt2xl.py` (656 行, 自包含)

Pipeline 5 阶段循环:
1. **混合数据** — human text + 上一代 synthetic text，按 mix_ratio 比例
2. **LoRA 微调** — 从 base model 重新微调 (r=16, alpha=32, 3 epochs, lr=2e-4, bf16, max_seq_len=512)
3. **文本生成** — 生成 5000 samples (nucleus: top_p=0.95, temp=1.0, max_new_tokens=512, batch=16)
4. **特征提取** — 19 维统计特征 (PPL 9 维 + surprisal 3 维 + lexical 7 维)，用同一 base model 做 ref
5. **RF 评估** — 200 trees, 5-fold CV

Phase 1-3 对 depth 1→2→3 各执行一次，Phase 4-5 最后执行一次。

**已有结果** (accum_v2 = GPT-2 XL nucleus):

| Mix Ratio | Overall Acc | Balanced Acc | Δ vs Full-Replace | 耗时 |
|-----------|------------|-------------|-------------------|------|
| 25% human | 70.08% | 70.08% | −15.82% | 4.14h |
| 50% human | 69.05% | 69.05% | −16.85% | 4.28h |

### 2. 模型与数据就绪状态

| 项目 | Pythia-1.4B nucleus | OLMo-1B temp0.9 |
|------|-------------------|-----------------|
| 模型路径 | `/root/autodl-tmp/models/pythia-1.4b` | `/root/autodl-tmp/models/olmo-1b-hf` |
| LoRA targets | `query_key_value` | `q_proj, k_proj, v_proj` |
| depth_0 (human) | `data/pythia_nucleus/depth_0.jsonl` → symlink to `data/depth_0.jsonl` (5000) | `data/olmo_temp09/depth_0.jsonl` → symlink to `data/olmo/depth_0.jsonl` (5000) |
| depth_1 (full-rep) | `data/pythia_nucleus/depth_1.jsonl` → `data/depth_1.jsonl` (5000) | `data/olmo_temp09/depth_1.jsonl` (5000, real file) |
| 解码策略 | nucleus (top_p=0.95, temp=1.0) | temp_only (temp=0.9) |

所有 depth_0 文件内容相同 (Wikipedia seed text)。模型和数据**全部就绪**。

### 3. 需要修改的参数 (相对于 GPT-2 XL 版本)

| 参数 | GPT-2 XL (已有) | Pythia-1.4B nucleus | OLMo-1B temp0.9 |
|------|-----------------|---------------------|-----------------|
| MODEL_ID | `gpt2-xl` | `/root/autodl-tmp/models/pythia-1.4b` | `/root/autodl-tmp/models/olmo-1b-hf` |
| LoRA target_modules | `["c_attn", "c_proj"]` | `["query_key_value"]` | `["q_proj", "k_proj", "v_proj"]` |
| Generation top_p | 0.95 | 0.95 | 不使用 |
| Generation temp | 1.0 | 1.0 | 0.9 |
| human_data 路径 | `data/gpt2xl/depth_0.jsonl` | `data/pythia_nucleus/depth_0.jsonl` | `data/olmo_temp09/depth_0.jsonl` |
| fullrep_d1 路径 | `data/gpt2xl/depth_1.jsonl` | `data/pythia_nucleus/depth_1.jsonl` | `data/olmo_temp09/depth_1.jsonl` |
| Results 目录 | `results/accumulation_v2/` | `results/accumulation_v3/pythia_nucleus/` | `results/accumulation_v3/olmo_temp09/` |
| Checkpoints 目录 | `checkpoints/accumulation_v2/` | `checkpoints/accumulation_v3/pythia_nucleus/` | `checkpoints/accumulation_v3/olmo_temp09/` |

### 4. 执行方案

**最佳方案**: 复制 `accumulation_pipeline_gpt2xl.py`，创建两个变体脚本:
- `accumulation_pipeline_pythia_nucleus.py`
- `accumulation_pipeline_olmo_temp09.py`

加上对应 shell wrapper:
- `run_accumulation_pythia_nucleus.sh`
- `run_accumulation_olmo_temp09.sh`

**注意**: OLMo temp0.9 的 `generate_text()` 函数需要修改生成参数 — 去掉 `top_p=0.95`，改为 `temperature=0.9` 且不传 `top_p`/`top_k`。

**执行命令** (每次只能运行一个，因 GPU 内存):
```bash
# 依次执行 4 个 run:
CUDA_VISIBLE_DEVICES=1 python3 scripts/accumulation_pipeline_pythia_nucleus.py --mix_ratio 0.25
CUDA_VISIBLE_DEVICES=1 python3 scripts/accumulation_pipeline_pythia_nucleus.py --mix_ratio 0.5
CUDA_VISIBLE_DEVICES=1 python3 scripts/accumulation_pipeline_olmo_temp09.py --mix_ratio 0.25
CUDA_VISIBLE_DEVICES=1 python3 scripts/accumulation_pipeline_olmo_temp09.py --mix_ratio 0.5
```

### 5. 资源估算

- **磁盘**: ~1.5GB/model × 2 mix ratios = ~6GB 新增 (75GB 空闲，充裕)
- **时间**: Pythia/OLMo 比 GPT-2 XL 小，预估每个 mix ratio ~3h，4 runs 串行 ≈ 12-14h
- **GPU**: cuda:1 (已分配给 N1)
- **已有 accumulation_v2 checkpoints**: 1.3GB (不影响新实验)

### 6. 注意事项

1. `data/pythia_nucleus/` 下全是 symlinks (→ `../depth_*.jsonl`)，指向的是原始 Pythia-1.4B **nucleus** full-replacement 数据，符合预期
2. Pipeline 内置 skip 逻辑: 如果 adapter 或 output 已存在会自动跳过，支持断点续跑
3. 特征提取的 ref model 必须改成对应的 base model (Pythia/OLMo)，不能继续用 gpt2-xl
4. Full-replacement baseline 数值需要从各模型自己的 full-replacement 结果中获取，不是 GPT-2 XL 的 0.8428

---
