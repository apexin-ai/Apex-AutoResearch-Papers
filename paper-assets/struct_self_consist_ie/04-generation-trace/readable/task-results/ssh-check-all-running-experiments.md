# ssh check all running experiments

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_all_running_experiments_20260521T203643_result.json`
- **Structured JSON:** [`188e5f795c07ec44d2e4.json`](../../sessions/18/188e5f795c07ec44d2e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the complete status report:

## GPU 状态总览

| 服务器 | GPU | 实验 | PID | 状态 | 进度 |
|--------|-----|------|-----|------|------|
| autodl-5090 | cuda:0 | exp_fewnerd_mf4v2_s42_v3 | 70770 | **FAILED** | tokenizer TypeError (model_path=None) |
| autodl-5090 | cuda:1 | exp_fewnerd_5epoch_s42 | 63198 | **COMPLETE** ✅ | 37648/37648 |
| autodl-5090 | cuda:2 | exp_fewnerd_5epoch_s123 | 63337 | **COMPLETE** ✅ | 37648/37648 |
| autodl-5090 | cuda:3 | — | — | 空闲 | — |
| autodl-5090-c | cuda:0 | exp_fewnerd_5epoch_s456 | 353735 | **RUNNING** | ~100% (运行1:52, 同规模实验约1:47完成) |
| autodl-5090-c | cuda:1 | exp_fewnerd_mf4v2_s123_v3 | 357394 | **RUNNING** | ~48% (145896/301184, 51min elapsed) |
| autodl-5090-c | cuda:2 | exp_fewnerd_mf4v2_s456_v3 | 357662 | **RUNNING** | ~49% (146376/301184, 52min elapsed) |
| autodl-5090-c | cuda:3 | exp_e2_pretrained_fewnerd_s42 | 346388 | **RUNNING** | ~58% (176336/301184, 2h26m elapsed) |

## 5-epoch 分析结果

### Seed 42
- greedy_f1: **0.7980**
- mv_strict_f1: **0.7935**
- MV Δ (strict): **-0.45pp**
- degeneracy %: **25.7%**
- alpha_crit_eff_strict: **0.5369**
- oracle_f1: **0.8781**

### Seed 123
- greedy_f1: **0.7976**
- mv_strict_f1: **0.7941**
- MV Δ (strict): **-0.35pp**
- degeneracy %: **27.1%**
- alpha_crit_eff_strict: **0.5468**
- oracle_f1: **0.8814**

(LP selection Δ 未在 `recompute_alpha_crit_unified.py` 输出中包含，需要额外脚本)

## 对比 3-epoch 数据

| 指标 | 3-epoch | 5-epoch s42 | 5-epoch s123 | 变化趋势 |
|------|---------|-------------|--------------|----------|
| greedy_f1 | 0.7969 | 0.7980 | 0.7976 | +0.1pp ↑ |
| mv_strict_f1 | 0.7695 | 0.7935 | 0.7941 | +2.4pp ↑↑ |
| MV Δ | -2.74pp | -0.45pp | -0.35pp | 大幅改善 |
| degeneracy | 8.8% | 25.7% | 27.1% | 大幅上升 ↑↑ |
| α_crit_eff_strict | — | 0.5369 | 0.5468 | — |
| oracle_f1 | — | 0.8781 | 0.8814 | — |

**关键发现**: 5-epoch 模型的 MV Δ 从 -2.74pp 收窄到约 -0.4pp，MV 几乎不再损害性能。但 degeneracy 从 8.8% 飙升到 ~26%，说明模型多样性显著降低——更多样本退化为相同输出。greedy_f1 基本持平（+0.1pp）。

## 异常

1. **exp_fewnerd_mf4v2_s42_v3 (autodl-5090 cuda:0) — FAILED**: `TypeError: expected str, bytes or os.PathLike object, not NoneType` — tokenizer 加载失败，model_path 可能为 None。需要检查 checkpoint 路径是否正确。
2. **exp_e2_pretrained_fewnerd_s456 (autodl-5090-c) — CRASHED**: 在 16% (47392/301184) 时 engine 执行 shutdown，aborting 253282 requests。tmux session (PID 345834) 仍在但 Python 进程已死。cuda:2 已被 mf4v2_s456_v3 接管。
3. **autodl-5090 全部 GPU 空闲**: 4 个 GPU 均闲置（0% utilization, 2 MiB），可重新分配任务。

---
