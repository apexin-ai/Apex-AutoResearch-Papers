# ops check all gpu progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-all-gpu-progress_20260522T010356_result.json`
- **Structured JSON:** [`652570ebb03991e7460b.json`](../../sessions/65/652570ebb03991e7460b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4 GPU 实验状态总览

| GPU | 实验 | PID | 进度 | 状态 |
|-----|------|-----|------|------|
| 0 | Qwen s123 eval | 94100 | 2516/9784 (25.7%) | RUNNING |
| 1 | **DS s456 eval** | 63490 | **8896/9784 (90.9%)** | RUNNING |
| 2 | DS s123 v2 eval | 100824 | 1384/9784 (14.1%) | RUNNING (自动接替已完成的 train) |
| 3 | Qwen s456 eval | 96730 | 2032/9784 (20.8%) | RUNNING |

GPU 利用率：0=82%, 1=85%, 2=85%, 3=76%，全部满载。

---

### DS s456 eval partial analysis (8896 samples, 91% done)

| 指标 | DS s456 | DS s42 baseline | Δ |
|------|---------|-----------------|---|
| Overall accuracy | **56.22%** | 61.49% | **-5.3pp** |
| Unparseable rate | 57.1% | 62.5% | -5.4pp (s456 解析更好) |
| Parseable-only acc | **32.32%** | 38.7% | **-6.4pp** |
| F1-macro | 50.67% | — | — |
| Fail recall | 42.08% | — | — |

### Scenario 判断：**Scenario C（中间偏 B）**

s456 与 s42 差距 5-6pp，方向一致地**更差**。具体表现：
- s456 的 unparseable rate 反而更低（57.1% vs 62.5%），说明 parse 更好
- 但 parseable predictions 准确率大幅下降（32.3% vs 38.7%，Δ=-6.4pp）
- 综合 overall accuracy 下降 5.3pp

这表明 **CWM 在 DeepSeek 上高 variance，seed 间波动显著**。s456 模型学到了更好的格式遵从（fewer unparseable），但判别能力更差。

---

### 其他 eval 的 partial snapshot

| 实验 | Samples | Overall acc | Unparseable | Parseable-only acc |
|------|---------|-------------|-------------|-------------------|
| Qwen s456 | 2032 | **67.52%** | 60.2% | **48.95%** |
| Qwen s123 | 2516 | **67.37%** | 62.9% | **47.16%** |
| DS s123 v2 | 1384 | 56.86% | 51.1% | 42.39% |

Qwen 两个 seed 高度一致（67.4% ± 0.1pp），**远好于 DeepSeek 全系列**。DS s123 v2 early signal 与 s456 接近（~56-57% acc），但 unparseable rate 更低（51.1%）、parseable accuracy 更好（42.4%）。

---
