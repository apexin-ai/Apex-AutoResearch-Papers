# ops check running experiments status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-running-experiments-status_20260515T050728_result.json`
- **Structured JSON:** [`e70eee6fa36d95c26af9.json`](../../sessions/e7/e70eee6fa36d95c26af9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新完成。汇总如下：

## 实验存活状态汇总

### 已完成（RUNNING → DONE）
| 实验 | PID | 原 GPU | 状态 |
|------|-----|--------|------|
| exp_001_eval_3B_d025_v2_para_aligned | 499610 (dead) | cuda:2 | **DONE** ✓ 有 .done 标记 |
| exp_001_eval_3B_d100_v2_aligned_v2 | 477489 (dead) | cuda:0 | **DONE** ⚠ 输出完整但无 .done，需验证 4 个 benchmark |
| exp_008_instruct_05B_eval | 493617 (dead) | cuda:4 | **DONE** ⚠ 输出完整但无 .done，需验证 4 个 benchmark |

### 仍在运行（保持 RUNNING）
| 实验 | PID | GPU | 运行时间 | VRAM |
|------|-----|-----|----------|------|
| exp_001_sft_3B_d100_s123 | 471296 | cuda:5 | 4h56m | 17.9 GB |
| exp_001_sft_05B_d025_s123_v2 | 498153 | cuda:0 | 1h07m | 12.5 GB |
| exp_001_eval_3B_d000_v2_s123_aligned | 492660 | cuda:1 | 1h46m | 8.9 GB |
| exp_001_eval_05B_d000_s42_v7 | 494109 | cuda:4 | 1h41m | 3.7 GB |
| exp_001_eval_3B_d025_v2_aligned | 503791 | cuda:3 | 11m | 8.9 GB |
| exp006-s1only-gsm8k-2pl | 496852 | CPU | 1h20m | — |
| exp006-oracle-arc-4pl-pooled | Stan chain 3 | CPU | ~1h | — |
| exp_004_sim_sweep_v5 | 652931 | local CPU | 4h41m | — |

### QUEUED → RUNNING
- **exp_001_eval_3B_d025_v2_aligned** 实际已在 GPU 3 上运行（PID 503791），registry 已更新为 RUNNING。

### GPU 使用状态
| GPU | 状态 | 进程 | VRAM |
|-----|------|------|------|
| cuda:0 | **占用** | SFT 0.5B d025 s123 | 12.5/24.6 GB |
| cuda:1 | **占用** | Eval 3B d000 s123 | 9.0/24.6 GB |
| cuda:2 | **空闲** | — | 0/24.6 GB |
| cuda:3 | **占用** | Eval 3B d025 aligned | 9.0/24.6 GB |
| cuda:4 | **占用** | Eval 0.5B d000 s42 | 3.7/24.6 GB |
| cuda:5 | **占用** | SFT 3B d100 s123 | 18.0/24.6 GB |

**cuda:2 完全空闲**，可调度新任务。cuda:4 剩余 ~20 GB 也有空间共存小模型。

---
