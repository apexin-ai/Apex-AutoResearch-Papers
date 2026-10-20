# paper writing experiments d041

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_d041_20260516T043441_result.json`
- **Structured JSON:** [`2972333821485926bf18.json`](../../sessions/29/2972333821485926bf18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

experiments.tex 已全量重写。主要变更：

- **§4.1**: 新增 source (f) branch-split，其余保持简洁
- **§4.2**: DINO cls_token 0.692 领先；新增 branch-split 段落（DINOv2=0.619 ≈ SigLIP=0.621，fusion=0.634 > 两者，projector 压缩 0.634→0.615）；CKA 反转讨论保留
- **§4.3**: 标题改为 "Non-Monotonic LLM Transformation"；核心叙事：inverted-U（L0=0.612→L12=0.628 peak ABOVE projector 0.615→L32=0.422）；RSA-CKA dissociation；readout concentration 保留
- **§4.4**: 标题改为 "Training Redistributes, Does Not Create"；best-vs-best Δ=+0.017 n.s.；same-layer L12 Δ=+0.079 p<0.0001；instruction invariance |Δ|<0.006

所有 \label 与旧版一致，数字均来自权威数据表。

---
