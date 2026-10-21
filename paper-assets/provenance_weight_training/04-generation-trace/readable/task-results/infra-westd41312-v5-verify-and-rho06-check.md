# infra westd41312 v5 verify and rho06 check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd41312_v5_verify_and_rho06_check_20260520T085312_result.json`
- **Structured JSON:** [`701f45c301c5c25d2845.json`](../../sessions/70/701f45c301c5c25d2845.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. nvidia-smi
- **GPU 0**: RTX PRO 6000 Black — 61693/97887 MiB, **100% 利用率**, PID 453128 (python)
- **GPU 1**: RTX PRO 6000 Black — 61693/97887 MiB, **100% 利用率**, PID 453205 (python)
- **GPU 2**: 空闲 (0 MiB, 0%)
- **GPU 3**: 空闲 (0 MiB, 0%)

GPU 0/1 在跑训练进程。**GPU 2/3 没有 eval 进程** — eval 已经跑完了。

### 2. 1.7B 训练日志

**uniform_1_7b_seed42_v5**: step 8/6103, ~2.89s/it, ETA ~4h53m
- `weighted_loss` ≈ 1.78–2.36 (uniform 下 b=0, weighted=unweighted)

**adaptive_1_7b_seed42_v5**: step 7/6103, ~3.07s/it, ETA ~5h11m
- `b` 在 0.39–1.16 间变化, `ess` ≈ 2.0–3.5, 权重机制已生效

两个训练都在正常输出 step，刚启动不久。

### 3. rho06 eval 结果（全部已完成）

**seed42 holdout PPL**: **17.73**
- OOD OpenWebText PPL: **18.41**
- OOD Wikipedia PPL: **15.35**

| 指标 | seed42 | seed123 | seed456 |
|------|--------|---------|---------|
| holdout eval | ✅ | ✅ | ✅ |
| OOD openwebtext | ✅ | ✅ | ✅ |
| OOD wikipedia | ✅ | ✅ (16:40) | ✅ (16:49) |
| downstream | ✅ (16:51) | ✅ (16:44) | ✅ (16:45) |

**seed42 downstream (0-shot)**:
| Task | acc | acc_norm |
|------|-----|----------|
| ARC-Challenge | 32.5% | 34.2% |
| ARC-Easy | 65.7% | 61.3% |
| HellaSwag | 38.1% | 48.1% |
| PIQA | 68.2% | 68.6% |
| WinoGrande | 57.9% | — |

全部 3 个 seed 的 eval（holdout + 2×OOD + downstream）已完成。

### 4. 磁盘
`/root/autodl-tmp/`: 250G 总量, 75G 已用, **176G 可用 (30%)**。空间充足。

---
