# audit gam keff data loading

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gam-keff-data-loading_20260523T173750_result.json`
- **Structured JSON:** [`0e3536e48c59c7a51d05.json`](../../sessions/0e/0e3536e48c59c7a51d05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心发现：

**K_eff 值完全一致**，两个脚本从同一 JSON 文件读取相同字段。差异根因是 **ASR 计算的 error handling 不同**：

| | 原始 GAM 脚本 | Bootstrap 脚本 |
|---|---|---|
| Error 处理 | `.get("winner", "tie")` → error 当作 tie | `_is_valid_score()` → 跳过 error |
| 结果 | 6:6 split (targeted +, shared-bias -) | 12/12 全部正向 |

**6:6 split 是 bug 产物**。3 个 frontier API 模型 (gemini-3.5-flash 17.7%、gemini-3.1-pro-preview 8.0%、gpt-5.5 3.1%) 有大量 error scores。将 error 当作 "tie" 虚增了这些高 K_eff 模型的 ASR，导致 shared-bias attacks 的 GAM partial dependence 被人为翻转为负向。

正确处理 error 后（跳过无效样本），全部 12 个 condition 的 K_eff 效果均为正向。V1 的 shared-bias 负向 slope 仅 -0.15 ~ -2.9，而正确计算的 slope 为 +14 ~ +39，说明原来的"负向"极其脆弱。

报告已保存到 `artifacts/diagnostic_gam_keff_mismatch.txt`。

---
