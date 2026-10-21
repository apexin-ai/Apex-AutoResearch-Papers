# deploy simplerenv westd27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_simplerenv_westd27271_20260524T180143_result.json`
- **Structured JSON:** [`a540c06a9166371102f9.json`](../../sessions/a5/a540c06a9166371102f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

L2norm 实验修复成功：Model loaded → 进入 PutCarrotOnPlateInScene-v1 任务，无报错。两个实验都在正常运行。

## 部署总结

| 项目 | 状态 |
|------|------|
| **Step 1: Dry-run** | 通过。修复了 2 个兼容性 bug：① PIL image batch 维度 squeeze ② transformers 5.x `past_key_values` DynamicCache 兼容 |
| **Step 2: 部署** | 2 个实验已启动 |
| GPU0 `eval_baseline` | tmux `eval_baseline`, 4 tasks × 50 eps, `--prune_mode none` |
| GPU1 `eval_l2norm_k09` | tmux `eval_l2norm_k09`, 4 tasks × 50 eps, `--prune_mode l2norm --keep_ratio 0.9`（修复了 projector hook 路径） |
| **Step 3: 监控** | Cron 每 15 分钟检查实验状态 (job b80c5c9a) |
| **Registry** | 两个实验均 RUNNING，hypothesis 已设 |

**修复的 bug：**
1. `eval_openvla_simplerenv_ms3.py:144` — 图像 ndim>3 时 squeeze batch 维度
2. `modeling_prismatic.py` — 4 处修改适配 transformers 5.x 的 DynamicCache
3. `eval_openvla_simplerenv_ms3.py` — projector hook 路径从 `vla.vision_backbone.projector` 改为 `vla.projector`

预计每个实验运行 ~2-3 小时（4 tasks × 50 eps × ~16s/ep）。

---
