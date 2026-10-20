# Research conversation: Complementary Specialization in Unified Sparse-Dense Decoder Retrieval with Learned Query Routing ## Core Research Quest

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f.jsonl`
- **Structured JSON:** [`3bd40d5900e6a7ca0220.json`](../../sessions/3b/3bd40d5900e6a7ca0220.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T07:18:34.541Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T07:18:34.541Z",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "content": "# Complementary Specialization in Unified Sparse-Dense Decoder Retrieval with Learned Query Routing\n\n## Core Research Question\n\nIn a decoder-only LLM with shared transformer backbone, do sparse (lexical) and dense (semantic) retrieval heads develop complementary specialization—or do they compete for representational capacity? This is the central scientific question of this work. We hypothesize that joint training with bidirectional self-knowledge-distillation forces complementary specialization, yielding representations superior to independently trained models. Two derivative contributions support this investigation: (1) the unified architecture itself serves as a testbed for studying this question, and (2) a lightweight learned router exploits per-query complementarity patterns, doubling as a query-level retrieval signal diagnosis tool.\n\n## Research Opportunity\n\nThree verified gaps converge: (1) No decoder-only LLM produces both sparse and dense representations from a single forward pass with learned heads—LACONIC-8B (arXiv:2601.01684, Jan 2026) and Lion-SP/DS (SIGIR 2025) train separate models, while BGE-M3 (ACL Findings 2024) unifies but only on encoder-only XLM-RoBERTa; (2) No learned per-query router exists within a unified retrieval model—RouterRetriever (AAAI 2025) routes between separate external models, DAT (arXiv:2503.23013) requires additional LLM inference for post-hoc alpha tuning, and BGE-M3 uses fixed interpolation weights; (3) Bidirectional self-distillation between sparse and dense heads has never been validated in decoder-only architectures for text retrieval—the CIKM 2025 proof uses VLP encoder models (BLIP/ALBEF) on cross-modal tasks.\n\nThe scientific question left open: Lion-SP/DS (SIGIR 2025) showed sparse outperforms dense by 10.5% on OOD benchmarks at 8B scale, confirming strong signal complementarity, but trained them separately and thus cannot determine whether shared-backbone joint training amplifies or diminishes this complementarity. BGE-M3 answered this for encoder-only architectures (joint training helps), but decoder-only models with modified attention (causal→bidirectional) may behave differently due to distinct inductive biases. Our work directly resolves this open question.\n\n## Addressing the Trivial Alternative\n\nThe simplest alternative is running separate sparse and dense models (e.g., Lion-SP-8B + Lion-DS-8B) with post-hoc score fusion—fixed-weight (BGE-M3 style) or per-query adaptive (DAT style). We provide two lines of justification for shared-backbone joint training:\n\n(a) **Mutual Feature Transfer Hypothesis**: Shared transformer layers enable sparse and dense heads to develop complementary feature specialization through bidirectional self-KD cross-pollination. We verify through: (i) linear CKA similarity between joint vs. independently trained models at each layer, (ii) layer-wise linear probing for lexical features (exact n-gram overlap detection) vs. semantic features (paraphrase detection), (iii) attention entropy analysis per head per layer, (iv) direct comparison of joint-trained individual head performance vs. independently trained counterparts.\n\n**Sub-hypothesis on directional asymmetry**: SPLADE's vocab-space inductive bias (ReLU + FLOPS regularization encourages sparse term weighting) may limit its capacity to absorb upper-layer semantic features from self-KD, potentially making cross-pollination primarily unidirectional (dense benefits from lexical features, but sparse gains less from semantic features). We test this explicitly via unidirectional vs. bidirectional KD comparison; asymmetric benefit is itself a valuable finding about representation learning under architectural constraints.\n\n(b) **Computational Efficiency**: Single forward pass through one 8B model vs. two separate 8B forward passes yields ~2× encoding throughput and ~50% parameter reduction at serving time.\n\n## Research Landscape and Differentiation\n\n**Unified retrieval models** form a taxonomy along two axes: (1) what is unified (task modality vs. representation paradigm), and (2) how (parameter-switching vs. parameter-sharing). GritLM (ICLR 2025) unifies generation + embedding (different task modalities) via parameter-sharing, demonstrating zero-loss coexistence, but only produces dense representations. Hydra (arXiv:2603.28554, 2026) unifies retrieval + generation via parameter-switching (LoRA toggle), isolating modes in different parameter subsets. BGE-M3 (ACL Findings 2024) unifies sparse + dense + multi-vector via parameter-sharing but on encoder-only XLM-RoBERTa. Our work uniquely combines: same representation paradigm (sparse+dense), parameter-sharing, decoder-only architecture—the only configuration that can answer whether complementary specialization emerges in modern LLM backbones.\n\n**Dense SOTA**: Qwen3-Embedding-8B (MTEB multilingual 70.58, different backbone/training pipeline), Llama-Embed-Nemotron-8B (arXiv:2511.07025, same Llama-3.1-8B backbone, MMTEB #1), NV-Embed-v2 (ICLR 2025, Mistral-7B, latent attention pooling). **Sparse SOTA**: LACONIC-8B (60.2 MTEB-R, 61.5 BEIR-14), CSplade-bi-8B (IJCNLP 2025, 55.3 BEIR), Lion-SP-8B (SIGIR 2025, 55.2 BEIR). **Per-query routing**: RouterRetriever (AAAI 2025, +2.1 nDCG@10, domain-level routing between separate models), DAT (arXiv:2503.23013, external LLM per-query α, post-hoc). Our router operates internally from the query's [EOS] representation at zero extra inference cost—a finer-grained and cheaper approach.\n\n## Transfer Conditions for Self-KD\n\nThe CIKM 2025 bidirectional self-KD was validated on VLP encoder models (BLIP/ALBEF) for text-image cross-modal retrieval, where sparse and dense handle different modality alignment problems. Transfer to decoder-only text-text retrieval faces a different complementarity source: sparse (lexical) and dense (semantic) operate on the same modality. We argue validity because: (1) Lion-SP/DS empirically showed 10.5% OOD performance gap, demonstrating genuinely different signals in text-text; (2) the KL-divergence loss formulation is modality-agnostic; (3) we design explicit ablation to validate the transfer and quantify per-direction benefit.\n\n## Proposed Approach\n\nFine-tune Llama-3.1-8B with bidirectional attention, adding dual heads over shared backbone: sparse SPLADE head (vocab projection + ReLU + FLOPS regularization; DF-FLOPS variant (arXiv:2505.15070, SIGIR 2025) considered for training stability) and dense head (latent attention pooling). Three-stage curriculum: (1) sparse-only adaptation (10k steps, CSplade protocol) stabilizing ReLU activations, (2) joint contrastive training with bidirectional self-KD between heads using CIKM 2025 formula extended to decoder-only text retrieval, using GradCache to decouple effective batch size from GPU memory, (3) hard-negative fine-tuning with learned 2-layer MLP router predicting per-query sparse-dense interpolation weights from the query's [EOS] representation.\n\n## Experimental Design\n\n### Baselines (structured by comparability)\n\n**Primary (same backbone / controlled comparison):**\n- Sparse: LACONIC-8B, Lion-SP-8B, CSplade-bi-8B\n- Dense: Llama-Embed-Nemotron-8B (arXiv:2511.07025, same Llama-3.1-8B backbone), Lion-DS-8B\n- Post-hoc fusion: Lion-SP-8B + Lion-DS-8B with (i) best fixed α, (ii) DAT-style per-query α\n\n**Secondary (standard baselines):**\n- BM25 (Pyserini), SPLADE-v3, Contriever-msmarco\n\n**Reference (different backbone/pipeline, not apple-to-apple):**\n- Qwen3-Embedding-8B, NV-Embed-v2, GritLM-7B\n- BGE-M3 (all three modes: dense, sparse, multi-vector, and weighted combination)\n\n**Scope note on multi-vector**: We do not include a multi-vector (ColBERT-style) head because the storage cost at 8B scale (per-token embeddings × sequence length) makes it impractical for large-scale retrieval. BGE-M3's multi-vector results are reported as reference. Multi-vector integration is discussed as future work.\n\n### Evaluation Benchmarks\n- BEIR-14: per-dataset nDCG@10 for all 14 subsets\n- MTEB Retrieval subset: aggregate and per-dataset\n- MS MARCO dev: MRR@10\n- TREC DL 2019 and 2020: nDCG@10 and MAP\n- Multilingual retrieval (e.g., MIRACL) is out of scope for this English-focused study; discussed in limitations.\n\n### Ablation Studies\n\n1. **Self-KD ablation** (5 conditions): (a) no KD, (b) dense→sparse only, (c) sparse→dense only, (d) bidirectional (ours), (e) cross-encoder teacher KD (external reranker as teacher for both heads). Report sparse-only, dense-only, and fused nDCG@10. Tests directional asymmetry sub-hypothesis.\n\n2. **Router ablation** (6 conditions + analysis): (a) α=0 pure dense, (b) α=1 pure sparse, (c) α=0.5 equal, (d) best fixed α (grid search), (e) per-query oracle upper bound, (f) learned MLP router (ours). Supplementary: per-domain α distribution visualization across BEIR-14 subsets, revealing what query/domain characteristics the router learns to associate with sparse vs. dense preference.\n\n3. **Stage ablation** (4 conditions): (a) stage 1 only, (b) stage 1+2, (c) full pipeline, (d) skip stage 1. Report performance and sparsity levels at each checkpoint.\n\n4. **Representational analysis**: Linear CKA at each layer (joint vs. independent training), layer-wise linear probing (lexical: n-gram overlap detection; semantic: paraphrase detection), attention entropy per head per layer. Reveals whether dual-head training induces layer-wise specialization absent in single-task models.\n\n### Efficiency Evaluation\n- Index size: sparse vs dense vs combined, compared to separate model indices\n- Encoding throughput: queries/sec and docs/sec (1×8B unified vs 2×8B separate)\n- End-to-end retrieval latency including router\n- Parameter count: ~8.05B (shared backbone + dual heads) vs 16B (two separate 8B models)\n\n### Compute-Controlled Comparisons\n- Same-compute: Hydra-Retrieve (1×8B forward) vs two-model ensemble (2×8B) with post-hoc fusion\n- Same-parameter: per-head performance vs single-task 8B counterparts (any degradation?)\n\n### Performance Claims (three-dimensional)\nRather than targeting a single aggregate number, we evaluate success on three axes:\n1. **Mutual benefit**: each head in the unified model performs ≥ its independently trained counterpart (validates complementary specialization)\n2. **Routing value**: learned router > best fixed α by meaningful margin; gap to oracle < 30% of oracle-vs-best-fixed improvement\n3. **Efficiency**: ~2× throughput and ~50% serving parameters at comparable or better retrieval quality vs. two-model setup\n\n## Feasibility and Compute Budget\n\nTraining Llama-3.1-8B with bidirectional attention and dual heads. Bidirectional attention increases memory (O(n²) vs incremental KV-cache), limiting per-GPU batch size to 1-2 at 8B scale. Mitigation: GradCache for decoupled contrastive batch size (effective batch 256-512 via gradient accumulation over 128-256 steps) + cross-GPU negative sharing. Estimated compute: 8×A100-80GB for 7-10 days (Stage 1: ~1 day, Stage 2: ~4-6 days, Stage 3: ~1-2 days), or 16×A100 for 5-7 days. Proof-of-concept at 3B scale first (~3 days on 4×A100) to validate method. LoRA fallback if full fine-tuning exceeds budget (rank 16-64, all attention + MLP layers trainable, expected <2% performance gap based on RouterRetriever precedent). Cross-encoder KD ablation adds ~20% compute to Stage 2 (cross-encoder inference on training pairs).\n\n## Key References\n\n- Scaling Sparse and Dense Retrieval in Decoder-Only LLMs (SIGIR 2025)\n- LACONIC: Dense-Level Effectiveness for Scalable Sparse Retrieval (arXiv:2601.01684, 2026)\n- CSPLADE: Learned Sparse Retrieval with Causal Language Models (IJCNLP 2025)\n- M3-Embedding: Multi-Linguality Multi-Functionality Multi-Granularity (ACL Findings 2024)\n- RouterRetriever: Routing over a Mixture of Expert Embedding Models (AAAI 2025)\n- NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models (ICLR 2025)\n- Generative Representational Instruction Tuning (ICLR 2025)\n- Sparse and Dense Retrievers Learn Better Together (CIKM 2025)\n- Qwen3-Embedding (2025)\n- DAT: Dynamic Alpha Tuning for Hybrid Retrieval (arXiv:2503.23013, 2025)\n- Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model (arXiv:2603.28554, 2026)\n- Llama-Embed-Nemotron-8B: A Universal Text Embedding Model (arXiv:2511.07025, 2025)\n- An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-Doc (arXiv:2505.15070, SIGIR 2025)"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T07:18:34.547Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T07:18:34.547Z",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---

## Round 1

53 recorded events

### User

_source line 3 · 2026-05-30T07:18:34.577Z_

# Complementary Specialization in Unified Sparse-Dense Decoder Retrieval with Learned Query Routing

## Core Research Question

In a decoder-only LLM with shared transformer backbone, do sparse (lexical) and dense (semantic) retrieval heads develop complementary specialization—or do they compete for representational capacity? This is the central scientific question of this work. We hypothesize that joint training with bidirectional self-knowledge-distillation forces complementary specialization, yielding representations superior to independently trained models. Two derivative contributions support this investigation: (1) the unified architecture itself serves as a testbed for studying this question, and (2) a lightweight learned router exploits per-query complementarity patterns, doubling as a query-level retrieval signal diagnosis tool.

## Research Opportunity

Three verified gaps converge: (1) No decoder-only LLM produces both sparse and dense representations from a single forward pass with learned heads—LACONIC-8B (arXiv:2601.01684, Jan 2026) and Lion-SP/DS (SIGIR 2025) train separate models, while BGE-M3 (ACL Findings 2024) unifies but only on encoder-only XLM-RoBERTa; (2) No learned per-query router exists within a unified retrieval model—RouterRetriever (AAAI 2025) routes between separate external models, DAT (arXiv:2503.23013) requires additional LLM inference for post-hoc alpha tuning, and BGE-M3 uses fixed interpolation weights; (3) Bidirectional self-distillation between sparse and dense heads has never been validated in decoder-only architectures for text retrieval—the CIKM 2025 proof uses VLP encoder models (BLIP/ALBEF) on cross-modal tasks.

The scientific question left open: Lion-SP/DS (SIGIR 2025) showed sparse outperforms dense by 10.5% on OOD benchmarks at 8B scale, confirming strong signal complementarity, but trained them separately and thus cannot determine whether shared-backbone joint training amplifies or diminishes this complementarity. BGE-M3 answered this for encoder-only architectures (joint training helps), but decoder-only models with modified attention (causal→bidirectional) may behave differently due to distinct inductive biases. Our work directly resolves this open question.

## Addressing the Trivial Alternative

The simplest alternative is running separate sparse and dense models (e.g., Lion-SP-8B + Lion-DS-8B) with post-hoc score fusion—fixed-weight (BGE-M3 style) or per-query adaptive (DAT style). We provide two lines of justification for shared-backbone joint training:

(a) **Mutual Feature Transfer Hypothesis**: Shared transformer layers enable sparse and dense heads to develop complementary feature specialization through bidirectional self-KD cross-pollination. We verify through: (i) linear CKA similarity between joint vs. independently trained models at each layer, (ii) layer-wise linear probing for lexical features (exact n-gram overlap detection) vs. semantic features (paraphrase detection), (iii) attention entropy analysis per head per layer, (iv) direct comparison of joint-trained individual head performance vs. independently trained counterparts.

**Sub-hypothesis on directional asymmetry**: SPLADE's vocab-space inductive bias (ReLU + FLOPS regularization encourages sparse term weighting) may limit its capacity to absorb upper-layer semantic features from self-KD, potentially making cross-pollination primarily unidirectional (dense benefits from lexical features, but sparse gains less from semantic features). We test this explicitly via unidirectional vs. bidirectional KD comparison; asymmetric benefit is itself a valuable finding about representation learning under architectural constraints.

(b) **Computational Efficiency**: Single forward pass through one 8B model vs. two separate 8B forward passes yields ~2× encoding throughput and ~50% parameter reduction at serving time.

## Research Landscape and Differentiation

**Unified retrieval models** form a taxonomy along two axes: (1) what is unified (task modality vs. representation paradigm), and (2) how (parameter-switching vs. parameter-sharing). GritLM (ICLR 2025) unifies generation + embedding (different task modalities) via parameter-sharing, demonstrating zero-loss coexistence, but only produces dense representations. Hydra (arXiv:2603.28554, 2026) unifies retrieval + generation via parameter-switching (LoRA toggle), isolating modes in different parameter subsets. BGE-M3 (ACL Findings 2024) unifies sparse + dense + multi-vector via parameter-sharing but on encoder-only XLM-RoBERTa. Our work uniquely combines: same representation paradigm (sparse+dense), parameter-sharing, decoder-only architecture—the only configuration that can answer whether complementary specialization emerges in modern LLM backbones.

**Dense SOTA**: Qwen3-Embedding-8B (MTEB multilingual 70.58, different backbone/training pipeline), Llama-Embed-Nemotron-8B (arXiv:2511.07025, same Llama-3.1-8B backbone, MMTEB #1), NV-Embed-v2 (ICLR 2025, Mistral-7B, latent attention pooling). **Sparse SOTA**: LACONIC-8B (60.2 MTEB-R, 61.5 BEIR-14), CSplade-bi-8B (IJCNLP 2025, 55.3 BEIR), Lion-SP-8B (SIGIR 2025, 55.2 BEIR). **Per-query routing**: RouterRetriever (AAAI 2025, +2.1 nDCG@10, domain-level routing between separate models), DAT (arXiv:2503.23013, external LLM per-query α, post-hoc). Our router operates internally from the query's [EOS] representation at zero extra inference cost—a finer-grained and cheaper approach.

## Transfer Conditions for Self-KD

The CIKM 2025 bidirectional self-KD was validated on VLP encoder models (BLIP/ALBEF) for text-image cross-modal retrieval, where sparse and dense handle different modality alignment problems. Transfer to decoder-only text-text retrieval faces a different complementarity source: sparse (lexical) and dense (semantic) operate on the same modality. We argue validity because: (1) Lion-SP/DS empirically showed 10.5% OOD performance gap, demonstrating genuinely different signals in text-text; (2) the KL-divergence loss formulation is modality-agnostic; (3) we design explicit ablation to validate the transfer and quantify per-direction benefit.

## Proposed Approach

Fine-tune Llama-3.1-8B with bidirectional attention, adding dual heads over shared backbone: sparse SPLADE head (vocab projection + ReLU + FLOPS regularization; DF-FLOPS variant (arXiv:2505.15070, SIGIR 2025) considered for training stability) and dense head (latent attention pooling). Three-stage curriculum: (1) sparse-only adaptation (10k steps, CSplade protocol) stabilizing ReLU activations, (2) joint contrastive training with bidirectional self-KD between heads using CIKM 2025 formula extended to decoder-only text retrieval, using GradCache to decouple effective batch size from GPU memory, (3) hard-negative fine-tuning with learned 2-layer MLP router predicting per-query sparse-dense interpolation weights from the query's [EOS] representation.

## Experimental Design

### Baselines (structured by comparability)

**Primary (same backbone / controlled comparison):**
- Sparse: LACONIC-8B, Lion-SP-8B, CSplade-bi-8B
- Dense: Llama-Embed-Nemotron-8B (arXiv:2511.07025, same Llama-3.1-8B backbone), Lion-DS-8B
- Post-hoc fusion: Lion-SP-8B + Lion-DS-8B with (i) best fixed α, (ii) DAT-style per-query α

**Secondary (standard baselines):**
- BM25 (Pyserini), SPLADE-v3, Contriever-msmarco

**Reference (different backbone/pipeline, not apple-to-apple):**
- Qwen3-Embedding-8B, NV-Embed-v2, GritLM-7B
- BGE-M3 (all three modes: dense, sparse, multi-vector, and weighted combination)

**Scope note on multi-vector**: We do not include a multi-vector (ColBERT-style) head because the storage cost at 8B scale (per-token embeddings × sequence length) makes it impractical for large-scale retrieval. BGE-M3's multi-vector results are reported as reference. Multi-vector integration is discussed as future work.

### Evaluation Benchmarks
- BEIR-14: per-dataset nDCG@10 for all 14 subsets
- MTEB Retrieval subset: aggregate and per-dataset
- MS MARCO dev: MRR@10
- TREC DL 2019 and 2020: nDCG@10 and MAP
- Multilingual retrieval (e.g., MIRACL) is out of scope for this English-focused study; discussed in limitations.

### Ablation Studies

1. **Self-KD ablation** (5 conditions): (a) no KD, (b) dense→sparse only, (c) sparse→dense only, (d) bidirectional (ours), (e) cross-encoder teacher KD (external reranker as teacher for both heads). Report sparse-only, dense-only, and fused nDCG@10. Tests directional asymmetry sub-hypothesis.

2. **Router ablation** (6 conditions + analysis): (a) α=0 pure dense, (b) α=1 pure sparse, (c) α=0.5 equal, (d) best fixed α (grid search), (e) per-query oracle upper bound, (f) learned MLP router (ours). Supplementary: per-domain α distribution visualization across BEIR-14 subsets, revealing what query/domain characteristics the router learns to associate with sparse vs. dense preference.

3. **Stage ablation** (4 conditions): (a) stage 1 only, (b) stage 1+2, (c) full pipeline, (d) skip stage 1. Report performance and sparsity levels at each checkpoint.

4. **Representational analysis**: Linear CKA at each layer (joint vs. independent training), layer-wise linear probing (lexical: n-gram overlap detection; semantic: paraphrase detection), attention entropy per head per layer. Reveals whether dual-head training induces layer-wise specialization absent in single-task models.

### Efficiency Evaluation
- Index size: sparse vs dense vs combined, compared to separate model indices
- Encoding throughput: queries/sec and docs/sec (1×8B unified vs 2×8B separate)
- End-to-end retrieval latency including router
- Parameter count: ~8.05B (shared backbone + dual heads) vs 16B (two separate 8B models)

### Compute-Controlled Comparisons
- Same-compute: Hydra-Retrieve (1×8B forward) vs two-model ensemble (2×8B) with post-hoc fusion
- Same-parameter: per-head performance vs single-task 8B counterparts (any degradation?)

### Performance Claims (three-dimensional)
Rather than targeting a single aggregate number, we evaluate success on three axes:
1. **Mutual benefit**: each head in the unified model performs ≥ its independently trained counterpart (validates complementary specialization)
2. **Routing value**: learned router > best fixed α by meaningful margin; gap to oracle < 30% of oracle-vs-best-fixed improvement
3. **Efficiency**: ~2× throughput and ~50% serving parameters at comparable or better retrieval quality vs. two-model setup

## Feasibility and Compute Budget

Training Llama-3.1-8B with bidirectional attention and dual heads. Bidirectional attention increases memory (O(n²) vs incremental KV-cache), limiting per-GPU batch size to 1-2 at 8B scale. Mitigation: GradCache for decoupled contrastive batch size (effective batch 256-512 via gradient accumulation over 128-256 steps) + cross-GPU negative sharing. Estimated compute: 8×A100-80GB for 7-10 days (Stage 1: ~1 day, Stage 2: ~4-6 days, Stage 3: ~1-2 days), or 16×A100 for 5-7 days. Proof-of-concept at 3B scale first (~3 days on 4×A100) to validate method. LoRA fallback if full fine-tuning exceeds budget (rank 16-64, all attention + MLP layers trainable, expected <2% performance gap based on RouterRetriever precedent). Cross-encoder KD ablation adds ~20% compute to Stage 2 (cross-encoder inference on training pairs).

## Key References

- Scaling Sparse and Dense Retrieval in Decoder-Only LLMs (SIGIR 2025)
- LACONIC: Dense-Level Effectiveness for Scalable Sparse Retrieval (arXiv:2601.01684, 2026)
- CSPLADE: Learned Sparse Retrieval with Causal Language Models (IJCNLP 2025)
- M3-Embedding: Multi-Linguality Multi-Functionality Multi-Granularity (ACL Findings 2024)
- RouterRetriever: Routing over a Mixture of Expert Embedding Models (AAAI 2025)
- NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models (ICLR 2025)
- Generative Representational Instruction Tuning (ICLR 2025)
- Sparse and Dense Retrievers Learn Better Together (CIKM 2025)
- Qwen3-Embedding (2025)
- DAT: Dynamic Alpha Tuning for Hybrid Retrieval (arXiv:2503.23013, 2025)
- Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model (arXiv:2603.28554, 2026)
- Llama-Embed-Nemotron-8B: A Universal Text Embedding Model (arXiv:2511.07025, 2025)
- An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-Doc (arXiv:2505.15070, SIGIR 2025)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "3f7055d0-9ad2-4b47-8a14-8539288e8c1f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T07:18:34.575Z_

```json
{
  "parentUuid": "3f7055d0-9ad2-4b47-8a14-8539288e8c1f",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "7b170f28-e90d-4c7e-be00-9d33b3155027",
  "timestamp": "2026-05-30T07:18:34.575Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T07:18:34.575Z_

```json
{
  "parentUuid": "7b170f28-e90d-4c7e-be00-9d33b3155027",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "27b548a9-07e3-48ad-a899-f52d95822a39",
  "timestamp": "2026-05-30T07:18:34.575Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Unified sparse-dense decoder retrieval with learned routing",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---

### Assistant

_source line 7 · 2026-05-30T07:18:38.565Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this proposal as the 补救 agent (remediation agent), focusing exclusively on experimental design and technical execution completeness. I need to first do thorough literature research to understand the current experimental standards in this field before making any suggestions.

Let me start by searching for recent papers on unified sparse-dense retrieval, decoder-only LLM retrieval, and related experimental designs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27b548a9-07e3-48ad-a899-f52d95822a39",
  "isSidechain": false,
  "requestId": "req_011CbYM2MTGvneQLWT61Fzeh",
  "type": "assistant",
  "uuid": "50a81467-2b55-42d6-bc1e-74db75e1f5df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Vg2rGy3iFJEYAskGcVKQy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4939,
      "cache_read_input_tokens": 14080,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 4939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4939
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-30T07:18:40.188Z_

I need to do thorough literature research before evaluating the experimental design. Let me search for recent papers on unified sparse-dense retrieval, baseline standards, and experimental norms in this area.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50a81467-2b55-42d6-bc1e-74db75e1f5df",
  "isSidechain": false,
  "requestId": "req_011CbYM2MTGvneQLWT61Fzeh",
  "type": "assistant",
  "uuid": "10db9187-b5f9-4dcd-96bf-45c86cb58d5d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Vg2rGy3iFJEYAskGcVKQy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4939,
      "cache_read_input_tokens": 14080,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 4939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4939
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-30T07:18:40.600Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Aag515DSUwHmDSWqaK6hgd`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10db9187-b5f9-4dcd-96bf-45c86cb58d5d",
  "isSidechain": false,
  "requestId": "req_011CbYM2MTGvneQLWT61Fzeh",
  "type": "assistant",
  "uuid": "1beade0e-6d31-4665-aca3-92b6cad46fd2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Vg2rGy3iFJEYAskGcVKQy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4939,
      "cache_read_input_tokens": 14080,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4939,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 214,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 4939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4939
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-30T07:18:40.608Z_

<details><summary>↩ Tool result · `toolu_01Aag515DSUwHmDSWqaK6hgd`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1beade0e-6d31-4665-aca3-92b6cad46fd2",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "299ae663-0a16-42e8-8a09-aa00ad828a9b",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "1beade0e-6d31-4665-aca3-92b6cad46fd2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Complementary Specialization in Unified Sparse-Dense Decoder Retrieval with Learned Query Routing  ## Core Research Question  In a decoder-only LLM with shared transformer backbone, do sparse (lexic…",
  "leafUuid": "299ae663-0a16-42e8-8a09-aa00ad828a9b",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Unified sparse-dense decoder retrieval with learned routing",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---

### Assistant

_source line 13 · 2026-05-30T07:18:43.833Z_

Now let me conduct my front-loaded literature research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "299ae663-0a16-42e8-8a09-aa00ad828a9b",
  "isSidechain": false,
  "requestId": "req_011CbYM2oNFSdXcDGpf88Ame",
  "type": "assistant",
  "uuid": "e8f7a1e7-afc9-429c-ab2c-b780b5c436d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb8SP1Ew4ifU84Eqj7eLBT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 19019,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 320,
          "cache_read_input_tokens": 19019,
          "cache_creation_input_tokens": 742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 742
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-30T07:18:44.982Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K9ybjMQ22FT4FFXN4YSQzr`</summary>

```json
{
  "query": "Lion sparse dense retrieval decoder LLM SIGIR 2025 experimental setup baselines evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8f7a1e7-afc9-429c-ab2c-b780b5c436d4",
  "isSidechain": false,
  "requestId": "req_011CbYM2oNFSdXcDGpf88Ame",
  "type": "assistant",
  "uuid": "8be9ec40-7cee-4fdc-807f-c1bfd6292ab4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb8SP1Ew4ifU84Eqj7eLBT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 19019,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 320,
          "cache_read_input_tokens": 19019,
          "cache_creation_input_tokens": 742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 742
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-30T07:18:45.823Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019CLZ1ymBr4gQzi88Kc9otK`</summary>

```json
{
  "query": "LACONIC-8B sparse retrieval 2026 BEIR MTEB evaluation baselines ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8be9ec40-7cee-4fdc-807f-c1bfd6292ab4",
  "isSidechain": false,
  "requestId": "req_011CbYM2oNFSdXcDGpf88Ame",
  "type": "assistant",
  "uuid": "e314ac95-7348-415f-84a1-778b02ddc492",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb8SP1Ew4ifU84Eqj7eLBT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 19019,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 320,
          "cache_read_input_tokens": 19019,
          "cache_creation_input_tokens": 742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 742
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-30T07:18:46.792Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0179VnthaWE7u4QrrYiUC43i`</summary>

```json
{
  "query": "BGE-M3 unified sparse dense multi-vector retrieval ablation self-knowledge distillation experimental design"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e314ac95-7348-415f-84a1-778b02ddc492",
  "isSidechain": false,
  "requestId": "req_011CbYM2oNFSdXcDGpf88Ame",
  "type": "assistant",
  "uuid": "e7696473-d72f-4deb-8956-5b17fc8a7e2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb8SP1Ew4ifU84Eqj7eLBT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 19019,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 320,
          "cache_read_input_tokens": 19019,
          "cache_creation_input_tokens": 742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 742
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-30T07:18:47.394Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HjqsfcP5TTsKPCU6Ck54dg`</summary>

```json
{
  "query": "RouterRetriever AAAI 2025 per-query routing retrieval baselines evaluation metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7696473-d72f-4deb-8956-5b17fc8a7e2a",
  "isSidechain": false,
  "requestId": "req_011CbYM2oNFSdXcDGpf88Ame",
  "type": "assistant",
  "uuid": "d80ddaea-1cfc-4a2a-bdeb-0ec67e3d3a1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb8SP1Ew4ifU84Eqj7eLBT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 19019,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 320,
          "cache_read_input_tokens": 19019,
          "cache_creation_input_tokens": 742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 742
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-30T07:18:48.171Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QzXHrDBq1waLMdnEpSYYNp`</summary>

```json
{
  "query": "GradCache contrastive learning decoder-only retrieval training 8B scale compute requirements 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d80ddaea-1cfc-4a2a-bdeb-0ec67e3d3a1c",
  "isSidechain": false,
  "requestId": "req_011CbYM2oNFSdXcDGpf88Ame",
  "type": "assistant",
  "uuid": "7785c7ca-e8b2-45d6-a61b-0069adcf724a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cb8SP1Ew4ifU84Eqj7eLBT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 742,
      "cache_read_input_tokens": 19019,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 742,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 320,
          "cache_read_input_tokens": 19019,
          "cache_creation_input_tokens": 742,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 742
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-30T07:18:52.392Z_

<details><summary>↩ Tool result · `toolu_019CLZ1ymBr4gQzi88Kc9otK`</summary>

```text
Web search results for query: "LACONIC-8B sparse retrieval 2026 BEIR MTEB evaluation baselines ablation"

Links: [{"title":"LACONIC: Dense-Level Effectiveness for Scalable Sparse ...","url":"https://www.arxiv.org/pdf/2601.01684"},{"title":"LACONIC: Dense-Level Effectiveness for Scalable Sparse Retrieval via a Two-Phase Training Curriculum","url":"https://arxiv.org/html/2601.01684v1"},{"title":"Benchmarking Google Embeddings 2 against Open-Source Models for Multilingual Dense Retrieval and RAG Systems","url":"https://arxiv.org/html/2605.23618"},{"title":"Scaling Sparse and Dense Retrieval in Decoder-Only LLMs","url":"https://arxiv.org/pdf/2502.15526"},{"title":"Benchmarking Information Retrieval Models on Complex Retrieval Tasks","url":"https://arxiv.org/html/2509.07253v1"},{"title":"BEIR Benchmark Leaderboard 2025 & 2026: NDCG@10 Scores & Rankings | Ailog RAG","url":"https://app.ailog.fr/en/blog/news/beir-benchmark-update"},{"title":"Milco: Learned Sparse Retrieval Across Languages via a Multilingual Connector","url":"https://arxiv.org/html/2510.00671"}]

Based on the search results, I found relevant information about LACONIC-8B:

## LACONIC-8B Performance and Evaluation

LACONIC-8B achieves an average of 60.2 nDCG@10 on 15 MTEB Retrieval datasets, ranking 15th on the leaderboard as of January 1, 2026, being the only learned sparse retrieval model at this position.

## Architecture and Training

LACONIC is a bi-encoder retrieval model which builds upon the SPLADE framework while incorporating architectural best practices for scaling sparse retrievers. The performance of LACONIC stems from the integration of powerful LLM backbones with a streamlined two-phase training curriculum.

## Efficiency and Scalability

LACONIC achieves these results using a fraction of the compute budget of its competitors while maintaining a significantly smaller index memory footprint. By combining a bidirectional adaptation of Llama3 with a targeted two-phase training curriculum, sparse retrieval can achieve performance parity with dense models while maintaining superior efficiency.

The research demonstrates that LACONIC-8B represents a significant advancement in learned sparse retrieval models, achieving competitive performance with established benchmarks while maintaining efficiency advantages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e314ac95-7348-415f-84a1-778b02ddc492",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "26761010-66bf-4cd8-915e-0b0b35e44ab0",
  "toolUseResult": {
    "query": "LACONIC-8B sparse retrieval 2026 BEIR MTEB evaluation baselines ablation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SUn7Vc3uqpDg6P4S8nxTDs",
        "content": [
          {
            "title": "LACONIC: Dense-Level Effectiveness for Scalable Sparse ...",
            "url": "https://www.arxiv.org/pdf/2601.01684"
          },
          {
            "title": "LACONIC: Dense-Level Effectiveness for Scalable Sparse Retrieval via a Two-Phase Training Curriculum",
            "url": "https://arxiv.org/html/2601.01684v1"
          },
          {
            "title": "Benchmarking Google Embeddings 2 against Open-Source Models for Multilingual Dense Retrieval and RAG Systems",
            "url": "https://arxiv.org/html/2605.23618"
          },
          {
            "title": "Scaling Sparse and Dense Retrieval in Decoder-Only LLMs",
            "url": "https://arxiv.org/pdf/2502.15526"
          },
          {
            "title": "Benchmarking Information Retrieval Models on Complex Retrieval Tasks",
            "url": "https://arxiv.org/html/2509.07253v1"
          },
          {
            "title": "BEIR Benchmark Leaderboard 2025 & 2026: NDCG@10 Scores & Rankings | Ailog RAG",
            "url": "https://app.ailog.fr/en/blog/news/beir-benchmark-update"
          },
          {
            "title": "Milco: Learned Sparse Retrieval Across Languages via a Multilingual Connector",
            "url": "https://arxiv.org/html/2510.00671"
          }
        ]
      },
      "Based on the search results, I found relevant information about LACONIC-8B:\n\n## LACONIC-8B Performance and Evaluation\n\nLACONIC-8B achieves an average of 60.2 nDCG@10 on 15 MTEB Retrieval datasets, ranking 15th on the leaderboard as of January 1, 2026, being the only learned sparse retrieval model at this position.\n\n## Architecture and Training\n\nLACONIC is a bi-encoder retrieval model which builds upon the SPLADE framework while incorporating architectural best practices for scaling sparse retrievers. The performance of LACONIC stems from the integration of powerful LLM backbones with a streamlined two-phase training curriculum.\n\n## Efficiency and Scalability\n\nLACONIC achieves these results using a fraction of the compute budget of its competitors while maintaining a significantly smaller index memory footprint. By combining a bidirectional adaptation of Llama3 with a targeted two-phase training curriculum, sparse retrieval can achieve performance parity with dense models while maintaining superior efficiency.\n\nThe research demonstrates that LACONIC-8B represents a significant advancement in learned sparse retrieval models, achieving competitive performance with established benchmarks while maintaining efficiency advantages."
    ],
    "durationSeconds": 6.560012587000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e314ac95-7348-415f-84a1-778b02ddc492",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-30T07:18:52.484Z_

<details><summary>↩ Tool result · `toolu_01K9ybjMQ22FT4FFXN4YSQzr`</summary>

```text
Web search results for query: "Lion sparse dense retrieval decoder LLM SIGIR 2025 experimental setup baselines evaluation"

Links: [{"title":"GitHub - HansiZeng/scaling-retriever: [SIGIR 2025] The official repo for \"Scaling Sparse and Dense Retrieval in Decoder-Only LLMs\" · GitHub","url":"https://github.com/HansiZeng/scaling-retriever"},{"title":"Scaling Sparse and Dense Retrieval in Decoder-Only LLMs","url":"https://arxiv.org/html/2502.15526"},{"title":"Scaling Sparse and Dense Retrieval in Decoder-Only LLMs | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/abs/10.1145/3726302.3730225"},{"title":"(PDF) Scaling Sparse and Dense Retrieval in Decoder-Only LLMs","url":"https://www.researchgate.net/publication/389274173_Scaling_Sparse_and_Dense_Retrieval_in_Decoder-Only_LLMs"},{"title":"Scaling Sparse and Dense Retrieval in Decoder-Only LLMs [Quick Review]","url":"https://liner.com/review/scaling-sparse-and-dense-retrieval-in-decoderonly-llms"},{"title":"Scaling Sparse and Dense Retrieval in Decoder-Only LLMs Hansi Zeng","url":"https://arxiv.org/pdf/2502.15526"}]

Based on the search results, I found comprehensive information about the Lion paper on sparse and dense retrieval in decoder-only LLMs accepted to SIGIR 2025. Here are the details:

## Experimental Setup

The research systematically investigated the scaling behaviors of sparse and dense retrieval models across different LLM sizes (1B, 3B, 8B) and fine-tuning objectives (CL, KD, CL+KD) using MSMARCO data. For MNTP pre-training, they used 2×A100 80GB GPUs with a training batch size per device of 32, maximum sequence length of 512, and gradient accumulation step of 1, with each training run completing within approximately 40–44 hours.

## Baselines and Evaluation

The proposed Lion models achieve state-of-the-art results among baselines with similar or smaller parameter sizes (≤ 1B), with Lion-SP-1B significantly outperforming ColBERTv2 by 3.2% on MS MARCO Dev and by 7.2% on BEIR. Lion-SP-8B achieves superior performance compared to RepLLaMA across both in-domain (MS MARCO Dev, TREC 19+20) and out-of-domain (BEIR) benchmarks.

## Key Findings

Sparse retrieval consistently outperformed dense retrieval across all fine-tuning objectives and demonstrated greater robustness, particularly on out-of-domain datasets. While contrastive loss benefits from scaling, knowledge distillation shows minimal improvement with increased model size, suggesting a capacity limitation relative to the teacher model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8be9ec40-7cee-4fdc-807f-c1bfd6292ab4",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "72b9e346-ab30-484e-b72d-acdf77915829",
  "toolUseResult": {
    "query": "Lion sparse dense retrieval decoder LLM SIGIR 2025 experimental setup baselines evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WUCpHAaktUyonHhfLh9hDy",
        "content": [
          {
            "title": "GitHub - HansiZeng/scaling-retriever: [SIGIR 2025] The official repo for \"Scaling Sparse and Dense Retrieval in Decoder-Only LLMs\" · GitHub",
            "url": "https://github.com/HansiZeng/scaling-retriever"
          },
          {
            "title": "Scaling Sparse and Dense Retrieval in Decoder-Only LLMs",
            "url": "https://arxiv.org/html/2502.15526"
          },
          {
            "title": "Scaling Sparse and Dense Retrieval in Decoder-Only LLMs | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval",
            "url": "https://dl.acm.org/doi/abs/10.1145/3726302.3730225"
          },
          {
            "title": "(PDF) Scaling Sparse and Dense Retrieval in Decoder-Only LLMs",
            "url": "https://www.researchgate.net/publication/389274173_Scaling_Sparse_and_Dense_Retrieval_in_Decoder-Only_LLMs"
          },
          {
            "title": "Scaling Sparse and Dense Retrieval in Decoder-Only LLMs [Quick Review]",
            "url": "https://liner.com/review/scaling-sparse-and-dense-retrieval-in-decoderonly-llms"
          },
          {
            "title": "Scaling Sparse and Dense Retrieval in Decoder-Only LLMs Hansi Zeng",
            "url": "https://arxiv.org/pdf/2502.15526"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the Lion paper on sparse and dense retrieval in decoder-only LLMs accepted to SIGIR 2025. Here are the details:\n\n## Experimental Setup\n\nThe research systematically investigated the scaling behaviors of sparse and dense retrieval models across different LLM sizes (1B, 3B, 8B) and fine-tuning objectives (CL, KD, CL+KD) using MSMARCO data. For MNTP pre-training, they used 2×A100 80GB GPUs with a training batch size per device of 32, maximum sequence length of 512, and gradient accumulation step of 1, with each training run completing within approximately 40–44 hours.\n\n## Baselines and Evaluation\n\nThe proposed Lion models achieve state-of-the-art results among baselines with similar or smaller parameter sizes (≤ 1B), with Lion-SP-1B significantly outperforming ColBERTv2 by 3.2% on MS MARCO Dev and by 7.2% on BEIR. Lion-SP-8B achieves superior performance compared to RepLLaMA across both in-domain (MS MARCO Dev, TREC 19+20) and out-of-domain (BEIR) benchmarks.\n\n## Key Findings\n\nSparse retrieval consistently outperformed dense retrieval across all fine-tuning objectives and demonstrated greater robustness, particularly on out-of-domain datasets. While contrastive loss benefits from scaling, knowledge distillation shows minimal improvement with increased model size, suggesting a capacity limitation relative to the teacher model."
    ],
    "durationSeconds": 7.493372304,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8be9ec40-7cee-4fdc-807f-c1bfd6292ab4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-30T07:18:55.253Z_

<details><summary>↩ Tool result · `toolu_0179VnthaWE7u4QrrYiUC43i`</summary>

```text
Web search results for query: "BGE-M3 unified sparse dense multi-vector retrieval ablation self-knowledge distillation experimental design"

Links: [{"title":"BGE-M3: Multilingual Bi-Encoder Model","url":"https://www.emergentmind.com/topics/bge-m3-model"},{"title":"Multilingual BGE-M3 Model","url":"https://www.emergentmind.com/topics/multilingual-bge-m3-model"},{"title":"[2402.03216v4] BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation","url":"https://arxiv.org/abs/2402.03216v4"},{"title":"BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation","url":"https://arxiv.org/html/2402.03216v3"},{"title":"BAAI/bge-m3 · Hugging Face","url":"https://huggingface.co/BAAI/bge-m3"},{"title":"BGE M3-Embedding Model","url":"https://www.emergentmind.com/topics/bge-m3-embedding-model"},{"title":"bge-m3","url":"https://ollama.com/library/bge-m3"},{"title":"Paper page - BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation","url":"https://huggingface.co/papers/2402.03216"},{"title":"M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation","url":"https://arxiv.org/html/2402.03216v5"},{"title":"M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation","url":"https://arxiv.org/pdf/2402.03216"}]

Based on the search results, here's what I found about BGE-M3 and its unified sparse dense multi-vector retrieval approach with self-knowledge distillation:

## Model Overview

BGE-M3 is a high-capacity, multilingual bi-encoder model enabling dense, sparse, and multi-vector retrieval across text granularities up to 8,192 tokens. It can simultaneously perform the three common retrieval functionalities of embedding model: dense retrieval, multi-vector retrieval, and sparse retrieval, which provides a unified model foundation for real-world IR applications.

## Self-Knowledge Distillation Framework

The model proposes a novel self-knowledge distillation approach, where the relevance scores from different retrieval functionalities can be integrated as the teacher signal to enhance the training quality. More specifically, each head learns not only from its direct target (e.g., InfoNCE loss) but also from an ensemble teacher combining the outputs of all heads, using soft label distribution matching.

## Experimental Design & Ablation Studies

The paper includes an ablation study of self-knowledge distillation with MIRACL, and performs ablation study by removing the long document data from the fine-tuning stage. For long document retrieval, M3 (Sparse) achieves about 10 points improvement over the dense method, while multi-vector retrieval brings 5.1+ points improvement over M3 (Dense).

The comprehensive research is detailed in the original paper: "BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation"


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e7696473-d72f-4deb-8956-5b17fc8a7e2a",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "22ccb649-5554-4174-8834-84cc1ba3e877",
  "toolUseResult": {
    "query": "BGE-M3 unified sparse dense multi-vector retrieval ablation self-knowledge distillation experimental design",
    "results": [
      {
        "tool_use_id": "srvtoolu_015LBinEMzskjctrqzuiTYCo",
        "content": [
          {
            "title": "BGE-M3: Multilingual Bi-Encoder Model",
            "url": "https://www.emergentmind.com/topics/bge-m3-model"
          },
          {
            "title": "Multilingual BGE-M3 Model",
            "url": "https://www.emergentmind.com/topics/multilingual-bge-m3-model"
          },
          {
            "title": "[2402.03216v4] BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation",
            "url": "https://arxiv.org/abs/2402.03216v4"
          },
          {
            "title": "BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation",
            "url": "https://arxiv.org/html/2402.03216v3"
          },
          {
            "title": "BAAI/bge-m3 · Hugging Face",
            "url": "https://huggingface.co/BAAI/bge-m3"
          },
          {
            "title": "BGE M3-Embedding Model",
            "url": "https://www.emergentmind.com/topics/bge-m3-embedding-model"
          },
          {
            "title": "bge-m3",
            "url": "https://ollama.com/library/bge-m3"
          },
          {
            "title": "Paper page - BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation",
            "url": "https://huggingface.co/papers/2402.03216"
          },
          {
            "title": "M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation",
            "url": "https://arxiv.org/html/2402.03216v5"
          },
          {
            "title": "M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation",
            "url": "https://arxiv.org/pdf/2402.03216"
          }
        ]
      },
      "Based on the search results, here's what I found about BGE-M3 and its unified sparse dense multi-vector retrieval approach with self-knowledge distillation:\n\n## Model Overview\n\nBGE-M3 is a high-capacity, multilingual bi-encoder model enabling dense, sparse, and multi-vector retrieval across text granularities up to 8,192 tokens. It can simultaneously perform the three common retrieval functionalities of embedding model: dense retrieval, multi-vector retrieval, and sparse retrieval, which provides a unified model foundation for real-world IR applications.\n\n## Self-Knowledge Distillation Framework\n\nThe model proposes a novel self-knowledge distillation approach, where the relevance scores from different retrieval functionalities can be integrated as the teacher signal to enhance the training quality. More specifically, each head learns not only from its direct target (e.g., InfoNCE loss) but also from an ensemble teacher combining the outputs of all heads, using soft label distribution matching.\n\n## Experimental Design & Ablation Studies\n\nThe paper includes an ablation study of self-knowledge distillation with MIRACL, and performs ablation study by removing the long document data from the fine-tuning stage. For long document retrieval, M3 (Sparse) achieves about 10 points improvement over the dense method, while multi-vector retrieval brings 5.1+ points improvement over M3 (Dense).\n\nThe comprehensive research is detailed in the original paper: \"BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation\""
    ],
    "durationSeconds": 8.458065215000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e7696473-d72f-4deb-8956-5b17fc8a7e2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-30T07:18:56.241Z_

<details><summary>↩ Tool result · `toolu_01HjqsfcP5TTsKPCU6Ck54dg`</summary>

```text
Web search results for query: "RouterRetriever AAAI 2025 per-query routing retrieval baselines evaluation metrics"

Links: [{"title":"GitHub - amy-hyunji/RouterRetriever","url":"https://github.com/amy-hyunji/RouterRetriever"},{"title":"RouterRetriever: Routing over a Mixture of Expert Embedding Models","url":"https://arxiv.org/html/2409.02685v2"},{"title":"RouterRetriever: Routing over a Mixture of Expert Embedding Models | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/33306"},{"title":"amy-hyunji-lee/RouterRetriever · Hugging Face","url":"https://huggingface.co/amy-hyunji-lee/RouterRetriever"},{"title":"ROUTERRETRIEVER: Routing over a Mixture of Expert Embedding Models Hyunji Lee1*","url":"https://arxiv.org/pdf/2409.02685"},{"title":"RouterRetriever: Exploring the Benefits of Routing over Multiple Expert Embedding Models","url":"https://arxiv.org/html/2409.02685v1"},{"title":"[2409.02685] RouterRetriever: Routing over a Mixture of Expert Embedding Models","url":"https://arxiv.org/abs/2409.02685"},{"title":"Query Routing for Retrieval-Augmented Language Models","url":"https://arxiv.org/html/2505.23052v1"}]

Based on the search results, here's what I found about RouterRetriever from AAAI 2025:

## Overview

RouterRetriever is a retrieval model that leverages a mixture of domain-specific experts by using a routing mechanism to select the most appropriate expert for each query. It is lightweight and allows easy addition or removal of experts without additional training.

## Baselines and Evaluation Metrics

Evaluation on the BEIR benchmark demonstrates that RouterRetriever outperforms both models trained on MSMARCO (+2.1 absolute nDCG@10) and multi-task models (+3.2). This is achieved by employing a routing mechanism, which surpasses other routing techniques (+1.8 on average) commonly used in language modeling.

The paper evaluated against:
- Models trained on MSMARCO (general-purpose baseline)
- Multi-task models (that combine both MSMARCO and domain-specific data)
- Other routing techniques used in language modeling

The primary evaluation metric used is **nDCG@10** (normalized Discounted Cumulative Gain at rank 10).

You can find more detailed information in the official AAAI publication or the GitHub repository at https://github.com/amy-hyunji/RouterRetriever.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d80ddaea-1cfc-4a2a-bdeb-0ec67e3d3a1c",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "05526827-15c2-4f73-b6dc-193e6e28b385",
  "toolUseResult": {
    "query": "RouterRetriever AAAI 2025 per-query routing retrieval baselines evaluation metrics",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NVzerdZ3QwZaVQvTUbYbqv",
        "content": [
          {
            "title": "GitHub - amy-hyunji/RouterRetriever",
            "url": "https://github.com/amy-hyunji/RouterRetriever"
          },
          {
            "title": "RouterRetriever: Routing over a Mixture of Expert Embedding Models",
            "url": "https://arxiv.org/html/2409.02685v2"
          },
          {
            "title": "RouterRetriever: Routing over a Mixture of Expert Embedding Models | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/33306"
          },
          {
            "title": "amy-hyunji-lee/RouterRetriever · Hugging Face",
            "url": "https://huggingface.co/amy-hyunji-lee/RouterRetriever"
          },
          {
            "title": "ROUTERRETRIEVER: Routing over a Mixture of Expert Embedding Models Hyunji Lee1*",
            "url": "https://arxiv.org/pdf/2409.02685"
          },
          {
            "title": "RouterRetriever: Exploring the Benefits of Routing over Multiple Expert Embedding Models",
            "url": "https://arxiv.org/html/2409.02685v1"
          },
          {
            "title": "[2409.02685] RouterRetriever: Routing over a Mixture of Expert Embedding Models",
            "url": "https://arxiv.org/abs/2409.02685"
          },
          {
            "title": "Query Routing for Retrieval-Augmented Language Models",
            "url": "https://arxiv.org/html/2505.23052v1"
          }
        ]
      },
      "Based on the search results, here's what I found about RouterRetriever from AAAI 2025:\n\n## Overview\n\nRouterRetriever is a retrieval model that leverages a mixture of domain-specific experts by using a routing mechanism to select the most appropriate expert for each query. It is lightweight and allows easy addition or removal of experts without additional training.\n\n## Baselines and Evaluation Metrics\n\nEvaluation on the BEIR benchmark demonstrates that RouterRetriever outperforms both models trained on MSMARCO (+2.1 absolute nDCG@10) and multi-task models (+3.2). This is achieved by employing a routing mechanism, which surpasses other routing techniques (+1.8 on average) commonly used in language modeling.\n\nThe paper evaluated against:\n- Models trained on MSMARCO (general-purpose baseline)\n- Multi-task models (that combine both MSMARCO and domain-specific data)\n- Other routing techniques used in language modeling\n\nThe primary evaluation metric used is **nDCG@10** (normalized Discounted Cumulative Gain at rank 10).\n\nYou can find more detailed information in the official AAAI publication or the GitHub repository at https://github.com/amy-hyunji/RouterRetriever."
    ],
    "durationSeconds": 8.844531668,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d80ddaea-1cfc-4a2a-bdeb-0ec67e3d3a1c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-30T07:18:56.450Z_

<details><summary>↩ Tool result · `toolu_01QzXHrDBq1waLMdnEpSYYNp`</summary>

```text
Web search results for query: "GradCache contrastive learning decoder-only retrieval training 8B scale compute requirements 2025 2026"

Links: [{"title":"Contrastive Learning for Retrieval: InfoNCE & DPR Guide - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/contrastive-learning-retrieval-infonce-dpr"},{"title":"Scaling Contrastive Learning with Limited Memory","url":"https://www.emergentmind.com/papers/2101.06983"},{"title":"GitHub - luyug/GradCache: Run Effective Large Batch Contrastive Learning Beyond GPU/TPU Memory Constraint","url":"https://github.com/luyug/GradCache"},{"title":"Scaling Deep Contrastive Learning Batch Size under Memory Limited Setup | Request PDF","url":"https://www.researchgate.net/publication/353492632_Scaling_Deep_Contrastive_Learning_Batch_Size_under_Memory_Limited_Setup"},{"title":"Scaling Sparse and Dense Retrieval in Decoder-Only LLMs","url":"https://arxiv.org/pdf/2502.15526"},{"title":"Scaling Deep Contrastive Learning Batch Size under Memory Limited Setup","url":"https://arxiv.org/pdf/2101.06983"},{"title":"Reusing Pre-Training Data at Test Time is a Compute Multiplier","url":"https://arxiv.org/pdf/2511.04234"}]

Based on the web search results, here's what I found:

## GradCache Overview

Gradient caching (sometimes called GradCache) addresses memory limitations by decoupling the batch size used for contrastive comparison from the batch size used for the encoder forward pass. This technique enables scaling deep contrastive learning on memory-limited setups without additional hardware investment.

## Decoder-Only LLM Retrieval Training at 8B Scale

There is recent research directly relevant to your query. A systematic study evaluated decoder-only LLMs (Llama-3 series: 1B, 3B, 8B) with contrastive loss and knowledge distillation approaches, using MSMARCO passages as the training dataset and a fixed compute budget.

Key findings revealed that scaling behaviors emerge clearly only with contrastive loss, where larger models achieve significant performance gains, whereas knowledge distillation-trained models show minimal improvement across the 1B, 3B, and 8B scales. State-of-the-art results were achieved by scaling sparse retrieval models with the combination of contrastive loss and knowledge distillation losses at 8B scale.

## Practical Application

The search results also show practical usage: In a 2025 study, GradCache was applied to train an 8B model with a batch size of 480 and a learning rate of 5e-4 for 80 steps.

However, the search results don't contain specific detailed compute requirement metrics (GPU hours, memory requirements, etc.) for 8B scale decoder-only retrieval training with GradCache in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7785c7ca-e8b2-45d6-a61b-0069adcf724a",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "b934129d-e908-4a4e-a204-bf3c793036e9",
  "toolUseResult": {
    "query": "GradCache contrastive learning decoder-only retrieval training 8B scale compute requirements 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EQsnYhrnd556MHdPkbwBs9",
        "content": [
          {
            "title": "Contrastive Learning for Retrieval: InfoNCE & DPR Guide - Interactive | Michael Brenndoerfer | Michael Brenndoerfer",
            "url": "https://mbrenndoerfer.com/writing/contrastive-learning-retrieval-infonce-dpr"
          },
          {
            "title": "Scaling Contrastive Learning with Limited Memory",
            "url": "https://www.emergentmind.com/papers/2101.06983"
          },
          {
            "title": "GitHub - luyug/GradCache: Run Effective Large Batch Contrastive Learning Beyond GPU/TPU Memory Constraint",
            "url": "https://github.com/luyug/GradCache"
          },
          {
            "title": "Scaling Deep Contrastive Learning Batch Size under Memory Limited Setup | Request PDF",
            "url": "https://www.researchgate.net/publication/353492632_Scaling_Deep_Contrastive_Learning_Batch_Size_under_Memory_Limited_Setup"
          },
          {
            "title": "Scaling Sparse and Dense Retrieval in Decoder-Only LLMs",
            "url": "https://arxiv.org/pdf/2502.15526"
          },
          {
            "title": "Scaling Deep Contrastive Learning Batch Size under Memory Limited Setup",
            "url": "https://arxiv.org/pdf/2101.06983"
          },
          {
            "title": "Reusing Pre-Training Data at Test Time is a Compute Multiplier",
            "url": "https://arxiv.org/pdf/2511.04234"
          }
        ]
      },
      "Based on the web search results, here's what I found:\n\n## GradCache Overview\n\nGradient caching (sometimes called GradCache) addresses memory limitations by decoupling the batch size used for contrastive comparison from the batch size used for the encoder forward pass. This technique enables scaling deep contrastive learning on memory-limited setups without additional hardware investment.\n\n## Decoder-Only LLM Retrieval Training at 8B Scale\n\nThere is recent research directly relevant to your query. A systematic study evaluated decoder-only LLMs (Llama-3 series: 1B, 3B, 8B) with contrastive loss and knowledge distillation approaches, using MSMARCO passages as the training dataset and a fixed compute budget.\n\nKey findings revealed that scaling behaviors emerge clearly only with contrastive loss, where larger models achieve significant performance gains, whereas knowledge distillation-trained models show minimal improvement across the 1B, 3B, and 8B scales. State-of-the-art results were achieved by scaling sparse retrieval models with the combination of contrastive loss and knowledge distillation losses at 8B scale.\n\n## Practical Application\n\nThe search results also show practical usage: In a 2025 study, GradCache was applied to train an 8B model with a batch size of 480 and a learning rate of 5e-4 for 80 steps.\n\nHowever, the search results don't contain specific detailed compute requirement metrics (GPU hours, memory requirements, etc.) for 8B scale decoder-only retrieval training with GradCache in 2025-2026."
    ],
    "durationSeconds": 8.273990980999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7785c7ca-e8b2-45d6-a61b-0069adcf724a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Complementary Specialization in Unified Sparse-Dense Decoder Retrieval with Learned Query Routing  ## Core Research Question  In a decoder-only LLM with shared transformer backbone, do sparse (lexic…",
  "leafUuid": "b934129d-e908-4a4e-a204-bf3c793036e9",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Unified sparse-dense decoder retrieval with learned routing",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---

### Tool call

_source line 26 · 2026-05-30T07:18:59.719Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XaYZHdS1GsnMdjbDHH3pp1`</summary>

```json
{
  "query": "CSplade causal language model learned sparse retrieval IJCNLP 2025 baselines BEIR evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b934129d-e908-4a4e-a204-bf3c793036e9",
  "isSidechain": false,
  "requestId": "req_011CbYM3xsmvk1pC2XsrRBqs",
  "type": "assistant",
  "uuid": "583ecba8-230d-4aba-9e2d-e057699fc753",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PeAryYC9WC1f4vW6k7U1ey",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4226,
      "cache_read_input_tokens": 19761,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 19761,
          "cache_creation_input_tokens": 4226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4226
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-30T07:19:00.872Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EcnWzspGm7Up7jLfnVFf3x`</summary>

```json
{
  "query": "Llama-Embed-Nemotron-8B embedding model 2025 training details evaluation MTEB BEIR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "583ecba8-230d-4aba-9e2d-e057699fc753",
  "isSidechain": false,
  "requestId": "req_011CbYM3xsmvk1pC2XsrRBqs",
  "type": "assistant",
  "uuid": "744d4dec-a5ac-4188-b7e7-73a19c997ed0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PeAryYC9WC1f4vW6k7U1ey",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4226,
      "cache_read_input_tokens": 19761,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 19761,
          "cache_creation_input_tokens": 4226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4226
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-30T07:19:02.287Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JFHWmJ2fStiyGCxwmwV7Cj`</summary>

```json
{
  "query": "DAT dynamic alpha tuning hybrid retrieval per-query sparse dense fusion 2025 experimental evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "744d4dec-a5ac-4188-b7e7-73a19c997ed0",
  "isSidechain": false,
  "requestId": "req_011CbYM3xsmvk1pC2XsrRBqs",
  "type": "assistant",
  "uuid": "388abf9b-9b21-475d-ba6c-fd4109f83f4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PeAryYC9WC1f4vW6k7U1ey",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4226,
      "cache_read_input_tokens": 19761,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 19761,
          "cache_creation_input_tokens": 4226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4226
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-30T07:19:02.677Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CPucPHTNzpQU4N7ADi7Cni`</summary>

```json
{
  "query": "BEIR benchmark 2025 2026 standard baselines retrieval evaluation norms reviewer expectations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "388abf9b-9b21-475d-ba6c-fd4109f83f4e",
  "isSidechain": false,
  "requestId": "req_011CbYM3xsmvk1pC2XsrRBqs",
  "type": "assistant",
  "uuid": "6e6c72cb-3789-4626-9f3b-f6fc42631efc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PeAryYC9WC1f4vW6k7U1ey",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4226,
      "cache_read_input_tokens": 19761,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 251,
          "cache_read_input_tokens": 19761,
          "cache_creation_input_tokens": 4226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4226
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-30T07:19:07.511Z_

<details><summary>↩ Tool result · `toolu_01XaYZHdS1GsnMdjbDHH3pp1`</summary>

```text
Web search results for query: "CSplade causal language model learned sparse retrieval IJCNLP 2025 baselines BEIR evaluation"

Links: [{"title":"CSPLADE: Learned Sparse Retrieval with Causal Language Models - ACL Anthology","url":"https://aclanthology.org/2025.ijcnlp-long.7/"},{"title":"Computer Science Apr 2025","url":"https://arxiv.org/list/cs/2025-04?skip=5050&show=2000"},{"title":"[2504.10816] CSPLADE: Learned Sparse Retrieval with Causal Language Models","url":"https://arxiv.org/abs/2504.10816"},{"title":"dblp: IJCNLP-AACL 2025 - Long Papers","url":"https://dblp.org/db/conf/ijcnlp/ijcnlp2025-l.html"},{"title":"CSplade: Learned Sparse Retrieval with Causal Language Models","url":"https://arxiv.org/html/2504.10816v1"},{"title":"CSPLADE: Learned Sparse Retrieval with Causal Language Models","url":"https://arxiv.org/pdf/2504.10816"},{"title":"(PDF) CSPLADE: Learned Sparse Retrieval with Causal Language Models","url":"https://www.researchgate.net/publication/390932501_CSPLADE_Learned_Sparse_Retrieval_with_Causal_Language_Models"},{"title":"CSPLADE: Learned Sparse Retrieval with Causal Language Models","url":"https://assets.amazon.science/8f/92/a835b4b346e4a4ed7a797010d501/aacl2025-csplade.pdf"}]

I found the paper you're looking for! Here's what the search revealed:

CSPLADE: Learned Sparse Retrieval with Causal Language Models was authored by Zhichao Xu, Aosong Feng, Yijun Tian, Haibo Ding, and Lin Lee Cheong and published at the Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics in December 2025.

**Key Technical Contributions:**

The paper addresses the challenge of training learned sparse retrieval (LSR) models with decoder-only large language models at scales beyond BERT (110M and 330M parameters), identifying two key challenges: training instability from the dying ReLU problem and suboptimal retrieval performance from unidirectional attention in decoder-only LLMs.

To address these challenges, the authors propose a lightweight adaptation training phase to eliminate training instability and two model variants to enable bidirectional information, allowing them to train LSR models with 8B scale LLMs while achieving competitive retrieval performance with reduced index size.

**Evaluation:**

The paper is among the first to analyze the performance-efficiency tradeoff of LLM-based LSR models through the lens of model quantization and provides insights into adapting LLMs for efficient retrieval modeling.

The paper is available on the ACL Anthology and arXiv (arXiv:2504.10816).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "583ecba8-230d-4aba-9e2d-e057699fc753",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "d2757aa7-fa94-4d45-a695-5acf6fa7d337",
  "toolUseResult": {
    "query": "CSplade causal language model learned sparse retrieval IJCNLP 2025 baselines BEIR evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PxFpyBbN8js5ERYZ6mYSCi",
        "content": [
          {
            "title": "CSPLADE: Learned Sparse Retrieval with Causal Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2025.ijcnlp-long.7/"
          },
          {
            "title": "Computer Science Apr 2025",
            "url": "https://arxiv.org/list/cs/2025-04?skip=5050&show=2000"
          },
          {
            "title": "[2504.10816] CSPLADE: Learned Sparse Retrieval with Causal Language Models",
            "url": "https://arxiv.org/abs/2504.10816"
          },
          {
            "title": "dblp: IJCNLP-AACL 2025 - Long Papers",
            "url": "https://dblp.org/db/conf/ijcnlp/ijcnlp2025-l.html"
          },
          {
            "title": "CSplade: Learned Sparse Retrieval with Causal Language Models",
            "url": "https://arxiv.org/html/2504.10816v1"
          },
          {
            "title": "CSPLADE: Learned Sparse Retrieval with Causal Language Models",
            "url": "https://arxiv.org/pdf/2504.10816"
          },
          {
            "title": "(PDF) CSPLADE: Learned Sparse Retrieval with Causal Language Models",
            "url": "https://www.researchgate.net/publication/390932501_CSPLADE_Learned_Sparse_Retrieval_with_Causal_Language_Models"
          },
          {
            "title": "CSPLADE: Learned Sparse Retrieval with Causal Language Models",
            "url": "https://assets.amazon.science/8f/92/a835b4b346e4a4ed7a797010d501/aacl2025-csplade.pdf"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search revealed:\n\nCSPLADE: Learned Sparse Retrieval with Causal Language Models was authored by Zhichao Xu, Aosong Feng, Yijun Tian, Haibo Ding, and Lin Lee Cheong and published at the Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics in December 2025.\n\n**Key Technical Contributions:**\n\nThe paper addresses the challenge of training learned sparse retrieval (LSR) models with decoder-only large language models at scales beyond BERT (110M and 330M parameters), identifying two key challenges: training instability from the dying ReLU problem and suboptimal retrieval performance from unidirectional attention in decoder-only LLMs.\n\nTo address these challenges, the authors propose a lightweight adaptation training phase to eliminate training instability and two model variants to enable bidirectional information, allowing them to train LSR models with 8B scale LLMs while achieving competitive retrieval performance with reduced index size.\n\n**Evaluation:**\n\nThe paper is among the first to analyze the performance-efficiency tradeoff of LLM-based LSR models through the lens of model quantization and provides insights into adapting LLMs for efficient retrieval modeling.\n\nThe paper is available on the ACL Anthology and arXiv (arXiv:2504.10816)."
    ],
    "durationSeconds": 7.786378372000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "583ecba8-230d-4aba-9e2d-e057699fc753",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-30T07:19:09.147Z_

<details><summary>↩ Tool result · `toolu_01JFHWmJ2fStiyGCxwmwV7Cj`</summary>

```text
Web search results for query: "DAT dynamic alpha tuning hybrid retrieval per-query sparse dense fusion 2025 experimental evaluation"

Links: [{"title":"DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation","url":"https://www.emergentmind.com/papers/2503.23013"},{"title":"[2503.23013] DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2503.23013"},{"title":"Entropy-Based Dynamic Hybrid Retrieval for Adaptive Query Weighting in","url":"https://openreview.net/pdf?id=bwGaZOVo0c"},{"title":"DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2503.23013v1"},{"title":"[PDF] DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DAT:-Dynamic-Alpha-Tuning-for-Hybrid-Retrieval-in-Hsu-Tzeng/4e57d2fa070c8c9e2f36341c5f86e35b6ca33f2c"},{"title":"Preprint. Under review. DAT: Dynamic Alpha Tuning for Hybrid Retrieval in","url":"https://arxiv.org/pdf/2503.23013"},{"title":"DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/dat-dynamic-alpha-tuning-hybrid-retrieval-retrieval"},{"title":"(PDF) DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation","url":"https://www.researchgate.net/publication/390354940_DAT_Dynamic_Alpha_Tuning_for_Hybrid_Retrieval_in_Retrieval-Augmented_Generation"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Hsin-Ling+Hsu+and+Jengnan+Tzeng.+2025.+DAT:+Dynamic+alpha+tuning+for+hybrid+retrieval+in+retrieval-augmented+generation.+arXiv+preprint+arXiv:2503.23013+(2025)."}]

Based on the search results, here's what I found about DAT (Dynamic Alpha Tuning):

## Overview

DAT (Dynamic Alpha Tuning) is a novel hybrid retrieval framework that dynamically balances dense retrieval and BM25 for each query. Hybrid retrieval techniques in Retrieval-Augmented Generation (RAG) systems enhance information retrieval by combining dense and sparse (e.g., BM25-based) retrieval methods.

## Problem It Addresses

Existing approaches struggle with adaptability, as fixed weighting schemes fail to adjust to different queries.

## How DAT Works

DAT leverages a large language model (LLM) to evaluate the effectiveness of the top-1 results from both retrieval methods, assigning an effectiveness score to each. It then calibrates the optimal weighting factor through effectiveness score normalization, ensuring a more adaptive and query-aware weighting between the two approaches.

## Performance Results

Empirical results show that DAT consistently significantly outperforms fixed-weighting hybrid retrieval methods across various evaluation metrics.

## Paper Details

The paper was published on arXiv on March 29, 2025 (arXiv:2503.23013) by authors Hsin-Ling Hsu and Jengnan Tzeng. You can find the full paper on arXiv or through other academic sources linked in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "388abf9b-9b21-475d-ba6c-fd4109f83f4e",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "32781884-2dd7-404c-8432-0753d38f46da",
  "toolUseResult": {
    "query": "DAT dynamic alpha tuning hybrid retrieval per-query sparse dense fusion 2025 experimental evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P5K1UTprux5sH4Xqz7BEgM",
        "content": [
          {
            "title": "DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation",
            "url": "https://www.emergentmind.com/papers/2503.23013"
          },
          {
            "title": "[2503.23013] DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2503.23013"
          },
          {
            "title": "Entropy-Based Dynamic Hybrid Retrieval for Adaptive Query Weighting in",
            "url": "https://openreview.net/pdf?id=bwGaZOVo0c"
          },
          {
            "title": "DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2503.23013v1"
          },
          {
            "title": "[PDF] DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/DAT:-Dynamic-Alpha-Tuning-for-Hybrid-Retrieval-in-Hsu-Tzeng/4e57d2fa070c8c9e2f36341c5f86e35b6ca33f2c"
          },
          {
            "title": "Preprint. Under review. DAT: Dynamic Alpha Tuning for Hybrid Retrieval in",
            "url": "https://arxiv.org/pdf/2503.23013"
          },
          {
            "title": "DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/dat-dynamic-alpha-tuning-hybrid-retrieval-retrieval"
          },
          {
            "title": "(PDF) DAT: Dynamic Alpha Tuning for Hybrid Retrieval in Retrieval-Augmented Generation",
            "url": "https://www.researchgate.net/publication/390354940_DAT_Dynamic_Alpha_Tuning_for_Hybrid_Retrieval_in_Retrieval-Augmented_Generation"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar?q=Hsin-Ling+Hsu+and+Jengnan+Tzeng.+2025.+DAT:+Dynamic+alpha+tuning+for+hybrid+retrieval+in+retrieval-augmented+generation.+arXiv+preprint+arXiv:2503.23013+(2025)."
          }
        ]
      },
      "Based on the search results, here's what I found about DAT (Dynamic Alpha Tuning):\n\n## Overview\n\nDAT (Dynamic Alpha Tuning) is a novel hybrid retrieval framework that dynamically balances dense retrieval and BM25 for each query. Hybrid retrieval techniques in Retrieval-Augmented Generation (RAG) systems enhance information retrieval by combining dense and sparse (e.g., BM25-based) retrieval methods.\n\n## Problem It Addresses\n\nExisting approaches struggle with adaptability, as fixed weighting schemes fail to adjust to different queries.\n\n## How DAT Works\n\nDAT leverages a large language model (LLM) to evaluate the effectiveness of the top-1 results from both retrieval methods, assigning an effectiveness score to each. It then calibrates the optimal weighting factor through effectiveness score normalization, ensuring a more adaptive and query-aware weighting between the two approaches.\n\n## Performance Results\n\nEmpirical results show that DAT consistently significantly outperforms fixed-weighting hybrid retrieval methods across various evaluation metrics.\n\n## Paper Details\n\nThe paper was published on arXiv on March 29, 2025 (arXiv:2503.23013) by authors Hsin-Ling Hsu and Jengnan Tzeng. You can find the full paper on arXiv or through other academic sources linked in the search results."
    ],
    "durationSeconds": 6.857357713000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "388abf9b-9b21-475d-ba6c-fd4109f83f4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-30T07:19:09.977Z_

<details><summary>↩ Tool result · `toolu_01CPucPHTNzpQU4N7ADi7Cni`</summary>

```text
Web search results for query: "BEIR benchmark 2025 2026 standard baselines retrieval evaluation norms reviewer expectations"

Links: [{"title":"BEIR Benchmark Leaderboard 2025 & 2026: NDCG@10 Scores & Rankings | Ailog RAG","url":"https://app.ailog.fr/en/blog/news/beir-benchmark-update"},{"title":"Benchmarking IR Information Retrieval (BEIR)","url":"https://zilliz.com/glossary/beir"},{"title":"BEIR — BGE documentation","url":"https://bge-model.com/API/evaluation/beir.html"},{"title":"BEIR Benchmark for IR Models","url":"https://www.emergentmind.com/topics/beir-benchmark"},{"title":"What is the BEIR benchmark and how is it used?","url":"https://milvus.io/ai-quick-reference/what-is-the-beir-benchmark-and-how-is-it-used"},{"title":"BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models | OpenReview","url":"https://openreview.net/forum?id=wCu6T5xFjeJ"},{"title":"BEIR: A Heterogeneous Benchmark for Zero-shot ...","url":"https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/65b9eea6e1cc6bb9f0cd2a47751a186f-Paper-round2.pdf"},{"title":"Andreas Rücklé | BEIR: Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models","url":"https://rueckle.net/publication/BEIR/"},{"title":"BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information   Retrieval Models","url":"https://arxiv.org/pdf/2104.08663"},{"title":"GitHub - beir-cellar/beir: A Heterogeneous Benchmark for Information Retrieval. Easy to use, evaluate your models across 15+ diverse IR datasets. · GitHub","url":"https://github.com/beir-cellar/beir"}]

Based on the search results, here's what I found about BEIR benchmark standards and expectations for 2025-2026:

## Overview

BEIR (Benchmarking Information Retrieval) is a heterogeneous benchmark for zero-shot evaluation of retrieval models, created in 2021, testing models across 18 diverse datasets including MS MARCO, Natural Questions, TREC-COVID, and domain-specific corpora.

## Standard Baselines

BM25 is a robust baseline, and BM25 remains a highly competitive zero-shot method across the 18 BEIR datasets, outperforming most neural/sparse models in out-of-distribution scenarios absent domain-specific adaptation. Evaluations use metrics like nDCG@k and Recall@k, with BM25 often serving as a robust baseline to assess out-of-distribution retrieval performance.

## Current Performance Norms (2025-2026)

Dense retrieval now consistently outperforms BM25 by 15-25% on BEIR datasets. However, lexical search still outperforms dense models in 2 out of 14 datasets.

## Evaluation Focus

The primary goal of BEIR is to measure how well a retrieval model generalizes to tasks it wasn't explicitly trained on, which is critical for assessing real-world applicability, and developers and researchers use BEIR to compare models fairly by testing them on the same set of tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e6c72cb-3789-4626-9f3b-f6fc42631efc",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "07c06fad-a529-407b-9175-d56d40dfeeac",
  "toolUseResult": {
    "query": "BEIR benchmark 2025 2026 standard baselines retrieval evaluation norms reviewer expectations",
    "results": [
      {
        "tool_use_id": "srvtoolu_017Ssu3hdS2ekFjxF7xYwQgj",
        "content": [
          {
            "title": "BEIR Benchmark Leaderboard 2025 & 2026: NDCG@10 Scores & Rankings | Ailog RAG",
            "url": "https://app.ailog.fr/en/blog/news/beir-benchmark-update"
          },
          {
            "title": "Benchmarking IR Information Retrieval (BEIR)",
            "url": "https://zilliz.com/glossary/beir"
          },
          {
            "title": "BEIR — BGE documentation",
            "url": "https://bge-model.com/API/evaluation/beir.html"
          },
          {
            "title": "BEIR Benchmark for IR Models",
            "url": "https://www.emergentmind.com/topics/beir-benchmark"
          },
          {
            "title": "What is the BEIR benchmark and how is it used?",
            "url": "https://milvus.io/ai-quick-reference/what-is-the-beir-benchmark-and-how-is-it-used"
          },
          {
            "title": "BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models | OpenReview",
            "url": "https://openreview.net/forum?id=wCu6T5xFjeJ"
          },
          {
            "title": "BEIR: A Heterogeneous Benchmark for Zero-shot ...",
            "url": "https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/65b9eea6e1cc6bb9f0cd2a47751a186f-Paper-round2.pdf"
          },
          {
            "title": "Andreas Rücklé | BEIR: Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models",
            "url": "https://rueckle.net/publication/BEIR/"
          },
          {
            "title": "BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information   Retrieval Models",
            "url": "https://arxiv.org/pdf/2104.08663"
          },
          {
            "title": "GitHub - beir-cellar/beir: A Heterogeneous Benchmark for Information Retrieval. Easy to use, evaluate your models across 15+ diverse IR datasets. · GitHub",
            "url": "https://github.com/beir-cellar/beir"
          }
        ]
      },
      "Based on the search results, here's what I found about BEIR benchmark standards and expectations for 2025-2026:\n\n## Overview\n\nBEIR (Benchmarking Information Retrieval) is a heterogeneous benchmark for zero-shot evaluation of retrieval models, created in 2021, testing models across 18 diverse datasets including MS MARCO, Natural Questions, TREC-COVID, and domain-specific corpora.\n\n## Standard Baselines\n\nBM25 is a robust baseline, and BM25 remains a highly competitive zero-shot method across the 18 BEIR datasets, outperforming most neural/sparse models in out-of-distribution scenarios absent domain-specific adaptation. Evaluations use metrics like nDCG@k and Recall@k, with BM25 often serving as a robust baseline to assess out-of-distribution retrieval performance.\n\n## Current Performance Norms (2025-2026)\n\nDense retrieval now consistently outperforms BM25 by 15-25% on BEIR datasets. However, lexical search still outperforms dense models in 2 out of 14 datasets.\n\n## Evaluation Focus\n\nThe primary goal of BEIR is to measure how well a retrieval model generalizes to tasks it wasn't explicitly trained on, which is critical for assessing real-world applicability, and developers and researchers use BEIR to compare models fairly by testing them on the same set of tasks."
    ],
    "durationSeconds": 7.298151333999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6e6c72cb-3789-4626-9f3b-f6fc42631efc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-30T07:19:10.322Z_

<details><summary>↩ Tool result · `toolu_01EcnWzspGm7Up7jLfnVFf3x`</summary>

```text
Web search results for query: "Llama-Embed-Nemotron-8B embedding model 2025 training details evaluation MTEB BEIR"

Links: [{"title":"Llama-Embed-Nemotron-8B: A Universal Text Embedding Model for Multilingual and Cross-Lingual Tasks","url":"https://arxiv.org/html/2511.07025v1"},{"title":"README.md · nvidia/llama-embed-nemotron-8b at 98a9b8e24dcabb6e7203becf8296c6e265b2571b","url":"https://huggingface.co/nvidia/llama-embed-nemotron-8b/blob/98a9b8e24dcabb6e7203becf8296c6e265b2571b/README.md"},{"title":"nvidia/llama-embed-nemotron-8b · Hugging Face","url":"https://huggingface.co/nvidia/llama-embed-nemotron-8b"},{"title":"README.md · nvidia/llama-embed-nemotron-8b at 8fed692af1559a82abf9f8325bf675223efc05d1","url":"https://huggingface.co/nvidia/llama-embed-nemotron-8b/blob/8fed692af1559a82abf9f8325bf675223efc05d1/README.md"},{"title":"Llama-Embed-Nemotron-8B: Multilingual Embedding Model","url":"https://www.emergentmind.com/topics/llama-embed-nemotron-8b"},{"title":"(PDF) Llama-Embed-Nemotron-8B: A Universal Text Embedding Model for Multilingual and Cross-Lingual Tasks","url":"https://www.researchgate.net/publication/397480951_Llama-Embed-Nemotron-8B_A_Universal_Text_Embedding_Model_for_Multilingual_and_Cross-Lingual_Tasks"},{"title":"[2511.07025] Llama-Embed-Nemotron-8B: A Universal Text Embedding Model for Multilingual and Cross-Lingual Tasks","url":"https://arxiv.org/abs/2511.07025"},{"title":"[Quick Review] Llama-Embed-Nemotron-8B: A Universal Text Embedding Model for\\n Multilingual and Cross-Lingual Tasks","url":"https://liner.com/review/llamaembednemotron8b-universal-text-embedding-model-for-multilingual-and-crosslingual-tasks"},{"title":"Llama‑Embed‑Nemotron‑8B Text Embedding Model Ranks First on Multilingual MTEB Leaderboard","url":"https://huggingface.co/blog/nvidia/llama-embed-nemotron-8b"},{"title":"Paper page - Llama-Embed-Nemotron-8B: A Universal Text Embedding Model for Multilingual and Cross-Lingual Tasks","url":"https://huggingface.co/papers/2511.07025"}]

Based on the search results, here are the key details about the Llama-Embed-Nemotron-8B embedding model:

## Overview

Llama-Embed-Nemotron-8B is a versatile text embedding model trained by NVIDIA and optimized for retrieval, reranking, semantic similarity, and classification use cases. It was built by fine-tuning the Llama-3.1-8B foundation model and applies cross-lingual representation learning to deliver unified, high-fidelity embeddings across linguistically diverse content.

## Training Details

The model was trained on a novel data mix of 16.1 million query-document pairs, split between 7.7 million samples from public datasets and 8.4 million synthetically generated examples from various open-weight LLMs. The model employs a two-stage training approach, starting with retrieval pretraining and followed by fine-tuning on diverse tasks like retrieval, classification, STS, and bitext mining.

The final llama-embed-nemotron-8b model is an average of six diverse individual models, weighted equally, with this diversity stemming from varying data mixes and hyperparameter sets used during training.

## Architecture

The base model consists of 7.5B parameters with 32 hidden layers (hidden size dimension = 4,096), and a key innovation that replaces uni-directional causal attention with bi-directional self-attention, enabling richer semantic understanding across the full token context.

## MTEB and Evaluation Performance

The model achieves state-of-the-art performance on the multilingual MTEB leaderboard as of October 21, 2025. The model was tested on 131 tasks from MMTEB: Massive Multilingual Text Embedding Benchmark (MTEB(Multilingual, v2) split). The model achieved state-of-the-art performance, securing the top rank on the Multilingual Massive Text Embedding Benchmark (MMTEB) leaderboard with 39,573 Borda votes, representing a significant lead of over 200 votes compared to its closest competitors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "744d4dec-a5ac-4188-b7e7-73a19c997ed0",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "e69cb0cc-107a-4a3f-be1d-61b4eea101c7",
  "toolUseResult": {
    "query": "Llama-Embed-Nemotron-8B embedding model 2025 training details evaluation MTEB BEIR",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A46G6pjStVUwo7jDgWEyLg",
        "content": [
          {
            "title": "Llama-Embed-Nemotron-8B: A Universal Text Embedding Model for Multilingual and Cross-Lingual Tasks",
            "url": "https://arxiv.org/html/2511.07025v1"
          },
          {
            "title": "README.md · nvidia/llama-embed-nemotron-8b at 98a9b8e24dcabb6e7203becf8296c6e265b2571b",
            "url": "https://huggingface.co/nvidia/llama-embed-nemotron-8b/blob/98a9b8e24dcabb6e7203becf8296c6e265b2571b/README.md"
          },
          {
            "title": "nvidia/llama-embed-nemotron-8b · Hugging Face",
            "url": "https://huggingface.co/nvidia/llama-embed-nemotron-8b"
          },
          {
            "title": "README.md · nvidia/llama-embed-nemotron-8b at 8fed692af1559a82abf9f8325bf675223efc05d1",
            "url": "https://huggingface.co/nvidia/llama-embed-nemotron-8b/blob/8fed692af1559a82abf9f8325bf675223efc05d1/README.md"
          },
          {
            "title": "Llama-Embed-Nemotron-8B: Multilingual Embedding Model",
            "url": "https://www.emergentmind.com/topics/llama-embed-nemotron-8b"
          },
          {
            "title": "(PDF) Llama-Embed-Nemotron-8B: A Universal Text Embedding Model for Multilingual and Cross-Lingual Tasks",
            "url": "https://www.researchgate.net/publication/397480951_Llama-Embed-Nemotron-8B_A_Universal_Text_Embedding_Model_for_Multilingual_and_Cross-Lingual_Tasks"
          },
          {
            "title": "[2511.07025] Llama-Embed-Nemotron-8B: A Universal Text Embedding Model for Multilingual and Cross-Lingual Tasks",
            "url": "https://arxiv.org/abs/2511.07025"
          },
          {
            "title": "[Quick Review] Llama-Embed-Nemotron-8B: A Universal Text Embedding Model for\\n Multilingual and Cross-Lingual Tasks",
            "url": "https://liner.com/review/llamaembednemotron8b-universal-text-embedding-model-for-multilingual-and-crosslingual-tasks"
          },
          {
            "title": "Llama‑Embed‑Nemotron‑8B Text Embedding Model Ranks First on Multilingual MTEB Leaderboard",
            "url": "https://huggingface.co/blog/nvidia/llama-embed-nemotron-8b"
          },
          {
            "title": "Paper page - Llama-Embed-Nemotron-8B: A Universal Text Embedding Model for Multilingual and Cross-Lingual Tasks",
            "url": "https://huggingface.co/papers/2511.07025"
          }
        ]
      },
      "Based on the search results, here are the key details about the Llama-Embed-Nemotron-8B embedding model:\n\n## Overview\n\nLlama-Embed-Nemotron-8B is a versatile text embedding model trained by NVIDIA and optimized for retrieval, reranking, semantic similarity, and classification use cases. It was built by fine-tuning the Llama-3.1-8B foundation model and applies cross-lingual representation learning to deliver unified, high-fidelity embeddings across linguistically diverse content.\n\n## Training Details\n\nThe model was trained on a novel data mix of 16.1 million query-document pairs, split between 7.7 million samples from public datasets and 8.4 million synthetically generated examples from various open-weight LLMs. The model employs a two-stage training approach, starting with retrieval pretraining and followed by fine-tuning on diverse tasks like retrieval, classification, STS, and bitext mining.\n\nThe final llama-embed-nemotron-8b model is an average of six diverse individual models, weighted equally, with this diversity stemming from varying data mixes and hyperparameter sets used during training.\n\n## Architecture\n\nThe base model consists of 7.5B parameters with 32 hidden layers (hidden size dimension = 4,096), and a key innovation that replaces uni-directional causal attention with bi-directional self-attention, enabling richer semantic understanding across the full token context.\n\n## MTEB and Evaluation Performance\n\nThe model achieves state-of-the-art performance on the multilingual MTEB leaderboard as of October 21, 2025. The model was tested on 131 tasks from MMTEB: Massive Multilingual Text Embedding Benchmark (MTEB(Multilingual, v2) split). The model achieved state-of-the-art performance, securing the top rank on the Multilingual Massive Text Embedding Benchmark (MMTEB) leaderboard with 39,573 Borda votes, representing a significant lead of over 200 votes compared to its closest competitors."
    ],
    "durationSeconds": 9.422725724000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "744d4dec-a5ac-4188-b7e7-73a19c997ed0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-30T07:19:10.327Z_

```json
{
  "parentUuid": "e69cb0cc-107a-4a3f-be1d-61b4eea101c7",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "40be2b2a-d7f3-404e-b232-e06996c8b4b7",
  "timestamp": "2026-05-30T07:19:10.327Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Complementary Specialization in Unified Sparse-Dense Decoder Retrieval with Learned Query Routing  ## Core Research Question  In a decoder-only LLM with shared transformer backbone, do sparse (lexic…",
  "leafUuid": "40be2b2a-d7f3-404e-b232-e06996c8b4b7",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Unified sparse-dense decoder retrieval with learned routing",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---

### Tool call

_source line 37 · 2026-05-30T07:19:13.085Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01883btLQHHCtQLWfQvnXdKb`</summary>

```json
{
  "query": "bidirectional self-knowledge distillation sparse dense retrieval CIKM 2025 ablation experimental design"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40be2b2a-d7f3-404e-b232-e06996c8b4b7",
  "isSidechain": false,
  "requestId": "req_011CbYM4zAhL2Q8FCxeM4Q93",
  "type": "assistant",
  "uuid": "c1f491c6-38f0-4f5d-9c25-fadd48643eb6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6RgWsPmF4JjX1Wu1RPXaL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1889,
      "cache_creation_input_tokens": 2475,
      "cache_read_input_tokens": 23987,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1889,
          "output_tokens": 184,
          "cache_read_input_tokens": 23987,
          "cache_creation_input_tokens": 2475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2475
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-30T07:19:14.169Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0196D6pLc2ZGvCiaJVE39yGR`</summary>

```json
{
  "query": "Qwen3-Embedding 2025 evaluation MTEB retrieval baselines training methodology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1f491c6-38f0-4f5d-9c25-fadd48643eb6",
  "isSidechain": false,
  "requestId": "req_011CbYM4zAhL2Q8FCxeM4Q93",
  "type": "assistant",
  "uuid": "fbd00fad-f0fa-4fc3-a7e6-716192b764e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6RgWsPmF4JjX1Wu1RPXaL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1889,
      "cache_creation_input_tokens": 2475,
      "cache_read_input_tokens": 23987,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1889,
          "output_tokens": 184,
          "cache_read_input_tokens": 23987,
          "cache_creation_input_tokens": 2475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2475
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-30T07:19:15.237Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016BgSLnzBzjQ81GVbYrfqSY`</summary>

```json
{
  "query": "linear CKA representation analysis retrieval models complementary specialization 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbd00fad-f0fa-4fc3-a7e6-716192b764e9",
  "isSidechain": false,
  "requestId": "req_011CbYM4zAhL2Q8FCxeM4Q93",
  "type": "assistant",
  "uuid": "73027426-e76e-4cef-bd33-453649f1071d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C6RgWsPmF4JjX1Wu1RPXaL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1889,
      "cache_creation_input_tokens": 2475,
      "cache_read_input_tokens": 23987,
      "output_tokens": 184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2475,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1889,
          "output_tokens": 184,
          "cache_read_input_tokens": 23987,
          "cache_creation_input_tokens": 2475,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2475
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-30T07:19:22.004Z_

<details><summary>↩ Tool result · `toolu_01883btLQHHCtQLWfQvnXdKb`</summary>

```text
Web search results for query: "bidirectional self-knowledge distillation sparse dense retrieval CIKM 2025 ablation experimental design"

Links: [{"title":"Sparse and Dense Retrievers Learn","url":"https://dl.acm.org/doi/pdf/10.1145/3746252.3760959"},{"title":"Sparse and Dense Retrievers Learn Better Together: Joint Sparse-Dense Optimization for Text-Image Retrieval","url":"https://arxiv.org/html/2508.16707"},{"title":"GitHub - holi-lab/mm-sparse-retrieval: Repo for the paper \"Sparse and Dense Retrievers Learn Better Together: Joint Sparse-Dense Optimization for Text-Image Retrieval\" (CIKM 2025 Short Track)","url":"https://github.com/holi-lab/mm-sparse-retrieval"},{"title":"Sparse and Dense Retrievers Learn Better Together: Joint Sparse-Dense Optimization for Text-Image Retrieval","url":"https://arxiv.org/pdf/2508.16707"},{"title":"DiSCo: LLM Knowledge Distillation for Efficient Sparse Retrieval in Conversational Search | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3726302.3729966"},{"title":"Salient Phrase Aware Dense Retrieval: Can a Dense Retriever Imitate a   Sparse One?","url":"https://arxiv.org/pdf/2110.06918"},{"title":"PROD: Progressive Distillation for Dense Retrieval","url":"https://arxiv.org/pdf/2209.13335"},{"title":"Scaling Sparse and Dense Retrieval in Decoder-Only LLMs Hansi Zeng","url":"https://maroo.cs.umass.edu/pub/web/getpdf.php?id=1538"}]

I found relevant information about the research paper you're asking about. Here's what I found:

## Paper Overview

The paper "Sparse and Dense Retrievers Learn Better Together: Joint Sparse-Dense Optimization for Text-Image Retrieval" was accepted to CIKM 2025 Short Track. The paper is authored by Jonghyun Song, Youngjune Lee, Gyu-Hwung Cho, Ilhyeon Song, Saehun Kim, and Yohan Jo, and was presented at the 34th ACM International Conference on Information and Knowledge Management (CIKM '25) in November 2025, Seoul, Republic of Korea.

## Methodology: Bidirectional Self-Knowledge Distillation

The framework enables bi-directional learning between dense and sparse representations through Self-Knowledge Distillation, addressing limitations where methods often relied on computationally expensive contrastive pre-training or distillation from a frozen dense model.

The model is trained using a combination of contrastive loss and a self-knowledge distillation loss that jointly optimizes the dense and sparse scores. The distillation loss leverages an integrated score as a teacher signal to supervise both the dense and sparse representations, inspired by recent advances in knowledge distillation.

## Ablation Study

The paper includes an ablation study on the final layer fine-tuning and self-knowledge distillation, with the best configuration marked.

## Key Finding

The bi-directional supervision from the self-knowledge distillation leads to better sparse representations, an advantage not captured by standard unidirectional distillation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1f491c6-38f0-4f5d-9c25-fadd48643eb6",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "660c9e8f-ea7c-4b73-b625-a710a210a867",
  "toolUseResult": {
    "query": "bidirectional self-knowledge distillation sparse dense retrieval CIKM 2025 ablation experimental design",
    "results": [
      {
        "tool_use_id": "srvtoolu_018MzNonzoL4Y7azvJavqf7A",
        "content": [
          {
            "title": "Sparse and Dense Retrievers Learn",
            "url": "https://dl.acm.org/doi/pdf/10.1145/3746252.3760959"
          },
          {
            "title": "Sparse and Dense Retrievers Learn Better Together: Joint Sparse-Dense Optimization for Text-Image Retrieval",
            "url": "https://arxiv.org/html/2508.16707"
          },
          {
            "title": "GitHub - holi-lab/mm-sparse-retrieval: Repo for the paper \"Sparse and Dense Retrievers Learn Better Together: Joint Sparse-Dense Optimization for Text-Image Retrieval\" (CIKM 2025 Short Track)",
            "url": "https://github.com/holi-lab/mm-sparse-retrieval"
          },
          {
            "title": "Sparse and Dense Retrievers Learn Better Together: Joint Sparse-Dense Optimization for Text-Image Retrieval",
            "url": "https://arxiv.org/pdf/2508.16707"
          },
          {
            "title": "DiSCo: LLM Knowledge Distillation for Efficient Sparse Retrieval in Conversational Search | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval",
            "url": "https://dl.acm.org/doi/10.1145/3726302.3729966"
          },
          {
            "title": "Salient Phrase Aware Dense Retrieval: Can a Dense Retriever Imitate a   Sparse One?",
            "url": "https://arxiv.org/pdf/2110.06918"
          },
          {
            "title": "PROD: Progressive Distillation for Dense Retrieval",
            "url": "https://arxiv.org/pdf/2209.13335"
          },
          {
            "title": "Scaling Sparse and Dense Retrieval in Decoder-Only LLMs Hansi Zeng",
            "url": "https://maroo.cs.umass.edu/pub/web/getpdf.php?id=1538"
          }
        ]
      },
      "I found relevant information about the research paper you're asking about. Here's what I found:\n\n## Paper Overview\n\nThe paper \"Sparse and Dense Retrievers Learn Better Together: Joint Sparse-Dense Optimization for Text-Image Retrieval\" was accepted to CIKM 2025 Short Track. The paper is authored by Jonghyun Song, Youngjune Lee, Gyu-Hwung Cho, Ilhyeon Song, Saehun Kim, and Yohan Jo, and was presented at the 34th ACM International Conference on Information and Knowledge Management (CIKM '25) in November 2025, Seoul, Republic of Korea.\n\n## Methodology: Bidirectional Self-Knowledge Distillation\n\nThe framework enables bi-directional learning between dense and sparse representations through Self-Knowledge Distillation, addressing limitations where methods often relied on computationally expensive contrastive pre-training or distillation from a frozen dense model.\n\nThe model is trained using a combination of contrastive loss and a self-knowledge distillation loss that jointly optimizes the dense and sparse scores. The distillation loss leverages an integrated score as a teacher signal to supervise both the dense and sparse representations, inspired by recent advances in knowledge distillation.\n\n## Ablation Study\n\nThe paper includes an ablation study on the final layer fine-tuning and self-knowledge distillation, with the best configuration marked.\n\n## Key Finding\n\nThe bi-directional supervision from the self-knowledge distillation leads to better sparse representations, an advantage not captured by standard unidirectional distillation."
    ],
    "durationSeconds": 8.914485740999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c1f491c6-38f0-4f5d-9c25-fadd48643eb6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-30T07:19:22.610Z_

<details><summary>↩ Tool result · `toolu_016BgSLnzBzjQ81GVbYrfqSY`</summary>

```text
Web search results for query: "linear CKA representation analysis retrieval models complementary specialization 2024 2025"

Links: [{"title":"Centered Kernel Alignment (CKA) Similarity","url":"https://www.emergentmind.com/topics/centered-kernel-alignment-cka-similarity"},{"title":"Centered Kernel Alignment (CKA) Overview","url":"https://www.emergentmind.com/topics/centered-kernel-alignment-cka"},{"title":"Similarity of Neural Network Representations Revisited","url":"http://proceedings.mlr.press/v97/kornblith19a/kornblith19a.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/03d113a060c0ac93a5859517a0f07271-Paper-Conference.pdf"},{"title":"[2210.16156] Reliability of CKA as a Similarity Measure in Deep Learning","url":"https://arxiv.org/abs/2210.16156"},{"title":"An Equivalence Between Representational Similarity Analysis and Centered","url":"https://2025.ccneuro.org/abstract_pdf/Williams_2025_An_Equivalence_Between_Representational_Similarity_Analysis.pdf"},{"title":"Do Vision and Language Encoders Represent the World Similarly?","url":"https://arxiv.org/pdf/2401.05224"},{"title":"Equivalence between representational similarity analysis, centered kernel alignment, and canonical correlations analysis","url":"https://www.biorxiv.org/content/10.1101/2024.10.23.619871.full.pdf"}]

Based on the search results, I found relevant information about linear CKA and representation analysis. Here are the key findings:

## Linear CKA in Representation Analysis

Linear CKA disproportionately emphasizes alignment of high-variance principal directions, which is an important consideration when analyzing neural network representations.

## CKA and Retrieval/Matching Applications

CKA-based quadratic assignment has been used for zero-shot matching and retrieval between vision and language encoders, demonstrating applications in multi-modal systems.

## Recent Advances (2024-2025)

Recent work has focused on several important aspects:

- Unbiased CKA recovers brain region–layer correspondences with applications to fMRI, MEG, and direct recordings
- CKA serves as an explicit criterion in pruning and training regularization, yielding up to 50% reduction without accuracy loss
- Layer-wise representation similarity for transformer models on a per-sample basis enables multi-exit models with early exit during inference

## Complementary Analysis Approaches

High CKA does not guarantee functionally similar or transferable features, and complementary diagnostics including linear probes, filter visualization, and class separability are advised.

The search results indicate that linear CKA remains a central tool for representation analysis, with ongoing refinements to address limitations and expanded applications in both retrieval tasks and model interpretability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73027426-e76e-4cef-bd33-453649f1071d",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "6b483986-b46e-44ba-b390-101a1a4ebed0",
  "toolUseResult": {
    "query": "linear CKA representation analysis retrieval models complementary specialization 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VV5riF3xrsx6YAgVgCYgoh",
        "content": [
          {
            "title": "Centered Kernel Alignment (CKA) Similarity",
            "url": "https://www.emergentmind.com/topics/centered-kernel-alignment-cka-similarity"
          },
          {
            "title": "Centered Kernel Alignment (CKA) Overview",
            "url": "https://www.emergentmind.com/topics/centered-kernel-alignment-cka"
          },
          {
            "title": "Similarity of Neural Network Representations Revisited",
            "url": "http://proceedings.mlr.press/v97/kornblith19a/kornblith19a.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/03d113a060c0ac93a5859517a0f07271-Paper-Conference.pdf"
          },
          {
            "title": "[2210.16156] Reliability of CKA as a Similarity Measure in Deep Learning",
            "url": "https://arxiv.org/abs/2210.16156"
          },
          {
            "title": "An Equivalence Between Representational Similarity Analysis and Centered",
            "url": "https://2025.ccneuro.org/abstract_pdf/Williams_2025_An_Equivalence_Between_Representational_Similarity_Analysis.pdf"
          },
          {
            "title": "Do Vision and Language Encoders Represent the World Similarly?",
            "url": "https://arxiv.org/pdf/2401.05224"
          },
          {
            "title": "Equivalence between representational similarity analysis, centered kernel alignment, and canonical correlations analysis",
            "url": "https://www.biorxiv.org/content/10.1101/2024.10.23.619871.full.pdf"
          }
        ]
      },
      "Based on the search results, I found relevant information about linear CKA and representation analysis. Here are the key findings:\n\n## Linear CKA in Representation Analysis\n\nLinear CKA disproportionately emphasizes alignment of high-variance principal directions, which is an important consideration when analyzing neural network representations.\n\n## CKA and Retrieval/Matching Applications\n\nCKA-based quadratic assignment has been used for zero-shot matching and retrieval between vision and language encoders, demonstrating applications in multi-modal systems.\n\n## Recent Advances (2024-2025)\n\nRecent work has focused on several important aspects:\n\n- Unbiased CKA recovers brain region–layer correspondences with applications to fMRI, MEG, and direct recordings\n- CKA serves as an explicit criterion in pruning and training regularization, yielding up to 50% reduction without accuracy loss\n- Layer-wise representation similarity for transformer models on a per-sample basis enables multi-exit models with early exit during inference\n\n## Complementary Analysis Approaches\n\nHigh CKA does not guarantee functionally similar or transferable features, and complementary diagnostics including linear probes, filter visualization, and class separability are advised.\n\nThe search results indicate that linear CKA remains a central tool for representation analysis, with ongoing refinements to address limitations and expanded applications in both retrieval tasks and model interpretability."
    ],
    "durationSeconds": 7.3690591639999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "73027426-e76e-4cef-bd33-453649f1071d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-30T07:19:23.322Z_

<details><summary>↩ Tool result · `toolu_0196D6pLc2ZGvCiaJVE39yGR`</summary>

```text
Web search results for query: "Qwen3-Embedding 2025 evaluation MTEB retrieval baselines training methodology"

Links: [{"title":"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen","url":"https://qwenlm.github.io/blog/qwen3-embedding/"},{"title":"GitHub - QwenLM/Qwen3-Embedding · GitHub","url":"https://github.com/QwenLM/Qwen3-Embedding"},{"title":"Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models","url":"https://arxiv.org/html/2506.05176v1"},{"title":"Qwen3 Embedding: Advancing Text ...","url":"https://arxiv.org/pdf/2506.05176"},{"title":"[2506.05176] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models","url":"https://arxiv.org/abs/2506.05176"},{"title":"Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking","url":"https://arxiv.org/pdf/2601.04720"},{"title":"Comparative Analysis of Qwen-3 and BGE-M3 Embedding Models for Multilingual Information Retrieval | by Aryan Kumar | Medium","url":"https://medium.com/@mrAryanKumar/comparative-analysis-of-qwen-3-and-bge-m3-embedding-models-for-multilingual-information-retrieval-72c0e6895413"},{"title":"[2601.04720] Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking","url":"https://arxiv.org/abs/2601.04720"},{"title":"QZhou-Embedding Technical Report","url":"https://arxiv.org/pdf/2508.21632"}]

Based on the search results, here's what I found about Qwen3-Embedding 2025 evaluation, MTEB retrieval baselines, and training methodology:

## Training Methodology

The training framework for the Qwen3 Embedding series follows the multi-stage training paradigm established by the GTE-Qwen series, with a three-stage training structure implemented during the training of the embedding model.

## MTEB Evaluation & Retrieval Baselines

The flagship model Qwen3-8B-Embedding attains a score of 70.58 on the MTEB Multilingual benchmark and 80.68 on the MTEB Code benchmark, surpassing the previous state-of-the-art proprietary embedding model, Gemini-Embedding.

Evaluation results are presented on MTEB (English, v2), CMTEB (Chinese), and MTEB (Code), with the Qwen3-Embedding-4B/8B models consistently outperforming others.

## Model Series & Performance

The Qwen3 Embedding series offers a spectrum of model sizes (0.6B, 4B, 8B) for both embedding and reranking tasks. The Qwen3-Embedding-4B/8B models achieve the best performance, while the smallest model, Qwen3-Embedding-0.6B, only lags behind the best-performing baseline method (Gemini-Embedding), despite having only 0.6B parameters.

For reranking evaluation, retrieval subsets of MTEB (English, v2), MTEB (Chinese, v1), MMTEB and MTEB (Code) are used.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fbd00fad-f0fa-4fc3-a7e6-716192b764e9",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "dd7e9d6c-67e1-4f22-bab0-ed8f8b0e124d",
  "toolUseResult": {
    "query": "Qwen3-Embedding 2025 evaluation MTEB retrieval baselines training methodology",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YHvQNKMxCJKJfsfHcbQfJA",
        "content": [
          {
            "title": "Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models | Qwen",
            "url": "https://qwenlm.github.io/blog/qwen3-embedding/"
          },
          {
            "title": "GitHub - QwenLM/Qwen3-Embedding · GitHub",
            "url": "https://github.com/QwenLM/Qwen3-Embedding"
          },
          {
            "title": "Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models",
            "url": "https://arxiv.org/html/2506.05176v1"
          },
          {
            "title": "Qwen3 Embedding: Advancing Text ...",
            "url": "https://arxiv.org/pdf/2506.05176"
          },
          {
            "title": "[2506.05176] Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models",
            "url": "https://arxiv.org/abs/2506.05176"
          },
          {
            "title": "Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking",
            "url": "https://arxiv.org/pdf/2601.04720"
          },
          {
            "title": "Comparative Analysis of Qwen-3 and BGE-M3 Embedding Models for Multilingual Information Retrieval | by Aryan Kumar | Medium",
            "url": "https://medium.com/@mrAryanKumar/comparative-analysis-of-qwen-3-and-bge-m3-embedding-models-for-multilingual-information-retrieval-72c0e6895413"
          },
          {
            "title": "[2601.04720] Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking",
            "url": "https://arxiv.org/abs/2601.04720"
          },
          {
            "title": "QZhou-Embedding Technical Report",
            "url": "https://arxiv.org/pdf/2508.21632"
          }
        ]
      },
      "Based on the search results, here's what I found about Qwen3-Embedding 2025 evaluation, MTEB retrieval baselines, and training methodology:\n\n## Training Methodology\n\nThe training framework for the Qwen3 Embedding series follows the multi-stage training paradigm established by the GTE-Qwen series, with a three-stage training structure implemented during the training of the embedding model.\n\n## MTEB Evaluation & Retrieval Baselines\n\nThe flagship model Qwen3-8B-Embedding attains a score of 70.58 on the MTEB Multilingual benchmark and 80.68 on the MTEB Code benchmark, surpassing the previous state-of-the-art proprietary embedding model, Gemini-Embedding.\n\nEvaluation results are presented on MTEB (English, v2), CMTEB (Chinese), and MTEB (Code), with the Qwen3-Embedding-4B/8B models consistently outperforming others.\n\n## Model Series & Performance\n\nThe Qwen3 Embedding series offers a spectrum of model sizes (0.6B, 4B, 8B) for both embedding and reranking tasks. The Qwen3-Embedding-4B/8B models achieve the best performance, while the smallest model, Qwen3-Embedding-0.6B, only lags behind the best-performing baseline method (Gemini-Embedding), despite having only 0.6B parameters.\n\nFor reranking evaluation, retrieval subsets of MTEB (English, v2), MTEB (Chinese, v1), MMTEB and MTEB (Code) are used."
    ],
    "durationSeconds": 9.149566561,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fbd00fad-f0fa-4fc3-a7e6-716192b764e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-30T07:19:26.665Z_

<details><summary>Logged reasoning block</summary>

```text
Let me now do a couple more targeted searches to check on specific concerns I have about the proposal's experimental design.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd7e9d6c-67e1-4f22-bab0-ed8f8b0e124d",
  "isSidechain": false,
  "requestId": "req_011CbYM5wobCEtsR1p9W4EpR",
  "type": "assistant",
  "uuid": "2b01838c-8d26-4be7-94b7-2a94d4684b50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHi3gzaDcYX4mnRhZUhZ5w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 3904,
      "cache_read_input_tokens": 26462,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 771,
          "output_tokens": 167,
          "cache_read_input_tokens": 26462,
          "cache_creation_input_tokens": 3904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3904
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-30T07:19:28.428Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DFeywWymF4DzrcGWFGe7MS`</summary>

```json
{
  "query": "DF-FLOPS SPLADE regularization SIGIR 2025 training stability sparse retrieval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b01838c-8d26-4be7-94b7-2a94d4684b50",
  "isSidechain": false,
  "requestId": "req_011CbYM5wobCEtsR1p9W4EpR",
  "type": "assistant",
  "uuid": "0f957d0e-5321-4cf5-9858-0f0c7c1c711f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHi3gzaDcYX4mnRhZUhZ5w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 3904,
      "cache_read_input_tokens": 26462,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 771,
          "output_tokens": 167,
          "cache_read_input_tokens": 26462,
          "cache_creation_input_tokens": 3904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3904
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-30T07:19:28.648Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D9nVZvrNdmVAnmyJMguCiu`</summary>

```json
{
  "query": "Hydra retrieval generation unified model 2026 arXiv 2603 experimental evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f957d0e-5321-4cf5-9858-0f0c7c1c711f",
  "isSidechain": false,
  "requestId": "req_011CbYM5wobCEtsR1p9W4EpR",
  "type": "assistant",
  "uuid": "46b38657-cce1-484a-916c-6e5ee4627a88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHi3gzaDcYX4mnRhZUhZ5w",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 771,
      "cache_creation_input_tokens": 3904,
      "cache_read_input_tokens": 26462,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 771,
          "output_tokens": 167,
          "cache_read_input_tokens": 26462,
          "cache_creation_input_tokens": 3904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3904
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-30T07:19:35.445Z_

<details><summary>↩ Tool result · `toolu_01DFeywWymF4DzrcGWFGe7MS`</summary>

```text
Web search results for query: "DF-FLOPS SPLADE regularization SIGIR 2025 training stability sparse retrieval"

Links: [{"title":"An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-Doc | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/10.1145/3726302.3730163"},{"title":"An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-Doc | Pengxiang Cheng","url":"https://www.pengxiang.me/publication/sigir2025/"},{"title":"Bloomberg's AI Engineers Publish 3 Information Retrieval Research Papers at SIGIR 2025 | Bloomberg LP","url":"https://www.bloomberg.com/company/stories/bloomberg-ai-engineers-publish-3-information-retrieval-research-papers-sigir-2025/"},{"title":"SPLADE-doc Variant in Sparse Retrieval","url":"https://www.emergentmind.com/topics/splade-doc-variant"},{"title":"An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-Doc","url":"https://arxiv.org/html/2505.15070v1"},{"title":"An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-Doc","url":"https://arxiv.org/pdf/2505.15070"},{"title":"An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-doc","url":"https://eprints.gla.ac.uk/352748/"},{"title":"An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-doc · smac.pub - smac.pub","url":"https://smac.pub/sigir2025-dfflops"},{"title":"[2505.15070] An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-Doc","url":"https://arxiv.org/abs/2505.15070"},{"title":"An Efficiency Study for SPLADE Models | Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval","url":"https://dl.acm.org/doi/abs/10.1145/3477495.3531833"}]

Based on the search results, here's what I found about DF-FLOPS SPLADE regularization at SIGIR 2025:

## Overview

A paper by Aldo Porco, Dhruv Mehra, Igor Malioutov, Karthik Radhakrishnan, Moniba Keymanesh, Daniel Preoțiuc-Pietro, Sean MacAvaney, and Pengxiang Cheng was published at SIGIR 2025.

## The Problem

SPLADE, the most popular Learned Sparse Retrieval (LSR) model, uses FLOPS regularization to encourage vector sparsity during training. However, FLOPS regularization does not ensure sparsity among terms—only within a given query or document. Terms with very high Document Frequencies (DFs) substantially increase latency in production retrieval engines, such as Apache Solr, due to their lengthy posting lists.

## The Solution: DF-FLOPS

DF-FLOPS enforces sparsity over both documents and terms, compared to the popular FLOPS regularization, which only does so within documents. This new regularization technique penalizes the usage of high-DF terms, thereby shortening posting lists and reducing retrieval latency.

## Key Results

With this method, retrieval latency of SPLADE-Doc can be lowered by 10x to the level of BM25, making learned sparse retrieval practical for deployment in production-grade search engines. The performance of the retrieval system decreases slightly when tested in the same domain as training (−2.2 MRR@10 on MS-MARCO), but it improves on 12/13 cross-domain datasets from the BEIR benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f957d0e-5321-4cf5-9858-0f0c7c1c711f",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "7bc5494a-5413-496e-a456-71fa6d4c5582",
  "toolUseResult": {
    "query": "DF-FLOPS SPLADE regularization SIGIR 2025 training stability sparse retrieval",
    "results": [
      {
        "tool_use_id": "srvtoolu_017KUeEDwKixJaQ7HoszcMdk",
        "content": [
          {
            "title": "An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-Doc | Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval",
            "url": "https://dl.acm.org/doi/10.1145/3726302.3730163"
          },
          {
            "title": "An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-Doc | Pengxiang Cheng",
            "url": "https://www.pengxiang.me/publication/sigir2025/"
          },
          {
            "title": "Bloomberg's AI Engineers Publish 3 Information Retrieval Research Papers at SIGIR 2025 | Bloomberg LP",
            "url": "https://www.bloomberg.com/company/stories/bloomberg-ai-engineers-publish-3-information-retrieval-research-papers-sigir-2025/"
          },
          {
            "title": "SPLADE-doc Variant in Sparse Retrieval",
            "url": "https://www.emergentmind.com/topics/splade-doc-variant"
          },
          {
            "title": "An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-Doc",
            "url": "https://arxiv.org/html/2505.15070v1"
          },
          {
            "title": "An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-Doc",
            "url": "https://arxiv.org/pdf/2505.15070"
          },
          {
            "title": "An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-doc",
            "url": "https://eprints.gla.ac.uk/352748/"
          },
          {
            "title": "An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-doc · smac.pub - smac.pub",
            "url": "https://smac.pub/sigir2025-dfflops"
          },
          {
            "title": "[2505.15070] An Alternative to FLOPS Regularization to Effectively Productionize SPLADE-Doc",
            "url": "https://arxiv.org/abs/2505.15070"
          },
          {
            "title": "An Efficiency Study for SPLADE Models | Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval",
            "url": "https://dl.acm.org/doi/abs/10.1145/3477495.3531833"
          }
        ]
      },
      "Based on the search results, here's what I found about DF-FLOPS SPLADE regularization at SIGIR 2025:\n\n## Overview\n\nA paper by Aldo Porco, Dhruv Mehra, Igor Malioutov, Karthik Radhakrishnan, Moniba Keymanesh, Daniel Preoțiuc-Pietro, Sean MacAvaney, and Pengxiang Cheng was published at SIGIR 2025.\n\n## The Problem\n\nSPLADE, the most popular Learned Sparse Retrieval (LSR) model, uses FLOPS regularization to encourage vector sparsity during training. However, FLOPS regularization does not ensure sparsity among terms—only within a given query or document. Terms with very high Document Frequencies (DFs) substantially increase latency in production retrieval engines, such as Apache Solr, due to their lengthy posting lists.\n\n## The Solution: DF-FLOPS\n\nDF-FLOPS enforces sparsity over both documents and terms, compared to the popular FLOPS regularization, which only does so within documents. This new regularization technique penalizes the usage of high-DF terms, thereby shortening posting lists and reducing retrieval latency.\n\n## Key Results\n\nWith this method, retrieval latency of SPLADE-Doc can be lowered by 10x to the level of BM25, making learned sparse retrieval practical for deployment in production-grade search engines. The performance of the retrieval system decreases slightly when tested in the same domain as training (−2.2 MRR@10 on MS-MARCO), but it improves on 12/13 cross-domain datasets from the BEIR benchmark."
    ],
    "durationSeconds": 7.011234629000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0f957d0e-5321-4cf5-9858-0f0c7c1c711f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Complementary Specialization in Unified Sparse-Dense Decoder Retrieval with Learned Query Routing  ## Core Research Question  In a decoder-only LLM with shared transformer backbone, do sparse (lexic…",
  "leafUuid": "7bc5494a-5413-496e-a456-71fa6d4c5582",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Unified sparse-dense decoder retrieval with learned routing",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---

### Tool result

_source line 49 · 2026-05-30T07:19:37.453Z_

<details><summary>↩ Tool result · `toolu_01D9nVZvrNdmVAnmyJMguCiu`</summary>

```text
Web search results for query: "Hydra retrieval generation unified model 2026 arXiv 2603 experimental evaluation"

Links: [{"title":"[2603.28554] Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model","url":"https://arxiv.org/abs/2603.28554"},{"title":"HYDRA: Unifying Multi-modal Generation and Understanding via Representation-Harmonized Tokenization","url":"https://arxiv.org/html/2603.15228"},{"title":"[2603.15228] HYDRA: Unifying Multi-modal Generation and Understanding via Representation-Harmonized Tokenization","url":"https://arxiv.org/abs/2603.15228"},{"title":"Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model","url":"https://arxiv.org/html/2603.28554"},{"title":"HYDRA: Unifying Multi-modal Generation and Understanding via Representation-Harmonized Tokenization","url":"https://arxiv.org/pdf/2603.15228"},{"title":"[2508.15099] Hydra: A Modular Architecture for Efficient Long-Context Reasoning","url":"https://arxiv.org/abs/2508.15099"}]

Based on the search results, I found two relevant "Hydra" papers from the 2603 arXiv series in 2026:

## 1. Hydra: Unifying Document Retrieval and Generation (arXiv:2603.28554)

This paper presents Hydra, a dual-head approach that provides both ColBERT-style late-interaction retrieval and autoregressive generation from a single vision-language model. A single LoRA adapter, trained only for retrieval, is toggled at inference: enabling it produces multi-vector embeddings; disabling it recovers the base model's generation quality, with 426 of 426 language-model weight tensors byte-for-byte identical to a freshly-loaded Qwen3.5-4B. The paper identifies two failure modes that can silently break generation in retrieval-fine-tuned VLMs (attention-mode restoration and lm_head preservation) plus an efficiency requirement (KV-cache-aware decoding).

## 2. HYDRA: Unifying Multi-modal Generation and Understanding (arXiv:2603.15228)

This paper presents HYDRA, a native unified framework integrating perception and generation within a single parameter space. It sets a benchmark in visual reconstruction (rFID 0.08) and achieves top-tier generation performance on GenEval (0.86), DPG-Bench (86.4), and WISE (0.53), while simultaneously outperforming previous native UMMs by an average of 10.0 points.

Both papers were submitted in March 2026 and address unified model architectures that combine retrieval/understanding with generation capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46b38657-cce1-484a-916c-6e5ee4627a88",
  "isSidechain": false,
  "promptId": "09214ac7-6074-40b6-902d-c1048b5c7fb2",
  "type": "user",
  "uuid": "64c83717-a1c0-44e8-bc49-11a50deef841",
  "toolUseResult": {
    "query": "Hydra retrieval generation unified model 2026 arXiv 2603 experimental evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E3cqxMfuqXsxuq7zQDmsuw",
        "content": [
          {
            "title": "[2603.28554] Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model",
            "url": "https://arxiv.org/abs/2603.28554"
          },
          {
            "title": "HYDRA: Unifying Multi-modal Generation and Understanding via Representation-Harmonized Tokenization",
            "url": "https://arxiv.org/html/2603.15228"
          },
          {
            "title": "[2603.15228] HYDRA: Unifying Multi-modal Generation and Understanding via Representation-Harmonized Tokenization",
            "url": "https://arxiv.org/abs/2603.15228"
          },
          {
            "title": "Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model",
            "url": "https://arxiv.org/html/2603.28554"
          },
          {
            "title": "HYDRA: Unifying Multi-modal Generation and Understanding via Representation-Harmonized Tokenization",
            "url": "https://arxiv.org/pdf/2603.15228"
          },
          {
            "title": "[2508.15099] Hydra: A Modular Architecture for Efficient Long-Context Reasoning",
            "url": "https://arxiv.org/abs/2508.15099"
          }
        ]
      },
      "Based on the search results, I found two relevant \"Hydra\" papers from the 2603 arXiv series in 2026:\n\n## 1. Hydra: Unifying Document Retrieval and Generation (arXiv:2603.28554)\n\nThis paper presents Hydra, a dual-head approach that provides both ColBERT-style late-interaction retrieval and autoregressive generation from a single vision-language model. A single LoRA adapter, trained only for retrieval, is toggled at inference: enabling it produces multi-vector embeddings; disabling it recovers the base model's generation quality, with 426 of 426 language-model weight tensors byte-for-byte identical to a freshly-loaded Qwen3.5-4B. The paper identifies two failure modes that can silently break generation in retrieval-fine-tuned VLMs (attention-mode restoration and lm_head preservation) plus an efficiency requirement (KV-cache-aware decoding).\n\n## 2. HYDRA: Unifying Multi-modal Generation and Understanding (arXiv:2603.15228)\n\nThis paper presents HYDRA, a native unified framework integrating perception and generation within a single parameter space. It sets a benchmark in visual reconstruction (rFID 0.08) and achieves top-tier generation performance on GenEval (0.86), DPG-Bench (86.4), and WISE (0.53), while simultaneously outperforming previous native UMMs by an average of 10.0 points.\n\nBoth papers were submitted in March 2026 and address unified model architectures that combine retrieval/understanding with generation capabilities."
    ],
    "durationSeconds": 8.798287333000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "46b38657-cce1-484a-916c-6e5ee4627a88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-30T07:20:56.416Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a solid understanding of the experimental landscape. Let me analyze the proposal's experimental design systematically.

Let me compile my findings and assess the proposal's experimental design against the standards I've found:

**Key findings from my research:**

1. **Lion-SP/DS (SIGIR 2025)**: Trained on MSMARCO, evaluated on BEIR-14, MS MARCO Dev, TREC DL 19/20. Used 1B/3B/8B scale comparison. Baselines included RepLLaMA, BM25, SPLADE variants. Key ablation: contrastive loss vs. KD vs. CL+KD across scales.


2. **LACONIC-8B (2026)**: Uses curriculum learning across two phases and tests on MTEB Retrieval's 15 datasets plus BEIR, achieving 60.2 nDCG@10 through bidirectional adaptation of Llama-3.
3. **BGE-M3 (ACL Findings 2024)**: Employs self-knowledge distillation between sparse, dense, and multi-vector representations with ablations isolating the self-KD contribution and long document data effects, evaluated across MIRACL and multilingual benchmarks.
4. **RouterRetriever (AAAI 2025)**: Evaluated on BEIR against MSMARCO-trained and multi-task baselines, showing a +2.1 nDCG@10 improvement over other routing approaches.
5. **CSplade (IJCNLP 2025)**: Tackles the dying ReLU problem and applies bidirectional attention to decoder-only lexical sparse retrieval, tested on BEIR.
6. **Llama-Embed-Nemotron-8B**: Builds on Llama-3.1-8B with bidirectional attention and two-stage training, using model averaging across 6 checkpoints to reach MMTEB's top ranking.
7. **DAT (2025)**: Leverages an LLM to evaluate top-1 results from both methods with per-query weighting, benchmarked across various RAG evaluation sets.
8. **CIKM 2025 Self-KD paper**: Explores knowledge distillation from vision-language models like BLIP and ALBEF for text-image retrieval, comparing bidirectional versus unidirectional supervision and finding that bidirectional KD strengthens sparse representations.
9. **Qwen3-Embedding**: Follows the multi-stage training approach of the GTE-Qwen series, achieving 70.58 on multilingual MTEB and 80.68 on code benchmarks.
10. **DF-FLOPS (SIGIR 2025)**: Proposes an alternative to standard FLOPS regularization by penalizing high document frequency terms, delivering 10x latency improvements with minor in-domain trade-offs but gains on 12 of 13 BEIR cross-domain datasets.
11. **Hydra (2026)**: Implements LoRA switching between retrieval and generation modes using ColBERT-style retrieval, built on Qwen3.5-4B.

Now looking at the experimental design, the baseline coverage is quite solid—it includes sparse SOTA models, dense SOTA models, post-hoc fusion approaches, secondary baselines like BM25 and SPLADE-v3, and reference models across different families. The ablation studies are comprehensive too, with separate conditions for self-KD, router design, training stages, and representational analysis using CKA and attention entropy metrics.

The evaluation setup uses standard benchmarks across BEIR, MTEB, MS MARCO, and TREC datasets, and the compute-controlled comparisons are well-designed. The three-dimensional performance claims are clearly defined, and there's a practical feasibility plan with a 3B proof-of-concept and LoRA fallback.

On the potential issues side, BGE-M3 is already included as a reference model, which makes sense given it's encoder-only XLM-RoBERTa. But there's a notable gap—the proposal converts Llama-3.1-8B from causal to bidirectional attention, which is a substantial architectural modification, yet there's no ablation isolating the impact of this change.

Actually, looking at the broader context, this attention modification is already standard practice in LACONIC, CSplade, and Llama-Embed-Nemotron, so it may not warrant its own ablation. The bigger concern is that the proposal doesn't specify what training data will be used—whether it's MS MARCO, synthetic data, or a multi-source approach. This is critical because training data can dramatically shift results, and without knowing what's being used, it's hard to make fair comparisons against baselines like Llama-Embed-Nemotron, which used 16.1M query-document pairs.

The pooling strategy also matters here—the proposal mentions latent attention pooling from NV-Embed-v2, but Llama-Embed-Nemotron uses its own pooling approach, which becomes a confounding factor when comparing models with the same backbone. Additionally, Llama-Embed-Nemotron is actually an ensemble average of 6 models, giving it an architectural advantage that a single-model comparison wouldn't capture fairly. I should note this distinction in the paper. Finally, there's no mention of statistical significance testing, which is important for evaluating results on benchmarks like BEIR.

For the sparse head evaluation, I need to specify which sparsity metrics I'll report—things like average non-zero terms or FLOPS reduction, which are standard in sparse retrieval papers. The efficiency evaluation claims to include end-to-end latency with the router, but I should break down the components separately (encoding time versus index lookup) to show that the router overhead is actually negligible. On the cross-encoder knowledge distillation side, I mentioned it adds about 20% compute to Stage 2, but I haven't specified which cross-encoder model will be used for this.

I'm also realizing I need to address reproducibility more directly—the three-stage curriculum has many hyperparameters (learning rates, stage durations, KD loss weights, FLOPS regularization), and I should include sensitivity analysis for these. The hard-negative fine-tuning in Stage 3 needs clarification too; I haven't specified whether I'm using BM25 negatives, cross-encoder mined negatives, or in-batch negatives, which significantly impacts retrieval performance. Finally, while I mentioned a 3B proof-of-concept, I'm not positioning this as a proper scaling analysis, and given the core question about complementary specialization, showing how this behavior changes across different model scales would make the paper much stronger.

The "mutual benefit" claim is also problematic—to truly validate that each head performs at least as well as its independently trained counterpart, I'd need to train separate sparse-only and dense-only 8B models with identical data, compute budgets, and hyperparameter tuning effort, but I haven't accounted for this additional compute cost in my budget.

Looking at what actually matters here, the critical gaps are the training data specification, the missing details on per-head versus independent training comparisons, lack of statistical significance testing, unspecified sparsity metrics, undefined hard negative mining strategy, and the unidentified cross-encoder teacher for the knowledge distillation ablation. The other concerns—like the model averaging difference from Nemotron, latency breakdowns, hyperparameter sensitivity, and upgrading the scaling analysis—are more minor or defensible omissions.

The compute budget seems feasible on paper, but there's a major ambiguity: the proposal needs to train independent sparse-only and dense-only baseline models to validate the core complementary specialization hypothesis, which would essentially double the training cost. It's also unclear whether the "per-head performance vs single-task 8B counterparts" comparison uses existing published models (which introduces training data confounds) or newly trained controls (which inflates the compute requirements), and the proposal doesn't clarify this critical distinction.

This is the crux of the experimental design problem — the hypothesis fundamentally requires a tightly controlled comparison between joint and independent training, but the proposal leaves this comparison underspecified. I should flag this as a significant gap that needs resolution before approval, though it's not insurmountable.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64c83717-a1c0-44e8-bc49-11a50deef841",
  "isSidechain": false,
  "requestId": "req_011CbYM6zAzYNSZUXeyXdGjH",
  "type": "assistant",
  "uuid": "eebcd0e9-1d01-4538-8d3c-f9f1bae8045a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vQ6y5wXj3FprWFgmi3vTp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2691,
      "cache_read_input_tokens": 30366,
      "output_tokens": 8834,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8834,
          "cache_read_input_tokens": 30366,
          "cache_creation_input_tokens": 2691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2691
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-30T07:22:50.168Z_

Now I have enough research to conduct a thorough evaluation. Let me organize my findings and assess the proposal's experimental design systematically.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **Lion-SP/DS (SIGIR 2025, arXiv:2502.15526)**: 在 1B/3B/8B 三个尺度做 scaling 分析，训练数据为 MSMARCO，评测覆盖 BEIR-14 (per-dataset nDCG@10)、MS MARCO Dev (MRR@10)、TREC DL 19/20。关键 ablation：CL vs KD vs CL+KD 在不同 scale 下的表现差异。独立训练 sparse 和 dense 模型，使用相同训练数据和 pipeline。
- **LACONIC-8B (arXiv:2601.01684, 2026)**: 两阶段 curriculum（adaptation + fine-tuning），基于 Llama-3.1-8B 做 bidirectional adaptation。评测 MTEB Retrieval (15 datasets) 和 BEIR。明确报告 sparsity 指标（average non-zero terms）。
- **BGE-M3 (ACL Findings 2024, arXiv:2402.03216)**: Self-KD 在 sparse/dense/multi-vector 三头之间；ablation 逐头移除 KD 信号。评测 BEIR、MIRACL、MLDR。明确报告每种模式的独立和组合性能。
- **RouterRetriever (AAAI 2025, arXiv:2409.02685)**: 在 BEIR 上评测 nDCG@10，对比 MSMARCO-trained 模型、multi-task 模型和其他 routing 技术。+2.1 nDCG@10。
- **Llama-Embed-Nemotron-8B (arXiv:2511.07025, 2025)**: 同 Llama-3.1-8B backbone，bidirectional attention，两阶段训练，16.1M 训练对（7.7M public + 8.4M synthetic），最终模型为 6 个模型的等权平均。
- **CIKM 2025 Self-KD (arXiv:2508.16707)**: VLP encoder 模型上的 bidirectional self-KD，ablation 比较 unidirectional vs. bidirectional，证明双向有利于 sparse 表征。
- **CSplade (IJCNLP 2025, arXiv:2504.10816)**: 解决 decoder-only 的 dying ReLU 问题，提出 lightweight adaptation phase，评测 BEIR 并分析 performance-efficiency tradeoff（含量化分析）。
- **Qwen3-Embedding-8B (arXiv:2506.05176, 2025)**: 三阶段训练（GTE-Qwen 范式），MTEB Multilingual 70.58，MTEB Code 80.68。

- **调研总结**: 该领域当前的实验设计标准要求：(1) 使用**相同训练数据和 pipeline** 训练的独立模型作为 controlled baseline 以隔离架构/方法贡献（Lion 在三个 scale 均如此）；(2) 明确报告 sparse head 的 sparsity 指标（non-zero terms、FLOPS）；(3) 明确规定训练数据来源和规模以确保对比公平性；(4) 审稿人普遍期望 hard negative mining 策略的具体说明和 ablation。

---

【缺陷 1】
- 类别: 实验设计不足
- 问题: **Core hypothesis 的 controlled comparison 定义不清**。Proposal 的核心 claim 是"joint training induces complementary specialization superior to independent training"，并在 Compute-Controlled Comparisons 中提到"per-head performance vs single-task 8B counterparts"。但未明确定义"counterpart"是指已发表的模型（LACONIC-8B、Lion-SP-8B 等）还是由作者自己用**完全相同的训练数据、相同的超参数搜索预算、相同的 training pipeline** 训练的独立 sparse-only 和 dense-only 模型。若使用已发表模型作为对照，训练数据差异（e.g., Llama-Embed-Nemotron 用了 16.1M pairs 含 8.4M synthetic，Lion 用 MSMARCO）构成严重 confound，无法归因于"joint training"本身。若训练新的独立模型，需额外 2 次 8B full fine-tuning，计算成本未纳入预算。
- 严重度: 可补救
- 补救方案: (1) 明确指定 "internal controlled baselines"：使用与 unified model **完全相同的训练数据、相同的超参数搜索预算**分别训练 sparse-only 和 dense-only 8B 模型。(2) 将这两个模型列为 **Primary baselines 中的首要对照**，将已发表的 LACONIC-8B、Lion-SP/DS 等降为 "external reference"（因为训练 pipeline 不同，不能做 controlled attribution）。(3) 将额外训练开销（~2×7-10 GPU-days = 14-20 GPU-days on 8×A100）明确纳入计算预算。(4) 同理，3B proof-of-concept 也应训练对应的 3B 独立模型做对照。
- 调研依据: Lion (SIGIR 2025) 在 1B/3B/8B 三个 scale 均使用完全相同训练数据独立训练 sparse 和 dense 模型做对照，这是隔离方法贡献的黄金标准。

【缺陷 2】
- 类别: 实验设计不足
- 问题: **训练数据规格完全未指定**。Proposal 未说明任何关于训练数据的选择：Stage 1/2/3 分别使用什么数据集？MS MARCO only？是否包含 synthetic hard negatives？数据量多大？这是当前领域论文的硬性要求——训练数据的差异是 retrieval 模型性能差异的最大来源之一。Llama-Embed-Nemotron 使用 16.1M pairs（含 8.4M synthetic），Lion 使用 MSMARCO，LACONIC 有自己的 curriculum——不同的训练数据会导致 5-10 nDCG@10 的差异，远超方法本身带来的增量。
- 严重度: 可补救
- 补救方案: (1) 明确指定每个训练阶段的数据来源和规模。建议 Stage 1/2 至少使用 MS MARCO passage ranking dataset（~500K training queries, 8.8M passages）以与 Lion、LACONIC 可比。(2) 如果使用 synthetic data 或额外数据源，需声明并在 ablation 中控制。(3) Stage 3 的 hard negative 来源必须明确说明（见缺陷 3）。(4) 数据选择本身应该有简短的 justification。
- 调研依据: Lion (SIGIR 2025)、LACONIC (2026)、CSplade (IJCNLP 2025) 均明确指定训练数据为 MS MARCO 并标准化数据条件。Llama-Embed-Nemotron 则使用大规模混合数据，这种差异直接导致性能不可比。

【缺陷 3】
- 类别: 实验设计不足
- 问题: **Hard negative mining 策略未指定**。Stage 3 提到 "hard-negative fine-tuning" 但未说明 hard negative 如何获取——BM25 top-k mining？Cross-encoder re-ranking mining？In-batch negatives？前一阶段模型自挖掘？这在 retrieval model 训练中是一个对最终性能影响极大的设计选择（可达 2-5 nDCG@10 差异），审稿人必问。
- 严重度: 可补救
- 补救方案: (1) 明确指定 hard negative mining pipeline：建议采用多轮 mining（先 BM25 top-100 → 再用 Stage 2 model 自挖 → cross-encoder rerank 取 top-k 最 confusing negatives），这与 Lion 和 LACONIC 的做法一致。(2) 可以在 ablation 中增加一个 hard negative 来源对比（BM25-mined vs. model-mined vs. cross-encoder-mined），但这不是必须的，只需在 paper 中明确说明选择理由。
- 调研依据: Lion (SIGIR 2025) 使用 KD 从 cross-encoder 进行 hard negative 训练；LACONIC 在第二阶段使用 mined hard negatives。这是该领域的标准实践。

【缺陷 4】
- 类别: ablation 不完整
- 问题: **Cross-encoder teacher KD ablation（Self-KD ablation condition (e)）的 teacher 未指定**。Proposal 列出了 "cross-encoder teacher KD (external reranker as teacher for both heads)" 作为 ablation condition，但未说明使用哪个 cross-encoder。Cross-encoder 的质量直接影响 KD 效果——用 MiniLM cross-encoder 和用 monoT5-3B 的结果可能差距很大。审稿人会质疑这个 ablation 的 validity。
- 严重度: 可补救
- 补救方案: 指定具体的 cross-encoder teacher model（建议使用广泛采用的 cross-encoder-ms-marco-MiniLM-L-12-v2 或更强的 bge-reranker-v2-m3 / Qwen3-Reranker），并说明选择理由。如果计算允许，可以尝试两个不同量级的 cross-encoder 以展示 teacher quality 的影响。
- 调研依据: Lion (SIGIR 2025) 在 KD 实验中使用了明确的 cross-encoder teacher；BGE-M3 的 self-KD 对比了有/无外部 teacher 的条件。基于领域实验规范判断，cross-encoder 选择需要明确。

【缺陷 5】
- 类别: 评估方案缺陷
- 问题: **Sparse head 的 sparsity 指标未列入评估方案**。Proposal 在 Efficiency Evaluation 中列出了 index size 和 throughput，在 Stage ablation 中提到 "report sparsity levels"，但未系统性地将 sparsity metrics 纳入评估框架。SPLADE 系列论文的标准做法是报告：(1) average number of non-zero terms per document/query，(2) FLOPS score（或 DF-FLOPS），(3) sparsity vs. effectiveness tradeoff curve。对于 8B scale 的 sparse model，sparsity 直接决定 index 实际可用性——如果 non-zero terms 膨胀到数百甚至上千，index 会变得不可用。
- 严重度: 可补救
- 补救方案: (1) 在 Evaluation Benchmarks 或 Efficiency Evaluation 下增加 Sparsity Metrics 子节：report average non-zero terms (per-query and per-document), FLOPS score, and DF-FLOPS distribution。(2) 在 Router ablation 的补充分析中，分析 router 在不同 sparsity level queries 上的行为。(3) 与 LACONIC-8B 和 CSplade-8B 的 sparsity-effectiveness tradeoff 做直接对比。
- 调研依据: LACONIC (2026) 和 CSplade (IJCNLP 2025) 均报告 average non-zero terms 和 sparsity-effectiveness tradeoff。DF-FLOPS (SIGIR 2025) 进一步要求报告 per-term DF 分布以评估生产可行性。

【缺陷 6】
- 类别: 评估方案缺陷
- 问题: **缺少统计显著性检验**。Proposal 规划了 BEIR-14 per-dataset nDCG@10 等多个评测维度，但未提及任何统计显著性测试。在 retrieval 评测中，0.5-1.0 nDCG@10 的差异经常不显著，审稿人会质疑 improvement 的 reliability，特别是在 BEIR 不同 subset 上 variance 很大的情况下。
- 严重度: 可补救
- 补救方案: (1) 对 MS MARCO dev 和 TREC DL 使用 paired t-test 或 bootstrap resampling（per-query comparison）。(2) 对 BEIR-14 的 aggregate nDCG@10 使用 Wilcoxon signed-rank test（跨 14 个 dataset 的 paired comparison）。(3) 在表格中用 * / ** 标注 p < 0.05 / 0.01。(4) 对于核心 claim（joint > independent），报告 effect size（Cohen's d）和 95% confidence interval。
- 调研依据: 基于领域实验规范判断——SIGIR/AAAI 审稿人对 retrieval 评测的统计显著性要求日益严格，特别是在增量较小的情况下。

【缺陷 7】
- 类别: 可行性问题
- 问题: **Compute budget 未包含 controlled independent baselines 的训练开销**。如缺陷 1 所述，验证核心 hypothesis 需要训练至少 2 个独立 8B 模型（sparse-only + dense-only）。加上 5 个 Self-KD ablation conditions、4 个 Stage ablation conditions（部分可以从训练 checkpoint 获取），实际总计算需求远超"8×A100 for 7-10 days"。粗略估计：unified model (7-10 days) + sparse-only control (5-7 days) + dense-only control (5-7 days) + cross-encoder KD variant (~+20%) + 3B proof-of-concept (~3 days × 3 models) ≈ 30-40 GPU-days on 8×A100，即约 240-320 A100-days。这仍然是可行的，但需要在预算中明确。
- 严重度: 可补救
- 补救方案: (1) 重新详细列出 compute budget，涵盖所有需要训练的模型变体：main unified model、sparse-only control、dense-only control、Self-KD ablation variants（注意部分可复用——e.g., "no KD" condition 即为 dense-only + sparse-only 独立训练）、3B PoC 及其 controls。(2) 识别可复用的训练 runs（e.g., Self-KD ablation condition (a) "no KD" 就是同时训练两个头但不做 KD，而 independent baselines 是完全分开训练——这些是不同的 condition，不能混为一谈）。(3) 如果总 compute 超出预算，明确 LoRA fallback 覆盖哪些 ablation conditions，以及这对实验 validity 的影响。
- 调研依据: Lion (SIGIR 2025) 在 3 个 scale × 3 种 training objective × 2 模式(sparse/dense) = 18 个模型上做了完整训练，表明该领域期望的 ablation 粒度。

【缺陷 8】
- 类别: 实验设计不足
- 问题: **3B proof-of-concept 可以升级为 scaling analysis**。当前 proposal 将 3B 训练纯粹定位为 feasibility validation（"validate method"），但 Lion 的核心发现之一是 sparse 和 dense 在不同 scale 有不同的 scaling behavior。如果 complementary specialization 效应在 3B 和 8B 上表现不同（例如 3B 上两个 head 竞争但 8B 上互补），这本身就是一个重要发现。将 3B 实验从 "PoC" 升级为正式的 scaling analysis 几乎零额外成本但显著增加 paper 的 analytical depth。
- 严重度: 可补救（优先级较低，属于增强而非修补）
- 补救方案: (1) 将 3B 实验结果纳入正式实验章节，增加 "Scaling Analysis" 子节。(2) 在 3B 和 8B 上做相同的 CKA、linear probing、Self-KD ablation 对比。(3) 如果计算允许，增加 1B scale 以形成 1B/3B/8B 三点 scaling curve。(4) 分析"complementary specialization 是否随 scale 增强"——这直接扩展 Lion 的 finding，提高论文的科学贡献。
- 调研依据: Lion (SIGIR 2025) 的三尺度 scaling 分析是其核心贡献之一，审稿人对该领域的 scaling behavior 有明确兴趣。

【缺陷 9】
- 类别: 评估方案缺陷
- 问题: **Router evaluation 缺少与 RouterRetriever 在 routing mechanism 层面的直接对比**。虽然 RouterRetriever 路由的是不同的外部模型（不是内部 head），但两者在 "per-query routing" 这个 claim 上直接竞争。Proposal 的 Router ablation (6 conditions) 覆盖了内部对比，但没有与 RouterRetriever 的 routing 效果做直接比较。审稿人可能要求：在相同 BEIR benchmark 上，proposed router 的 per-query α 选择质量 vs. RouterRetriever 的 domain-level routing quality。
- 严重度: 可补救（优先级较低）
- 补救方案: (1) 在 Router ablation 中增加一个 condition：simulated RouterRetriever-style domain-level routing（即对 BEIR 每个 subset 使用该 subset 上 grid-search 得到的最优 α，而非 per-query α）——这实际上已被 condition (d) "best fixed α" 部分覆盖，但需要 clarify 是 global best α 还是 per-domain best α。(2) 明确区分 per-query routing (proposed) vs. per-domain routing (RouterRetriever 风格) vs. global fixed routing，确保 ablation 覆盖这三个粒度。
- 调研依据: RouterRetriever (AAAI 2025) 的 routing 是 domain-level 的，DAT 是 per-query 的。Proposal 的 router 也是 per-query 的，需要与这两种粒度都做对比。

Sources:
- [Scaling Sparse and Dense Retrieval in Decoder-Only LLMs (SIGIR 2025)](https://arxiv.org/html/2502.15526)
- [LACONIC: Dense-Level Effectiveness for Scalable Sparse Retrieval](https://arxiv.org/html/2601.01684v1)
- [BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation](https://arxiv.org/abs/2402.03216v4)
- [RouterRetriever: Routing over a Mixture of Expert Embedding Models (AAAI 2025)](https://arxiv.org/html/2409.02685v2)
- [CSPLADE: Learned Sparse Retrieval with Causal Language Models (IJCNLP 2025)](https://arxiv.org/abs/2504.10816)
- [Llama-Embed-Nemotron-8B (arXiv:2511.07025)](https://arxiv.org/html/2511.07025v1)
- [DAT: Dynamic Alpha Tuning for Hybrid Retrieval](https://arxiv.org/abs/2503.23013)
- [CIKM 2025 Self-KD: Sparse and Dense Retrievers Learn Better Together](https://arxiv.org/html/2508.16707)
- [Qwen3-Embedding (arXiv:2506.05176)](https://arxiv.org/html/2506.05176v1)
- [DF-FLOPS: An Alternative to FLOPS Regularization (SIGIR 2025)](https://arxiv.org/abs/2505.15070)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eebcd0e9-1d01-4538-8d3c-f9f1bae8045a",
  "isSidechain": false,
  "requestId": "req_011CbYM6zAzYNSZUXeyXdGjH",
  "type": "assistant",
  "uuid": "7c7daf1c-d0d9-44d3-9495-96b498a49949",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vQ6y5wXj3FprWFgmi3vTp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2691,
      "cache_read_input_tokens": 30366,
      "output_tokens": 8834,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8834,
          "cache_read_input_tokens": 30366,
          "cache_creation_input_tokens": 2691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2691
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Complementary Specialization in Unified Sparse-Dense Decoder Retrieval with Learned Query Routing  ## Core Research Question  In a decoder-only LLM with shared transformer backbone, do sparse (lexic…",
  "leafUuid": "7c7daf1c-d0d9-44d3-9495-96b498a49949",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Unified sparse-dense decoder retrieval with learned routing",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Complementary Specialization in Unified Sparse-Dense Decoder Retrieval with Learned Query Routing  ## Core Research Question  In a decoder-only LLM with shared transformer backbone, do sparse (lexic…",
  "leafUuid": "7c7daf1c-d0d9-44d3-9495-96b498a49949",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Unified sparse-dense decoder retrieval with learned routing",
  "sessionId": "1b1ccde3-6b17-438b-a7e3-65e8cfb2be3f"
}
```

---
