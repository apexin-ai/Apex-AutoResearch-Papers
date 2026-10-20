# check gpu and taxei eval status

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-and-taxei-eval-status_20260515T163857_result.json`
- **Structured JSON:** [`0ee079620c9af012e376.json`](../../sessions/0e/0ee079620c9af012e376.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU 全景 (autodl-5090)

| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 19.5/32 GiB | 54% | Random seed1 训练 (PID 163144) |
| 1 | 19.5/32 GiB | 96% | Random seed7 训练 (PID 164126) |
| 2 | 17.1/32 GiB | 0% | **刚启动 TaxEI seed1 eval**（模型加载中） |
| 3 | 空闲 | 0% | — |

### TaxEI Eval 结果

**seed7 eval — 已完成 ✓**  success_rate = **61.7%** (29/47)

| 任务类型 | 成功率 |
|----------|--------|
| pick_heat_then_place_in_recep | **7/8 (87.5%)** |
| look_at_obj_in_light | 4/6 (66.7%) |
| pick_and_place_simple | 5/8 (62.5%) |
| pick_cool_then_place_in_recep | 4/7 (57.1%) |
| pick_two_obj_and_place | 4/7 (57.1%) |
| pick_clean_then_place_in_recep | 5/11 (45.5%) |

Registry 已更新 → `v4-taxei-seed7-eval` = DONE/success。

**seed1 eval — 刚重新启动**  
之前 OOM 崩溃（尝试在 GPU 0 上加载，但 GPU 0 被 random 训练占满）。已在 **GPU 2** 重新启动 tmux session `v4-taxei-seed1-eval`。

### Random 训练进度

| 实验 | 进度 | epoch | loss | 预计剩余 |
|------|------|-------|------|---------|
| random seed1 | **2330/3387** (68.8%) | 2.06 | 0.219 | ~34 min |
| random seed7 | **1985/3387** (58.6%) | 1.76 | 0.292 | ~46 min |

两个 random 训练均正常运行，seed1 约 34 分钟后完成，seed7 约 46 分钟后完成。

---
