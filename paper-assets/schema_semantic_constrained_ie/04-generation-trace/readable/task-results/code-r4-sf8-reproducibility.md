# code r4 sf8 reproducibility

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r4_sf8_reproducibility_20260517T105439_result.json`
- **Structured JSON:** [`22a580ec4c8b62d54ab1.json`](../../sessions/22/22a580ec4c8b62d54ab1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入 `artifacts/r4_sf8_reproducibility.md`。

关键数据摘要:

**LoRA 配置** (四个模型一致): r=16, alpha=32, dropout=0.05, 7 个 target modules, AdamW, lr=2e-4, cosine schedule, 3 epochs, effective batch size=16

**Training steps**: SciERC 333 步 (warmup 33), DocRED 573 步 (warmup 57)

**GPU**: 2x NVIDIA RTX PRO 6000 Blackwell (98GB); 训练约 SciERC ~11min, DocRED ~1.5h per model

**Inference time (Qwen, sec/doc)**:
- SciERC: Unconstrained 8.69±3.89, Full S1 6.76±3.67 (-22.2%), Beam k=4 5.92±2.34
- DocRED: Unconstrained 19.75±8.99, Full S1 20.39±9.43 (+3.2%), Beam k=4 31.35±26.09 (n=50)

DocRED beam search 只有 50 条 pilot 数据，没有全量 998 条的运行结果。

---
