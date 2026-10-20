# infra westd19912 olmo math fix

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd19912_olmo_math_fix_20260521T173859_result.json`
- **Structured JSON:** [`727ec4c7c7c1f694ef60.json`](../../sessions/72/727ec4c7c7c1f694ef60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。汇总如下：

## 执行结果

### GPU 布局
| GPU | 任务 | PID | 状态 |
|-----|------|-----|------|
| 0 | OLMo MATH（新启动） | 57889 | 运行中，400/57600 行 |
| 1 | 空闲 | - | 等待 Yi |
| 2 | 空闲 | - | 等待 Yi |
| 3 | OLMo GSM8K | 52660 | 运行中，47000/57600 行（~82%） |

### OLMo benchmark 进度（exp002_olmo, 目标各 57600 行*）
| Benchmark | 行数 | 状态 |
|-----------|------|------|
| MMLU | 288,000 | 完成 |
| ARC | 288,000 | 完成 |
| HellaSwag | 288,000 | 完成 |
| GSM8K | 47,000 | ~82%，GPU 3 |
| **MATH** | **400** | **已修复启动，GPU 0** |

*MMLU/ARC/HellaSwag 各 288 条件 × 1000 items = 288000；GSM8K/MATH 各 288 条件 × 200 items = 57600

### Yi benchmark 进度
尚未开始。`yi_after_olmo_v2.sh`（PID 58498）等待 OLMo GSM8K + MATH 两个都完成后自动在 4 GPU 上启动 Yi 全部 5 个 benchmark。

### 磁盘清理
ModelScope 临时目录不存在，无需清理。

### 磁盘状态
- 根分区：14G/30G（46%）
- 数据盘：124G/250G（50%）

### 修复措施
1. 杀掉原 `yi_after_olmo.sh`（会跳过 MATH 直接启动 Yi）
2. 在空闲 GPU 0 启动 OLMo MATH 与 GPU 3 的 GSM8K 并行
3. 部署 `yi_after_olmo_v2.sh` 等待两个 OLMo PID 完成后再启动 Yi

---
