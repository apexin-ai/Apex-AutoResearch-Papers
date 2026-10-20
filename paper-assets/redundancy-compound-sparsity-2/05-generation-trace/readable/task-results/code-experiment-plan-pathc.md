# code experiment plan pathc

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_experiment-plan-pathc_20260512T142124_result.json`
- **Structured JSON:** [`b1c3821ab4af33f59440.json`](../../sessions/b1/b1c3821ab4af33f59440.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个脚本全部 `--help` 通过。

**完成情况：**

**任务 1 — 实验计划**：写入 `experiment_plan.yaml`，覆盖 14 个实验，6 个阶段：
- Phase 0: 2 个 sanity gate（reasoning traces + wikitext 32K），已在 registry 运行中
- Phase 1: PPL budget sweep（30/50/70%）
- Phase 2: 2 个 baseline 对比（H2O + R-KV）
- Phase 3: 4 个 ablation（gamma / budget / grace / per-head）
- Phase 4: MATH-500 reasoning eval
- Phase 5: scaling（32K/64K）+ throughput

每个实验标注了 priority、depends_on、success_criterion、estimated_hours。总计 ~60 GPU-hours / ~30h wall-clock。

**任务 2 — 评估框架骨架**（远程 `/root/carc/`）：
- `eval_ppl.py` — 支持 full/ema/random/recency 四种方法，多 budget ratio，输出 JSON + degradation%
- `eval_math500.py` — 集成 CARCGenerator，支持多 budget ratio 对比，计算 retention ratio
- `run_ablation.sh` — 参数化 sweep launcher，支持 `--sweep gamma/budget/grace/perhead/all`

---
