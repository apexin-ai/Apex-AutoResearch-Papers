# diagnose ood eval temperature

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ood-eval-temperature_20260520T112000_result.json`
- **Structured JSON:** [`7b7d64b73e61a172254d.json`](../../sessions/7b/7b7d64b73e61a172254d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕，可以给出结论。

```json
{
  "eval_temperature": 0.4,
  "source": "vllm_rollout_spmd.py 的 is_validate 分支 + 日志确认",
  "config_temperature_eval": 0.4,
  "config_temperature_rollout": 1.0,
  "evidence": "见下方完整追踪"
}
```

### 追踪链

1. **Config** (`_alfworld_8b_v9d_ood_eval.yaml`):
   - `rollout.temperature: 1.0` (训练/默认)
   - `rollout.val_kwargs.temperature: 0.4`, `val_kwargs.do_sample: True`

2. **日志 line 4410** 确认 meta_info 传入了 `do_sample=True, validate=True`:
   ```
   test_gen_batch meta info: {'do_sample': True, 'validate': True, ...}
   ```

3. **vllm_rollout_spmd.py ~line 355-370** 的分支逻辑：
   ```python
   do_sample = prompts.meta_info.get("do_sample", True)   # True
   is_validate = prompts.meta_info.get("validate", False)  # True
   if not do_sample:
       kwargs = {..., "temperature": 0, ...}
   elif is_validate:
       kwargs = {
           "temperature": self.config.val_kwargs.temperature,  # 0.4
           ...
       }
   ```
   → 进入 `elif is_validate` 分支，使用 **T=0.4**。

4. **WorkerDict 日志中的 `temperature: 1.0`** 是 vLLM 引擎**初始化时的默认 SamplingParams**，不是推理时参数。实际推理通过 `update_sampling_params(**kwargs)` 上下文管理器覆盖为 0.4。

5. **`ctx_manager.gen_config.temperature`** 解析为 `${actor_rollout_ref.rollout.temperature}` = 1.0，但这是 ContextManager 的 prompt 构建配置，不影响 vLLM 采样参数。

**结论：OOD eval v5 实际推理使用 T=0.4。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "eval_temperature": 0.4,
    "source": "vllm_rollout_spmd.py 的 is_validate 分支 + 日志确认",
    "config_temperature_eval": 0.4,
    "config_temperature_rollout": 1.0,
    "evidence": "见下方完整追踪"
  }
}
```

</details>

---
