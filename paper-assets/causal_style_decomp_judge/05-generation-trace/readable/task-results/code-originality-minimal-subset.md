# code originality minimal subset

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_originality_minimal_subset_20260521T114355_result.json`
- **Structured JSON:** [`bdf3568a1d0e73fc8b70.json`](../../sessions/bd/bdf3568a1d0e73fc8b70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果完整。总结：

**Formality (n=88)**
| Subset | n | BT | 95% CI |
|--------|---|-----|--------|
| Full | 88 | .630 | [.558, .703] |
| Likert-balanced (|Δ|=0) | 55 | .627 | [.536, .718] |
| Consistent-only | 46 | .739 | [.609, .869] |
| Anti-originality | 13 | .769 | [.538, .999] |
| OC=1 (degenerate) | 40 | .500 | [.500, .500] |

Δ(Likert subset − full) = −0.003, CI=[−0.121, +0.114] — 包含0，无显著差异。

**Verbosity (n=86)**
| Subset | n | BT | 95% CI |
|--------|---|-----|--------|
| Full | 86 | .773 | [.703, .843] |
| Likert-balanced (|Δ|=0) | 50 | .760 | [.660, .850] |
| Consistent-only | 63 | .873 | [.794, .952] |
| Anti-originality | 36 | .861 | [.750, .972] |
| OC=1 (degenerate) | 23 | .500 | [.500, .500] |

Δ(Likert subset − full) = −0.013, CI=[−0.133, +0.103] — 包含0，无显著差异。

**关键发现：**
1. Originality count=1 方法不可用——这些 pair 的两次 trial 恰好各选一个 style，BT 必然=50%（construction artifact）
2. Likert-balanced subset（original 和 counterfactual 同分的 pair）上 BT 与全集无显著差异（Δ CI 含0），style effect 稳定
3. Anti-originality subset（style 偏好压过了 originality）上 BT 更强，进一步说明 style effect 不依赖 originality

脚本在 `csd_pipeline/originality_minimal_subset.py`，JSON 在 `data/originality_minimal_subset.json`。

---
