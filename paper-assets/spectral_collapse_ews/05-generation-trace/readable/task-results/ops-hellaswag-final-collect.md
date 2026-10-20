# ops hellaswag final collect

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_hellaswag-final-collect_20260521T111731_result.json`
- **Structured JSON:** [`868d3240e9e8bd384ef8.json`](../../sessions/86/868d3240e9e8bd384ef8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

### 3-SEED SUMMARY（2-seed only, seed43 全部缺失）

| Gen | Seed42 | Seed43 | Seed44 | Mean | Std |
|-----|--------|--------|--------|------|-----|
| 0 | 0.4130 | MISS | 0.4130 | 0.4130 | 0.0000 |
| 1 | 0.3897 | MISS | 0.3911 | 0.3904 | 0.0010 |
| 2 | 0.3764 | MISS | 0.3841 | 0.3803 | 0.0054 |
| 3 | 0.3658 | MISS | 0.3721 | 0.3690 | 0.0045 |
| 4 | 0.3558 | MISS | 0.3554 | 0.3556 | 0.0003 |
| 5 | 0.3439 | MISS | 0.3418 | 0.3428 | 0.0015 |
| 6 | 0.3311 | MISS | 0.3315 | 0.3313 | 0.0003 |
| 7 | 0.3187 | MISS | 0.3191 | 0.3189 | 0.0003 |
| 8 | 0.3103 | MISS | 0.3157 | 0.3130 | 0.0038 |
| 9 | 0.3009 | MISS | 0.3033 | 0.3021 | 0.0017 |
| 10 | 0.2951 | MISS | 0.3015 | 0.2983 | 0.0046 |

### Paper Values (2-seed)
- Gen 0 mean: **0.4130**, Gen 10 mean: **0.2983**, drop: **27.8%**
- Gen 2 mean: 0.3803 | Gen 5 mean: 0.3428 | Gen 7 mean: 0.3189

### 缺失项：Seed43 全部 11 个 gen (gen0–gen10)

Seed43 的 eval 目录存在，但里面只有 lm-eval 的 cache 子目录（如 `__root__autodl-tmp__spectral_collapse_ews__checkpoints_phase1__pure_collapse_seed43__gen_0`），没有 `results.json`。没有 eval 进程在运行。说明 seed43 的 lm_eval 评估从未成功完成——可能中途失败或被中断。

---
