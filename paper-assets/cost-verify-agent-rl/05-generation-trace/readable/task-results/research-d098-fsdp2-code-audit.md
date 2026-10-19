# research d098 fsdp2 code audit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d098_fsdp2_code_audit_20260519T183736_result.json`
- **Structured JSON:** [`5be4fee47c96b386bcc1.json`](../../sessions/5b/5be4fee47c96b386bcc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，以下是审计结论。

---

## 审计结果

### 1. init_model() — RAGEN worker import 路径 → **SAFE**

**证据**：
- RAGEN `ActorRolloutRefWorker.init_model()` (ragen/workers/fsdp_workers.py:73-84)：调用 `super().init_model()`，走 verl 原生路径完成所有 FSDP2 wrapping
- verl `init_model()` (verl/workers/fsdp_workers.py:506-522) 在 FSDP2 + `offload_policy` 时：
  ```python
  if role == "actor" and fsdp_config.offload_policy:
      cpu_offload = CPUOffloadPolicy(pin_memory=True)
      self._is_offload_param = False    # L515
      self._is_offload_optimizer = False  # L516
  ```
  然后 `apply_fsdp2()` + `fsdp2_load_full_state_dict()` 完成 wrapping
- RAGEN 仅在 `super().init_model()` 之后替换 `self.actor` 为 `RagenDataParallelPPOActor`，不碰模型 wrapping

**结论**：模型初始化完全委托给 verl，FSDP2 路径安全。

---

### 2. update_actor() — RAGEN 重写版本 → **SAFE**

**RAGEN 版本** (ragen/workers/fsdp_workers.py:163-173)：
```python
def update_actor(self, data, skip_optimizer_step=False):
    data = data.to(get_device_id())
    output = self.actor.update_policy(data)
    return DataProto(meta_info={"metrics": output})
```

**verl 版本** (verl/workers/fsdp_workers.py:865-903) 额外包含：
- `load_fsdp_model_to_gpu()` / `offload_fsdp_model_to_cpu()` — 受 `_is_offload_param` 守护
- `load_fsdp_optimizer()` / `offload_fsdp_optimizer()` — 受 `_is_offload_optimizer` 守护
- `ulysses_sharding_manager` 上下文
- `lr_scheduler.step()`、MFU 指标

**关键点**：FSDP2 + CPUOffloadPolicy 下，`_is_offload_param = False` 且 `_is_offload_optimizer = False`（L515-516），所以 verl 版本中的手动 offload 调用**本来就不执行**。RAGEN 省略这些逻辑对 FSDP2 无影响——CPUOffloadPolicy 是内建于 FSDP2 wrapper 的自动行为，不需要手动触发。

**注意**（非 FSDP2 问题）：RAGEN 跳过了 `lr_scheduler.step()` 和 `ulysses_sharding_manager`。如果 lr_scheduler 不在 `RagenDataParallelPPOActor.update_policy()` 内部处理，learning rate 不会衰减。这是预存问题，与 FSDP2 无关。

---

### 3. rollout_mode / trainer_mode 切换 → **SAFE**

**证据**：
- RAGEN fsdp_workers.py 中 `rollout_mode` / `trainer_mode` 仅在 L125/L137 被调用，**未被 override**
- verl 的 `rollout_mode()` (verl/workers/fsdp_workers.py:651+) 对 FSDP2 的处理：
  ```python
  # _is_offload_param = False → 跳过手动 load/offload
  params = self.actor_module_fsdp.state_dict()  # 返回 DTensor
  # DTensor → 全量 tensor 转换
  per_tensor_param = (
      (name, param.to(device, non_blocking=True).full_tensor()
       if isinstance(param, DTensor) else param)
      for name, param in params.items()
  )
  await self.rollout.update_weights(per_tensor_param, ...)
  ```
- DTensor `.to(device).full_tensor()` 是 FSDP2 的标准转换路径——将 sharded DTensor 移至 GPU 并 all-gather 为 full tensor，用于更新 rollout engine 权重

**结论**：verl 原生支持 FSDP2 DTensor 转换，RAGEN 未 override，安全透传。

---

### 4. Checkpoint save/load → **SAFE**

**证据**：
- `fsdp_version()` (fsdp_utils.py:399-405)：正确区分 FSDP1 (`isinstance(model, FSDP)`) vs FSDP2 (`isinstance(model, FSDPModule)`)
- **Sharded checkpoint** (fsdp_checkpoint_manager.py)：
  - `get_fsdp_state_ctx()` 对 FSDP2 返回 `nullcontext()` — FSDP2 不需要 FSDP1 的 state_dict_type 上下文
  - `model.state_dict()` 直接返回 DTensor state dict，`torch.save` 序列化每个 rank 的 local shard
  - 加载时 `torch.load` 恢复 local shard，`load_state_dict` 正常加载
- **HF model save** (fsdp_checkpoint_manager.py:308-309)：
  ```python
  state_dict = get_fsdp_full_state_dict(self.model, offload_to_cpu=True, rank0_only=True)
  ```
  `get_fsdp_full_state_dict` 对 FSDP2 使用 (fsdp_utils.py:439-446)：
  ```python
  from torch.distributed.checkpoint.state_dict import StateDictOptions, get_model_state_dict
  state_dict_config = StateDictOptions(full_state_dict=True, cpu_offload=True, broadcast_from_rank0=False)
  state_dict = get_model_state_dict(model, options=state_dict_config)
  ```
  这是 FSDP2 官方 API。
- RAGEN `CriticWorker._build_critic_model_optimizer` 也正确处理了 fsdp2 分支，含 CPUOffloadPolicy 设置

**结论**：checkpoint manager 通过 `fsdp_version()` 分发到正确路径，FSDP2 使用官方 DCP API，安全。

---

## 总结

| 审计点 | 结论 | 说明 |
|--------|------|------|
| 1. init_model | **SAFE** | `super().init_model()` 走 verl FSDP2 原生路径 |
| 2. update_actor | **SAFE** | 省略的手动 offload 在 FSDP2 下本来就不执行（`_is_offload_param=False`） |
| 3. rollout/trainer mode | **SAFE** | 未 override，verl 原生 DTensor→full_tensor 转换正确 |
| 4. checkpoint | **SAFE** | `fsdp_version()` 正确分发，使用 FSDP2 官方 state_dict API |

4 个关键路径全部 **SAFE**，v9b 可以继续。

---
