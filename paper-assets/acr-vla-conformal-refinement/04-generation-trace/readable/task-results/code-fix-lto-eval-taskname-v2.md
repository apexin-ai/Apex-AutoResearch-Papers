# code fix lto eval taskname v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-lto-eval-taskname-v2_20260519T051348_result.json`
- **Structured JSON:** [`6cd7e33dc7e55e1a9bda.json`](../../sessions/6c/6cd7e33dc7e55e1a9bda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已注册。总结：

## 结果

### 1. Bug 根因
之前的 evaluate.py 代码中有 `.replace` 调用（可能是 `.replace('_', ' ')` 或类似操作）导致 task name 格式被改变，子串匹配失败。之前版本（`.bak`，349 行）根本没有 `--task_names` 功能。

### 2. 修复
当前代码（今天 12:54 已更新）移除了 `.replace`，匹配逻辑正确：
- `task.name` 格式：`pick_up_the_ketchup_and_place_it_in_the_basket`（下划线连接完整描述）
- 子串匹配 `substr in te["task_name"]` 直接工作

### 3. 验证
`--task_names 'ketchup,milk,orange_juice,salad_dressing,tomato_sauce'` 精确匹配 5 个 held-out tasks：
- `pick_up_the_salad_dressing_and_place_it_in_the_basket` ✓
- `pick_up_the_ketchup_and_place_it_in_the_basket` ✓
- `pick_up_the_tomato_sauce_and_place_it_in_the_basket` ✓
- `pick_up_the_milk_and_place_it_in_the_basket` ✓
- `pick_up_the_orange_juice_and_place_it_in_the_basket` ✓

0 个 train tasks 匹配（alphabet_soup, cream_cheese, bbq_sauce, butter, chocolate_pudding）。日志已确认。

### 4. 实验状态
两个实验已在运行（由之前的 agent 在修复代码后部署），已注册到 registry：
- **`eval-lto-splitA-heldout-v2`** — cuda:1, CRM obs_only, tmux `eval-lto-splitA-heldout-r2`
- **`eval-lto-splitA-vla-only-v2`** — cuda:2, VLA-only baseline, tmux `eval-lto-splitA-vla-only-r2`

VLA-only baseline 第一个 task (salad_dressing) 已完成：30% SR。

---
