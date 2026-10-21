# research literature map init

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_map_init_20260514T211739_result.json`
- **Structured JSON:** [`d7455cc214050afaf0e5.json`](../../sessions/d7/d7455cc214050afaf0e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`literature_map.yaml` 已创建，共 15 篇论文，4 个类别均满足 ≥3 篇要求：

| Category | 数量 | 论文 |
|---|---|---|
| direct-competitor | 3 | Drayson (EMNLP'25, 同公式启发式b), He (黄金比例权重), Feng (verification-based) |
| method-component | 5 | importance weighting survey, PSIS/ESS, dynamic loss reweighting, data mixing laws, SoftDedup |
| background | 4 | model collapse (Nature), MAD (ICLR'24), strong collapse (ICLR'25), data-quality illusion |
| evaluation | 3 | DetectGPT, Min-K% Prob, synthetic data weighting evaluation |

所有论文均通过 WebSearch 确认存在，含完整 arxiv URL。Drayson et al. 的关键信息已补全：George Drayson, Emine Yilmaz, Vasileios Lampos（UCL），arxiv 2502.15654，使用 importance resampling 防止 model collapse。

---
