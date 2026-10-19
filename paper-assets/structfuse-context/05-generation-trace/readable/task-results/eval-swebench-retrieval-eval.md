# eval swebench retrieval eval

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_swebench-retrieval-eval_20260515T182122_result.json`
- **Structured JSON:** [`7d2b50abc67af64796b8.json`](../../sessions/7d/7d2b50abc67af64796b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告如下：

## SWE-bench Lite 纯检索评估 — 状态报告

### 1. Eval 脚本用法

`eval_swebench.py` 支持以下关键参数：
- `--checkpoint-path` — checkpoint 目录（含 model.pt + training_config.json）
- `--device` — 默认 `cuda`，支持 `cpu`
- `--swebench-split` — `lite` 或 `verified`
- `--repo-cache-dir` — 预克隆 repo 缓存（已有 12 个 repo 在 `/root/autodl-tmp/swebench/repos/`）
- `--top-k` — Recall@k 的 k 值，默认 `1,5,10,20`
- `--output-dir` — 输出目录
- `--batch-size`, `--max-seq-length`, `--num-instances`

数据集已缓存在本地（设置 `HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_OFFLINE=1` 即可离线加载）。

### 2. GPU 阻塞

**CPU 不可行**：3B 模型在 CPU 上做 encoding 极慢，1 个实例跑了数分钟仍在 0%。300 个实例预估需要数天。

**GPU 状态**：
| GPU | 训练任务 | 已用显存 | 空闲显存 |
|-----|---------|---------|---------|
| 0 | dataflow_aware_s43 (Qwen) | 51 GB | **46 GB** |
| 1 | starcoder embedding_distance_s42 | 54 GB | **43 GB** |

Eval 模型（Qwen2.5-Coder-3B + LoRA, inference only）估计只需 ~8GB 显存。**两张卡都有足够空闲显存**共跑 eval（43-46GB 空闲 vs 8GB 需求）。

### 3. 可选方案

**方案 A — 与训练并行跑**（推荐）：GPU 显存充裕，eval 是 inference-only (no_grad)，内存不会冲突。可能轻微影响训练速度（~10-20% GPU compute 竞争）。命令：
```bash
CUDA_VISIBLE_DEVICES=0 nohup bash /root/structfuse/evaluation/run_swebench_eval_all.sh > /root/runs/structfuse-context/swebench_eval.log 2>&1 &
```

**方案 B — 等训练完成后跑**：零风险，命令脚本已准备好（`/root/structfuse/evaluation/run_swebench_eval_all.sh`）。

### 4. 可用 Checkpoints（6 个）

| Run | 路径 |
|-----|------|
| random_s42 | `/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen/random_s42/best_by_recall_at_1` |
| random_s43 | 同上结构 |
| random_s44 | 同上结构 |
| embedding_distance_s43 | 同上结构 |
| embedding_distance_s44 | 同上结构 |
| dataflow_aware_s43 | 同上结构（额外发现的 checkpoint） |

批量 eval 脚本已写入：`/root/structfuse/evaluation/run_swebench_eval_all.sh`

**需要你确认**：选方案 A（与训练并行，用 GPU 0）还是方案 B（等训练结束）？

---
