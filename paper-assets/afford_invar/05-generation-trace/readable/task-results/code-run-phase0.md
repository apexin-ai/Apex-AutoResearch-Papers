# code run phase0

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_run-phase0_20260519T200204_result.json`
- **Structured JSON:** [`5387dc0cc016a1eba83d.json`](../../sessions/53/5387dc0cc016a1eba83d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Phase 0 完整结果

### 1. transformers 版本
已是 OpenVLA-OFT fork 4.40.1，无需恢复。prismatic 导入正常。

### 2. Diversity Metrics 汇总

| Metric | Overall Mean | Std | Range |
|--------|-------------|-----|-------|
| 1-BLEU | 0.7434 | 0.1724 | [0.214, 0.971] |
| OpenVLA embed_div (SigLIP, **primary**) | 0.2088 | 0.1682 | [0.0001, 0.583] |
| MiniLM embed_sim (ref) | 0.9290 | 0.0498 | [0.708, 0.990] |
| NLI entailment | 0.0550 | 0.1432 | [0.001, 0.887] |

**Per-tier:**

| Tier | n | Mean 1-BLEU | Mean OpenVLA embed_div | Mean NLI |
|------|---|-------------|----------------------|----------|
| Tier-1 | 170 | 0.7586 | 0.0137 | 0.0511 |
| Tier-2 | 185 | 0.7123 | 0.1289 | 0.0438 |
| Tier-3 | 295 | 0.7541 | 0.3713 | 0.0643 |

### 3. Tier 分布

| Tier | Count | Percentage |
|------|-------|------------|
| Tier-1 (trivial, sim > 0.95) | 170 | 26.2% |
| Tier-2 (moderate, 0.80-0.95) | 185 | 28.5% |
| Tier-3 (deep, < 0.80) | 295 | 45.4% |
| **Tier-2+ 合计** | **480** | **73.8%** |

### 4. KL Divergence (Layer 18)

| Stat | Value |
|------|-------|
| Mean KL | 0.000070 nats |
| Std KL | 0.000026 |
| Median KL | 0.000065 |
| Range | [0.000027, 0.000151] |
| n_tasks | 20 |
| n_pairs | 100 |

KL 在所有 task 间非常一致（0.000044–0.000096 per task），数值极低。

### 5. Phase 0 判定: **MARGINAL**

- **Tier-2+ = 73.8%** → 远超 40% 阈值 ✓
- **KL = 0.000070 nats** → 远低于 0.1 阈值 ✗

**解读**：paraphrases 在 SigLIP 嵌入空间中有很好的多样性（73.8% Tier-2+），但在 OpenVLA layer-18 attention 层面几乎没有差异。这说明虽然文本表面差异大，模型内部 attention pattern 几乎不受影响——paraphrase 改写在模型内部被"吸收"了。

这可能意味着：
1. OpenVLA 对 instruction paraphrasing 具有很强的内在不变性（好事——模型本身鲁棒）
2. 需要更深层的语义扰动（不只是词汇/句法变化）才能真正影响 attention
3. KL 阈值 0.1 对这种 attention-over-image-tokens 的度量可能过高

### 6. 结果文件路径

- `/root/afford_invar/data/phase0_results/diversity_metrics.json`
- `/root/afford_invar/data/phase0_results/tier_classification.json`
- `/root/afford_invar/data/phase0_results/kl_divergence.json`
- `/root/afford_invar/data/phase0_results/phase0_result.json`（已更新含 KL 数据）

---
