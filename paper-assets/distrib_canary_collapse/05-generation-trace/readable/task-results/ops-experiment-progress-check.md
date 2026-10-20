# ops experiment progress check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_experiment_progress_check_20260521T041226_result.json`
- **Structured JSON:** [`b5ed537ad7e1561d042b.json`](../../sessions/b5/b5ed537ad7e1561d042b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`save_project_file` 只支持写入 `memory.md`/`paper_framing.md`/`writing_plan.yaml`，报告已写入 `memory.md`。

## 汇总

### 8 个实验进度

| # | 实验 | 服务器 | GPU | 进度 | 当前阶段 | ETA |
|---|------|--------|-----|------|---------|-----|
| 1 | a048_s42_fp32 | 17855 | cuda:0 (0%) | 6/10 | Data gen | ~64 min |
| 2 | **t20_a025_s42_fp32** | 17855 | cuda:1 (67%) | **19/20** | Data gen | **~15 min** |
| 3 | a070_s42_fp32 | 17855 | cuda:2 (82%) | 7/10 | Data gen | ~48 min |
| 4 | scale_69b_a100_s43_bf16 | 17855 | cuda:3 (93%) | 4/10 | Data gen | ~6h |
| 5 | a052_s42_fp32 | 17855 | cuda:4 (75%) | 4/10 | Training 42% | ~1.5h |
| 6 | a046_s42_fp32 | 17855 | cuda:5 (66%) | 4/10 | Training 42% | ~1.5h |
| 7 | a048_s43_fp32 | 19828 | cuda:0 (93%) | 3/10 | Training 42% | ~1.8h |
| 8 | **pythia1b_c4_a100_s43_v2** | 19828 | cuda:1 (96%) | **9/10** | Training 11% | **~30 min** |

### 即将完成 (<30min)
- **t20_a025_s42_fp32** — 最后一代 (19/20)，~15 min
- **pythia1b_c4_a100_s43_v2** — 最后一代 (9/10)，~30 min

### C4 First-Diff MC — 已完成

PID 421289 已结束。核心发现：
- First-diff 有效控制 FPR（raw 在 φ=0.87 时膨胀到 10-12%，diff 控制在 ~5%）
- Power 代价：T=11 损失 44-67%；T=21 + 强信号下 power 0.67-0.74，可接受
- 完整结果在 `artifacts/c4_first_diff_montecarlo.json`

---
