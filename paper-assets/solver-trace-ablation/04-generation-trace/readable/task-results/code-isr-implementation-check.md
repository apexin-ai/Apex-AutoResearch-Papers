# code isr implementation check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_isr-implementation-check_20260520T060240_result.json`
- **Structured JSON:** [`ad182cba8385092127b9.json`](../../sessions/ad/ad182cba8385092127b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

最后确认 `train_grpo.py` 中哪些 reward_mode 实际使用 `_full_fn`（O(n) LOO）vs `_fast_fn`（O(1) binary）。

回读 train_grpo.py 158 行的关键分支，已有完整信息，汇总如下：

---

## 结论

训练中有 **两种** ISR 实现，按 reward_mode 分发：

### 1. `_full_fn`：O(n) Leave-One-Out

**文件**：
- FOL: `src/sta/reward.py` → `sta_reward()` (L72-154)
- Prolog: `src/sta/prolog_reward.py` → `prolog_sta_reward()` (L114-161)

**计算方式**：对每个 component（premise/conclusion part）逐一移除，每次重新调 solver，判断 proof 是否 break → `ISR = n_necessary / n_total`

**使用此函数的 reward_mode**：
- `execution_only` (L192) — 调 `_full_fn` 但只取 `execution_reward`，ISR 仅 log
- `random_reward` (L198) — 调 `_full_fn`，ISR 仅 log，reward 是随机值
- `additive_bonus` (L214) — `r = exec * (1 + beta * ISR)`，ISR 来自 full LOO
- `additive_random` (L225) — matched control，random 替代 ISR
- `isr_gated` (L240) — warmup 阶段 exec-only，之后 ISR gate 过滤
- `additive_bonus_gated` (L277) — additive + gate

### 2. `_fast_fn`：O(1) Binary tautology check

**文件**：
- FOL: `src/sta/isr.py` → `fast_isr_fol()` (L100-135)
- Prolog: `src/sta/prolog_reward.py` → `fast_prolog_sta_reward()` (L164-209)

**计算方式**：仅 2 次 solver 调用——(1) 原始 prove (2) 空 premises prove conclusion。如果 conclusion 不是 tautology 且原始可证 → ISR=1.0，否则 ISR=0.0。**纯 binary，无区分能力。**

**使用此函数的 reward_mode**：
- `execution_fast_sta` (L296) — 唯一使用 `_fast_fn` 的 mode

### 关键代码片段

**`_full_fn` 核心 (ablation.py L115-136)**:
```python
def run_sta(premises, conclusion, solver, timeout=5, original_result=None):
    components = decompose_fol(premises, conclusion)
    for comp in components:
        result = ablate_component(premises, conclusion, comp, solver, timeout,
                                  original_result=original_result)
        # is_necessary = original_proved and not ablated_proved
```

**`_fast_fn` 核心 (isr.py L100-128)**:
```python
def fast_isr_fol(premises, conclusion, solver, timeout=5):
    original = solver.prove(premises, conclusion, timeout=timeout)
    tautology_check = solver.prove([], conclusion, timeout=timeout)
    if not original.proved:       fast_isr = 0.0
    elif tautology_check.proved:  fast_isr = 0.0
    else:                         fast_isr = 1.0  # binary, no gradation
```

### 总结

**除 `execution_fast_sta` 外，所有 reward_mode 都使用 O(n) full LOO 计算 ISR。** `_fast_fn` 的 binary ISR 确实对 proved sample 无区分能力（非 tautology 恒返回 1.0），但它只在 `execution_fast_sta` mode 中作为 reward signal 使用。`additive_bonus`、`isr_gated` 等实际训练 mode 使用的是 full LOO ISR，具有 [0,1] 连续区分能力。

---
