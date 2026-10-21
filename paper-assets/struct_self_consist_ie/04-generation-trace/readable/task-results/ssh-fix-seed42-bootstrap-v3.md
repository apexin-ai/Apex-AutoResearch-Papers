# ssh fix seed42 bootstrap v3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-seed42-bootstrap-v3_20260520T054413_result.json`
- **Structured JSON:** [`d4b080066a71c7a8e8dd.json`](../../sessions/d4/d4b080066a71c7a8e8dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

**1. 服务器确认**: autodl-5090-c (`autodl-container-jb1uyxxe0t-1a1cc6c5`)

**2. Bootstrap Construction Test 结果** (B=10,000):

| 指标 | 值 |
|------|-----|
| Greedy F1 | **0.7851** |
| Construction F1 | 0.7811 |
| Observed diff | **−0.0040 (−0.40pp)** |
| 95% CI | [−0.0053, −0.0026] |
| p-value (one-sided) | **1.0** |
| Cohen's d | **−0.0319** |
| Significant (p<0.05) | **NO** |

**3. Greedy F1 校验**: 0.7851 ≈ 0.784（±0.002 范围内） ✓

**4. Construction Δ 校验**: −0.40pp, not significant — 与 seed42 signal report 一致 ✓

**5. 输出文件**: `/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/fewnerd_paired_bootstrap_result.json`

注：任务指定的脚本路径 `artifacts/bootstrap_construction.py` 不存在，实际路径是 `code/pipeline/bootstrap_construction.py`。

---
