# code db sweep prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_db-sweep-prep_20260516T200000_result.json`
- **Structured JSON:** [`35dab60e30c4c1b15f31.json`](../../sessions/35/35dab60e30c4c1b15f31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

| 项目 | 结果 |
|------|------|
| **当前默认 d_b** | 128（与约束 C003 一致） |
| **代码修改** | `train.py` 新增 `--bottleneck_dim` 参数（default=128），第 656 行 `PredictorWrapper` 初始化改用 `args.bottleneck_dim` |
| **sweep 脚本** | `/root/distill_sparse_swiglu/src/run_db_sweep.sh`（接受 `$1` 指定 GPU，默认 cuda:0） |
| **Dry-run** | d_b=64（38.2M params）和 d_b=512（302.5M params）均跑通 2 steps，无报错 |
| **benchmark_eval.py** | 已有 `--bottleneck_size` 参数，sweep 脚本中已正确传入 |

### Predictor 参数量（32 层）

| d_b | Params/layer | Total | % of LLM |
|-----|-------------|-------|-----------|
| 64 | ~1.19M | 38.2M | 0.48% |
| 128 | ~2.37M | 75.9M | 0.95% |
| 256 | ~4.72M | 151.0M | 1.88% |
| 512 | ~9.45M | 302.5M | 3.77% |

### 启动命令

```bash
nohup bash /root/distill_sparse_swiglu/src/run_db_sweep.sh 0 > /root/distill_sparse_swiglu/logs/db_sweep.log 2>&1 &
```

### 预估时间

当前 1000 steps KL-normalized 在单 RTX PRO 6000 上约 50-60 min（基于之前实验）。4 组训练 + eval 顺序执行，总计约 **4-5 小时**。

---
