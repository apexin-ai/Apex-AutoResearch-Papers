# diag westd41312 cuda23 eval retry

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd41312_cuda23_eval_retry_20260520T092740_result.json`
- **Structured JSON:** [`11eeaa591fa2498941cd.json`](../../sessions/11/11eeaa591fa2498941cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## westd-41312 诊断报告

### 1. 服务器健康状态

| 资源 | 状态 |
|------|------|
| GPU 0 | RTX PRO 6000 Blackwell, 61.7/97.9 GB, 100% — `uniform_1_7b_seed42_v5` |
| GPU 1 | RTX PRO 6000 Blackwell, 61.7/97.9 GB, 100% — `adaptive_1_7b_seed42_v5` |
| GPU 2 | 0/97.9 GB, 0% — **空闲** |
| GPU 3 | 0/97.9 GB, 0% — **空闲** |
| 根分区 | 9.5G/30G (32%) |
| autodl-tmp | 94G/250G (38%) |

服务器健康，无异常。

### 2. 1.7B 训练进度

| 任务 | GPU | Step | 进度 | 速度 | 预估剩余 |
|------|-----|------|------|------|----------|
| uniform_1_7b_seed42_v5 | cuda:0 | 729/6103 | 12% | 2.86s/step | ~4h17m |
| adaptive_1_7b_seed42_v5 | cuda:1 | 693/6103 | 11% | ~3.0s/step | ~4h30m |

两个任务都在 16:52 启动（约35分钟前），参数均为 rho=0.4, tau=0.8, Qwen3-1.7B, 200M tokens。预计今晚 ~21:30 完成。

### 3. rho=0.6 tau=0.8 Checkpoint 清单

全部为 0.6B 模型（Qwen3-0.6B）：

**已有 checkpoint + 已评估：**
- `contamination_60_adaptive_seed456` — adaptive, tau=0.8, **ppl=17.74** ✓
- `contamination_60_uniform_seed456` — uniform, tau=0.8 ✓
- `contamination_60_ess_only_seed123/456` — ess_only, **ppl=17.76** ✓
- `contamination_60_random_seed123/456` — random, **ppl=17.87/17.88** ✓

**不存在（从未训练）：**
- ❌ `contamination_60_adaptive_seed42` 
- ❌ `contamination_60_adaptive_seed123`
- ❌ `contamination_60_uniform_seed42`
- ❌ `contamination_60_uniform_seed123`

另有 `adaptive_rho06_tau07_seed42/123/456`（tau=**0.7** 非 0.8）和 `hybrid_rho06_seed42`（tau=0.7）。

### 4. Eval 失败原因诊断

| 失败 Worker | 原因 |
|------------|------|
| `eval_rho06_tau08_cuda3_seed123` | **Checkpoint 不存在** — `contamination_60_adaptive_seed123` 从未被训练，服务器上无此目录，无 exit file |
| `eval_westd41312_cuda3_remaining_evals` | 大概率同一原因：引用了不存在的 checkpoint 路径 |
| `eval_rho06_batch_v5` | `python: command not found`（未 activate conda） |
| `eval_rho06_batch_v6` | 脚本调用缺少 `--checkpoints` 参数 |

**根因：rho=0.6 adaptive/uniform 方法只训了 seed456 一个种子，seed42 和 seed123 的训练从未执行。** 要完成 eval 需要先补训这些 checkpoint，或者只用 seed456 的结果。

---
