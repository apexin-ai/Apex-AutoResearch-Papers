# ops prep plan010 nli ablation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep_plan010_nli_ablation_20260519T182044_result.json`
- **Structured JSON:** [`239714408f66c533d4ca.json`](../../sessions/23/239714408f66c533d4ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

探测完成。

---

## 探测结果

### 1. 当前 CED scoring 用的 NLI 模型
**`cross-encoder/nli-deberta-v3-base`** — 这是代码中唯一的默认值：
- `ced_reward.py:22`: `DEFAULT_NLI_MODEL = "cross-encoder/nli-deberta-v3-base"`
- `rsft_score_filter.py:490`: `default="cross-encoder/nli-deberta-v3-base"`
- 所有已有 `rsft_report.json`（s0-s3, s44, topk3, flat_nli）均记录 `nli_model_path: "cross-encoder/nli-deberta-v3-base"`
- scripts 目录中**没有任何脚本**引用过 v3-large

**结论：canonical CED s42 baseline (ign_f1=0.4517) 用的就是 v3-base，不是 v3-large。**

### 2. 原始 4B 候选路径
- `/root/autodl-tmp/rsft_generations/generations.jsonl` (207MB, 21952 records, 4 shards)
- Canonical scoring 将其拆分为 `rsft_score_input_s0` ~ `s3`，各自打分后合并到 `/root/autodl-tmp/rsft_filtered/`
- Canonical scoring 参数：`top_k=1, tau=0.5, f1_threshold=0.1`

### 3. NLI 模型下载状态
HF cache 中**两个模型都已下载**：
- `models--cross-encoder--nli-deberta-v3-base` ✓
- `models--cross-encoder--nli-deberta-v3-large` ✓

（本地 `/root/autodl-tmp/models/` 目录没有 NLI 模型，但 HF cache 够用）

### 4. rsft_score_filter.py 关键参数
| 参数 | 默认值 | 说明 |
|---|---|---|
| `--nli_model_path` | `cross-encoder/nli-deberta-v3-base` | NLI 模型路径 |
| `--nli_device` | None (auto) | GPU device |
| `--selection_strategy` | `top_pct` | `top_k` 或 `top_pct` |
| `--top_k` | 2 | k=1 for canonical |
| `--tau` | 0.5 | CED 阈值 |
| `--scoring_mode` | `ced` | `ced` 或 `flat_nli` |

### 5. **关键问题：ablation 方向需要反转**

任务描述假设 canonical 用的是 v3-large，ablation 用 v3-base。但实际情况是：
- **Canonical = v3-base**（已确认）
- **Ablation 应该用 v3-large** 重新打分

建议的 scoring 命令：

```bash
cd /root/autodl-tmp/freige && \
CUDA_VISIBLE_DEVICES=1 python -m freige.training.rsft_score_filter \
    --input_dir /root/autodl-tmp/rsft_generations \
    --output_path /root/autodl-tmp/rsft_scored_v3_large \
    --nli_model_path cross-encoder/nli-deberta-v3-large \
    --nli_device cuda:0 \
    --selection_strategy top_k --top_k 1 \
    --tau 0.5 --f1_threshold 0.1
```

### 6. 磁盘
`/root/autodl-tmp/`: 186G used / 250G total, **65GB free** — 足够。

---
