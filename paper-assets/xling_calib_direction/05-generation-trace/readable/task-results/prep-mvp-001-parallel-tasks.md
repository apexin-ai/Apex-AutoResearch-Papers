# prep mvp 001 parallel tasks

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_mvp_001_parallel_tasks_20260520T150620_result.json`
- **Structured JSON:** [`5722170057fa6107c224.json`](../../sessions/57/5722170057fa6107c224.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MMLU 也下载完成了！全部 3 项任务完成。汇总结果：

---

## Task 1: 数据集预下载 ✅

### cais/mmlu (config: `all`)
| Split | Samples | Columns |
|-------|---------|---------|
| test | 14,042 | question, subject, choices, answer |
| validation | 1,531 | 同上 |
| dev | 285 | 同上 |
| auxiliary_train | 99,842 | 同上 |

### CohereForAI/Global-MMLU
- **Config 命名**: 直接用语言代码（如 `zh`, `ar`, `hi`, `sw`, `ko`），共 42 种语言可用
- **所有 5 种语言均为**: test 14,042 + dev 285
- **Columns**: sample_id, subject, subject_category, question, **option_a, option_b, option_c, option_d**, answer, required_knowledge, time_sensitive, reference, culture, region, country, cultural_sensitivity_label, is_annotated

### 关键差异（脚本调试需注意）
1. **Answer format**: MMLU 用 `choices` (list) + `answer` (int index)；GlobalMMLU 用 `option_a/b/c/d` (str) + `answer` (str letter)
2. **Splits**: MMLU 有 4 个 split (含 validation 和 auxiliary_train)；GlobalMMLU 只有 test + dev
3. **下载方式**: 必须设 `HF_ENDPOINT=https://hf-mirror.com` 且**不启用** `source /etc/network_turbo`（network_turbo 代理导致 HF SSL 超时）

---

## Task 2: 脚本 Dry-run ✅

| 脚本 | 状态 | 说明 |
|------|------|------|
| train_probe.py | ✅ PASS | sklearn FutureWarning (penalty deprecation)，不影响运行 |
| transfer_eval.py | ✅ PASS | 输出 transfer_results.csv |
| analyze_results.py | ✅ PASS | 输出 auroc_by_layer.png, method_comparison.png, summary.txt |

测试数据已清理。无 import error 或 runtime error。

---

## Task 3: 磁盘空间 ✅

| 位置 | 总量 | 已用 | 可用 |
|------|------|------|------|
| 根分区 (/) | 30G | 942M (4%) | ~29G |
| 数据盘 (/dev/sda2) | 879G | 402G (49%) | 433G |
| /root/autodl-tmp/ | — | 8.1G | — |

预估需求 ~22GB，**空间充足**。

---

## 模型下载状态
Qwen2.5-7B-Instruct (ModelScope) ~49%，预计还需 ~40 分钟。

---
