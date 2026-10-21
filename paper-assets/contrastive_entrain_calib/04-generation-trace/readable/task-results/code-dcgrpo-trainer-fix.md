# code dcgrpo trainer fix

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dcgrpo_trainer_fix_20260518T113412_result.json`
- **Structured JSON:** [`73a2121650cdf274e7ca.json`](../../sessions/73/73a2121650cdf274e7ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 修复汇报

### 修复了什么

3 个 critical 问题导致训练时 R1=0, R2=0，退化为纯 R3。根因：reward 计算管道未接入 TRL 训练循环。

### 具体修改

**问题 1：`generate_completions()` 激活提取被注释**
- 取消注释并完成实现（`dcgrpo_trainer.py:620-663`）
- 处理 string 和 tensor 两种 prompt/completion 格式
- 带 try/except 保护，不影响主流程

**问题 2：缺失方法**
- `_find_asst_first_positions`、`_extract_activations`、`ActivationCache` 均已存在且实现完整，无需修改

**问题 3：`_noop_reward_fn` 返回全零，未接入 TRL 循环**
- 新增 `_DCRewardCallable` 类（L133-182），作为 TRL reward_funcs 的实际实现
- 在 `__init__` 中 `super().__init__()` 后替换 `self.reward_funcs = [_DCRewardCallable(self)]`（L250-253）
- `_DCRewardCallable.__call__` 接收 TRL 传入的 `prompts`、`completions` 和 dataset 列（`condition`、`pair_id`），执行 forward pass 提取激活，计算 R1+R2+R3
- R1/R2 的 forward pass 在 `torch.no_grad()` 下运行，不反传梯度

### 冒烟测试结果

```
R1: ['-0.0186', '-0.2187', '0.1115', '-0.1111']   ← 非零 ✓
R2: ['0.0499', '0.0499', '0.0554', '0.0554']       ← 非零 ✓
R3: ['0.4640', '0.4640', '0.4640', '0.4640']       ← 非零 ✓
Combined: [0.1493, -0.0900, 0.2477, 0.0520]
```

### 产出文件
1. `artifacts/training/dcgrpo_trainer.py` — 修复后的 trainer
2. `artifacts/training/smoke_test_dcgrpo.py` — 冒烟测试脚本

---
