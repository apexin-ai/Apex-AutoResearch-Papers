# analysis gpu1 status and plan009 prep

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpu1_status_and_plan009_prep_20260514T110420_result.json`
- **Structured JSON:** [`ba13a8e1ccb8196ee3e5.json`](../../sessions/ba/ba13a8e1ccb8196ee3e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务都完成。

---

### Part A: PID 210299 — **已退出，SUCCESS**

- 运行 1.43h (5134s)，结果存到 `c4_rerun_plan010_results.json`
- 核心结果：

| | A (C4→WT2) | B (WT2→C4) |
|---|---|---|
| bf16 PPL | 9.81 | 15.32 |
| Uniform 4-bit PPL | 15.45 | 35.42 |
| MCKP PPL | 11.29 | 20.56 |
| Δ (uniform-MCKP) | +4.15 | +14.86 |

- 两个方向 bit distribution 完全一致: `{8: 4, 2: 8, 4: 100}`
- Cross-domain agreement: **96.4%** (108/112 heads)

---

### Part B: `/root/ratekv/run_oracle_comparison.py`

**设计选择**:

1. **Per-layer oracle** (方案 A): 每层 4^4=256 种分配全部枚举，固定其他层为 MCKP。用 additive distortion 初筛，top-k 做实际 PPL eval
2. **Random search** (方案 B): 3种 budget-aware 操作（swap/upgrade-downgrade/layer-reshuffle），10K 迭代，找更优分配
3. **Distortion-matched alternatives**: 收集与 MCKP additive distortion 接近但结构不同的分配，用 PPL 直接检验 additive assumption

**Dry-run 结果** (`--skip-ppl`):
- Per-layer oracle: **0/28 层改进** — MCKP 在 additive model 下已经是 per-layer optimal
- Random search: 1357 valid / 10K iterations, **0 improvements** — greedy solver 无优化空间
- 收集到 **20 个 distortion-matched alternatives**，待 PPL eval 检验 additive assumption 是否成立

**预计运行时间**:
- `--skip-ppl`: <1 秒
- 完整 PPL eval: ~45 分钟（~20 次 PPL eval × ~2 min/次 + 模型加载）

**启动命令**:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/ratekv
# GPU 0 或 1 均可（c4_rerun 已完成，GPU 1 空闲）
nohup python run_oracle_comparison.py --gpu 1 > oracle_comparison.log 2>&1 &
```

---
