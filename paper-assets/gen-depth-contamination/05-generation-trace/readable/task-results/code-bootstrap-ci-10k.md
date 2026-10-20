# code bootstrap ci 10k

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bootstrap_ci_10k_20260522T144938_result.json`
- **Structured JSON:** [`c3dc4f2418e0abdeaef7.json`](../../sessions/c3/c3dc4f2418e0abdeaef7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

## Bootstrap CI 结果

| Case | AUC(1v2) | 95% CI | 99.5% CI (Bonferroni) | Lower > θ=0.60 | Perm p-value | Verdict |
|------|----------|--------|----------------------|----------------|--------------|---------|
| **Qwen-cont 10K** | 0.6346 | [0.6282, 0.6409] | [0.6255, 0.6436] | **0.6255 > 0.60** | 0.0001 | **PASS** |
| **Pythia-1.4B 10K** | 0.6175 | [0.6108, 0.6242] | [0.6078, 0.6273] | **0.6078 > 0.60** | 0.0001 | **PASS** |

两个 case 的 Bonferroni 修正后 99.5% CI lower bound 均超过 θ=0.60，permutation p-value 均为 0.0001（即 10001 次中仅 1 次达到 observed AUC）。

JSON 输出文件：
- 主脚本输出：`/root/autodl-tmp/gen-depth-contamination/artifacts/borderline_bootstrap_ci.json`（95% CI + permutation）
- Bonferroni 补充：`/tmp/bonferroni_results.json`（99.5% CI）

---
