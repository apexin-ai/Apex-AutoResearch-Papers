# run 3B rrf then pooled irt

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_3B_rrf_then_pooled_irt_20260516T104948_result.json`
- **Structured JSON:** [`daa6b293faab9884254a.json`](../../sessions/da/daa6b293faab9884254a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

---

## 执行结果

### Part 1: RRF 全量聚合
- **23 respondents**: 0.5B×8 + 1.5B×8 + 3B×7 (s42+s123, alpha16 blocklist 已过滤)
- 3 benchmarks 覆盖: MMLU 23, GSM8K 20, ARC 20 (3个 s123 目录的 gsm8k/arc 信号仍在计算中)
- 修复命名不匹配: 添加 `d000_s42_a32` / `d005_s42_a32` aliases
- 输出: `/root/autodl-tmp/exp003/rrf_all_scales/`

### Part 2: Pooled IRT (2PL+γ)

| Bench | N | γ̂ | 95% CI | R̂ | ESS | PPP | rawMAE | calMAE | ΔMAE | Pass? |
|---|---|---|---|---|---|---|---|---|---|---|
| MMLU | 15 | 0.517 | [-0.55, 1.60] | 1.007 | 1402 | **0.234** | 0.016 | 0.006 | +0.010 | **✓** |
| GSM8K | 20 | 0.172 | [-0.29, 0.64] | 1.007 | 1388 | **0.343** | 0.163 | 0.008 | +0.155 | **✓** |
| ARC | 13 | 0.486 | [-0.26, 1.25] | 1.007 | 1670 | **0.027** | 0.034 | 0.015 | +0.018 | ✗ PPP |

### vs 0.5B+1.5B baseline
- **ARC 大幅改善**: PPP 0.000→0.027, ΔMAE -0.064→+0.018 (校准从恶化变为改善)
- **GSM8K 校准增强**: ΔMAE 0.113→0.155 (+37%)
- **MMLU 新增可用**: 此前 0.5B+1.5B run 未包含 MMLU

所有 γ̂ CI 包含 0 — 需要更多 respondents (≥16 per benchmark) 来达到统计显著性。Registry `exp_006_pooled_irt_all_scales` 已更新。

---
