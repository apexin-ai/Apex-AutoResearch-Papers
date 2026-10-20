# code exp a2 humaneval sc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_a2_humaneval_sc_20260520T181633_result.json`
- **Structured JSON:** [`d99389bdb7e949cf139a.json`](../../sessions/d9/d99389bdb7e949cf139a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已完成，registry 已更新。产出报告：

---

**代码路径**: `artifacts/experiments/humaneval_sc/run_humaneval_sc.py`

**依赖列表**:
- `openai` (OpenAI SDK, 用于 API 调用)
- `datasets` (HuggingFace, 加载 HumanEval)
- `numpy`

安装: `pip install openai datasets numpy`

**Model ID**: `openai/gpt-5.5` (OpenRouter 确认, 2026-04-24 发布)

**API cost 估算**:
- 164 problems × (8 stochastic + 1 greedy) = 1476 次 completion
- 输入 ~300 tokens/problem × 1476 ≈ 443K input tokens → $2.2
- 输出 ~200 tokens/completion × 1476 ≈ 295K output tokens → $8.9
- **总计约 $11**

**预计时长**: ~30-60 min（取决于 API rate limit 和 test execution）

**脚本功能**:
- 增量 checkpoint（中断可恢复）
- `--test_api` 先测一个 problem 验证连通性
- 安全沙箱执行（subprocess + 30s timeout）
- 输出: `summary.json`（metrics + diagnostics）, `all_results.jsonl`（逐题详情）

**评估指标**: greedy pass rate, pass@1, pass@8, MV pass rate, random pass rate, oracle pass rate

**诊断指标**: degeneracy rate, majority agreement rate, majority correct rate, all-pass/all-fail/mixed distribution, unique solutions diversity

---
