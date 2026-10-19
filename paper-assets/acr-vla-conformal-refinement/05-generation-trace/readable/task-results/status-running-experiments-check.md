# status running experiments check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_running-experiments-check_20260522T104025_result.json`
- **Structured JSON:** [`8876d6759684d96c7819.json`](../../sessions/88/8876d6759684d96c7819.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

### 1. Unified CRM Training (bjb1-18228 cuda:1)
- **进度**: Epoch 3/50 刚完成 (6%)
- **指标**: train_loss=0.0172, val_loss=**0.0099** (new best)
- **预计剩余**: ~47 epochs，按当前速度估计还需较长时间

### 2. π0.5 CRM Object Eval (bjb1-32546 cuda:0-2)
- **进度**: 3 seeds 均为 **4/10 tasks 完成**，正在跑第 5 个 task (ketchup)

| Task | seed42 | seed43 | seed44 |
|------|--------|--------|--------|
| alphabet_soup | 100% | 100% | 90% |
| cream_cheese | 80% | 80% | 80% |
| salad_dressing | 80% | 85% | 85% |
| bbq_sauce | 75% | 70% | 65% |
| ketchup | 5/10 running | 4/10 running | 4/10 running |

- **已完成 task 平均**: ~83.8%
- **预计剩余**: ~50% (5/10 tasks 未完成)

### 3. π0.5 CRM Spatial Eval (bjb2-28827 cuda:0-2)
- **进度**: 3 seeds 均为 **5/10 tasks 完成**，正在跑第 6 个 task (bowl_on_ramekin)

| Task | seed42 | seed43 | seed44 |
|------|--------|--------|--------|
| between_plate_and_ramekin | 90% | 85% | 85% |
| next_to_ramekin | 95% | 95% | 90% |
| table_center | 100% | 95% | 95% |
| cookie_box | 100% | 90% | 90% |
| top_drawer | 95% | 90% | 95% |
| bowl_on_ramekin | running | running | running |

- **已完成 task 平均**: ~93.0%
- **预计剩余**: ~50% (5/10 tasks 未完成)

### 4. Precomputes (bjb2-28827)
- **goal (bjb2-28827)**: 日志停在模型加载阶段，但 cache 目录已有 16 个 partial 文件 (0-8000)。可能已完成前段或卡住，需进一步确认
- **long (bjb2-28827)**: **8,800/136,090** (6.5%), 0.06s/sample, **~2.2 小时剩余**
- **long (bjb1-32546)**: **❌ CRASHED** — `RuntimeError: Parent directory /root/autodl-tmp/crm_cache_v5/long does not exist`

### 5. Loss Combined (pid 265357)
- **❌ 进程不存在** — 两台服务器均未找到 pid 265357，已结束或被 kill

---

**需要处理**:
1. bjb1-32546 的 long precompute 崩溃了（缺少目录 `/root/autodl-tmp/crm_cache_v5/long`），需要创建目录后重启
2. bjb2-28827 的 goal precompute 状态不明，建议检查进程是否还活着

---
