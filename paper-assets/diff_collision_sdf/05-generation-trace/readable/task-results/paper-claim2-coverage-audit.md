# paper claim2 coverage audit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_claim2_coverage_audit_20260525T074050_result.json`
- **Structured JSON:** [`f4c468f7d4b23d880699.json`](../../sessions/f4/f4c468f7d4b23d880699.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是审计结果。

---

## Claim 2 证据覆盖审计

> **注意**: paper_framing.md 中 Claim 2 定义为 "Task Capability vs Safety Anti-correlation"，而非 "Generalizability"。跨模型泛化性对应的是 **Reviewer Concern R1**（最致命）以及 Claim 1 (Fake Safety) 的跨模型证据。以下按用户要求审计 fake safety 跨模型泛化的证据覆盖。

---

### 1. 证据覆盖矩阵

| Model Family | TSR | CAR | real_CAR | fake_rate | displacement | Episodes | 状态 |
|---|---|---|---|---|---|---|---|
| **Pi0 (A1-SDF)** | 0% | 91.5% | ≈0.4% | 99.6% | 0.0027 | 800 | ✅ 完整 |
| **Pi0 (LoRA baseline)** | 0% | 82% | — | 未量化 | 0.01 | 200 | ⚠️ 缺 fake_rate |
| **Pi0 (Full-FT baseline)** | 0.5% | 83% | — | 未量化 | 0.027 | 200 | ⚠️ 缺 fake_rate |
| **Pi0.5 (baseline)** | 73-76% | 25-28% | 0.5% | 98.2% | 0.15 | 600 (3-seed) | ✅ 完整 |
| **Pi0.5+A1** | ? | ? | ? | ? | ? | — | ⏳ 4 evals RUNNING |
| **OpenVLA (base)** | — | — | — | — | — | 0 | ❌ 无数据 |

**关键指标缺失**：
- Pi0 baseline 变体缺少 `fake_safe_rate` 的显式计算（displacement 数据有，但未做阈值分析）
- OpenVLA 完全空白

---

### 2. 缺口清单

| 优先级 | 缺口 | 影响 | 工作量 |
|---|---|---|---|
| **P0 (必须)** | OpenVLA zero-shot eval + displacement 分析 | 没有第 3 个 model family，R1 无法防御 | ~5h inference (200 ep) |
| **P0 (必须)** | Pi0 baseline fake_rate 显式量化 | 当前仅 A1 有 fake_rate，需证明 fake safety 不是 A1 引入的而是 Pi0 固有的 | 重新分析已有数据，~30min |
| **P1 (应做)** | 统一对比表（所有模型 × 统一阈值 × 统一指标） | 没有 apples-to-apples 对比，reviewer 会质疑 | 脚本编写 ~2h |
| **P1 (应做)** | OpenVLA fine-tuned 变体 eval | base OpenVLA 可能 TSR≈0（类似 Pi0），需要 fine-tuned 版本才有说服力 | ~5h inference |
| **P2 (加分)** | spatial_bowl 跨模型对比 | 目前仅 object_pudding 有多模型数据 | 取决于 spatial_bowl 训练进度 |

---

### 3. 核心问题

**当前最大弱点：Pi0 和 Pi0.5 来自同一 model family (Physical Intelligence)**。

- Pi0 = 3.5B flow matching model
- Pi0.5 = 同家族更强版本

Reviewer 可以说 "这只证明了 Pi 系列的问题，不是 VLA 的普遍问题"。**必须有一个非 PI 家族的模型**。

**Pi0 证据的说服力有限**：TSR=0% 意味着模型根本不动，fake safety 是 trivially expected（不动 = 不碰撞）。这不是 "fake safety 现象" 的有力证据，更像是 "坏模型的自然结果"。Pi0.5 的证据更有价值——模型能完成 73% 的任务，但 safe episodes 中 98.2% 仍是 fake。

---

### 4. 最小投入方案

让 Claim 2（泛化性）达到投稿标准的最小路径：

**Step 1 (立即, ~30min)**: 对 Pi0 baseline 已有的 200ep 数据重新计算 fake_safe_rate，使用与 A1 相同的 displacement 阈值。证明 fake safety 在 Pi0 所有训练方式中都存在。

**Step 2 (今天, ~5-8h)**: 完成 OpenVLA base eval 200ep。即使 OpenVLA base TSR≈0（类似 Pi0），只要 displacement 分析显示 safe episodes 是 frozen 的，就能写 "fake safety observed across 3 architecturally distinct VLA families"。

**Step 3 (可选但推荐, +5h)**: 跑 OpenVLA fine-tuned (openvla-7b-finetuned-libero-object) eval。如果 fine-tuned 版有 TSR>0 且仍有高 fake_rate，论证力度大幅增强（类比 Pi0.5）。

**Step 4 (1-2h)**: 编写统一对比表生成脚本，输出:

```
Model Family | Architecture | TSR | CAR | real_CAR | fake_rate | N_episodes
Pi0 (A1)     | 3.5B flow    | 0%  | 91.5% | 0.4% | 99.6% | 800
Pi0 (base)   | 3.5B flow    | 0%  | 82%   | X%   | Y%    | 200  
Pi0.5        | Pi0.5        | 74% | 27%   | 0.5% | 98.2% | 600
OpenVLA      | 7B ViT+LLM   | ?%  | ?%    | ?%   | ?%    | 200
```

**完成 Step 1-3 后，Reviewer #37 的接受率估算从 ~40% → ~55-65%**（2 tasks + 3 models 档位）。

---
