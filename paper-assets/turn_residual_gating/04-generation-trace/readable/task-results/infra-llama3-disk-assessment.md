# infra llama3 disk assessment

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_llama3_disk_assessment_20260519T144230_result.json`
- **Structured JSON:** [`1f44904a400d3f959138.json`](../../sessions/1f/1f44904a400d3f959138.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。

## 磁盘现状

| 分区 | 总空间 | 已用 | 可用 |
|------|--------|------|------|
| 根分区 `/` | 30GB | 16GB | **15GB** |
| 数据盘 `/root/autodl-tmp/` | 250GB | 4.6GB | **246GB** |

## 大文件分布

| 项目 | 大小 | 位置 |
|------|------|------|
| **Qwen2.5-7B-Instruct 模型** | **15GB** | `/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct/`（根分区） |
| ultrachat_200k 数据集 | 4.6GB | `/root/autodl-tmp/.hf_cache/`（数据盘，含重复缓存） |
| Training runs (3个checkpoint) | 260MB | `/root/turn_residual_gating/runs/`（根分区） |
| 项目代码 + data | 374MB | `/root/turn_residual_gating/`（根分区） |
| HuggingFace cache | 20KB | 几乎为空 |
| Llama 文件 | **0** | 之前下载的 tokenizer 已不存在 |

## Llama-3 空间需求

- 模型权重: ~16GB
- 训练产出预估 (LoRA checkpoints): ~1GB
- 总需求: ~17GB

## 评估结论

- **根分区可用 15GB，放不下 16GB 的 Llama 权重。**
- **数据盘可用 246GB，空间完全充裕。**

### 建议方案（两个选项，可叠加）

**方案 A：Llama 模型直接下到数据盘（推荐，零风险）**
- 下载到 `/root/autodl-tmp/.hf_cache/` 或 `/root/autodl-tmp/models/`
- 设 `HF_HOME=/root/autodl-tmp/.hf_cache` 或 ModelScope `cache_dir=/root/autodl-tmp/models/`
- 无需清理任何东西，246GB 足够

**方案 B：把 Qwen 模型缓存移到数据盘，腾出根分区空间**
- 将 `/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct/`（15GB）移到 `/root/autodl-tmp/` 并建软链接
- 根分区释放 15GB → 可用 ~30GB
- 风险：需确认 Qwen eval 代码的模型路径正确指向新位置

### 必须保留
- `runs/phase2_tg_s42_v7/` (91MB) — TG checkpoint，论文需要
- `runs/phase2_ug_s42/` (91MB) — UG checkpoint，论文需要
- `runs/phase2_lora_only_s42/` (78MB) — LoRA-only baseline checkpoint，论文需要
- `runs/4way_eval/` + `phase2_4way_eval_heldout/` — eval 结果，论文需要
- Qwen 模型缓存 — 可移动但不可删除

---
