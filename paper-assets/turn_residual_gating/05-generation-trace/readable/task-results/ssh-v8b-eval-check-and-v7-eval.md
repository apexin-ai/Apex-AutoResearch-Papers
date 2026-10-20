# ssh v8b eval check and v7 eval

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v8b_eval_check_and_v7_eval_20260521T225041_result.json`
- **Structured JSON:** [`5bfed299b13c9a5d64f0.json`](../../sessions/5b/5bfed299b13c9a5d64f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### eval_v8b_ss_s123 — DONE ✓

| | IID (50conv×3t) | Model-gen (5conv×10t) |
|---|---|---|
| GAR ours (mid) | **0.503** | **0.418** |
| GAR dongre (mid) | 0.394 | 0.441 |
| PPL | 2.781 | 1.389 |
| NTP loss | 0.976 | 0.325 |

- **gap_ratio = 1.20×** (s42 = 1.57×, 更紧 → SS 在 s123 下 exposure bias 更小)
- PPL 1.389 vs base 1.351 (+2.8%)，无恶化
- **PASS**，registry 已更新为 DONE/success

### eval_v7_tg_s123 — 已启动

- PID: 264869，tmux session: `eval_v7_tg_s123`
- 包含 4-way 对比：Base / LoRA-only (跳过，无 checkpoint) / TG v7 s123 / v8b-SS s123
- checkpoint: `runs/phase2_tg_s123_v7/epoch_2`
- 预计运行 ~1.5h

---
