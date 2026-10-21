# monitor a075 plan006 status

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_a075_plan006_status_20260515T063915_result.json`
- **Structured JSON:** [`0b7b65aef3fc30af0412.json`](../../sessions/0b/0b7b65aef3fc30af0412.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。简报如下：

---

## 实验状态简报

| 实验 | 当前进度 | GPU | GPU 利用率 | 显存占用 | 预估完成 |
|------|---------|-----|-----------|---------|---------|
| **plan_006_s42** (α=1.0, 20gen) | gen 14/20（正在生成合成数据） | cuda:0 | 45% | 14.4/97.9 GB | ~3h（≈09:40 UTC） |
| **alpha_sweep_a075_s42** (α=0.75) | gen 2/10（训练 step 490/5000） | cuda:1 | 89% | 12.5/97.9 GB | ~3.5h（≈10:10 UTC） |

**异常检查**：
- 两个进程均存活，无 OOM、无报错
- plan_006 的 45% GPU 利用率是因为当前处于合成数据生成阶段（推理），训练阶段会回到高利用率
- padding_side 警告是 HuggingFace 的常规 warning，不影响训练

**磁盘**：`/root/autodl-tmp/` 剩余 114GB（55% 使用），空间充裕。

**估算依据**：plan_006 已跑 ~7h 完成 14 gen，约 30 min/gen；a075 跑 55 min 完成 ~2.1 gen，约 26 min/gen。

---
