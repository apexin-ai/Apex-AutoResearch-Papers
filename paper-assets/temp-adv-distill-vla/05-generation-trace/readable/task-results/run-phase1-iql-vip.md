# run phase1 iql vip

**temp adv distill vla** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_phase1-iql-vip_20260515T063437_result.json`
- **Structured JSON:** [`4683d829123e28202635.json`](../../sessions/46/4683d829123e28202635.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Step 1 跨任务 MLP 验证结果：**FAILED — 停止后续步骤**

按指令要求，7/9 任务 R² < 0.8，不满足"全部任务 R² > 0.8"的通过条件。**Step 2/3 不执行。**

### Step 1: 跨任务 MLP 验证

| Task | Mean R² | Status |
|------|---------|--------|
| bbq_sauce | 0.5531 | FAIL |
| butter | 0.5127 | FAIL |
| chocolate_pudding | 0.7758 | FAIL |
| cream_cheese | 0.0405 | FAIL |
| **ketchup** | **0.8159** | **PASS** |
| **milk** | **0.9439** | **PASS** |
| orange_juice | 0.5688 | FAIL |
| salad_dressing | 0.1258 | FAIL |
| tomato_sauce | 0.5103 | FAIL |

**通过率**: 2/9 (22%)

### 分析

MLP 在训练任务 alphabet_soup 上 R²=0.985，但跨任务泛化极差：
- **最差**: cream_cheese (R²=0.04)、salad_dressing (R²=0.13) — 几乎无预测能力
- **中等**: bbq_sauce/butter/orange_juice/tomato_sauce 聚集在 R²≈0.5 — 仅捕获粗粒度趋势
- **接近通过**: chocolate_pudding (R²=0.78) — 差 0.02 未达阈值
- **通过**: milk (0.94)、ketchup (0.82) — 可能视觉外观与 alphabet_soup 相似

**根因**: MLP 训练在单任务 VIP 特征上，VIP embedding 空间中不同物体的 progress 映射不同。单任务 MLP 学到的是 alphabet_soup 特有的视觉→进度映射，不是通用的任务进度信号。

### 产出文件
- `artifacts/cross_task_mlp_validation.json` — 完整结果

### 后续建议（供 Director 决策）
1. **Per-task MLP**: 每个任务单独训练 MLP，放弃单一通用 MLP
2. **Multi-task MLP**: 用全部 10 个任务数据联合训练
3. **降低阈值**: 若仅需粗粒度 reward shaping，R²>0.5 可能已够用（5/9 通过）

---
