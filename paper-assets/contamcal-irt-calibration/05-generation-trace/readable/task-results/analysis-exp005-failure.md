# analysis exp005 failure

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp005-failure_20260514T031535_result.json`
- **Structured JSON:** [`13dea582600122feb7af.json`](../../sessions/13/13dea582600122feb7af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 部分结果
**无可用结果。** output_v2/ 空目录。唯一完成的 ME fit（σ_e=0.1, seed=42, 5713s）因 `run_single` 要求两个模型都完成才返回结果，Simple 崩溃后整个 run 丢失。

### v3 修复内容

| 问题 | v2 | v3 修复 |
|------|-----|---------|
| /tmp 磁盘耗尽 | CmdStanPy 默认写 `/tmp`（3.9GB tmpfs） | `output_dir=output_v3/stan_output/`，写本地磁盘（51GB可用） |
| ME 模型欠识别 | 全 ME：10231参数 vs 9000观测，Rhat=1.945 | 换 analytic ME：1231参数，Rhat=1.006，0 divergences |
| ME 失败连带 Simple 丢失 | ME 先跑，崩了 Simple 没结果 | Simple 先跑，ME 后跑 |
| 无断点续跑 | 全部重来 | 加载已有 results.json，跳过已完成的 (σ_e, seed) |
| 磁盘累积 | chain CSV 不清理 | 每次 fit 后 `shutil.rmtree` 清理 chain CSV |
| 去掉了 Part B | Post-hoc noise injection 部分（不影响核心实验） | — |

### v3 重跑命令

```bash
cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation && \
nohup /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/mvp_simulation/.venv/bin/python \
  run_noise_propagation_v3.py \
  --output-dir output_v3 \
  --base-seed 42 \
  --n-seeds 5 \
  > exp005_v3.log 2>&1 &
echo $!
```

### 预计运行时间

- Simple model: ~5 min/fit × 25 fits = **~125 min**
- Analytic ME: ~23 min/fit × 25 fits = **~575 min**
- **总计: ~11-12 小时**（本地 CPU）

编译耗时约 2 min（若已编译过的 exe 存在则跳过）。

---
