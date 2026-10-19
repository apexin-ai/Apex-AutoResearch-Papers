# ops gpu status check urgent

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check-urgent_20260518T054419_result.json`
- **Structured JSON:** [`d01d777bd9803c475715.json`](../../sessions/d0/d01d777bd9803c475715.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

kl50_s456_train launched successfully on cuda:1.

## 状态汇报

```
westd-34887 cuda:0: IDLE          | util 100%* | VRAM 0G  | kl50_s123_eval 已完成
westd-34887 cuda:1: PID 2589      | util 100%  | VRAM 66G | kl_50pct_s456 训练中 (step 10/1000) ← 刚提交
westd-41718 cuda:0: IDLE          | util 0%    | VRAM 0G  | c4_ood_kl30_s123 崩溃
westd-41718 cuda:1: IDLE          | util 0%    | VRAM 0G  | c4_ood_dense_baseline 崩溃
```

\* cuda:0 显示 100% util 但 0MiB 无进程，driver artifact。

### 崩溃原因

| 实验 | 原因 |
|---|---|
| **kl50_s456_train** (westd-34887) | OOM，与另一进程抢同卡。已用 `WANDB_MODE=offline` 重新提交，当前正常运行 |
| **kl30_s456_reeval** (westd-34887) | MMLU eval 进行到 ~85% 时被 kill。仅保存 PPL=8.9332，无 benchmark 结果 |
| **c4_ood_kl30_s123** (westd-41718) | `run_c4_ppl()` 调 HF Hub 时 httpx client closed。C4 数据集在缓存中但代码仍尝试 HTTP 验证 |
| **c4_ood_dense_baseline** (westd-41718) | 同上 |

### 待决策

1. **westd-34887 cuda:0** 空闲：是否重跑 kl30_s456_reeval？
2. **westd-41718 两卡空闲**：C4 OOD eval 需加 `HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1` 重提交。需要原始启动命令来修复重跑。

---
