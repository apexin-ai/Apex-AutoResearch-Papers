# ops westd status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-status-check_20260516T014255_result.json`
- **Structured JSON:** [`d03d42e353d62149676e.json`](../../sessions/d0/d03d42e353d62149676e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 状态汇报

### GPU 利用率

| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| cuda:0 | RTX PRO 6000 Blackwell (96GB) | 17,661 / 97,887 MiB (18%) | **91%** |
| cuda:1 | RTX PRO 6000 Blackwell (96GB) | 0 / 97,887 MiB | **0% — 完全空闲** |

### eval_sft_unpruned_full (N=1319) 进度

- **PID 74134** — `eval_gsm8k.py --model_path sft_unpruned_baseline --max_samples 1319`
- 当前进度: **97/1319 (7.4%)**，已运行 ~4min15s
- 速度: ~3.0-3.7 s/it
- 50 样本时 acc = **0.8200**, eos_rate = 100%
- 预计剩余: **~60-75 min**（总计约 1h20min）
- 输出文件 `eval_sft_unpruned_baseline_full.json` 尚未写入（完成后一次性写入）

### 已完成的 eval

- `eval_grpo_standard_step50_full.json` — 1319 样本，**已完成** (999KB, 09:34)
- `eval_sft_rasp_20_westd_full.json` — **已完成** (1MB, 05:38)
- `eval_sft_standard_20_westd_full.json` — **已完成** (1MB, 05:41)

### 磁盘

`/root/autodl-tmp`: **213G / 250G (86%)**，剩余 38G。

---
