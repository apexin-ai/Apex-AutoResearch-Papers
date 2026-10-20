# code phase0 run

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase0-run_20260519T194852_result.json`
- **Structured JSON:** [`e26491899abd49b2b51c.json`](../../sessions/e2/e26491899abd49b2b51c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Phase 0 完整结果报告

### 1. transformers 修复确认
- 从 `transformers==5.8.1` 恢复为 OFT fork `transformers==4.40.1`
- `tokenizers==0.19.1`
- `prismatic` import 验证通过
- 额外修复：`timm` 从 1.0.27 降级到 0.9.16（OpenVLA 模型要求）

### 2. Embedding 修改说明
diversity_metrics.py 已经集成了双 embedding 架构（前一个 Worker 已完成）：
- **主要 embedding**: SigLIP text encoder，从 `/root/autodl-tmp/siglip-base-local/` 加载 `SiglipTextModel`，输出 768 维归一化向量
- **辅助参考**: `all-MiniLM-L6-v2` (sentence-transformers)
- tier_classifier.py 优先使用 `openvla_embed_sim`

额外修复：
- `kl_divergence.py` 的 `pixel_values` dtype 不匹配（float32 vs bf16）
- `kl_divergence.py` 的 image token 检测方式（OpenVLA 不使用 special token ID，而是直接 prepend image patch embeddings）

### 3. Phase 0 完整结果

| 指标 | 均值 | 标准差 | 范围 |
|------|------|--------|------|
| **1-BLEU** | 0.7434 | 0.1724 | [0.2139, 0.9715] |
| **openvla_embed_sim** | 0.7912 | 0.1682 | [0.4165, 0.9999] |
| **minilm_embed_sim** | 0.9290 | 0.0498 | [0.7082, 0.9898] |
| **nli_entailment** | 0.0550 | 0.1432 | [0.0010, 0.8866] |

**Tier 分布** (基于 openvla_embed_sim):
| Tier | 数量 | 百分比 |
|------|------|--------|
| Tier-1 (trivial, sim>0.95) | 170 | 26.2% |
| Tier-2 (moderate, 0.80-0.95) | 185 | 28.5% |
| Tier-3 (deep, <0.80) | 295 | 45.4% |
| **Tier-2+** | **480** | **73.8%** |

**KL Divergence** (Layer 18, 20 tasks, 100 pairs):
| 指标 | 值 |
|------|-----|
| Mean KL | 0.000070 nats |
| Std KL | 0.000026 |
| Median | 0.000065 |
| Range | [0.000027, 0.000151] |

### 综合判定: **MARGINAL**

- Tier-2+ = 73.8% (>40%) ✓ paraphrase diversity 很好
- KL = 0.0001 nats (<0.1) ✗ attention 分布几乎不变

KL 极低说明在 dummy image 条件下，不同 paraphrase 对 layer-18 attention-to-image 分布的影响极小。这可能意味着需要用真实任务图片而非 dummy image 来测 KL，或模型本身对 text variation 具有较强的 invariance。

### 4. 结果文件路径
- `/root/afford_invar/results/phase0/diversity_metrics.json`
- `/root/afford_invar/results/phase0/tier_classification.json`
- `/root/afford_invar/results/phase0/kl_divergence.json`
- `/root/afford_invar/results/phase0/phase0_result.json`

---
