# validate d080 nan check immediate

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validate_d080_nan_check_immediate_20260519T003751_result.json`
- **Structured JSON:** [`50e05686863c14efb391.json`](../../sessions/50/50e05686863c14efb391.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。结果如下：

| 实验 | GPU | Step | Gen | Loss | Grad Norm | 状态 |
|------|-----|------|-----|------|-----------|------|
| a005_v3 | 3 | - | 1/10 (generating) | - | - | 正常运行中 |
| a060_v3 | 2 | - | 1/10 (generating) | - | - | 正常运行中 |
| interv_v4 | 4 | - | 1/10 (generating) | - | - | 正常运行中 |

**19828 md5**: `5b37837e7a6378f42bcb740f8f5e4773` ✓

**详细状态**：
- 3 个实验启动于 08:23，当前 08:38（运行 ~15 min）
- 均已完成 Gen 0 baseline 计算（ppl=26.95, entropy=3.2342, eff_rank=46.6）
- 当前处于 Gen 1/10 的 **"Generating synthetic data"** 阶段（文本生成），尚未进入训练步骤
- **无 NaN/inf** 出现
- 无 "Casting model" 日志（Pythia-410m 原生 fp32，无需显式转换）
- GPU 显存：GPU 2/3/4 各 ~12706 MiB，利用率 65-79%

需等训练步骤开始后才能观察 loss/grad_norm 是否正常。按当前进度，预计再 ~5-10 分钟进入训练阶段。

---
