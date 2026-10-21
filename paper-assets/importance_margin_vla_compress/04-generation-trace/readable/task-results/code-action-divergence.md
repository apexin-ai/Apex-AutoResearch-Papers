# code action divergence

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_action_divergence_20260517T100440_result.json`
- **Structured JSON:** [`783217fe37841bf2ca0e.json`](../../sessions/78/783217fe37841bf2ca0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查通过。

脚本已部署到 `/root/autodl-tmp/importance_margin_vla_compress/artifacts/analyze_action_divergence.py`。

**设计要点：**
- 方式一：baseline 驱动环境，每步同时给两个模型相同 observation，只用 baseline action 推进 env
- 每次 re-plan（每 50 步或首步）时对两个模型分别预测 action chunk
- ACIS pruning 通过 forward hook 对 connector 输出做 mask（k=0.7, retain 70%）
- 对比 `libero_full_ft_100k`（baseline）vs `libero_acis_stage1only_k07`（ACIS pruned）

**输出：**
- `artifacts/action_divergence_data.json` — 每步 raw action pairs + L2 distance
- `artifacts/action_divergence_curve.pdf` — 三图: overall divergence curve, per-dim breakdown, per-task comparison
- `artifacts/action_divergence_summary.pdf` — 统计摘要

**运行命令**（GPU 0/1 空闲后）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/importance_margin_vla_compress
python artifacts/analyze_action_divergence.py --gpu 2 --num_episodes 5 --task_ids 0,1,2
```

---
