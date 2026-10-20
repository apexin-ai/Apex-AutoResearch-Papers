# ops gpu status check 20260517

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_20260517_20260517T045512_result.json`
- **Structured JSON:** [`5d2ba49760f466d9ee6c.json`](../../sessions/5d/5d2ba49760f466d9ee6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## nvidia-smi 摘要

| GPU | 显存 | Util | 进程 |
|-----|------|------|------|
| cuda:0 | 0MiB / 32607MiB | 0% | **空闲** — PID 396333 (plan_002_test_rsft_s44) 已完成 |
| cuda:1 | 29569MiB / 32607MiB | 98% | PID 406515 — plan_006_qwen3_1_7b_rsft_train |
| cuda:2 | 22985MiB / 32607MiB | 93% | PID 409565 — plan_016_llama_rsft_train_r3 |
| cuda:3 | 1539MiB / 32607MiB | 37% | PID 411032 — plan_006_qwen3_8b_ced_scoring |

## 各任务状态

**plan_002_test_rsft_s44 (cuda:0)** — 已完成
- test split, 1000 docs, 26925 predictions, 626 truncated, format_ok=99.6%
- 推理时间: 12494s (~3.5h)
- 这是 test set（无 gold labels），需提交 CodaLab 评分
- `predictions.json` 在 `/root/autodl-tmp/eval_results/plan_002_test_rsft_s44/predictions.json`

**plan_006_qwen3_1_7b_rsft_train (cuda:1)** — 运行中
- 进度: 1297/1698 steps (**76%**)，已跑 ~1h38m
- ~2.8s/it，预计还需约 19min 完成

**plan_016_llama_rsft_train_r3 (cuda:2)** — 刚开始
- 进度: 24/3312 steps (**0.7%**)，~3.1s/it
- 刚启动约 1min，预计总时长 ~2h50m

**plan_006_qwen3_8b_ced_scoring (cuda:3)** — 运行中
- 进度: 17000/24216 records (**70%**)
- ~2min/500 records，预计还需约 30min

## RSFT s44 dev predictions

**没有找到 RSFT s44 dev set 的 predictions.json 文件。** 已有的 s44 相关 predictions 都是 test split:
- `/root/autodl-tmp/eval_results/plan_002_test_rsft_s44/predictions.json` (test)
- `/root/autodl-tmp/eval_results/test_rsft_ced_s44/predictions.json` (test)

dev eval 目录 `/root/autodl-tmp/eval_results/rsft_s44/` 只有 `metrics.json` 和 `eval.log`，没有保存 predictions。dev metrics:
- **F1: 46.55**, Ign_F1: 46.55
- Evi_F1: 80.87, Evi_F1_joint: 37.13, EDCR: 63.50

如果后续 CED reranking 实验需要 dev predictions，需要重新跑一次 rsft_s44 dev eval 并加 `--save_predictions` 参数。cuda:0 现在空闲，可以立即启动。

---
