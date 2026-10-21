# check olmo arxiv progress

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_olmo_arxiv_progress_20260524T105749_result.json`
- **Structured JSON:** [`88d1918c7529b386d7cd.json`](../../sessions/88/88d1918c7529b386d7cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验已完成**，耗时 365.8s，结果如下：

### OLMo-1B arXiv Cross-Scorer (Scorer: Qwen2.5-1.5B-Instruct)

| Pair | AUC | 95% CI | p_perm | Sig? | CI > θ=0.6? |
|------|-----|--------|--------|------|-------------|
| 0v1 | 0.9994 | [0.9990, 0.9997] | 0.0001 | **SIG** | **PASS** |
| 1v2 | 0.4996 | [0.4828, 0.5166] | 0.5100 | n.s. | FAIL |
| 2v3 | 0.4971 | [0.4796, 0.5138] | 0.6267 | n.s. | FAIL |
| 3v4 | 0.5091 | [0.4922, 0.5262] | 0.1488 | n.s. | FAIL |
| 4v5 | 0.5360 | [0.5183, 0.5533] | 0.0001 | **SIG** | FAIL |

**K\* = 1**（cross-scorer），与 self-scoring 的 K\*=1 一致。其他 arXiv generators（Qwen/LLaMA/Mistral/Pythia）的 K\*=3。

OLMo 在 arXiv 域上只有 0v1 能被可靠区分（AUC≈1.0），depth 1 之后的代际差异完全消失。4v5 虽然 permutation 显著但 AUC 仅 0.536、CI 远未达到 θ=0.6 阈值，不满足 PASS 条件。

---
