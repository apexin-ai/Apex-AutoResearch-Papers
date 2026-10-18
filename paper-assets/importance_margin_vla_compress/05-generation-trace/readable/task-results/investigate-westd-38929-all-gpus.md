# investigate westd 38929 all gpus

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_westd-38929-all-gpus_20260522T015818_result.json`
- **Structured JSON:** [`114a023805b4a96d19be.json`](../../sessions/11/114a023805b4a96d19be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-38929 GPU 状态汇总

| GPU | 状态 | 实验 | PID | 进度 |
|-----|------|------|-----|------|
| **0** | **活跃** (10.6GB, 51%) | L2norm k=0.85 Spatial v2 | 227018 | Task 2/10 进行中，T0=98%, T1=94%，预计~1.5h 完成 |
| **1** | 空闲 | — | — | — |
| **2** | 空闲 | Random k=0.925 Object seed43 | 已结束 | **完成**: SR=30.0% (150/500) |
| **3** | 空闲 | Random k=0.85 Spatial seed42 | 已结束 | **完成**: SR=58.4% (292/500) |

### L2norm k=0.95 Spatial (最高优先级)

**状态**: 崩溃（同 k=0.85 v1 一样的 `Network is unreachable` 错误）

模型加载成功，但在初始化 preprocessor 时尝试下载 `google/paligemma-3b-pt-224` tokenizer 失败。需要用 `HF_HUB_OFFLINE=1` 重跑。

日志路径: `/root/runs/importance_margin_vla_compress/eval_pi05_l2norm_k095_spatial_seed42.log`

Registry 已更新 (metrics/log_path/checkpoint_path)。

### L2norm k=0.85 Spatial v2

正常运行中，早期结果非常强（T0=98%, T1=94%）。Registry 已创建并推进到 RUNNING（PID 227018, GPU 0）。

### 待办

- GPU 1/2/3 空闲，可用于重跑 **L2norm k=0.95 Spatial**（需 `HF_HUB_OFFLINE=1`）
- Random k=0.925 Object (SR=30.0%) 和 Random k=0.85 Spatial (SR=58.4%) 的 registry 可能也需要更新

---
