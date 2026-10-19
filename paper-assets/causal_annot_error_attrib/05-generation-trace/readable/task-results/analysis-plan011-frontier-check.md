# analysis plan011 frontier check

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan011_frontier_check_20260521T110109_result.json`
- **Structured JSON:** [`31e9df71f7933244fe8b.json`](../../sessions/31/31e9df71f7933244fe8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Plan011 Frontier Annotations 状态总结

### 根因
API 端点 `http://47.94.22.126` **余额耗尽 (HTTP 402)**，导致大量标注失败。humaid 最先跑、完成度最高；vast 跑到一半断了；civil_comments 几乎全军覆没。

### 可用数据一览（parse rate ≥ 80%）

| Dataset | Model | 可用 prompt configs | 备注 |
|---------|-------|-------------------|------|
| **humaid** | llama4 | zero/3/5-shot ✓ | 100%/99.9%/98.1% |
| **humaid** | deepseek | zero/3-shot ✓ | 100%/89.7%（5-shot 82.5% 勉强可用）|
| **humaid** | qwen3 | zero/3-shot ✓ | 100%/94.9%（5-shot 全 402）|
| **vast** | llama4 | zero/3-shot ✓ | 99.7%/100%（5-shot 仅 23%）|
| **vast** | qwen2.5-7b | zero/3/5-shot ✓ | 99.9%~100%（本地模型，后补）|
| **civil_comments** | qwen2.5-7b | zero/3/5-shot ✓ | 100%（本地模型，后补）|

**vast** 的 deepseek/qwen3 全部 402 失败。**civil_comments** 的 llama4/deepseek/qwen3 全部 402 失败。**humaid 缺 qwen2.5-7b**。

### 统计
- 理论组合：3 datasets × 4 models × 3 prompts = **36 configs**
- 可用（≥80%）：**15 configs**（42%）
- 完全失败：**18 configs**（全 402）
- 部分失败：**3 configs**

### 产出文件
远程 `/home/sonny/causal_annot_error_attrib/results/` 下有 JSONL + confusion matrix (.npz)。本地 `artifacts/plan011_frontier_annotations/` 有脚本和 STATUS.md（记录了 TUM API key 401 的 blocker，但实际跑通了部分任务用的是另一个端点）。

### 恢复建议
需要充值 `47.94.22.126` API 余额或切换到新端点，重跑 vast (deepseek/qwen3 全部, llama4 5-shot) + civil_comments (llama4/deepseek/qwen3 全部) + humaid (qwen2.5-7b)，共约 21 configs。

---
