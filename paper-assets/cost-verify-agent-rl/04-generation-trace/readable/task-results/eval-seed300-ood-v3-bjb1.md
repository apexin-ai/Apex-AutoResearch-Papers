# eval seed300 ood v3 bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_seed300_ood_v3_bjb1_20260522T191554_result.json`
- **Structured JSON:** [`3c35215e91e4c3bc8f46.json`](../../sessions/3c/3c35215e91e4c3bc8f46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Runtime 确认成功：两个 `enable_response_mask` 均为 False。**

从 v3 log 中的 resolved config：
- 顶层 `'enable_response_mask': False` — 顶层 override 生效
- `actor_rollout_ref.model.enable_response_mask`: False — 嵌套 override 生效
- TaskRunner 输出两行均为 `'enable_response_mask': False`

这就是 v2 失败的根因：v2 只在 YAML 嵌套层设了 false，但代码读的是顶层的 `enable_response_mask`（base config 默认 True）。

**汇报：**
- **PID**: 452290（主进程）/ TaskRunner 453685
- **GPU**: cuda:0 已加载模型（8133 MiB），cuda:1 不受影响（56437 MiB）
- **Runtime enable_response_mask**: **False**（顶层 + 嵌套均 False）
- **Config**: `_alfworld_seed300_step5_ood_eval_v3.yaml`，134 OOD tasks
- **Log**: `/root/autodl-tmp/logs/seed300_step5_ood_eval_v3.log`
- **Hydra overrides**: `enable_response_mask=false actor_rollout_ref.model.enable_response_mask=false`（双重保险，解决了 v2 的 bug）

---
