# ssh exp 017 018 urgent check

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp_017_018_urgent_check_20260523T013850_result.json`
- **Structured JSON:** [`3cc6393f97ddabb2cf77.json`](../../sessions/3c/3cc6393f97ddabb2cf77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验进程都存活。汇总：

---

**exp_017** (r=0.2, seed43, cuda:1)
- Generation: **9/10**
- 状态: **running** — 训练阶段，Step 4700，avg_loss=0.9592
- 训练 loss 已收敛（Step 3000 后在 0.96 附近波动），预计很快完成 Gen 9 训练 → 进入 Gen 9 评估 → Gen 10

**exp_018** (r=0.5, seed43, cuda:0)
- Generation: **5/10**
- 状态: **running** — 生成阶段，24320/25000 samples
- Gen 4 已完成的 metrics: eff_rank=503.05, ppl=11.12, distinct4=0.4632
- 进度约 50%，还有 Gen 5-10 要跑

两个进程均存活（共 6 个相关 PID）。exp_017 接近尾声，exp_018 还需要较长时间。

---
