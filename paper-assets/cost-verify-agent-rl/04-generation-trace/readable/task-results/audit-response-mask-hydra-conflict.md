# audit response mask hydra conflict

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_response_mask_hydra_conflict_20260522T192101_result.json`
- **Structured JSON:** [`fb2a85f08ae6544f2ebb.json`](../../sessions/fb/fb2a85f08ae6544f2ebb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整结果。

---

## 1. Runtime `enable_response_mask` 值（表格）

### westd-47453 上的 eval（Table 1 主要数据源）

| Eval | 日志文件 | runtime 值 | 状态 |
|------|---------|-----------|------|
| seed4 step15 v2 | `seed4_step15_ood_eval_v2.log` | **False** | ✅ |
| seed5 step10 v2 | `ragen_seed5_ood_eval_v2.log` | **False** | ✅ |
| seed6 step15 v2 | `seed6_step15_ood_eval_v2.log` | **False** | ✅ |
| seed6 step15 v3 | `seed6_step15_ood_eval_v3.log` | **False** | ✅ |
| seed8 step5 v2 | `ragen_seed8_ood_eval_v2.log` | **False** | ✅ |
| seed42 v2 | `ragen_seed42_ood_eval_v2.log` | **False** | ✅ |
| seed2048 v4 | `ragen_seed2048_ood_eval_v4.log` | **False** | ✅ |
| intervention_c v3 | `ragen_intervention_c_ood_eval_v3.log` | **False** | ✅ |
| c_prime step5 | `ragen_c_prime_step5_ood_eval.log` | **False** | ✅ |
| high_kl step5 | `ragen_high_kl_step5_ood_eval.log` | **False** | ✅ |
| seed2 v2 | `ragen_seed2_ood_eval_v2.log` | **False** | ✅ |
| SFT baseline v2 | `ragen_sft_ood_eval_v2_restart.log` | 日志中不含该字段（旧格式） | ⚠️ 无法确认 |

### bjb1-17606 上的 seed300 eval

| Eval | 日志文件 | runtime 值 | 状态 |
|------|---------|-----------|------|
| seed300 v1 | `seed300_step5_ood_eval.log` | **True** | ❌ BUG |
| seed300 v2 | `seed300_step5_ood_eval_v2.log` | **True** | ❌ BUG |
| seed300 ID diag | `seed300_step5_id_eval_diag.log` | **True** | ❌ BUG |
| seed300 v3 | `seed300_step5_ood_eval_v3.log` | **False** | ✅ 已修复 |

---

## 2. 根因：Hydra 配置层级放错

**bjb1 上的 seed300 config**（`_alfworld_seed300_step5_ood_eval.yaml` 第42行）：
```yaml
actor_rollout_ref:
  model:
    enable_response_mask: false    # ← 放在了 actor_rollout_ref.model 下面
```

**base.yaml**（第16行）：
```yaml
enable_response_mask: True         # ← 顶层
```

**代码读取路径**（`ctx_manager.py:893`）：
```python
self.config.enable_response_mask   # ← 读的是顶层
```

所有 westd 上的 eval config（seed4/5/6/8/42/2048 等）把 `enable_response_mask: False` 放在**顶层**（覆盖 base.yaml），所以正确解析为 False。

bjb1 的 seed300 config 把它放在了 `actor_rollout_ref.model` 嵌套路径下，**没有覆盖顶层的 True**，导致 runtime 读到 True。

---

## 3. 结论：历史 eval 是否受影响？

**Table 1 数据不受影响。** 理由：

1. **westd 上的全部 eval** runtime 值均为 `False`，配置正确
2. **`enable_response_mask` 只影响 loss_mask**（控制哪些 token 参与梯度计算），不影响 generation/rollout 行为。在 `val_only=True` 的 eval 模式下，不做 loss 计算、不做梯度更新，所以即使 seed300 v1/v2 读到了 True，**任务成功率（Alfworld OOD accuracy）不受影响**
3. **问题仅存在于 bjb1 上的 seed300 config**，且是因为 config 文件写法不同（嵌套在 `actor_rollout_ref.model` 下而非顶层），不是 Hydra 框架 bug

**SFT baseline** 的旧 log 不含 runtime config dump，无法从日志确认，但其 yaml 文件 `_alfworld_sft_baseline_ood_eval_v3.yaml:99` 设置了顶层 `enable_response_mask: False`，与其他正常 eval 一致。

---
