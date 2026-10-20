# check phi3v r2 and figure fix

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phi3v_r2_and_figure_fix_20260520T022821_result.json`
- **Structured JSON:** [`7c1a4ff5af5753b5aefc.json`](../../sessions/7c/7c1a4ff5af5753b5aefc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. phi3v_r2_action_probe — 进行中（Feature Extraction 阶段）

- **Phase 1 Feature Extraction**：正在提取第 10/10 个 task (`turn_on_the_stove`)
- 已完成 9 个 task 的 feature 文件（共 ~8.5GB），第 10 个正在写入（`.h5.tmp` 当前 ~476MB）
- 结果文件尚未生成，Phase 2（probe 训练）还没开始
- GPU 0 占用 8705 MiB，利用率 55%
- **预计剩余时间**：最后一个 task 的 feature 文件大约还需 1-2 分钟写完。之后进入 Phase 2 probe 训练（33 layers × 5 seeds），预计还需 10-20 分钟。**总计约 15-25 分钟完成。**

### 2. specificity 图表修复 — 已完成

- 图表已于 **09:55** 生成：
  - `results/figures/fig_specificity_bootstrap_30seeds.pdf` (17KB)
  - `results/figures/fig_specificity_bootstrap_30seeds.png` (48KB)

---
