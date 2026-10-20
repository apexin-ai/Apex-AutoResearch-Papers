# analysis bf16 qw rand s020

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16_qw_rand_s020_20260514T082247_result.json`
- **Structured JSON:** [`133db54dee80a465fb73.json`](../../sessions/13/133db54dee80a465fb73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bf16_qw_rand_s020 分析结果：**FAIL**（符合预期）

| 指标 | 值 |
|------|-----|
| Phase median II (high) | 0.4739 |
| Phase median II (mid) | 0.8757 |
| Phase median II (low) | 0.4847 |
| Median diff (low − high) | 0.0576 |
| Permutation p-value (B=10000) | **0.352** |
| Cohen's d | 0.247 (small) |
| Bootstrap 95% CI | [−0.139, 0.215]，**包含零** |
| Wilcoxon p | 0.149 |

**判定：FAIL** — permutation p=0.352 远大于 0.05，bootstrap CI 跨零，Cohen's d 仅 small。三相 II 无显著差异，random masking 作为 negative control 有效。

与 DeepSeek random 系列（D029/D030 全 FAIL）一致，与 Qwen importance 系列（D034 全 PASS，s020 Cohen's d=0.549 medium）形成对照。

Registry 已更新：status=DONE, conclusion=negative, metrics 已写入。分析产出保存在服务器 `/root/autodl-tmp/pacs/analysis_output/bf16_qw_rand_s020/analysis_results.json`。

---
