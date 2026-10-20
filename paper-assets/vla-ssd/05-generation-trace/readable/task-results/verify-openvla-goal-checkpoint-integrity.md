# verify openvla goal checkpoint integrity

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_openvla_goal_checkpoint_integrity_20260523T180758_result.json`
- **Structured JSON:** [`d49198d4306d14586d61.json`](../../sessions/d4/d49198d4306d14586d61.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 核查结论

### 1. config 中 model 字段完整内容

| Suite | config.model | config.experiment | config.unnorm_key |
|-------|-------------|-------------------|-------------------|
| **libero_goal** | `openvla-7b-finetuned-libero-object` ❌ | `counterfactual_libero_long` ❌ | `libero_goal` ✅ |
| libero_object | `openvla-7b-finetuned-libero-object` ✅ | `counterfactual_libero_object` ✅ | `libero_object` ✅ |
| libero_spatial | `openvla-7b-finetuned-libero-object` ❌ | `counterfactual_libero_long` ❌ | `libero_spatial` ✅ |

### 2. 脚本中实际配置的 checkpoint 路径

文件由 `libero_goal_full_pipeline.py` 生成（输出在 `results/libero_goal/`，无 `trained/` 子目录）。

该脚本第 28 行：
```python
TRAINED_CKPT = "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal"
```
**实际加载的 checkpoint 是正确的 Goal checkpoint。**

但 `run_counterfactual()` 函数中，config dict 是**硬编码字符串字面量**：
```python
"experiment": "counterfactual_libero_long",   # 复制自 long 脚本，未改
"model": "openvla-7b-finetuned-libero-object", # 复制自 object 脚本，未改
```
而 `unnorm_key` 用了变量 `UNNORM`，所以是对的。

### 3. Checkpoint 路径差异

文件系统中两个 checkpoint 确认都存在且独立：
- Goal: `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal`（May 22 08:32）
- Object: `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-object`（May 21 09:13）

### 4. 结论：**Metadata stale（实际加载正确）**

**证据链：**

1. **脚本代码路径正确**：`libero_goal_full_pipeline.py` 顶部 `TRAINED_CKPT` 明确指向 `openvla-7b-finetuned-libero-goal`，`main()` 函数用此变量加载模型
2. **config metadata 是硬编码复制粘贴错误**：`model` 和 `experiment` 字段是字符串字面量，未使用 `TRAINED_CKPT` 变量，从 object/long 脚本复制时忘了改
3. **unnorm_key 佐证**：config 中 `unnorm_key: "libero_goal"` 正确，因为它引用了变量 `UNNORM`——如果真的用了 Object checkpoint + Object unnorm_key，解码出的 action 值域会完全错误
4. **任务列表正确**：10 个 Goal 任务名完全匹配 Goal suite
5. **Spatial 有同样的 stale bug**：进一步证实这是系统性的复制粘贴遗漏，不是个案

**同一 bug 也影响 `libero_spatial/counterfactual_combined.json`**，config 中同样写了 `openvla-7b-finetuned-libero-object`，需要一并修正。

---
