# infra urgent 5gpu status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_urgent-5gpu-status-check_20260518T211845_result.json`
- **Structured JSON:** [`a07cde660805c05abf5d.json`](../../sessions/a0/a07cde660805c05abf5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态汇总

### seetacloud-westd-4x5090

| GPU | 实验 | PID | 状态 | 进度 | 速度 | 预估 ETA |
|-----|------|-----|------|------|------|----------|
| **0** | CLS v5 ckpt-2105 eval | 761181 | **已完成** (EXIT_CODE=0) | 9784/9784 | — | — |
| **1** | CWM s42 e2 @4096 | 662946 | 运行中 (1d 5h) | 8313/9784 (85%) | ~4.8/min | **~5h** |
| **2** | D131 CWM s42 e3 @2048 | 734440 | 运行中 (7h 28m) | 2449/9784 (25%) | ~5.0/min (~12s/sample) | **~25h** |
| **3** | CWM s123 e2 @4096 | 668680 | 运行中 (1d 4h) | 7842/9784 (80%) | ~4.7/min | **~7h** |

### home-1x5090

| GPU | 实验 | PID | 状态 | 进度 | 速度 | 预估 ETA |
|-----|------|-----|------|------|------|----------|
| **0** | D133 CWM s42 e2 @2048 resume | 4187955 | 运行中 (27min) | 3236/9784 (33%) | ~7.4/min (~8s/sample) | **~15h** |

D133 已 resume 3039 条旧结果，新推理 197 条，running_acc=64.5%。

### 关键发现

1. **GPU 0 (seetacloud) 空闲可用** — CLS v5 eval 已正常结束，最终结果：
   - fail: P=76.9% R=51.0% F1=61.4%
   - pass: P=83.9% R=94.3% F1=88.8%
   
2. GPU 1/2/3 (seetacloud) 和 home GPU 0 均正常工作，无异常。

3. GPU 2 (@2048) 比 GPU 1/3 (@4096) 每 sample 更快，但总量相同，还需约 25h 才能完成。

---
