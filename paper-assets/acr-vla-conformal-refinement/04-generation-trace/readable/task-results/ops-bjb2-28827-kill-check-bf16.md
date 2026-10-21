# ops bjb2 28827 kill check bf16

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb2-28827-kill-check-bf16_20260524T192652_result.json`
- **Structured JSON:** [`4376d8330ace4d70576e.json`](../../sessions/43/4376d8330ace4d70576e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 1. Kill 结果
PID 388593 已成功终止（SIGTERM 即停，无需 force kill）。cuda:1 已释放至 1 MiB。

### 2. cuda:2/cuda:3 内存状态

| GPU | 已用 | 总量 | 占比 | 利用率 |
|-----|------|------|------|--------|
| cuda:2 (Goal) | 13,966 MiB | 24,564 MiB | 57% | 20% |
| cuda:3 (Object) | 14,088 MiB | 24,564 MiB | 57% | 21% |

**OOM 风险评估**：~10GB 余量，暂无 OOM 风险。模型加载后推理的 KV cache 会动态增长，但 57% 占比是稳态，应可跑完。

### 3. 实验进度
- **Goal**: Task 1/10 `open_the_middle_drawer_of_the_cabinet` — rollout 5/20, 成功 4/5
- **Object**: Task 1/10 `pick_up_the_alphabet_soup_and_place_it_in_the_basket` — rollout 5/20, 成功 3/5

两个都还在第一个 task 上（共 10 tasks × 20 rollouts = 200 rollouts），进展正常。

### 4. evaluate.py 的 dtype/bf16 支持

**不支持。** 代码中：
- `evaluate.py`：无 `--dtype`/`--bf16` 参数
- `pi05_wrapper.py`：无任何 bf16/bfloat16/half 引用
- 模型加载（line 67）：`self.policy.to(self.device)` — 纯 fp32

要支持 bf16，需修改 `Pi05Wrapper.__init__`：
```python
# 改 line 67 附近
self.policy.to(self.device, dtype=torch.bfloat16)
```
并确保输入 tensor（line 214 的 `state_t = torch.tensor(..., dtype=torch.float32)`）也 cast 到 bf16。

### 5. 建议

- **不 kill cuda:2/cuda:3**，让它们继续跑完。57% 内存占比是安全的。
- **Spatial 需用 bf16 重试**：fp32 14.4GB 在 24GB 卡上 inference 时 KV cache 膨胀导致 OOM。bf16 可降至 ~7.2GB 模型参数，给 KV cache 留充足空间。
- 需要在 `pi05_wrapper.py` 和 `evaluate.py` 中添加 dtype 支持后再重启 Spatial 实验。

---
