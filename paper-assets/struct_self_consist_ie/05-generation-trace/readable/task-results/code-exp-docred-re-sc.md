# code exp docred re sc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_docred_re_sc_20260520T192023_result.json`
- **Structured JSON:** [`336f81f96494cf6d6707.json`](../../sessions/33/336f81f96494cf6d6707.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。提交报告：

---

## DocRED RE SC Pilot — 完成报告

### 代码路径

| 位置 | 路径 |
|------|------|
| 本地脚本 | `artifacts/experiments/docred_re/prepare_docred_data.py` |
| 本地脚本 | `artifacts/experiments/docred_re/run_docred_re_sc.py` |
| 服务器脚本 | `/root/autodl-tmp/struct_self_consist_ie/experiments/docred_re/` |
| 服务器数据 | `/root/autodl-tmp/struct_self_consist_ie/data/docred_re_instances.jsonl` |
| Schema hint | `/root/autodl-tmp/struct_self_consist_ie/data/docred_schema.json` |
| 模型 | `/root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct` |

### 数据概况

- **数据集**: DocRED validation split (原始 998 文档，985 有效)
- **采样**: 200 instances (seed=42)
- **金标关系总数**: 2306
- **关系类型**: 88 种 (全集 96 种)
- **平均每文档**: ~11.5 个关系
- **文本长度**: 平均 1079 chars (最短 572, 最长 2873)
- **实体类型**: PER, ORG, LOC, TIME, NUM, MISC

### 运行命令

```bash
cd /root/autodl-tmp/struct_self_consist_ie
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

CUDA_VISIBLE_DEVICES=3 python3 experiments/docred_re/run_docred_re_sc.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct \
    --data data/docred_re_instances.jsonl \
    --schema data/docred_schema.json \
    --output-dir output/docred_re_sc
```

### 预计时长

- 200 instances × 9 passes (8 stochastic + 1 greedy) ≈ 1800 prompts
- DocRED 文档比 SciERC 长 (平均 1079 vs ~150 chars)，prompt 含 88 种关系类型的 schema hint (~1465 chars)
- 预计 **25-35 分钟**（比 SciERC 的 15 分钟更长，因为更长的 context）

### 关键设计决策

1. **使用 validation split**（test split 无标注）
2. **关系类型用 human-readable names**（从 `rel_info.json` 映射 Wikidata property IDs）
3. **Entity coreference 取第一个 mention** 作为代表，strict span matching 评估
4. **Schema hint 包含全部 88 种关系类型**（采样后的覆盖数）
5. **`use_train_format=False`** — 使用 `_RE_TEMPLATE`（纯 RE 模式）

### GPU 状态

- cuda:3 空闲 (0 MiB / 32607 MiB, 0% utilization)
- cuda:0 和 cuda:2 正在运行其他 vLLM 任务

### Registry

- `exp_docred_re_sc` — status: PREPARING

---
