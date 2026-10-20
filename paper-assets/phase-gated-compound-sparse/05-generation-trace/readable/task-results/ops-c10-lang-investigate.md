# ops c10 lang investigate

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c10_lang_investigate_20260516T073734_result.json`
- **Structured JSON:** [`0b371edd9a811352a1f7.json`](../../sessions/0b/0b371edd9a811352a1f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1. c10_lang_s020_s025 状态：**已完成**

尽管日志最后显示 `Terminated / EXIT_CODE=143`（进程在 [18/50] 时被 SIGTERM），但**结果文件完整**：

**输出文件：**
- `/root/autodl-tmp/pacs/results_c10_lang_s020_s025.json` (1242 行)
- `/root/autodl-tmp/pacs/results_c10_lang_s020_s025_raw_text.json` (405 行)

**结果摘要：**

| 条件 | n | accuracy | switch_rate | switch_count | mean_cn_ratio | cn_acc | en_acc |
|------|---|----------|-------------|--------------|---------------|--------|--------|
| s020 | 50 | 0.26 | 0.14 | 7 | 0.066 | 0.333 | 0.250 |
| s025 | 50 | 0.10 | 0.32 | 16 | 0.152 | 0.200 | 0.057 |

- 总耗时 11,680.6s (~3.2h)
- 两个条件各 50 样本全部完成，数据完整
- 终止信号可能来自实验完成后的清理/看门进程

**关键发现：** 更高稀疏度 (s025) 导致更多语言切换 (32% vs 14%) 和更低准确率 (10% vs 26%)。

---

## 2. GPQA 就绪情况

**数据：就绪**
- `/root/autodl-tmp/pacs/data/gpqa_diamond.json` 存在 (1585 行)
- 格式正确：`{id, problem, answer}` 多选题 (A/B/C/D)，已内嵌 "Think step by step" 提示

**Profiling 脚本：未就绪**
- `test_dsr1_gpqa.py` 是探索性测试脚本（CPU 推理，仅 3 样本，max_new_tokens=200），不适合正式 profiling
- `profiling/run_profiling.py`（主 profiling 脚本）**不支持 GPQA**——无 gpqa 相关引用
- `scripts/` 目录下无 GPQA profiling 脚本
- `run_profiling_single.py` 不存在

**需要：** 编写 GPQA profiling 脚本或扩展现有 `run_profiling.py` 以支持 GPQA 数据集。

---
