# ops bjb1 18228 redeploy and fill

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-18228-redeploy-and-fill_20260519T055205_result.json`
- **Structured JSON:** [`0cc48fece29d09591d70.json`](../../sessions/0c/0cc48fece29d09591d70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个新任务全部正常加载模型，无报错。

## 产出

### Task A: VLA-only baseline r3
- **已启动** `eval-lto-splitA-vla-only-r3` on GPU 1 (与 heldout-r2 共享)
- `--task_names` 功能正常（代码中无 `.replace("_", " ")`，直接按逗号拆分 + substring 匹配）

### Task B: 加跑实验（去重后替代方案）

原建议 4 个实验全部已 DONE 或 RUNNING，替换为：

| GPU | 原有实验 | 新增实验 | 补充目标 |
|-----|---------|---------|---------|
| 0 | k5-seed47 (4.2GB) | **obs_only ε=0.05 seed48** | obs_only ε=0.05 → n=5 |
| 1 | heldout-r2 (2.9GB) | **VLA-only r3** (Task A) | LTO baseline |
| 2 | argmin-k5-seed43 (4.7GB) | **perdof ε=0.05 seed47** | perdof ε=0.05 → n=5 |
| 3 | k5-seed46 (4.2GB) | **perdof ε=0.03 seed47** | perdof ε=0.03 → n=6 |

每张卡现在跑 2 个实验，总 VRAM ~8-10GB/24GB。

---
