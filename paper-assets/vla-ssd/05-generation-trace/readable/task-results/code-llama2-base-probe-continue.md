# code llama2 base probe continue

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama2_base_probe_continue_20260517T054618_result.json`
- **Structured JSON:** [`7dfcb618ba01955a4901.json`](../../sessions/7d/7dfcb618ba01955a4901.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here is the complete **Step 6 Summary**:

---

## Llama-2-7B Base Control Experiment — Complete Results

### 1. Checkpoint Creation ✓

**Path**: `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-llama2base/`  
**Total size**: ~15 GB

| File | Size |
|------|------|
| model-00001-of-00003.safetensors | 13G |
| model-00002-of-00003.safetensors | 560M |
| model-00003-of-00003.safetensors | 785M |
| config.json + processor files | <1M |

- 289 LLM tensors fully replaced with Llama-2-7B base weights
- 2 tensors partially replaced (embed_tokens, lm_head: first 32000 rows from Llama-2, extra 64 from trained OpenVLA)
- 691 tensors kept (vision encoder + projector from trained OpenVLA)

---

### 2. Dense Probe: 10-Way Cross-Instruction Classification (per layer)

| Layer | trained | untrained | llama2base |
|-------|---------|-----------|------------|
| L0 | 0.100 | 0.100 | 0.100 |
| L1 | 0.996 | 1.000 | **0.802** |
| L2 | 1.000 | 1.000 | 0.987 |
| L3 | 1.000 | 1.000 | 0.991 |
| L4 | 1.000 | 0.998 | 0.995 |
| L5 | 1.000 | 0.999 | 1.000 |
| L6 | 1.000 | 0.996 | 1.000 |
| L7 | 1.000 | 0.996 | 0.999 |
| L8 | 1.000 | 0.986 | 0.999 |
| Chance | 0.100 | — | — |

**Key finding**: All three conditions achieve near-perfect classification from L2 onward. The llama2base condition shows a notable dip at L1 (0.802 vs 1.000 for untrained and 0.996 for trained), suggesting Llama-2's pretrained representations initially encode instruction information differently at early layers. By L2+, the pretrained LLM representations are equally separable.

---

### 3. L1 Attention: Per-Head Instruction Token Attention Fraction (32 heads)

**Llama2base condition** (task 0, representative; all 5 tasks show identical 9-head pattern):

| Head | text_attn | >50%? | | Head | text_attn | >50%? |
|------|-----------|-------|-|------|-----------|-------|
| H0 | 0.533 | **Y** | | H16 | 0.515 | **Y** |
| H1 | 0.215 | N | | H17 | 0.769 | **Y** |
| H2 | 0.302 | N | | H18 | 0.546 | **Y** |
| H3 | 0.258 | N | | H19 | 0.219 | N |
| H4 | 0.247 | N | | H20 | 0.227 | N |
| H5 | 0.191 | N | | H21 | 0.183 | N |
| H6 | 0.215 | N | | H22 | 0.127 | N |
| H7 | 0.222 | N | | H23 | 0.582 | **Y** |
| H8 | 0.238 | N | | H24 | 0.245 | N |
| H9 | 0.198 | N | | H25 | 0.844 | **Y** |
| H10 | 0.302 | N | | H26 | 0.528 | **Y** |
| H11 | 0.248 | N | | H27 | 0.900 | **Y** |
| H12 | 0.206 | N | | H28 | 0.277 | N |
| H13 | 0.411 | N | | H29 | 0.256 | N |
| H14 | 0.347 | N | | H30 | 0.268 | N |
| H15 | 0.572 | **Y** | | H31 | 0.198 | N |

**Instruction-attending heads**: {0, 15, 16, 17, 18, 23, 25, 26, 27} — **9/32 heads** (consistent across all 5 tasks)

---

### 4. Three-Way Comparison Summary

| Metric | trained | untrained | llama2base |
|--------|---------|-----------|------------|
| **L1 heads >50% text attn** | **25-26/32** | **0/32** | **9/32** |
| **L1 mean text attn** | 0.577 | 0.117 | 0.365 |
| **L1 mean image attn** | 0.213 | 0.878 | 0.617 |
| **L1 mean BOS attn** | 0.210 | 0.005 | 0.027 |
| **Dense probe L1 acc** | 0.996 | 1.000 | 0.802 |
| **Dense probe L8 acc** | 1.000 | 0.986 | 0.999 |

### Interpretation

The llama2base condition provides the critical missing control:

1. **Language pretraining contributes partial instruction routing**: Llama-2 base (no VLA training) already dedicates 9/32 heads to instruction tokens at L1, with 36.5% mean text attention. This is intermediate between untrained (0/32, 11.7%) and VLA-trained (25-26/32, 57.7%).

2. **VLA fine-tuning amplifies instruction routing beyond pretraining**: The jump from 9 → 25-26 instruction-attending heads shows VLA training doesn't just inherit language attention patterns but substantially reorganizes L1 attention to prioritize instruction tokens.

3. **Dense probe reveals a subtlety**: Despite having 9 instruction-attending heads, llama2base shows *lower* L1 classification accuracy (0.802) than untrained (1.000). This suggests Llama-2's pretrained representations encode language information in ways that don't directly map to instruction-discriminative features at L1, even though its attention patterns are more text-focused. The pretrained representations become fully discriminative by L2 (0.987).

4. **The instruction routing hierarchy is clear**: untrained (0 heads) → llama2base (9 heads) → trained (25-26 heads). This supports the claim that instruction-conditioned attention routing is primarily a product of VLA fine-tuning, with language pretraining providing a partial foundation.

---

**Output files**:
- Classification: `/root/autodl-tmp/vla-ssd/results/cross_instruction_dense/classification_results_with_llama2base.json`
- Dense features: `/root/autodl-tmp/vla-ssd/results/cross_instruction_dense/llama2base_cross_inst_dense.h5` (711.7 MB)
- L1 attention: `/root/autodl-tmp/vla-ssd/results/attention/l1_attention_llama2base_summary.json`
- L1 attention plot: `/root/autodl-tmp/vla-ssd/results/attention/l1_attention_llama2base.pdf`
- Checkpoint: `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-llama2base/`

---
