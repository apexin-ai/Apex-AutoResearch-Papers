# ops check running experiments

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-running-experiments_20260516T021408_result.json`
- **Structured JSON:** [`88bf18cdd48a41cf38ed.json`](../../sessions/88/88bf18cdd48a41cf38ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。状态报告：

---

## 实验状态报告 (2026-05-16 10:14 UTC)

### 1. cwm8b-ckpt400-test-eval-v3 — **RUNNING** ✓
- **PID**: 443221, GPU 3 (21.1GB, 89% util), 运行 1h27m
- **进度**: 6024/9784 (61.6%), 已处理 737 new + 5287 resumed
- **running_acc**: ~64.7%
- **输出文件**: `results_incremental.jsonl` 6032 行
- **预计剩余**: ~55 min（按 ~1 min/8 samples）

### 2. cls8b-s42-resume-ckpt3600-test-v2 — **已完成** ✓
- **退出码**: 0, 完成于 01:40:47 UTC
- **结果**:
  - Accuracy: **84.48%** (majority baseline 73.0%, +11.5pp)
  - F1 macro: **78.17%**
  - F1 fail: 66.4% (P=80.1%, R=56.8%)
  - F1 pass: 89.9% (P=85.5%, R=94.8%)
- **输出已保存**: `/root/autodl-tmp/eval_results/cls8b_s42_resume_ckpt3600_test_v2/`

### 3. cwm8b-ckpt400-test-eval-shard2 — **RUNNING** ✓
- **PID**: 448100, GPU 1 (21.1GB, 89% util), 运行 ~49min
- **进度**: 424 行已写入 `results_incremental.jsonl`（start_idx=7680, 总量 9784-7680=2104）
- **完成度**: ~424/2104 ≈ 20%
- **预计剩余**: ~3h

### 4. cls8b-seed123-ckpt3000-mutation — **已完成** ✓
- **PID 447483 已退出**, 无 agent-ml exit 文件但输出完整
- **结果**:
  - Overall accuracy: **85.60%** (+12.6pp vs majority)
  - F1 macro: **78.38%**
  - Mutation breakdown:
    - gold: 99.6% (4613/4633)
    - operator_swap: 82.6% (2773/3357)
    - off_by_one: 79.2% (145/183)
    - return_value: 66.4% (373/562)
    - boundary_removal: 44.9% (471/1049)
- **输出已保存**: `/root/autodl-tmp/eval_results/cls8b_seed123_ckpt3000_test_mutation/`

### GPU 占用
| GPU | 显存 | 利用率 | 进程 |
|-----|------|--------|------|
| 0 | 0MB | 0% | 空闲 |
| 1 | 21.1GB | 89% | shard2 eval |
| 2 | 0MB | 0% | 空闲 |
| 3 | 21.1GB | 89% | cwm8b-ckpt400-test-eval-v3 |

**GPU 0 和 GPU 2 空闲，可用于新任务。**

---
