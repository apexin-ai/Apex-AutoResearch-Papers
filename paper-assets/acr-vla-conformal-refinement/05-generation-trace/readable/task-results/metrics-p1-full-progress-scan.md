# metrics p1 full progress scan

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_metrics_p1-full-progress-scan_20260515T133901_result.json`
- **Structured JSON:** [`4ad6e94dec42b939a863.json`](../../sessions/4a/4ad6e94dec42b939a863.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是全量扫描报告。

---

## P1 全量进度扫描报告 (2026-05-15)

---

### 1. bjb1-32546 — Object eval seed=42

6 张卡全部在用（GPU util 18-23%，VRAM 1.9-2.9 GiB），但只发现 **5 个实验日志**。

| GPU | 实验 | Mode | 进度 | Running Avg | 状态 |
|-----|------|------|------|-------------|------|
| ? | v4-default | acr_vla (perdof) | 3.5/10 | 0.0% (0/30) | Running |
| ? | **v4-obs-only** | crm_obs_only, norm=0.1 | **8/10** | **13.75%** (11/80) | Running |
| ? | v4-scalar | crm_scalar, norm=0.1 | 7.5/10 | 4.3% (3/70) | Running |
| ? | vla-only-k1 | vla_only, K=1 | 0.5/10 | N/A | Running (早期) |
| ? | obs-only-norm02 | crm_obs_only, norm=0.2 | 6.5/10 | 16.7% (10/60) | Running |
| ? | ??? (第 6 张卡) | — | — | — | **日志缺失** |

**obs_only object seed=42 逐 task 明细（8/10 完成）：**
| Task | SR |
|------|----|
| alphabet_soup | 0% |
| cream_cheese | 10% |
| salad_dressing | 20% |
| bbq_sauce | 40% |
| ketchup | 10% |
| tomato_sauce | 0% |
| butter | 10% |
| milk | 20% |
| **Running Avg** | **13.75%** |

---

### 2. bjb1-18228 — seed=43 + misc

| GPU | VRAM | 实验 | 进度 | Running Avg | 状态 |
|-----|------|------|------|-------------|------|
| 0 | 2535M | mag-obsonly-norm03-r2 (spatial) | 7/10 | 47.1% (33/70) | Running（未完成） |
| 1 | 5664M | perdof-object-seed43 | **0/10** | N/A | **加载完毕，无 rollout 输出** |
| 2 | 5200M | obs-only-object-seed43 | 1/10 | 0% (0/10) | Running（极早期） |
| 3 | 5164M | argmin-object-seed43 | 1/10 | 0% (0/10) | Running（极早期） |

**注意：**
- `eval-argmin-object-seed43` 实际运行的是 **reconvla** mode（不是 argmin），文件名与内容不一致
- perdof-seed43 log 停在 "10 tasks loaded"，但 GPU 1 占用 5.6GB 说明进程存活，可能刚启动第一个 rollout
- norm03-r2 在 cuda:0 **未完成**（7/10 tasks），不空闲

---

### 3. bjb2-28827 — Magnitude sweep (6-way, spatial)

| GPU | VRAM | 实验 | 进度 | Running Avg | 状态 |
|-----|------|------|------|-------------|------|
| ? | 2006M | obsonly-norm005 (norm=0.05) | 8/10 | 37.5% (30/80) | Running |
| ? | 2535M | obsonly-norm02 (norm=0.2) | 8/10 | 40.0% (32/80) | Running |
| ? | 2535M | perdof-norm003 (norm=0.03) | 8/10 | 35.0% (28/80) | Running |
| ? | 2535M | perdof-norm005 (norm=0.05) | 7.5/10 | 40.0% (28/70) | Running |
| ? | 2006M | perdof-norm02 (norm=0.2) | 7.5/10 | 35.7% (25/70) | Running |
| ? | 2005M | perdof-norm03 (norm=0.3) | 7.5/10 | 32.9% (23/70) | Running |

---

### 4. bjb2-40593 — obsonly-norm003-b2 (spatial)

| GPU | VRAM | 实验 | 进度 | Running Avg | 状态 |
|-----|------|------|------|-------------|------|
| 0 | 4088M | obsonly-norm003-b2 (norm=0.03) | 4.5/10 | 55.0% (22/40) | Running |

---

## 汇总

### 1. 预计最先完成的实验

**bjb2-28827** 上的 3 个实验（obsonly-norm005, obsonly-norm02, perdof-norm003）都在 **8/10 tasks**，只剩 2 个 task。预计 **1-2 小时内**最先完成。

**bjb1-32546** 的 v4-obs-only 也在 8/10，同样接近完成。

### 2. obs_only object seed=42 当前 SR（最关键指标）

**13.75%**（8/10 tasks 完成，11/80 rollouts 成功）

### 3. 异常

| 异常 | 严重程度 | 说明 |
|------|---------|------|
| bjb1-32546 第 6 张 GPU 无对应日志 | ⚠️ 中 | 6 张卡都有 VRAM 占用，但只有 5 个 log 文件 |
| bjb1-18228 perdof-seed43 无 rollout 输出 | ⚠️ 中 | log 停在 "10 tasks loaded"，GPU 占 5.6GB 说明进程在，可能刚起步或卡住 |
| argmin-seed43 实际跑的是 reconvla | ⚠️ 低 | 文件名与实际 mode 不一致，需确认是否符合预期 |
| bjb1-18228 cuda:0 norm03-r2 未完成 | ℹ️ | 仍在 7/10，cuda:0 不空闲 |
| 无进程死亡或 GPU 利用率为 0 的情况 | ✅ | 所有 GPU 均有 12-23% 利用率 |

---
