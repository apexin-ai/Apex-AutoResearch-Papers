# ops validate analysis pipeline

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_validate-analysis-pipeline_20260515T025554_result.json`
- **Structured JSON:** [`7a94bd853db81c6aa8b0.json`](../../sessions/7a/7a94bd853db81c6aa8b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。报告如下：

---

## n=500 分析 Pipeline 就绪性报告

### 1. 脚本状态
- **存在**: `analyze_n500_unified.py`, 26,519 bytes, 最后修改 2026-05-15 08:05
- **功能**: 5 项统计分析 — median II(low-high) + bootstrap 95% CI (B=10000), mid-phase null rate, within-importance paired Cohen's d_z (D059), permutation monotonicity test, Bonferroni correction
- **参数**: `--model {deepseek,qwen,all}`, `--dry-run`, `--csv`, `--latex`

### 2. 依赖
- 仅需 `numpy` + `scipy`（无 pandas）
- 脚本已成功运行过，生成了 `analysis_output/n500_unified.json` 和 `.csv` → **依赖已确认满足**

### 3. 数据完整性（16 conditions 中）

**已完成（11/16，有 profiling_results.json）：**

| Model | imp_s015 | imp_s020 | imp_s025 | imp_s030 | rand_s015 | rand_s020 | rand_s025 | rand_s030 |
|-------|----------|----------|----------|----------|-----------|-----------|-----------|-----------|
| DeepSeek | ✅ n=496 | ✅ n=496 | ❌ 空目录 | ❌ **无目录** | ✅ n=496 | ✅ n=496 | ✅ | ❌ 空目录 |
| Qwen | ✅ n=475 | ✅ n=475 | ✅ n=475 | ❌ 空目录 | ✅ n=475 | ✅ n=475 | ✅ n=475 | ❌ 空目录 |

**缺失 5 个 condition：**
- `ds_imp_s025` — 目录存在但空
- `ds_imp_s030` — **目录不存在**（可能未启动）
- `ds_rand_s030` — 目录存在但空
- `qw_imp_s030` — 目录存在但空
- `qw_rand_s030` — 目录存在但空

### 4. 脚本容错
脚本可安全处理缺失数据：`load_problems()` 对不存在的文件返回 `None`，分析代码跳过缺失 condition 并输出 `{"error": "missing data"}`。**不会崩溃。**

### 5. 现有输出质量
`n500_unified.csv` 已包含 10 个 condition 的完整统计结果，d_z 和 imp-vs-rand 对比均正常。数据格式合规。

### 6. 能否直接运行 `python3 analyze_n500_unified.py --csv --latex`？
**可以**，但当前会输出不完整结果（缺 5 个 condition，所有 s030 对比和 ds_imp_s025 会标 "missing data"）。

### 7. 风险
1. **`ds_imp_s030` 无目录** — 该实验可能未启动，需确认
2. **全部 4 个 s030 condition 缺失** — dose-response monotonicity test 无法计算完整梯度，`s025_vs_s030` d_z 对全部缺失
3. PRE_REGISTRATION_C2.md 只列了 8 个 DeepSeek condition，但脚本默认 `--model all` 会同时分析 Qwen（16 conditions）—— 这不是 bug，只是超出预注册范围

---
