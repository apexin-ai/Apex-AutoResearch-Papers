# ssh v7 tg s123 completion

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v7_tg_s123_completion_20260521T211422_result.json`
- **Structured JSON:** [`1fcf13d23f8429a2c0c1.json`](../../sessions/1f/1fcf13d23f8429a2c0c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### v7 TG s123 — 训练成功 ✓

| Metric | Epoch 1 | Epoch 2 |
|--------|---------|---------|
| avg_loss | 0.9447 | 0.9315 |
| avg_ntp_loss | 0.9434 | 0.9305 |
| avg_gar_loss | 0.0013 | 0.0010 |
| avg_div_loss | 0.0000 | 0.0000 |

**Final gate:** mean=0.9467, std=0.0510, min=0.7930, max=1.0000
**Gate profile 特征:** L1(0.793) 和 L5(0.797) 最低，L27(1.000) 最高，与 s42 的 pattern 一致（浅层抑制、深层接近1）
**训练耗时:** 21425.2s (~5.95h)
**Checkpoint:** `runs/phase2_tg_s123_v7/epoch_2/` (gate_params.pt + lora adapter)

### 操作完成
- Registry → ANALYZING + metrics + checkpoint_path + log_path
- Cron `v7_tg_s123` 已删除
- **eval_v8b_ss_s123 已启动** — PID 259767, tmux session `eval_v8b_ss_s123`, GPU 0

---
