# diagnosis gemma task list verify

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_gemma-task-list-verify_20260520T081439_result.json`
- **Structured JSON:** [`c2b5337b01cb1ac387df.json`](../../sessions/c2/c2b5337b01cb1ac387df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### Gemma 脚本 task list：**正确，与论文 11 tasks 完全一致**

**GPU0** (`scripts/run_gemma_gpu0.sh`): 6 tasks
- chemistry-mix, find-animal, find-non-living-thing, freeze, grow-fruit, identify-life-stages-1

**GPU1** (`scripts/run_gemma_gpu1.sh`): 5 tasks
- identify-life-stages-2, inclined-plane-determine-angle, lifespan-longest-lived, lifespan-longest-lived-then-shortest-lived, measure-melting-point-unknown-substance

### boil/melt 的来源

`boil` 和 `melt` 来自**另一个脚本** `scripts/run_extended_validation_gpu0.sh`（extended task validation），不在 GPU0/GPU1 脚本中。它们写到了同一个输出目录 `results/gemma_scienceworld_counterfactual/`，造成混淆。

- `boil/`: 20 episodes 已完成（最后修改 16:09）
- `melt/`: 1 episode 已完成，可能仍在跑（最后修改 16:12）

### 严重问题：11-task 脚本全部失败

两个 GPU 脚本在 14:30 启动后，**所有 task 都 crash 了**：
- `chemistry-mix`：Gemma chat template Jinja 渲染报错（`apply_chat_template` 失败）
- `find-animal`：被 Killed（疑似双 GPU 同时加载模型时 OOM）
- `inclined-plane-determine-angle`：同样被 Killed
- 后续 task 也逐一失败

结果目录中 11 个 task 的子目录**全部为空**（只有 6 bytes 的空目录），没有产出任何 episode 数据。

### 总结

| 项目 | 状态 |
|------|------|
| 脚本 task list | 正确（11 tasks） |
| boil/melt | 来自 extended_validation 脚本，不影响论文 task list |
| 论文 11 tasks 的实际数据 | **零**——全部因 Gemma chat template 错误而失败 |

需要修复 Gemma 的 `apply_chat_template` 兼容性问题后重跑。

---
