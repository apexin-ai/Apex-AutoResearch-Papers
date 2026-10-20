# ssh check probe target

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-probe-target_20260516T021626_result.json`
- **Structured JSON:** [`4b6844de1f21b0ba6309.json`](../../sessions/4b/4b6844de1f21b0ba6309.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收齐。结论如下：

---

## 结果

### 1. 原始 probe → 预测 **a_{t+1}**

**`action_probe_projector.py`** (p0_functional_action_probe) L82-83:
```python
x = torch.from_numpy(feat[:T-1])
y = torch.from_numpy(act[1:T])
```

**`action_probe_v2.py`** (p0_functional_probe_v2) 不做自己的训练，直接读取 `action_probe_projector.json` 的结果，继承相同的 a_{t+1} 对齐。

**`dino_action_probe.py`** L73/77:
```python
x = torch.from_numpy(feat[:T-1])
y = torch.from_numpy(act[1:T])  # action mode
```

**`train_probes.py`** L587-591 (`build_shifted` 函数):
```python
Xs.append(torch.from_numpy(feat[:T - 1]))
Ys.append(torch.from_numpy(act[1:T]))
```

### 2. 统一 probe → 预测 **a_{t+1}**

**`unified_action_probe.py`** L148-149:
```python
x = torch.from_numpy(feat[: T - 1])
y = torch.from_numpy(act[1:T])
```

### 3. 结论：两者一致，都是 a_{t+1}

**原始 probe 和统一 probe 用的是完全相同的 target 对齐方式：`feat[t] → act[t+1]`。不存在差异。**

唯一例外是 `run_clip_action_probe_final.py` L34 用 `feat[:T], act[:T]`（预测 a_t），但这个脚本是独立的 CLIP 对比实验，不属于 p0_functional_action_probe 系列。

### 4. 是否需要修复？

**不需要。** 跨方法比较中所有 probe（projector / DINO / CLIP / VLA image_mean / VLA last_preaction）都使用同一 target，对比是公平的。

关于 a_t vs a_{t+1} 的语义问题：VLA 在 time t 看到 obs_t 后输出 action_t，所以 `feat[t] → a_t` 测的是"特征是否编码当前 action"，语义更直接。但所有 probe 统一用 a_{t+1} 后，差异只影响 R² 绝对值（a_{t+1} 更难预测，R² 偏低），不影响方法间的排序和结论。如果想回答"projector 是否编码了 VLA 应该输出的 action"，可以考虑加一组 a_t 对照实验，但不是 blocker。

---
