# ops gpu status and fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-and-fix_20260515T140513_result.json`
- **Structured JSON:** [`33fc718018ac0bb81cba.json`](../../sessions/33/33fc718018ac0bb81cba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

### GPU 分配

| GPU | 显存占用 | 利用率 | 任务 |
|-----|----------|--------|------|
| **0** | 1701/32607 MiB | 42% | PID 178055 — `ced_reranker` CED scoring，318/985 (32%)，已跑 6h |
| **1** | 14083/32607 MiB | 69% | PID 197386 — `mvp2_eval_rsft_r2b_maxtok1536_r2` inference，82/124 (66%)，已跑 2h10m |
| **2** | **0 MiB** | **0%** | **空闲** — mvp2_eval_rsft_s43_r2 已完成 (exit=0, 21:15) |
| **3** | 19560/32607 MiB | 90% | PID 208155 — flat-NLI scoring (1410 MiB) + PID 210104 — plan_011 GRPO (18136 MiB) **两个进程共享** |

### 各项检查

**mvp2_eval_rsft_s43_r2 (已完成)**:
- F1=0.4683, Ign-F1=0.4683, Evi-F1=0.8156, EDCR=0.6388
- 171/985 truncated, 结果写入 `/root/autodl-tmp/eval_results/rsft_s43/`

**flat-NLI scoring (PID 208148→208155)**: 进行中，2500/21728 scored (11.5%)。输出目录 `/rsft_filtered_flat_nli/` 当前为空（未写最终文件）。速率 ~500条/1.5min，预计还需 ~50min。

**DREEAM evaluation.py bug**: **已修复**。`scores != []` 已改为 `if len(scores) > 0:`（grep 确认无残留）。但 **DREEAM 训练未重启**——crash log 在 21:52，evaluation.py 修改在 21:58，之后没有新的训练进程。cuda:2 完全空闲。

**topk3_random 数据**: **就绪**。`rsft_train.jsonl` 8037 行 (26.7 MB)，包含 input/output/ced_score/f1_reward/combined_score 等字段。

**plan_011 GRPO (PID 210099→210104)**: 正常运行，48/100 steps (48%)，已跑 ~5min，在 GPU 3 上。

### 需要关注

1. **cuda:2 空闲** — DREEAM bug 已修复但未重启训练，可以立即利用
2. **GPU 3 双进程共享** — flat-NLI (1.4GB) + GRPO (18.1GB) 合计 19.5GB/32GB，暂未 OOM 但较紧

---
