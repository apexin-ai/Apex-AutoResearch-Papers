# diagnose seed6 exit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_seed6_exit_20260521T073212_result.json`
- **Structured JSON:** [`ede57064aeb6b079df77.json`](../../sessions/ed/ede57064aeb6b079df77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**FAILED**（训练完成但最终 checkpoint 损坏）

### 详情

**训练进度**：15/15 steps 全部完成（step 0-14 的训练循环正常执行完毕）。

**失败点**：在保存 step 15 的 checkpoint 时崩溃：
```
RuntimeError: basic_ios::clear: iostream error
RuntimeError: [enforce fail at inline_container.cc:668] . unexpected pos 2855431360 vs 2855431252
```
- 根因：`No space left on device` — 磁盘在写 optimizer state 时满了
- Ray log 也报了 `No space left on device`

### Checkpoint 状态

| Checkpoint | 状态 | 说明 |
|---|---|---|
| `global_step_5` | 完整 | model + optim + extra_state + huggingface |
| `global_step_10` | 完整 | 同上, `latest_checkpointed_iteration.txt`=10 |
| `global_step_15` | **损坏** | 仅有 model 文件(~4GB×2), optim 文件截断(2.8GB/3.4GB vs 正常 6.8GB×2), 缺 extra_state 和 huggingface |

### Validation 指标

| Step | val-env/AlfworldSG/success | val/pass@1 |
|---|---|---|
| 0 (initial) | **9.375%** (3/32) | 0.09375 |
| 10 | **40.625%** (13/32) | 0.40625 |
| 15 | 未执行（崩溃在 eval 之前） | — |

训练 success rate 在 step 14 达到 **78.9%**。

### 可用资产
- **最新可靠 checkpoint**: `/root/autodl-tmp/checkpoints/exp029-seed6/global_step_10/actor/`
- **step 15 model 权重可能可用**（model_world_size_2_rank_*.pt 大小正常），但 optimizer 损坏，无法 resume 训练
- 当前磁盘已恢复到 184G/250G (74% used)，有 67GB 空余
- GPU 已全部释放

### W&B

日志中未找到与 seed6（cuda:2,3）对应的 W&B run。W&B run `x05q7im0` 的 config 显示 `CUDA_VISIBLE_DEVICES='0,1'` 和 seed=456，属于另一个实验。

### 建议处理

如需 step 15 的完整 checkpoint：需要清理磁盘空间后从 step 10 resume 训练 5 步。或者如果只需 eval，step 15 的 model 权重文件大小与 step 10 一致，可能仍可用于推理（但需要验证文件完整性）。

---
