# ops gpu status and dpo fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_and_dpo_fix_20260515T193559_result.json`
- **Structured JSON:** [`d0b1d7f8ac014bc33aa1.json`](../../sessions/d0/d0b1d7f8ac014bc33aa1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练稳定运行中。Step 2/167，~11.8s/step，显存 21-29 GiB 波动（正常）。

汇总：

| GPU | 使用 | 任务 |
|-----|------|------|
| cuda:0 | 16281 MiB | plan_001_flat_nli_seed43 (RSFT) |
| cuda:1 | 0 MiB | 空闲（eval_sft_baseline_noquant 已完成） |
| cuda:2 | 21-29 GiB | **plan_012_dpo_ced_1ep** (刚提交，167 steps，预计 ~33min) |
| cuda:3 | 20093 MiB | plan_008_rsft_topk3 |

已完成：
1. **排查 GPU 状态** — 4 卡状态已确认
2. **ckpt-400 eval** — 已 OOM 失败（每个 batch 都 OOM），杀掉并更新 registry 为 DONE(failed)
3. **DPO 1ep 训练** — 已提交到 cuda:2，batch_size 从 2 降到 1（grad_accum 16 补偿），训练正常进行
4. **cuda:1 已空闲** — 可用于后续 ckpt-400 eval 重跑

---
