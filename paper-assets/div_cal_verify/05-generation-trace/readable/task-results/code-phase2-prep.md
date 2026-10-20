# code phase2 prep

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2_prep_20260512T202818_result.json`
- **Structured JSON:** [`e93560eec850da60642a.json`](../../sessions/e9/e93560eec850da60642a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结：

### 产出

**`/root/div_cal_verify/run_phase2.sh`** — 可直接执行
- 3 方法串行：RGDS → External-only → Uncurated
- 超参：5M tokens/gen, 3 epochs, lr=5e-5, 6 generations
- 双卡 `--gpu_ids 0,1`（generator cuda:0, student cuda:1）
- 输出到 `/root/autodl-tmp/div_cal_verify/results_phase2/{method}/`
- 日志到 `~/runs/div_cal_verify/phase2_{method}.log`

### Bug 修复

**`run_mvp.py` 第 192-195 行**：Contriever 改为所有方法都加载（原来只对 rgds/external_only 加载）。

根因：uncurated 方法 `contriever_model=None` → `run_evaluation` 跳过 `rank_correlation` 计算 → 后续 print `metrics['rank_correlation']` KeyError 崩溃。旧日志 `mvp_uncurated_v1.log` 确认了这个崩溃路径（虽然具体 traceback 是更早版本在 `compute_rank_correlation` 内部崩的，guard 加了之后变成 KeyError）。

修复：Contriever 是评估指标（rank correlation），不是选择方法，所有方法都应计算，且 CPU 加载开销极小。备份在 `run_mvp.py.bak`。

### Phase 1 状态
- PID 93696 存活，RGDS gen_0 目录已创建，尚无 metrics.json
- 日志仅一行 `torch_dtype` 弃用警告 → 仍在 gen_0 早期
- **Phase 1 的 uncurated 运行也会受益于此修复**（RGDS 跑完后才轮到 uncurated）

---
