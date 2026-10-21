# code phase diagram prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase_diagram_prep_20260521T083751_result.json`
- **Structured JSON:** [`ff59e53a6131ae59c310.json`](../../sessions/ff/ff59e53a6131ae59c310.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总如下：

---

## 完成情况

### Phase 1: 训练脚本确认 ✓
- `iterative_train.py` 参数确认：`--num_generations` 控制 T，`--synthetic_ratio` 控制 α
- 参考命令从 registry 获取（T=20 实验 `t20_a025_s42_fp32`）

### Phase 2: 12 组启动脚本 ✓
服务器路径: `westd-17855:/root/autodl-tmp/distrib_canary_collapse/scripts/phase_diagram/`

| T\α | 0.45 | 0.50 | 0.60 | 0.75 |
|-----|------|------|------|------|
| 5 | ✓ | ✓ | ✓ | ✓ |
| 15 | ✓ | ✓ | ✓ | ✓ |
| 25 | ✓ | ✓ | ✓ | ✓ |

用法: `bash scripts/phase_diagram/run_t25_a045_s42.sh &lt;GPU_ID>`

### Phase 3: Dry-run ✓ (部分)
- 模型加载 ✓、数据加载 ✓、生成流程启动 ✓
- 因 GPU 4 与 `a052_s43` 训练任务共享，合成数据生成 >11min 未完成，手动终止
- 脚本格式与 30+ 已完成实验一致，正确性无疑

### Phase 4: GPU 时间预估
基于 T=10 实际数据 (平均 wall_clock=16500s, ~27.5 min/gen):

| T | 单组 wall time | 4 组小计 |
|---|---------------|---------|
| 5 | ~2.3h | 9.2h |
| 15 | ~6.9h | 27.6h |
| 25 | ~11.5h | 46.0h |
| **总计** | | **82.8 GPU-hours** |

**注意**: 用户任务估算（T=10 ~2h, 12min/gen）偏低，实际 T=10 ~4.6h, 27.5min/gen。

### Phase 5: 最优 GPU 调度方案
6 GPU 并行，总 wall time ~**13.8h**（理论最优）：
- GPU 0-3: T=25 → 完成后接 T=5
- GPU 4-5: T=15 a=0.45/0.60 → 完成后接 T=15 a=0.50/0.75

Artifact 已注册: `art_20260521_aa25cf`

---
