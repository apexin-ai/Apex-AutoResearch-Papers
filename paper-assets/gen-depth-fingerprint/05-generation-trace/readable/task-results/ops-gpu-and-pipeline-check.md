# ops gpu and pipeline check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-and-pipeline-check_20260515T174738_result.json`
- **Structured JSON:** [`86b4a62a90e7f25cf6ec.json`](../../sessions/86/86b4a62a90e7f25cf6ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态表

| GPU | 显存占用 | 利用率 | 进程/任务 |
|-----|---------|--------|----------|
| 0 | 3 / 32607 MiB | 0% | **空闲** |
| 1 | 627 / 32607 MiB | 0% | PID 223500 — `human_edit_robustness.py` (1h44m) |
| 2 | 3977 / 32607 MiB | 42% | PID 226113 — `run_high_only.py` (1h00m) |
| 3 | 3979 / 32607 MiB | 44% | PID 222783 — `sampling_ablation.py --phase all` (1h46m) |

**GPU 0 完全空闲。**

---

### OLMo Instruct Pipeline — 已全部完成

- Step 1 generation: `generations_shard0.jsonl` — 4429 条 ✓
- Step 2 features: `features_olmo-2-0425-1b-instruct.csv` — 4430 行 ✓
- Step 3 evaluation: `review_p1c_olmo_instruct.json` — 已生成 ✓

结论：instruct tuning 显著削弱 depth signal（instruct LOGO F1 = 0.338 vs base OLMo = 0.763，Δ = -0.425）。**无需手动启动任何步骤。**

---

### Human Edit 重跑

- PID 223500 **仍在运行**（1h44m），当前在 Phase 4: LOGO evaluation（`/tmp/human_edit_robustness.log`）
- PID 228872 `wait_and_rerun.sh`（运行 37min）正在等 223500 结束后自动触发重跑
- GPU 1 利用率 0% 说明当前处于 CPU-bound 的 LOGO 评估阶段，非闲置

---

### Sampling Ablation 进度

| GPU | 配置 | 进度 | 速率 | 预估剩余 |
|-----|------|------|------|---------|
| 2 | `high_t10_p095` | 301/996 (30%) | ~13s/it | ~2.5h |
| 3 | `low_t05_p08` | 480/996 (48%) | ~14s/it | ~2h |

cuda:3 跑的是 `--phase all`，`low_t05_p08` 完成后可能还有 default 配置要跑。

---
