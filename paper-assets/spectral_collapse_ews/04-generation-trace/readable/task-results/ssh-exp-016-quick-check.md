# ssh exp 016 quick check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp_016_quick_check_20260522T152207_result.json`
- **Structured JSON:** [`95455b0c206557846400.json`](../../sessions/95/95455b0c206557846400.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_016 状态报告：**

- **配置**: Phase 1, fixed_mix, r=0.3, pythia-410m, seed=44
- **当前进度**: **Gen 9** 正在生成合成样本，已到 ~16640/35000（约 47%）
- **已完成**: Gen 0–8 全部完成（含训练+评估+保存 checkpoint）
- **日志仍在写入**: 最后修改时间 2026-05-22 23:23:01（刚刚），进程活跃

**Gen 0–8 指标趋势**:

| Gen | eff_rank | ppl | distinct-4 | train_loss |
|-----|----------|------|-----------|------------|
| 0 | 417.55 | 9.55 | 0.7305 | — |
| 1 | 476.91 | 10.19 | 0.6714 | 1.836 |
| 4 | 494.35 | 11.24 | 0.4720 | 1.425 |
| 8 | 511.33 | 12.58 | 0.4286 | 1.265 |

**预计完成时间**: 每个 generation 约占 ~1300 行日志，当前在 Gen 9 生成阶段。Gen 9 生成完还需训练+评估，如果总共跑 10 代（Gen 0–9），预计 **再需 1–2 小时完成**。如果跑更多代则更久。

---
