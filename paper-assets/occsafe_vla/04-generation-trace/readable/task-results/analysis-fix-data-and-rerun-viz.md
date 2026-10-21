# analysis fix data and rerun viz

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fix-data-and-rerun-viz_20260521T195354_result.json`
- **Structured JSON:** [`6f98f5fbba904cdbb09e.json`](../../sessions/6f/6f98f5fbba904cdbb09e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇总如下：

---

## 产出报告

### 1. 实际使用的 50r 文件

| 文件 | Checkpoint | Rollouts/task | Total |
|------|-----------|--------------|-------|
| `vanilla_s0_50r.json` | vanilla_s0/50000 | 50 | 500 |
| `vanilla_s1_50r.json` | vanilla_s1/50000 | 50 | 500 |
| `occ_s2_47500_50r.json` | occ_s2/47500 | 50 | 500 |

### 2. 数据传输记录

- `westd-34685:/root/autodl-tmp/checkpoints/occ_s2/eval_47500_50r.json` → `westd-34685:/root/occsafe_vla/eval_results/occ_s2_47500_50r.json` (cp)

### 3. comparison_stats.json 关键结果 (vanilla 2 seeds vs occ 1 seed)

所有 task 的 p 值 > 0.5，无统计显著差异。细节：

| Task | TSR diff (V-O) | CAR diff (V-O) | 备注 |
|------|---------------|----------------|------|
| T0 | 0.00 | 0.00 | 完全持平 |
| T1 | 0.00 | -0.07 [-0.12,-0.03] | OCC CAR 略优 |
| T2 | -0.04 | -0.03 | OCC 略优 |
| T3 | +0.04 | +0.07 | Vanilla 略优 |
| T5 | +0.13 [-0.04,0.29] | -0.07 | TSR vanilla 优，CAR occ 优 |
| T8 | +0.05 | 0.00 | 差异不大 |
| T9 | -0.03 | 0.00 | 差异不大 |

### 4. instability_stats.json

**OCC 只有 1 seed，std dev 全为 0，levene_p 全为 null——此分析当前无意义。**

Vanilla (N=2): T3 std=0.156 (最不稳定)，其余 0~0.042。

### 5. 剩余数据问题

| 缺失数据 | 现状 | 可否补救 |
|----------|------|---------|
| **vanilla_s2 50r** | 只有 20r (westd-10894)，checkpoint 已删除 | ❌ 无法重跑 |
| **occ_s0 47500 50r** | 只有 20r，**checkpoint 在 westd-34685 可用** | ✅ 可以跑 50r eval |

**建议下一步：** 在 westd-34685 上对 occ_s0 47500 checkpoint 跑 50r eval，拿到后重跑分析可以有 vanilla(2 seeds) vs occ(2 seeds)，seed_instability 分析也才有参考价值。vanilla_s2 50r 永久丢失。

---
