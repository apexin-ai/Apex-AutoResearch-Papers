# audit experiments c1 data verify

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_experiments_c1_data_verify_20260514T004234_result.json`
- **Structured JSON:** [`856154fd3ff73174b212.json`](../../sessions/85/856154fd3ff73174b212.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both fixes are already applied (likely by a concurrent process or linter). The file now shows the correct values:
- Line 30: `p = 0.002` ✓
- Line 36: Qwen-cont 0v1 = `0.9971` ✓

## 校验报告

| 检查项 | 结果 |
|--------|------|
| **AUC 值** (所有 pairwise AUC, 20 cells) | ✓ 正确 (修正 Qwen-cont 0v1: 0.9972→0.9971) |
| **K\* 值** (K\*=2) | ✓ 正确，与 registry 一致 |
| **CI 区间** (16 bounds) | ✓ 全部正确 |
| **p-values** (10 values) | ✓ 正确 (修正 caption p=0.000→p=0.002) |
| **模型名** | ✓ 无 7B 模型，仅 Pythia-1.4B / OLMo-1B / Qwen2.5-1.5B-Instruct |
| **Transfer matrix** (16 cells) | ✓ 全部与 exp_013 一致 |
| **Transfer retention %** | ✓ Pythia↔OLMo 90-92%, Qwen-rw→others 61-63%, Qwen-cont↔Pythia 84-85%, Qwen-cont↔OLMo 80-85% |
| **Feature 排名** (4 models × top 3) | ✓ 全部与 exp_005 一致 |
| **Spearman ρ** (3 values) | ✓ 0.95, 0.9143, 0.85 与 exp_005 一致 |
| **Kendall τ** (5 values) | ✓ 0.733, 0.695, 0.543, 0.467, 0.429 与 exp_005 一致 |
| **Mean pw AUC** (within/cross) | ✓ 0.6099 / 0.5905 与 exp_013 一致 |
| **LLM zero-shot** | N/A — 本文件未包含 exp_011 数据 |

**修正 2 处**，其余全部正确。文件已就绪。

---
