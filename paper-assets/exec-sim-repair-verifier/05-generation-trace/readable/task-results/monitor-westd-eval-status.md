# monitor westd eval status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-eval-status_20260514T233830_result.json`
- **Structured JSON:** [`95fc4deb7da5f54a1538.json`](../../sessions/95/95fc4deb7da5f54a1538.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### cls8b-s42-ckpt800-val8192-eval

**状态: 未启动 (never launched)**

- GPU 0 完全空闲（0MiB / 0% util），无任何进程
- `/tmp/agent-ml-exit/` 中无 `cls8b-s42-ckpt800` 相关 exit 文件
- `/root/autodl-tmp/results/` 中无 ckpt-800 相关结果目录
- checkpoint-800 存在于 `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/checkpoint-800`（由 s42-resume 训练产生），但 eval 从未被启动

### 4 张 GPU 状态

| GPU | 显存 | 利用率 | 进程 | 状态 |
|-----|------|--------|------|------|
| 0 | 0MiB / 32607MiB | 0% | 无 | **空闲** |
| 1 | 27311MiB / 32607MiB | 98% | `train_repo_verifier.py` s42-resume (PID 295794) | ✅ 正常 |
| 2 | 30733MiB / 32607MiB | 95% | `train_repo_cwm.py` cwm-v4 (PID 266816) | ✅ 正常 |
| 3 | 30913MiB / 32607MiB | 97% | `train_repo_verifier.py` seed123-v3 (PID 266449) | ✅ 正常 |

### 3 个训练进程详情

- **cuda:1 s42-resume**: step 1173/6633 (18%), epoch 0.52, loss=0.984, eval_loss=0.182@step1000, ~8s/it
- **cuda:2 cwm-v4**: 从 ckpt-1600 恢复，正常运行
- **cuda:3 seed123-v3**: 从 ckpt-3000 恢复，正常运行

**结论**: GPU 0 空闲可用，ckpt-800 eval 需要手动启动。

---
