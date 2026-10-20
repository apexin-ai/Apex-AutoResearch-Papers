# eval ced kl001 r4 multi checkpoint

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ced-kl001-r4-multi-checkpoint_20260514T174126_result.json`
- **Structured JSON:** [`fcd7401cca32fd818b83.json`](../../sessions/fc/fcd7401cca32fd818b83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已成功启动并在运行中：

- **PID**: 78850 (GPU进程 78857)
- **GPU**: cuda:2，已占用 6924 MiB
- **当前状态**: 正在评估 checkpoint-10，模型已加载，inference 进行中 (0/62 batches)

**提交的 checkpoint 列表**: 10, 20, 30, 40, 60, 70, 80（共 7 个，排除了 cuda:1 正在跑的 checkpoint-50）

**预计耗时**: 每个 checkpoint ~1.5-2h，7 个 checkpoint 共 ~10.5-14h

**日志位置**: `~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_multi.log`

**待对比 baseline** (eval 完成后):
| 指标 | SFT baseline | MVP-2 pass 条件 |
|------|-------------|----------------|
| rel_f1 | 0.4057 | ≥ 0.3557 (不退化 -5pp) |
| evi_f1 | 0.7979 | ≥ 0.8179 (+2pp) |
| edcr | 0.7118 | - |

训练还在跑（~step 80/100），完成后 checkpoint-90/100 需要再单独跑 eval。

---
