# ssh diagnose 30476 eval all

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_30476_eval_all_20260517T222206_result.json`
- **Structured JSON:** [`f913ec73988963fbb814.json`](../../sessions/f9/f913ec73988963fbb814.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。汇总如下：

---

## 1. nvidia-smi 完整输出

```
Mon May 18 06:22:26 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.82.09    Driver Version: 580.82.09    CUDA Version: 13.0                 |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:98:00.0 Off |    41757MiB/97887MiB |  98%  |
|   1  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:A8:00.0 Off |    41757MiB/97887MiB |  99%  |
|   2  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:B8:00.0 Off |        0MiB/97887MiB |   0%  |
|   3  NVIDIA RTX PRO 6000 Blac...    On  |   00000000:D8:00.0 Off |    71173MiB/97887MiB | 100%  |
+-----------------------------------------+------------------------+----------------------+
| Processes:                                                                              |
|   0: python (PID 54784) - grid_b0_3_seed456_r2      41748MiB                           |
|   1: python (PID 53826) - grid_b0_3_seed123_r2      41748MiB                           |
|   3: python (PID 48891) - batchsize16_nmin8_r2      71164MiB                           |
+-----------------------------------------------------------------------------------------+
```

## 2. 实验状态

| 实验 | 状态 | Checkpoint 路径 | 进度 |
|------|------|----------------|------|
| **rho02_adaptive_tau08_seed42** | **COMPLETED** | `/root/autodl-tmp/output/models/rho02_adaptive_tau08_seed42/final` | 6103/6103 |
| grid_b0_3_seed456_r2 | RUNNING (GPU 0) | `/root/autodl-tmp/output/models/grid_b0_3_seed456_r2/` (ckpt-2000) | **2315/6103 (38%)**, ETA ~2h12m |
| grid_b0_3_seed123_r2 | RUNNING (GPU 1) | `/root/autodl-tmp/output/models/grid_b0_3_seed123/` (ckpt-3000) | **3339/6103 (55%)**, ETA ~1h37m |
| batchsize16_nmin8_r2 | RUNNING (GPU 3) | `/root/autodl-tmp/provenance_weight_training/output/models/batchsize16_nmin8_r2/` (ckpt-4000) | **4131/6103 (68%)**, ETA ~1h21m |

注：`batchsize16_nmin8_r3` 不存在。实际跑的是 `batchsize16_nmin8_r2`（output_dir 在 `/root/autodl-tmp/provenance_weight_training/output/models/` 而非 `/root/autodl-tmp/output/models/`）。

## 3. Eval PPL 结果

| 实验 | Perplexity | Loss | Eval Tokens |
|------|-----------|------|-------------|
| **rho02_adaptive_tau08_seed42** | **17.38** | 2.855 | 4,077,068 |

## 4. 运行中实验当前进度

- **grid_b0_3_seed456_r2**: step 2315/6103, 38%, ~2.09s/it, 预计还需 ~2h12m
- **grid_b0_3_seed123_r2**: step 3339/6103, 55%（从 ckpt-1000 恢复）, ~2.09s/it, 预计还需 ~1h37m
- **batchsize16_nmin8_r2**: step 4131/6103, 68%, ~2.46s/it, 预计还需 ~1h21m

三个跑着的实验预计今天内全部完成，完成后 GPU 2 可以依次跑 eval。

---
