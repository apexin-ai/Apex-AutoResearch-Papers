# infra westd30476 kill and migrate

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd30476_kill_and_migrate_20260520T053916_result.json`
- **Structured JSON:** [`5bdc4c0059751578559f.json`](../../sessions/5b/5bdc4c0059751578559f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

**KILL**: done — PID 191550, 193988, 199767, 199839 全部已杀

**GPU**: all released — 4 张卡均 0 MiB

**TMUX**: cleared

**迁移文件清单** (→ `westd-41312:/root/autodl-tmp/provenance_weight_training/output/eval_results_from_30476/`):

| 文件 | 大小 | 内容 |
|------|------|------|
| `bs8_auto_nmin_seed42_eval.json` | 169B | bs8 baseline eval |
| `batchsize16_nmin8_r2_eval.json` | 272B | batchsize16 eval |
| `eval_results_contamination_60_all.json` | 1056B | contamination_60 四组 (seed123/uniform/random/grid) |
| `contamination_60_grid_b0_3_seed42_eval.json` | 562B | contamination_60_grid final + ckpt-5500 |
| `rho02_adaptive_tau08_seed42_eval.json` | 258B | rho02 adaptive eval |
| `grid_b0_3_seed123_eval.json` | 539B | grid b0.3 seed123 re-eval |
| `grid_b0_3_seed456_r2_eval.json` | 247B | grid b0.3 seed456 r2 |
| `grid_b0_2_eval.json` | 990B | grid b0.2 四组 (seed456/123 final + ckpt-5500) |
| `detect_remove_eval.json` | 1733B | detect_remove 10 组 (q02-q09 各 seed) |

**无 OOD eval 结果文件**（OOD 输入数据 .jsonl 不需迁移）

**可释放: YES**

---
