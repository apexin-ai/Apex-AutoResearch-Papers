# code exp45 resubmit

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp45_resubmit_20260522T063313_result.json`
- **Structured JSON:** [`d05e0fb0725561dbcd24.json`](../../sessions/d0/d05e0fb0725561dbcd24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 进度

N=0, 5, 10, 25 **全部完成**（含训练+评估），结果已写入 `results/exp45_benign_adaptation_curve.json`。进程在 **N=50 的 Stage 1 DAPT** 期间死亡。N=50 有部分 checkpoint（`deberta_multitask` 目录存在但不完整，无 GRU）。

### 已完成结果

| N | Train | WC FPR | IID F1 | DD F1 | AA F1 | FITD F1 | Time |
|---|-------|--------|--------|-------|-------|---------|------|
| 0 | 350 | 0.6531 | 1.0000 | 1.0000 | 0.9809 | 1.0000 | 1.7m |
| 5 | 355 | 0.1633 | 1.0000 | 0.9904 | 0.9809 | 1.0000 | 1.7m |
| 10 | 360 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.7m |
| 25 | 375 | 0.0000 | 1.0000 | 1.0000 | 0.9530 | 1.0000 | 1.7m |

### Resume 支持

脚本**不支持 resume**。它按顺序遍历 `N_VALUES = [0, 5, 10, 25, 50, 100, 150]`，没有跳过已完成 N 值的逻辑。每次运行都会覆盖 `results/exp45_benign_adaptation_curve.json`（每完成一个 N 就增量写入）。

### 运行命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 python /root/persuasion_turn_jailbreak_detect/scripts/exp45_benign_adaptation_curve.py 2>&1 | tee /tmp/exp45_curve.log
```

脚本内部硬编码 `DEVICE = torch.device("cuda:0")`，单卡运行。

### 建议

**直接全部重跑**。理由：
- 每个 N 值只需 ~1.7 min，总共 7 个点 ≈ 12 min
- 不支持 resume，改脚本不值得
- 结果 JSON 是增量写入的，全跑完会自动包含所有 N 值
- N=50 的不完整 checkpoint 不影响（脚本会覆盖）

---
