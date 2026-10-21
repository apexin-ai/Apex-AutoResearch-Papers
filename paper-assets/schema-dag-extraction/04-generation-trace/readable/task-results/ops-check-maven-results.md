# ops check maven results

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_maven_results_20260519T135138_result.json`
- **Structured JSON:** [`658fd844c956b6457754.json`](../../sessions/65/658fd844c956b6457754.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**实验完整完成。** 5 个 arm 全部跑完，summary.json 包含所有结果。EXIT_CODE=129（SIGHUP，进程被杀但数据已写完）。

### MAVEN SDGD-zero 三臂对比（168 types, 1000 samples, Qwen3-32B-FP8）

| Mode | Precision | Recall | F1 |
|------|-----------|--------|----|
| single_pass | 0.2866 | 0.1618 | **0.2068** |
| sdgd_zero | 0.0911 | 0.1907 | 0.1233 |
| random_batch (avg 3 seeds) | 0.0820 | 0.1769 | 0.1114 |

- SDGD vs SP: F1 -0.084, recall +0.029, precision -0.196
- SDGD vs Random Batch: F1 +0.012（SDGD 略优于随机分批）
- SDGD merge: 5242 raw → 5212 merged（去重极少，tau=0.319）

### GPU 状态
RTX PRO 6000 Black (98GB) — **完全空闲**，0MB 显存占用，无运行进程。

### 结论
不需要重跑。所有 5 个 arm（single_pass + sdgd_zero + random_batch×3 seeds）数据完整。MAVEN 上 SDGD-zero 的表现不如 single_pass（F1 差 8.4 个点），但比 random batch 略好 1.2 个点，说明 DAG 分批有微弱优势但不足以弥补 168 types 分批带来的 precision 损失。

---
