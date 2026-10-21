# infra scp and pipeline

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_scp-and-pipeline_20260522T165558_result.json`
- **Structured JSON:** [`d34375ab1fe088c92909.json`](../../sessions/d3/d34375ab1fe088c92909.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 已完成。汇报：

1. **SCP 传输**：126 个 API 模型 scoring 文件全部传输成功（9 模型 × 14 条件）
2. **旧文件清理**：删除 9 个过时的 `gpt-4o__*.json` 文件
3. **最终文件数**：126 个文件，覆盖 9 个 API 模型：claude-3-haiku, claude-opus-4-6, claude-sonnet-4-6, gemini-3.1-pro-preview, gemini-3.5-flash, gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, gpt-5.5
4. **Pipeline 状态**：已完成全部 4 步（Step 3 MI Matrix → Confound Diagnosis → Step 4 Panel Regression → Step 5 Random Fault）
   - 中途修复了 pingouin 0.6.1 的列名变更（`p-val` → `p_val`），本地和远程都已同步修复
   - 产出文件：`mi_matrix_15models.json`（352KB）、`confound_diagnosis.json`、`confound_scatter.png`、`step4_regression_results.json`（33KB）、`step5_random_fault_results.json`（17KB）
   - K_eff 在 Random Fault 模型下 12/12 条件显著，diversity benefit 在 adaptive attack 下被削弱

---
