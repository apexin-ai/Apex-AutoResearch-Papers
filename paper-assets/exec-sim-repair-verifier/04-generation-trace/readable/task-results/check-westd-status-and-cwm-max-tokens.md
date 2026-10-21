# check westd status and cwm max tokens

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-status-and-cwm-max-tokens_20260514T171919_result.json`
- **Structured JSON:** [`d5521d0540cf1a140bdd.json`](../../sessions/d5/d5521d0540cf1a140bdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## 汇总

### Part 1: 4 张卡状态

| GPU | 任务 | PID | 存活 | 显存 | GPU利用率 | 进度 | 关键指标 |
|-----|------|-----|------|------|-----------|------|----------|
| cuda:0 | CWM seed123 eval | 195531 | ✅ 运行16h+ | 13.0/32.6 GB | 90% | **9168/9784** (93.7%) | running_acc=**59.0%** |
| cuda:1 | CWM v12 eval | 195668 | ✅ 运行16h+ | 13.0/32.6 GB | 88% | **9280/9784** (94.8%) | running_acc=**57.9%** |
| cuda:2 | CWM 8B training | 245775 | ✅ 运行2h51m | 21.2/32.6 GB | 90% | **step 1637/6633** (24.7%) | loss=0.2796, eval_loss=0.374 |
| cuda:3 | CLS 8B seed123 training | 248041 | ✅ 运行2h33m | 26.8/32.6 GB | 98% | **step 3000/6633** (45.2%) | loss=0.369, eval_loss=0.426 |

两个 eval 预计 ~1 小时内完成。两个 training 还需较长时间。

### Part 2: CWM max_new_tokens — **没有问题**

从 `/proc/cmdline` 确认两个 CWM eval 的实际启动参数：

- **PID 195531** (seed123): `--max_new_tokens 1024`
- **PID 195668** (v12): `--max_new_tokens 1024`

**`max_new_tokens=1024`，不是 64。** v10 的问题已在当前 eval 中修复，当前结果可信。

CWM seed123 的 59.0% 和 CWM v12 的 57.9% 是在 1024 tokens 下的真实准确率，不存在 unparseable 导致的低估问题。

---
