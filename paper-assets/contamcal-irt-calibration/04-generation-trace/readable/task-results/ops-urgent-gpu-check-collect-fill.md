# ops urgent gpu check collect fill

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-gpu-check-collect-fill_20260521T055930_result.json`
- **Structured JSON:** [`dc54daa71c03166673b3.json`](../../sessions/dc/dc54daa71c03166673b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## GPU 状态

| 服务器 | GPU | 状态 |
|--------|-----|------|
| westd-29999 | cuda:0 | **RUNNING** — d050 ARC eval (PID 481293) |
| westd-29999 | cuda:1 | **RUNNING** — d100 GSM8K eval (PID 481792) |
| westd-29999 | cuda:2 | 空闲 |
| westd-29999 | cuda:3 | 空闲 |
| cqa1-21977 | cuda:0 | 空闲（无 Qwen-14B 模型，不可用于 14B eval） |

## 已完成 Eval 结果

| Benchmark | Dosage | Accuracy | Correct/Total |
|-----------|--------|----------|---------------|
| **GSM8K** | d000 (clean) | **74.98%** | 989/1319 |
| **GSM8K** | d005 | **71.19%** | 939/1319 |
| **GSM8K** | d025 | **79.30%** | 1046/1319 |
| **MMLU** | d025 | **65.05%** | 9135/14042 |
| **MMLU** | d050 | **55.33%** | 7770/14042 |
| **MMLU** | d100 | **43.85%** | 6157/14042 |
| **ARC** | d100 | **81.06%** | 950/1172 |

GSM8K 跨 benchmark 效应非线性：d005 下降 3.8pp，d025 反弹至 +4.3pp（高于 baseline）。

## 新启动任务

1. **d050 ARC eval** → cuda:0, PID 481293（关键路径：补齐 ARC s0 dose-response 曲线）
2. **d100 GSM8K eval** → cuda:1, PID 481792（补齐 GSM8K s0 完整 5-dosage 数据）

## Registry 更新

- 5 个已完成实验 → DONE (success) + metrics
- 2 个新实验 → RUNNING

## 剩余空闲

westd cuda:2 和 cuda:3 空闲，可分配额外任务。cqa1 无 14B 模型无法跑 eval。

---
