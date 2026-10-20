# research verify related work

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_related_work_20260513T164334_result.json`
- **Structured JSON:** [`5b0ddddc65d60a234247.json`](../../sessions/5b/5b0ddddc65d60a234247.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verifications complete. Here's the summary:

## 验证结果

| 论文 | Citation Key | 状态 | 说明 |
|------|-------------|------|------|
| **NE-Dreamer** | `nedreamer2026` | ✓ 准确 | Bredis et al., arXiv 2603.02765。描述正确 |
| **R2-Dreamer** | `r2dreamer2026` | ✓ 准确 | Morihira et al., ICLR 2026。描述正确 |
| **TAWM** | ~~`freed2024tawm`~~ → `nhu2025tawm` | **已修正** | 描述匹配的是 Nhu, Son & Lin (ICML 2025) 的 "Time-Aware World Model"，不是 Freed et al. (ICML 2023) 的 skill-conditioned temporal abstraction。已修正 citation key |
| **THICK** | `romac2024thick` | ✓ 准确 | Gumbsch et al., ICLR 2024。描述正确 |
| **HWM** | `zhang2026hwm` | ✓ 准确 | 第一作者 Wancong Zhang，arXiv 2604.03208。描述正确 |
| **LS-Imagine** | `li2025lsimagine` | ✓ 准确 | 第一作者 Jiajian Li，ICLR 2025 Oral。kurtosis 机制描述已确认 |
| **I-TAP** | `itap2026` | ✓ 准确 | RQ-VAE 描述正确（之前 Worker 已修正 VQ-VAE→RQ-VAE） |
| **DMWM** | `wang2025dmwm` | ✓ 准确 | Lingyi Wang et al., NeurIPS 2025。描述正确 |
| **DyMoDreamer** | `dymodreamer2025` | ✓ 准确 | NeurIPS 2025。描述正确 |
| **ELVIS** | `du2026elvis` | ✓ 准确 | Yurui Du et al., arXiv 2605.04709。描述正确 |
| **EA-WM** | `eawm2026` | ✓ 准确 | arXiv 2605.06192。描述正确 |
| **FiGAR / TempoRL** | — | 未出现在草稿中 | 无需处理 |

**唯一修正**：TAWM 的 citation key 从 `freed2024tawm` 改为 `nhu2025tawm`。对应 bib 文件也需更新（作者: Anh N. Nhu, Sanghyun Son, Ming Lin; venue: ICML 2025）。

无 `[NEED VERIFY]` 标记残留。

---
