# ops verify obs only default seed44 45 logs

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-obs-only-default-seed44-45-logs_20260518T062629_result.json`
- **Structured JSON:** [`c4c71f3e93511f512d4b.json`](../../sessions/c4/c4c71f3e93511f512d4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认了对比：
- `norm01` 版本 → `max_correction_norm: 0.1`（显式传入）
- `default` 版本 → `max_correction_norm: None`（不传，使用类默认值 1.42）

## 结论

- **seed44**: actual max_correction_norm = **1.42**（类默认值）
  - 来源：`/root/runs/acr-vla-conformal-refinement/eval-obs-only-object-default-seed44.log` 第 1 行显示 `'max_correction_norm': None`；checkpoint 不含该字段；`ConformalRefinementModule.__init__` 默认值 `1.42`；无 CLI override

- **seed45**: actual max_correction_norm = **1.42**（类默认值）
  - 来源：`/root/acr-vla-conformal-refinement/logs/eval_object_obs_only_default_seed45.log` 第 1 行显示 `'max_correction_norm': None`；同样的代码路径

**验证链**（不是代码猜测）：
1. 两个 log 文件记录了启动时 `args` → `max_correction_norm: None`
2. Checkpoint 只含 `['input_mean', 'input_std', 'net.0.weight', ...]`，无 `max_correction_norm` key
3. evaluate.py 第 378 行：`None is not None` → 不触发 override
4. CRM 类 `__init__` 默认参数 `max_correction_norm=1.42` 生效
5. 对比组验证：同一 seed44 的 `norm01` log 显示 `max_correction_norm: 0.1`（显式传入时确实会记录为 0.1）

**这与之前 seed42/seed43 "实际是 0.1" 的发现矛盾**——如果 seed42/43 也是用同样的代码和相同的 default 方式运行的，它们也应该是 1.42 而不是 0.1。建议回查 seed42/seed43 的原始 log 确认那个 0.1 的结论是否正确。

---
