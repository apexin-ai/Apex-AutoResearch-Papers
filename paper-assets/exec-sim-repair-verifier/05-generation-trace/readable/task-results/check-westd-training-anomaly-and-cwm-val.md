# check westd training anomaly and cwm val

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-training-anomaly-and-cwm-val_20260514T195722_result.json`
- **Structured JSON:** [`69ec2d4bce4e589ca0c4.json`](../../sessions/69/69ec2d4bce4e589ca0c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部收集完毕。以下是汇报。

---

## 1. 训练异常排查结果：**虚惊一场（误读日志）**

上一轮检查读的是 `repo-level-cwm-v4.log`，但该文件实际是一个 **Qwen3-4B CWM** 的独立训练（step 386/6633），不是 CWM 8B 的日志。

CWM 8B (PID 266816) 实际写入 `repo-level-cwm-8b-conda-v2.log`（通过 `/proc/266816/fd/1` 确认）。

**两个训练的真实指标完全不同：**

| | CWM 8B (PID 266816, GPU 2) | CLS 8B seed123 (PID 266449, GPU 3) |
|---|---|---|
| 脚本 | `train_repo_cwm.py` | `train_repo_verifier.py` |
| 模型 | Qwen3-8B | Qwen3-8B |
| 当前 step | ~1955/6633 (29%) | ~3650/6633 (55%) |
| Epoch | ~0.86 | ~1.65 |
| 最新 loss | 0.2261 | 0.3716 |
| 最新 lr | 3.757e-5 | 2.368e-5 |
| 最新 eval_loss | 0.3866 (step 1900) | 0.3874 (step 3600) |
| 最新 checkpoint | checkpoint-1900 (03:48) | checkpoint-3600 (03:51) |
| CUDA_VISIBLE_DEVICES | 2 | 3 |
| tmux session | `repo-level-cwm-8b-conda-v2` | (nohup) |

**结论：训练正常，无配置错误。** 之前的"一致指标"是读错了日志文件。

---

## 2. GPU 全面状态

| GPU | VRAM | Util | PID | 任务 |
|-----|------|------|-----|------|
| cuda:0 | 19794/32607 MiB | 99% | 276775 | CLS 8B ckpt-200 val eval |
| cuda:1 | 13629/32607 MiB | 100% | 277670 | **CLS v5 (4B) ckpt-200 val eval** |
| cuda:2 | 30733/32607 MiB | 98% | 266816 | CWM 8B 训练 (step ~1955) |
| cuda:3 | 30913/32607 MiB | 89% | 266449 | CLS 8B seed123 训练 (step ~3650) |

PID 277670 在 GPU 0 上还有 546 MiB 溢出（主要在 GPU 1）。

---

## 3. CLS 8B val sweep (cuda:0)

- PID 276775（非 276768，可能是重启过）
- 正在 eval checkpoint-200，进度 **3600/9335 (~39%)**
- running_acc = **64.1%**
- 尚无 summary.json 产出（第一个 checkpoint 还没跑完）
- 预计还需 ~10 分钟完成当前 checkpoint

---

## 4. cuda:1 无法启动 CWM v12 val

cuda:1 被 **CLS v5 (Qwen3-4B) checkpoint-200 val eval**（PID 277670）占用，已运行 ~7 分钟。无法启动 CWM v12 eval。

---

## 5. 额外发现

`repo-level-cwm-v4.log` 是一个独立的 **Qwen3-4B CWM 训练**（非 8B），目前在 step 386/6633（~6%）。但它没有在 nvidia-smi 中出现任何 GPU 进程，可能已经结束或挂起。需要确认是否有意为之。

---
