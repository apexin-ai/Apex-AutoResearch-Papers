# ops gpu status check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260516T142435_result.json`
- **Structured JSON:** [`50352de284358ba55553.json`](../../sessions/50/50352de284358ba55553.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### GPU 状态
| GPU | 利用率 | 显存占用 | 总显存 |
|-----|--------|----------|--------|
| 0 | 100% | 88,265 MiB | 97,887 MiB |
| 1 | 100% | 36,535 MiB | 97,887 MiB |

进程：PID 271786 (GPU0, 39GB) / PID 279483 (GPU1, 36.5GB)

### 训练进度

```
codellama13b_exception_only_seed42 | GPU0 | 400/444 steps (90%) | ~21s/it | 预计剩余 ~15min
codellama13b_vota_seed42           | GPU1 | 2/444 steps (0.5%)  | ~30s/it | 预计剩余 ~3.7h
```

### 完成检查
- PID 271776 **仍在运行**（注意：实际训练进程是 PID 271786）
- `eval_results.json` **尚未生成**
- `codellama13b_exception_only_seed42` 已到 90%，约 15 分钟内完成训练，之后还需跑 eval

### 备注
- `codellama13b_vota_seed42` 刚启动不久（刚完成 tokenization，仅跑了 2 steps），还需约 3.7 小时
- `codellama13b_exception_only_seed42` 已运行约 2h20min，即将完成

---
