# check llama3 auc verification

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_llama3_auc_verification_20260522T153327_result.json`
- **Structured JSON:** [`8afc1e145143b097f842.json`](../../sessions/8a/8afc1e145143b097f842.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。

## 报告

### 1. Table 20 的 0.949/0.877 来源

**文件**: `results/cross_scale_llama3_8b_003/summary.json` → `consecutive_binary`
- d0v1 auc = 0.9494 → 四舍五入 0.949 ✓
- d1v2 auc = 0.8768 → 四舍五入 0.877 ✓
- d2v3 auc = 0.7706 → 0.771 ✓
- d3v4 auc = 0.716 ✓
- d4v5 auc = 0.6183 → 0.618 ✓

### 2. Table 21 的 0.965/0.874 来源

**在服务器上找不到任何对应的源数据文件。** 搜索范围覆盖了：
- 所有 `results/` 下的 JSON 文件
- 所有 llama 相关日志 (pipeline.log, pipeline_002.log, pipeline_003.log, pipeline_tmux.log, base_pipeline.log)
- 所有 `.py`, `.csv`, `.txt`, `.sh` 文件
- 本地 artifacts 目录

0.965 仅出现在 `paper/section_appendix.tex:446` (Table 21 本身) 和编译产物 `main.txt`。artifacts 中的 0.965 是 dream report 中 binoculars 实验的虚构数据，无关。

### 3. 差异分析

| 指标 | Table 20 | Table 21 | 003 原始数据 | 匹配情况 |
|------|----------|----------|-------------|---------|
| d0v1 | 0.949 | **0.965** | 0.9494 | Table 20 正确，Table 21 错误 |
| d1v2 | 0.877 | **0.874** | 0.8768 | Table 20 正确，Table 21 错误 |
| d2v3 | 0.771 | 0.771 | 0.7706 | 两表一致 |
| d3v4 | 0.716 | 0.716 | 0.716 | 两表一致 |
| d4v5 | 0.618 | 0.618 | 0.6183 | 两表一致 |

Table 21 的 Base 行（0.918/0.794/0.682/0.730/0.595）与 `results/cross_scale_llama3_base/summary.json` 完全匹配，无问题。

排除了其他 run 的可能性：pipeline run 001 和 002 都在 depth-1 LoRA 训练时 JSON 解析错误崩溃，从未到达评估阶段，结果目录为空。

### 4. 结论

**Table 21 Instruct 行的 d0v1=0.965 和 d1v2=0.874 是无源数据支撑的错误值**，可能是手动填写时的笔误。正确值应与 Table 20 一致：d0v1=0.949, d1v2=0.877（来自 `cross_scale_llama3_8b_003/summary.json` 的 `consecutive_binary` 指标）。

---
