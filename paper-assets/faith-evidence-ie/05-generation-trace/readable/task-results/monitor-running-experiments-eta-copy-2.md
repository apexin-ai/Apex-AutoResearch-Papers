# monitor running experiments eta

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_running_experiments_eta_20260516T015218_result.json`
- **Structured JSON:** [`cb6a96be930ca2031c8a.json`](../../sessions/cb/cb6a96be930ca2031c8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度快照 (2026-05-16 ~09:52 UTC)

| exp_id | GPU | PID存活 | 进度 | 预计完成 | 备注 |
|--------|-----|---------|------|----------|------|
| eval_flat_nli_s44 | cuda:0 (11GB/32GB) | ✅ 270462 | 204/247 (83%) | ~30min (~10:22 UTC) | ~45s/batch |
| rsft_ced_s43_train_r3 | cuda:1 (28.7GB/32GB) | ✅ 277310 | 510/510 (100%) | 即将完成 | 训练步已跑完，正在收尾(eval/save) |
| eval_rsft_ced_s45 | cuda:2 (10.8GB/32GB) | ✅ 283838 | 33/247 (13%) | ~2h15min (~12:07 UTC) | ~38s/batch，刚启动22min |
| eval_flat_nli_seed45 | cuda:3 (11GB/32GB) | ✅ 272164 | 164/247 (66%) | ~66min (~10:58 UTC) | ~48s/batch |

要点：
- rsft_ced_s43_train_r3 训练 510 步已 100% 完成，进程仍存活可能在做最终 eval 或保存 checkpoint
- 其余 3 个 eval 正常推进，无异常

---
