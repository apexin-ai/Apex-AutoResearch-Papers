# code exp 004 preparation

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-004-preparation_20260519T160600_result.json`
- **Structured JSON:** [`b93ad4a6d9e270483b42.json`](../../sessions/b9/b93ad4a6d9e270483b42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有依赖确认可用。下面输出产出报告。

---

## exp-004 准备报告

### 1. 模型 Attention 层结构

三个架构的 hybrid-3-1 模型结构完全一致：

| 属性 | 值 |
|------|-----|
| 总层数 | 24 |
| Attention 层索引 | **[2, 5, 8, 11, 14, 17, 20, 23]** (8层) |
| Attention 头数 | 16 (GQA: 8 KV heads) |
| head_dim | hidden_size / 16 |
| Attention 类 | `fla.layers.attn.Attention` (标准 softmax + RoPE) |
| 实现 | Flash Attention (`flash_attn_func`)，不返回 attention weights |

非 attention 层的 mixer 因架构而异：

| 架构 | 非 attn 层 mixer | Block 类名 |
|------|-----------------|-----------|
| GatedDeltaNet | `GatedDeltaNet` | GatedDeltaNetBlock |
| RetNet | `MultiScaleRetention` | RetNetBlock |
| HGRN2 | `HGRN2Attention` | HGRN2Block |

### 2. Hook Point

所有架构统一：`model.model.layers[i].attn` (i ∈ [2,5,8,11,14,17,20,23])

Attention 层内部结构（三架构一致）：
```
attn.q_proj: Linear
attn.k_proj: Linear
attn.v_proj: Linear
attn.o_proj: Linear
attn.rotary: RotaryEmbedding
```

加载方式：
- GDN: `from fla.models.gated_deltanet import GatedDeltaNetForCausalLM`
- RetNet: `from fla.models.retnet import RetNetForCausalLM`
- HGRN2: `from fla.models.hgrn2 import HGRN2ForCausalLM` + monkey-patch `_tied_weights_keys`

### 3. exp-003 Sample IDs 数据

**文件**: `/root/entrainment_gated_ft/analysis/sample_perplexity_results.csv`

| 架构 | helped | hurt | neutral | 总计 |
|------|--------|------|---------|------|
| GDN | 462 | 615 | 4076 | 5153 |
| RetNet | 426 | 495 | 4232 | 5153 |
| HGRN2 | 548 | 395 | 4210 | 5153 |

列：`doc_id, {GDN,RetNet,HGRN2}_{pure_loss,helped,hurt}` (boolean flags)

注：`lambada_matched_per_example.csv` 有 h31 的 acc/logprob 但不含 RetNet 列；`sample_perplexity_results.csv` 是完整的三架构 helped/hurt 标签源。

### 4. 脚本

**路径**: `artifacts/exp-004/extract_attention_weights.py`

**策略**: Flash Attention 不返回 attention weights，脚本通过 forward hook 截获 Q、K（经 RoPE 后），手动计算 `softmax(Q·K^T / √d)` 并处理 GQA 的 KV head 重复。仅保存最后一个 token 的 attention 分布以节省内存。

**结构**:
- `AttentionWeightExtractor` — 注册/管理 hooks，计算 last-token attention
- `extract_attention_patterns()` — 逐样本推理 + 保存 `.pt` + 计算 entropy
- `analyze_helped_vs_hurt()` — helped/hurt 组间 entropy 对比
- `analyze_cross_arch_similarity()` — 跨架构同样本 attention 的 cosine similarity

**运行命令**（待 exp-011 结束后）:
```bash
python extract_attention_weights.py --arch gdn --device cuda:0
python extract_attention_weights.py --arch retnet --device cuda:0
python extract_attention_weights.py --arch hgrn2 --device cuda:0
python extract_attention_weights.py --analyze
```

---
