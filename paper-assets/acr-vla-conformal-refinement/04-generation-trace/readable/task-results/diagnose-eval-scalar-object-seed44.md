# diagnose eval scalar object seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-scalar-object-seed44_20260516T050726_result.json`
- **Structured JSON:** [`129c1555a18f2fb246e8.json`](../../sessions/12/129c1555a18f2fb246e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**失败原因**：`FileNotFoundError` — checkpoint 文件不存在。

实验尝试加载：
```
/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt
```

但该路径不存在。服务器上 `crm_v3_norm` 目录下只有 `perdof/` 和 `obs_only/`，没有 `scalar_unc/`。

`scalar_unc` 的 `crm_best.pt` 存在于 **`crm_v3`**（无 `_norm`）目录下：
```
/root/autodl-tmp/checkpoints/crm_v3/scalar_unc/crm_best.pt
```

**根因**：`crm_v3_norm` 版本的 `scalar_unc` 模型尚未训练/部署到该服务器，但 eval 任务的 `--crm_checkpoint` 参数已经指向了这个不存在的路径。

**修复方案**：
1. 如果需要 eval 的确实是 `crm_v3_norm` 的 scalar_unc → 先完成该模型的训练，将 checkpoint 放到 `/root/autodl-tmp/checkpoints/crm_v3_norm/scalar_unc/crm_best.pt`
2. 如果实际上应该 eval `crm_v3`（非 norm 版）的 scalar_unc → 修正路径为 `/root/autodl-tmp/checkpoints/crm_v3/scalar_unc/crm_best.pt`

---
