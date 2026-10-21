# ops urgent collect and fill 34887

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-collect-and-fill-34887_20260518T105627_result.json`
- **Structured JSON:** [`d6b8050824414b8e32d9.json`](../../sessions/d6/d6b8050824414b8e32d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都已通过数据集加载，正在跑 lm-eval loglikelihood 请求。问题已解决。

---

## 状态汇总

### 1. 原 westd-34887 eval 结果（失败 + 部分数据）

两个 eval 都因 `HF_DATASETS_OFFLINE=1` 导致 lm-eval 在加载 `allenai/ai2_arc` 时报 `OfflineModeIsEnabled`，WikiText-2 PPL 已算出但 downstream tasks 全部失败：

| 实验 | WikiText-2 PPL (已获取) | Downstream | 原因 |
|------|------------------------|------------|------|
| kl_comp_30pct_s123_eval | **8.9788** | FAILED | HF_DATASETS_OFFLINE=1 |
| kl50_s456_uniform_eval | **11.9538** | FAILED | HF_DATASETS_OFFLINE=1 |

**修复**: 去掉 `HF_DATASETS_OFFLINE=1`，保留 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`。已重跑。

### 2. westd-41718 训练进度

两个训练都已完成：

| 实验 | Steps | Final Loss | Checkpoint |
|------|-------|------------|------------|
| kl_comp_30pct_s456 | **1000/1000** | 0.6797 | `compensation.pt` (128MB) |
| kl_comp_50pct_s42 | **1000/1000** | 1.0703 | `compensation.pt` (128MB) |

已合并为 `predictor_with_comp.pt`（predictor + comp_network），registry 已更新为 DONE。

### 3. 新提交的实验

SCP 不通（服务器间无密钥），改为直接在 41718 本地跑 eval（模型 + 数据集缓存齐全）：

| 实验 | 服务器 | GPU | 状态 |
|------|--------|-----|------|
| kl_comp_30pct_s456_eval | westd-41718 | cuda:0 | RUNNING |
| kl_comp_50pct_s42_eval | westd-41718 | cuda:1 | RUNNING |

### 4. 四卡最终状态

| 服务器 | GPU | 实验 | GPU Util | VRAM |
|--------|-----|------|----------|------|
| westd-34887 | cuda:0 | kl_comp_30pct_s123_eval (re-run) | 100% | 49GB |
| westd-34887 | cuda:1 | kl50_s456_uniform_eval (re-run) | 97% | 49GB |
| westd-41718 | cuda:0 | kl_comp_30pct_s456_eval (new) | 99% | 42GB |
| westd-41718 | cuda:1 | kl_comp_50pct_s42_eval (new) | 100% | 40GB |

**所有 4 卡满载**。预计 ~35 分钟出结果（基于 s42 eval 历史耗时 ~37 分钟）。

---
