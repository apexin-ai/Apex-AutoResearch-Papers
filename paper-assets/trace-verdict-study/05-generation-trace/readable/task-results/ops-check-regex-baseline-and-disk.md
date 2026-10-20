# ops check regex baseline and disk

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_regex_baseline_and_disk_20260517T125800_result.json`
- **Structured JSON:** [`29bfd9f5ada8dba91fcf.json`](../../sessions/29/29bfd9f5ada8dba91fcf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. Regex Baseline 已存在

文件位置：`/root/trace-verdict-study/analysis/regex_baseline_results.json`

测试集：**exception_only_test.jsonl**（1190 samples，851 pass / 339 fail）

#### 核心 Metrics

| Baseline | Accuracy | Fail F1 | Pass F1 | Macro F1 |
|----------|----------|---------|---------|----------|
| B1_ERROR_tag | 93.45% | 0.8734 | 0.9558 | 0.9146 |
| B2_Traceback | 71.51% | 0 | 0.8339 | 0.4170 |
| B3_any_keyword | 93.45% | 0.8734 | 0.9558 | 0.9146 |
| **B4_exception_regex** | **93.61%** | 0.8762 | 0.9570 | 0.9166 |
| **B5_no_exception_data_heuristic** | **99.33%** | 0.9883 | 0.9953 | 0.9918 |
| B6_error_count_t1 | 93.45% | 0.8734 | 0.9558 | 0.9146 |
| B6_error_count_t2 | 92.02% | — | — | — |
| B6_error_count_t3 | 85.13% | 0.6495 | 0.9056 | 0.7776 |
| **SFT (ours)** | **99.83%** | 0.9971 | 0.9988 | 0.9979 |

#### 跨格式对比

| Format | SFT Acc | Best Regex Acc | Gap |
|--------|---------|---------------|-----|
| exception_only | 99.83% | 93.61% (standard) / 99.33% (artifact heuristic) | 6.2pp / 0.5pp |
| vota | 99.41% | 75.55% | 23.9pp |
| full_trace | 81.76% | 77.39% | 4.4pp |
| no_trace | 75.13% | 71.51% | 3.6pp |

**结论**：B5 (99.33%) 利用了数据格式 artifact（`[No exception data in trace]` marker），非真实错误检测能力。标准 regex 最高 93.6%，与 SFT 99.83% 有 6.2pp gap。McNemar p=0.041 显著。

---

### 2. 磁盘空间

| 挂载点 | 总容量 | 已用 | 可用 | 使用率 |
|--------|--------|------|------|--------|
| `/` (系统盘) | 30G | 24G | **6.2G** | 80% |
| `/root/autodl-tmp` (数据盘) | 250G | 209G | **42G** | 84% |

主要占用：
- checkpoints: 73G
- data: 767M

---
