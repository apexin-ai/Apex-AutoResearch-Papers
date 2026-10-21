# check westd full gpu status and eval results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-full-gpu-status-and-eval-results_20260514T212843_result.json`
- **Structured JSON:** [`2727495a6f92629d7e9b.json`](../../sessions/27/2727495a6f92629d7e9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结如下：

---

## Westd 全面状态报告

### 1. GPU 全景

| GPU | PID | 任务 | 显存 | 利用率 |
|-----|-----|------|------|--------|
| cuda:0 | 294727 | **ckpt-600 test@8192 eval** (刚提交) | 17.4G/32.6G | 99% |
| cuda:1 | 291117 | seed123 ckpt3000 val@8192 eval (**已完成**) | 19.2G/32.6G | 91% |
| cuda:2 | 266816 | CWM 8B 训练 (step 1621/9335, 17%) | 30.7G/32.6G | 97% |
| cuda:3 | 266449 | CLS 8B seed123 训练 v3 (step 4122/6633, 62%, loss=0.37) | 30.9G/32.6G | 37% |

### 2. Eval 状态

| Eval | 状态 | 备注 |
|------|------|------|
| cls8b-s42-ckpt400-test8192-eval | **DONE** ✅ | 结果已收集 |
| cls8b-seed123-ckpt3000-val8192-eval | **DONE** ✅ | 结果已收集 |
| cls4b-seed123-ckpt800-val5120-eval | **NOT_ON_WESTD** | 不在此服务器 |
| cls8b-seed123-ckpt3000-val-eval (旧) | **DONE/killed** ✅ | registry 已更新 |

### 3. 完整 Metrics

**cls8b-s42-ckpt400-test8192-eval** (test, 9784 samples):
- Accuracy: **84.79%** (+11.84pp vs majority 72.96%)
- F1 macro: **81.18%**
- F1_fail: 72.93% (P=70.3%, R=75.7%)
- F1_pass: 89.43% (P=90.7%, R=88.2%)
- Unparseable: 0

**cls8b-seed123-ckpt3000-val8192-eval** (val, 9335 samples):
- Accuracy: **88.69%** (+12.8pp vs majority 75.9%)
- F1 macro: **81.73%**
- F1_fail: 70.5% (P=95.2%, R=55.9%)
- F1_pass: 93.0% (P=87.6%, R=99.1%)
- Unparseable: 9

### 4. ckpt-600 test@8192 提交确认
- PID: 294727, tmux: `cls8b-s42-ckpt600-test8192-eval`
- 已开始运行 (300/9784 at 05:41)
- Registry 已创建，parent=repo-level-cls-8b-conda

### 5. 旧 eval registry 更新确认
- cls8b-seed123-ckpt3000-val-eval → status=DONE, conclusion=killed, notes="进程已确认死亡。缺少 --max_seq_length 参数（默认 2048），结果不可比。已被 cls8b-seed123-ckpt3000-val8192-eval 替代。"

---
