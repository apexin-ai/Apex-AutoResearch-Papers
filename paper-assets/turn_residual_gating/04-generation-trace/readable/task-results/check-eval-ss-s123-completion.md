# check eval ss s123 completion

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_ss_s123_completion_20260523T180141_result.json`
- **Structured JSON:** [`3763ad8ed089ed11dddb.json`](../../sessions/37/3763ad8ed089ed11dddb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. 进程状态
- PID 109008, 110052: **已退出**（eval 完成）
- PID 108997 (gpu_chain): **仍在运行**（37 min），已推进到 Step 2

### 2. GPU 当前状态
- **PID 112418** — `train_phase2_v8b.py --seed 456 --resume runs/d048_ss_s456/epoch_0`，运行 2m18s，占用 **66122 MiB**
- SS s456 resume 训练已启动

### 3. SS s123 Eval 完成状态

**全部完成**: TF (ours + dongre) + AR (beta 0/3/5) + base AR

### 4. 完整 AR 结果

| Model | Beta | Mid-GAR | Std | PPL | n |
|-------|------|---------|-----|-----|---|
| **Base** | 0.0 | 0.0186 | 0.0166 | 1.4468 | 39 |
| **SS s123** | 0.0 | **0.4231** | 0.0601 | 1.4408 | 39 |
| **SS s123** | 3.0 | **0.5903** | 0.0485 | 1.6070 | 39 |
| **SS s123** | 5.0 | **0.7174** | 0.0600 | 1.7852 | 39 |

对比 SS s42 (from CI summary):

| Model | Beta | Mid-GAR | 95% CI |
|-------|------|---------|--------|
| SS s42 | 0.0 | 0.3471 | [0.327, 0.366] |
| SS s42 | 3.0 | 0.5933 | [0.574, 0.613] |
| SS s42 | 5.0 | 0.7170 | [0.696, 0.738] |

**s123 vs s42**: beta=0.0 s123 大幅高于 s42 (+0.076)，beta=3.0 基本持平 (-0.003)，beta=5.0 基本持平 (+0.0004)。

### 5. TF 结果 (2-turn teacher-forcing, 200 convs)

| Variant | Turn 1 GAR | Turn 2 GAR | PPL |
|---------|-----------|-----------|-----|
| ours | 0.5536 | 0.5193 | 2.6123 |
| dongre | 0.4106 | 0.3935 | 2.6123 |

### 6. Bootstrap CI
`d048_summary_ci_wilcoxon.json` 仅包含 s42 seed 的数据，未更新 s123。s123 没有单独生成 bootstrap CI 文件。

---
