# exp vanilla react baseline

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_vanilla-react-baseline_20260514T080922_result.json`
- **Structured JSON:** [`f6bc29a4900743aa038c.json`](../../sessions/f6/f6bc29a4900743aa038c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 已全部释放。评测完成，汇报如下：

---

## Vanilla ReAct Baseline 评测报告

**模型**: Qwen3-8B (zero-shot, no SFT, no adapter, `enable_thinking=False`)  
**数据集**: ALFWorld valid_unseen (47 tasks)  
**配置**: `max_new_tokens=512`, `--no_inject`, `CUDA_VISIBLE_DEVICES=1`

### 1. Overall 成功率

**20/47 = 42.6%**

### 2. Per-task-type 成功率

| Task Type | Success | Total | Rate |
|---|---|---|---|
| pick_heat_then_place_in_recep | 5 | 8 | **62.5%** |
| look_at_obj_in_light | 3 | 6 | 50.0% |
| pick_and_place_simple | 4 | 8 | 50.0% |
| pick_clean_then_place_in_recep | 5 | 11 | 45.5% |
| pick_two_obj_and_place | 3 | 7 | 42.9% |
| pick_cool_then_place_in_recep | 0 | 7 | **0.0%** |

`pick_cool_then_place_in_recep` 全军覆没（7/7 FAIL），模型在 zero-shot 下完全无法完成"冷却后放置"任务流程（需要 open fridge → put in → close → wait → open → take out 的多步操作）。

### 3. 平均步数

| 指标 | 值 |
|---|---|
| 全部任务平均步数 | **37.2** |
| 成功任务平均步数 | **20.0** |
| 失败任务步数 | 50（全部触达上限） |

成功任务中，最快 5 步（pick_and_place_simple-Mug），最慢 47 步（look_at_obj_in_light-Bowl）。所有失败任务都耗尽了 50 步上限。

### 4. 评测耗时

约 **2 小时**（结束时间戳 08:45:02 UTC）。FAIL episode 每个约 3 分钟（50 步推理），成功 episode 几秒到 2 分钟不等。

### 5. 遇到的问题和修复

| 问题 | 原因 | 修复 |
|---|---|---|
| SSH 超时导致进程中断 | 用 `tee` 管道保持了 SSH 连接依赖 | 改用 `nohup ... > log 2>&1 &` |
| CUDA OOM 第二次启动失败 | 第一次进程未完全释放 GPU 显存 | `kill -9` 旧进程后重新启动 |
| valid_unseen 只有 47 个任务 | 数据集 split 实际大小，非 134 | 无需修复，脚本自动适配 |

---

结果文件已保存在服务器 `/root/autodl-tmp/tax_error_inject_agent/eval_results/vanilla_react_baseline.json`，GPU 显存已全部释放。

---
