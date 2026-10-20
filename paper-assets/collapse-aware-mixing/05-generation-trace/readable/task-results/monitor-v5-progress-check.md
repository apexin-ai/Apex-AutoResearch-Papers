# monitor v5 progress check

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_v5_progress_check_20260513T012840_result.json`
- **Structured JSON:** [`988a2513a7c3e1c83e5d.json`](../../sessions/98/988a2513a7c3e1c83e5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成，汇总如下。

---

## mvp_pilot_v5 进度报告

### 1. 进程状态
| PID | 状态 | 已运行 | 说明 |
|-----|------|--------|------|
| 32154 | Ss+ (存活) | 9h37m | bash wrapper，含 `timeout 86400` (24h) |
| 32492 | Rl (运行中) | 9h36m | `pilot_pipeline.py` 主进程 |

GPU：28% 利用率，15.6 GB / 97.9 GB 显存

### 2. 当前阶段
**G0 / 合成数据生成 / 第 293 批 (共 1374 批，21%)**

pipeline 流程进度：
| 阶段 | 状态 | 耗时 |
|------|------|------|
| G0 训练 (90M tokens, 1373 steps) | ✅ 完成 | ~56 min |
| G0 评估 (11 个 checkpoint) | ✅ 完成 | ~2.5h |
| G0 合成数据生成 | 🔄 21% (293/1374) | 已 6h12m，剩余 ~22h |
| G1 训练+评估+生成 | ⏳ 未开始 | 预计 ~32h |
| G2 训练+评估 | ⏳ 未开始 | 预计 ~3.5h |

### 3. G0 关键指标趋势

| Step | Tokens | eff_rank | ppl | entropy_var | unigram_H | coverage |
|------|--------|----------|-----|-------------|-----------|----------|
| 152 | 10M | **670.65** | **13.14** | 2.816 | 6.995 | 0.469 |
| 304 | 20M | 665.62 | 12.80 | 2.824 | 6.968 | 0.469 |
| 456 | 30M | 663.51 | 12.67 | 2.826 | 6.980 | 0.465 |
| 608 | 40M | 662.67 | 12.61 | 2.827 | 6.972 | 0.464 |
| 1216 | 80M | 662.17 | 12.57 | 2.827 | 6.956 | 0.468 |
| 1368 | 90M | 662.16 | 12.57 | 2.827 | 6.995 | 0.472 |
| 1373 | 90M | 662.16 | 12.57 | 2.827 | 6.938 | 0.464 |
| final | — | **662.16** | **12.57** | **2.827** | 6.959 | 0.469 |

**趋势分析：**
- **eff_rank**：670.7 → 662.2，下降 1.3%，训练早期快速下降后收敛（step 760 起基本不变）
- **ppl**：13.14 → 12.57，下降 4.3%，正常收敛
- **entropy_var**：2.816 → 2.827，微增 0.4%，基本稳定
- **unigram_H**：波动在 6.94~7.00 之间，无明显方向性变化
- **coverage**：稳定在 0.464~0.475

G0 阶段尚未出现明显 collapse 信号（符合预期——这是用真实数据训练的基线代）。

### 4. 预估剩余时间
| 阶段 | 预估 |
|------|------|
| G0 合成数据生成完成 | ~22h |
| G1 全周期 | ~32h |
| G2 全周期 | ~3.5h |
| **全部完成** | **~58h** |

### 5. ⚠️ 关键风险
**timeout 将在 ~14h23m 后触发 (24h 上限)，但仅 G0 合成数据生成就还需 ~22h。** 进程会在 G0 合成数据生成完成前被 kill。

### 6. 磁盘
- G0 已占用 59 GB（10 个 checkpoint × ~5.7GB + final_model ~1.9GB）
- 数据盘剩余 99 GB / 250 GB（61% 已用）
- 预计 3 代总共需要 ~180 GB，磁盘可能紧张

---
