# ops pipeline readiness check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_pipeline-readiness-check_20260514T122031_result.json`
- **Structured JSON:** [`5d2bc7cb91f17000a580.json`](../../sessions/5d/5d2bc7cb91f17000a580.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Pipeline 就绪状态报告

### exp-002 Signal Pipeline

**进度: 0/27 任务完成（0/9 for 0.5B 模型）**

- 当前正在跑 **task 1/9**：`Qwen2.5-0.5B_d000_s42 / mmlu`（signals: embedding, minkpp, selfcritique），GPU 0
- PID 353390，已运行 ~2.5 小时 CPU time
- 已产出的中间文件（d000_s42 目录）：
  - `signal_embedding_mmlu.json` (6MB) ✅
  - `signal_embedding_gsm8k.json` (568KB) ✅ （前次运行遗留）
  - `signal_embedding_arc_challenge.json` (515KB) ✅ （前次运行遗留）
  - `signal_minkpp_mmlu.json` (2.1MB) ✅
  - selfcritique — **未完成，当前正在计算**
- `d005_s42` 目录仅有 embedding_mmlu（前次运行遗留），`d100_s42` 目录不存在
- 0.5B 需 9 tasks（3 dosages × 3 benchmarks），全部完成后还有 1.5B 和 3B（各 9 tasks）
- **预估**：当前 task 还需 ~30min-1hr 完成 selfcritique，整个 0.5B 约需 20+ 小时，全部 27 tasks 可能需 3-5 天

### exp-003 RRF Aggregation

**不存在独立 exp003 目录。RRF 代码在 `exp002/aggregate_rrf.py` 中。**

代码 ✅ 就绪：
- RRF fusion（k=60），auto-detect available signals
- 支持从多个 signal JSON 文件 load + merge
- 支持 ablation variants（单信号、等权平均）

### exp-006 IRT Calibration + Baselines

**代码 ✅ 全部就绪**

| 文件 | 状态 |
|------|------|
| `run_irt_calibration.py` — CmdStanPy 4PL+γ MCMC | ✅ |
| `run_irt_stan.py` — 备用 Stan pipeline | ✅ |
| `run_all_baselines.py` — 统一运行入口 | ✅ |
| `baselines.py` — 7 baselines 统一接口 | ✅ |
| `evaluate_calibration.py` — MAE/coverage/sharpness/kendall_tau | ✅ |

7 baselines 全部实现：B0 Raw, B1 Remove-rescore, B2 Single-signal 2PL+γ, B3 Vanilla 4PL, B4 Linear regression, B5 Emperor's mitigation, B6 DCR fuzzy

Dry-run 已通过（`dryrun_no_stan.json` 有完整合成数据验证结果）

### Stan Models

4 个 .stan 模型 + 已编译二进制 ✅：`contam_irt_4pl_simple`, `contam_irt_4pl`, `contam_irt_2pl_gamma`, `vanilla_4pl`

### 阻塞项

| 阻塞 | 影响 |
|------|------|
| **exp-002 signal 产出未完成** | exp-003 RRF 和 exp-006 IRT 都依赖 signal 数据，无法运行真实数据 |
| 仅 0.5B 在跑，1.5B/3B 未开始 | 完整实验需 27 tasks，当前 0/27 completed |
| exp-001 eval 仍在并行跑（d005 aligned, 1.5B para, 3B d100） | 这些 eval 结果也是 exp-002 的前置依赖 |

---
