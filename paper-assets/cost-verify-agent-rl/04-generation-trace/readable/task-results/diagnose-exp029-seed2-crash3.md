# diagnose exp029 seed2 crash3

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp029-seed2-crash3_20260518T091521_result.json`
- **Structured JSON:** [`a8c81c5d2f2b0ccbb74b.json`](../../sessions/a8/a8c81c5d2f2b0ccbb74b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 诊断结果

### 崩溃原因：OOM（`loss.backward()` 阶段）

**确认是 OOM**，第三次崩溃与前两次原因相同。

### 崩溃位置
- **Training step 0**（val_before_train 完成后进入第一个 training step 的 backward pass）
- 仅完成了 step 0 的 validation（success=12.5%），尚未完成任何 training step
- Traceback：`dp_actor.py:468 → loss.backward()` → `torch.AcceleratorError: CUDA error: out of memory`
- 崩溃发生在 **Worker PID 19998**（Rank 1，即 cuda:1）

### 当前 config 内存相关参数

| 参数 | 值 |
|---|---|
| `enable_gradient_checkpointing` | `true` |
| `micro_batch_size_per_gpu` | `1` |
| `ppo_mini_batch_size` | `8` |
| `ppo_max_token_len_per_gpu` | `16384` |
| `max_model_len` | `20480` |
| `max_num_batched_tokens` | `20480` |
| `max_prompt_length` | `16384` |
| `response_length` | `1024` |
| `gpu_memory_utilization` (vLLM rollout) | `0.35` |
| `optimizer_offload` | `True` |
| `context_window_mode` | `full` |
| `train env_groups × group_size` | `16 × 8 = 128 episodes` |

### 日志最后 50 行

```
ray.exceptions.RayTaskError(AcceleratorError): ray::WorkerDict.actor_rollout_update_actor() (pid=19998, ip=172.17.0.6, actor_id=a9d0c5ad21256432b245a66a01000000)
  File ".../ray/base.py", line 700, in func
    return getattr(self.worker_dict[key], name)(*args, **kwargs)
  File ".../base/decorator.py", line 442, in inner
    return func(*args, **kwargs)
  File ".../transferqueue_utils.py", line 199, in dummy_inner
    return func(*args, **kwargs)
  File ".../profiler/profile.py", line 256, in wrapper
    return func(self_instance, *args, **kwargs_inner)
  File ".../ragen/workers/fsdp_workers.py", line 169, in update_actor
    output = self.actor.update_policy(data)
  File ".../profiler/performance.py", line 105, in f
    return self.log(decorated_function, *args, **kwargs)
  File ".../profiler/performance.py", line 118, in log
    output = func(*args, **kwargs)
  File ".../ragen/workers/actor/dp_actor.py", line 468, in update_policy
    loss.backward()
  File ".../torch/_tensor.py", line 630, in backward
    torch.autograd.backward(
  File ".../torch/autograd/__init__.py", line 364, in backward
    _engine_run_backward(
  File ".../torch/autograd/graph.py", line 865, in _engine_run_backward
    return Variable._execution_engine.run_backward(
torch.AcceleratorError: CUDA error: out of memory
EXIT_CODE=1
```

### 分析

`full` context_window_mode 下 episode 长度达到 ~16K tokens（从 val 结果看 response_length=7088，加上 prompt 可达 16K+）。即使 gradient_checkpointing=True、micro_batch=1、optimizer_offload=True，`ppo_max_token_len_per_gpu=16384` 在 backward pass 时仍然 OOM。这是因为 full 模式的序列远长于 step_independent 模式，activation memory 在 backward 时超出了 GPU 容量。

---
