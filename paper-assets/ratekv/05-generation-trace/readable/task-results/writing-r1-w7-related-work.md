# writing r1 w7 related work

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_r1_w7_related_work_20260515T044227_result.json`
- **Structured JSON:** [`f6c36f5eba02d6bdf919.json`](../../sessions/f6/f6c36f5eba02d6bdf919.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Compilation clean: 14-page PDF built, no undefined-citation warnings. Summary of changes:

**`references.bib`** — added 8 verified entries:
- `dong2019hawq` (ICCV 2019), `dong2020hawqv2` (NeurIPS 2020), `wang2019haq` (CVPR 2019)
- `su2025rotatekv` (IJCAI 2025), `sharma2025minikv` (Findings of ACL 2025), `shutova2025aquakv` (ICML 2025, "Cache Me If You Must")
- `liu2025pmkvq` (arXiv preprint), `xia2025kitty` (arXiv preprint)
- Skipped "Don't Waste Bits!" — not verified.

**`related_work.tex`** —
- KV Cache Quantization paragraph: added RotateKV / MiniKV / AQUA-KV at the end of the uniform-precision enumeration.
- New **Mixed-Precision Quantization (Weights)** paragraph: HAWQ / HAWQ-V2 / HAQ, framed as the foundational weight-level mixed-precision lineage, with one transfer sentence to our per-head KV setting.
- Mixed-Precision Rate-Distortion Allocation paragraph: expanded RateQuant differentiation with the concrete additivity argument (single-bit gap → small-perturbation regime → polymatroid), the catastrophic-failure numbers (32.45 vs uniform 15.45 vs constrained 11.23 on Qwen2.5-7B at 4×, referencing `tab:solver_equiv`), and the framing that the cardinality constraint "restores the additive regime in which RateQuant's polymatroid argument applies." Also folded PM-KVQ (block-level) and Kitty (channel-level) into the granularity enumeration.

Sources:
- [HAWQ (ICCV 2019)](https://arxiv.org/abs/1905.03696)
- [HAWQ-V2 (NeurIPS 2020)](https://arxiv.org/abs/1911.03852)
- [HAQ (CVPR 2019)](https://arxiv.org/abs/1811.08886)
- [RotateKV (IJCAI 2025)](https://www.ijcai.org/proceedings/2025/690)
- [MiniKV (Findings of ACL 2025)](https://aclanthology.org/2025.findings-acl.952/)
- [AQUA-KV / Cache Me If You Must (ICML 2025)](https://proceedings.mlr.press/v267/shutova25a.html)
- [PM-KVQ](https://arxiv.org/abs/2505.18610)
- [Kitty](https://arxiv.org/abs/2511.18643)

---
