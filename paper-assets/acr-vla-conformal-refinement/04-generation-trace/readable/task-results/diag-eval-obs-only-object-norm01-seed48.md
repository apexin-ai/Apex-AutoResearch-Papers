# diag eval obs only object norm01 seed48

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-obs-only-object-norm01-seed48_20260520T195415_result.json`
- **Structured JSON:** [`a954f7bd42b242ccaa06.json`](../../sessions/a9/a954f7bd42b242ccaa06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验状态：retry 运行中途崩溃（进程被杀），但前次完整结果已存在。**

### 详情

1. **retry 运行（本次）**：日志 `eval-obs-only-object-norm01-seed48.log` 仅 32 行，实验在第 6 个 task（tomato_sauce）的 rollout 5/10 处停止，无错误信息，无 JSON 产出。创建时间 02:36，最后修改 03:36（运行约 1 小时后进程消失）。日志无任何错误输出——进程被静默杀死，最可能是 OOM kill。

2. **前次完整结果已存在**：`eval_object_obs_only_norm01_seed48.json`（2026-05-18 创建，不同命名格式），包含完整 10 tasks × 10 rollouts 结果：

| Task | SR |
|------|-----|
| alphabet_soup | 0% |
| cream_cheese | 0% |
| salad_dressing | 0% |
| bbq_sauce | 40% |
| ketchup | 10% |
| tomato_sauce | 20% |
| butter | 20% |
| milk | 30% |
| chocolate_pudding | 30% |
| orange_juice | 30% |
| **Overall** | **18%** |

3. **cron 判定正确**：retry 进程确实死了，不是误判。

### 结论

- **失败原因**：大概率 OOM kill（无错误日志、进程静默消失的典型特征）
- **是否需要重跑**：**不需要**。前次完整结果（SR=18%）已存在于 `eval_object_obs_only_norm01_seed48.json`，数据完整可用
- **注意**：两次运行的命名不一致（`eval_obs_only_object_` vs `eval_object_obs_only_`），如果有汇总脚本需确认能匹配到已有的 JSON 文件

---
