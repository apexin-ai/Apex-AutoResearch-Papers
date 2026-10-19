# probe v7 step5000 monitor

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_probe_v7-step5000-monitor_20260516T123123_result.json`
- **Structured JSON:** [`b0eda7c6a0341b862f67.json`](../../sessions/b0/b0eda7c6a0341b862f67.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Probe A 结果报告 — v7 contrastive checkpoint-5000

### 事件：训练中磁盘满导致崩溃

原始训练在 step 5000 保存 checkpoint 时因根分区 100% 满崩溃（`torch.save` I/O error）。
- **根因**：17GB outputs 放在 30GB 根分区
- **修复**：已将 outputs 移到数据盘 `/root/autodl-tmp/`，创建 symlink
- **训练已重启**，从 step 0 重新跑完到 step 5000

---

### Probe A: Fixed Image, Swap Instruction

| Pair | cos | L2 |
|------|-----|-----|
| inst 0 ("bbq sauce → basket") vs inst 1 ("black bowl near cookie → plate") | **0.476** | 4.748 |
| inst 0 ("bbq sauce → basket") vs inst 2 ("black bowl in drawer → plate") | **0.648** | 4.267 |
| inst 1 vs inst 2 (两个 "black bowl" 变体) | **0.894** | 2.433 |

**cos 范围: [0.476, 0.894]**

### Probe B: Natural Cross-Task Observations

| Pair | cos | L2 |
|------|-----|-----|
| task 0 vs 1 | 0.449 | 2.750 |
| task 0 vs 2 | 0.553 | 2.696 |
| task 1 vs 2 | 0.741 | 2.266 |

### Step 4000–5000 训练指标

| Step | task_loss | ctr_loss | ib_loss | scorer_mean | scorer_std |
|------|-----------|----------|---------|-------------|------------|
| 4000 | 0.1055 | 1.521 | 0.667 | 0.324 | 0.354 |
| 4200 | 0.0780 | 1.440 | 0.791 | 0.271 | 0.350 |
| 4400 | 0.0915 | 0.818 | 0.690 | 0.301 | 0.348 |
| 4600 | 0.0778 | 1.390 | 0.756 | 0.281 | 0.348 |
| 4800 | 0.0757 | 1.461 | 0.698 | 0.314 | 0.361 |
| 5000 | 0.0776 | 1.224 | 0.717 | 0.291 | 0.346 |

**趋势**：task_loss 稳定在 0.08 附近，ctr_loss 稳定 ~1.2-1.5，scorer_mean/std 稳定在 0.29/0.35 — 无退化迹象。

---

### 判定结论: ✅ 非常好 — Conditioning 持续有效

- **关键判据**：不同语义的任务对 cos ≤ 0.65（远低于 0.8 阈值）
- **唯一接近 0.9 的 pair (cos=0.894)** 是两个语义高度相似的任务（同为 "pick up black bowl and place on plate"，只是来源位置不同）— 这是**符合预期的行为**，相似任务应该产生相似的 importance map
- β warmup 结束后（step 2000+）IB loss 没有导致 scorer 退化为 position prior
- Probe B 进一步确认：不同观测下的 importance map 也是 task-dependent (cos 0.45-0.74)

**训练可继续运行到 20000 steps，无需干预。**

---
