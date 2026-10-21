# D096: 8B Cell C — FSDP CPU Offload 方案调研

## 1. 问题回顾

v7 配置通过 vLLM init 和 val_before_train，但 backward pass OOM：
- allocated 110.14 GiB, 需要 8.94 GiB, 只剩 5.21 GiB, 缺口 ~3.7 GiB
- 死锁：FSDP(actor+optimizer) + vLLM KV cache 填满显存

## 2. RAGEN FSDP 配置方式

### 2.1 配置层级

```
Hydra YAML → OmegaConf DictConfig → FSDPActorConfig (dataclass)
                                      ├── strategy: str = "fsdp"  (FSDP1 or FSDP2)
                                      └── fsdp_config: FSDPEngineConfig
                                            ├── param_offload: bool = False
                                            ├── optimizer_offload: bool = False
                                            ├── offload_policy: bool = False  (FSDP2 only)
                                            └── strategy: str = "fsdp"
```

### 2.2 两个 FSDP 版本

| 特性 | FSDP1 (strategy="fsdp") | FSDP2 (strategy="fsdp2") |
|------|------------------------|-------------------------|
| API | `FullyShardedDataParallel` wrapper | `fully_shard` composable API |
| Actor CPUOffload | **硬编码 None** (line 492) | 可通过 `offload_policy: True` 启用 |
| 禁用原因 | "causes incorrect results when using grad accumulation" | 不适用 |
| offload 机制 | 手动 offload/load（训练↔rollout 切换时） | `CPUOffloadPolicy(pin_memory=True)` 自动管理 |
| PyTorch 版本要求 | 任意 | >= 2.4（当前安装 2.10.0+cu128） |

**关键代码（verl/verl/workers/fsdp_workers.py:490-518）：**
```python
# FSDP1: actor 硬编码关闭 CPUOffload
cpu_offload = None if role == "actor" else CPUOffload(offload_params=True)

# FSDP2: actor 可通过 config 启用
if role == "actor" and fsdp_config.offload_policy:
    cpu_offload = CPUOffloadPolicy(pin_memory=True)
    self._is_offload_param = False   # 禁用手动 offload
    self._is_offload_optimizer = False
```

### 2.3 关键发现：v7 的 `optimizer_offload: True` 完全无效

**原因链条：**

1. `optimizer_offload: True` 在 init_model 中设置 `self._is_offload_optimizer = True`
2. init_model 末尾调用 `offload_fsdp_optimizer(optimizer)` — 但此时 optimizer.state 为空（尚未执行 step），函数直接 return
3. verl 的 `update_actor` 有完整的 load/offload 逻辑，但 **RAGEN 重写了 `update_actor`**（ragen/workers/fsdp_workers.py:170-180），不包含任何 offload 调用
4. 结果：optimizer states 始终停留在 GPU 上，`optimizer_offload: True` 是死代码

**RAGEN 的 update_actor（无 offload）：**
```python
def update_actor(self, data, skip_optimizer_step=False):
    data = data.to(get_device_id())
    output = self.actor.update_policy(data)   # 无 load/offload
    return DataProto(meta_info={"metrics": output})
```

**verl 原版 update_actor（有 offload，但 RAGEN 不调用）：**
```python
def update_actor(self, data):
    if self._is_offload_param:
        load_fsdp_model_to_gpu(...)
    if self._is_offload_optimizer:
        load_fsdp_optimizer(...)
    metrics = self.actor.update_policy(data=data)
    if self._is_offload_param:
        offload_fsdp_model_to_cpu(...)
    if self._is_offload_optimizer:
        offload_fsdp_optimizer(...)
```

## 3. CPUOffload 可行性评估

### 3.1 方案比较

| 方案 | 改动级别 | 预期省 VRAM | 风险 |
|------|---------|------------|------|
| **A. FSDP2 + offload_policy** | Config only | ~20+ GB/GPU (optimizer + params) | FSDP2 兼容性 |
| B. 修复 RAGEN update_actor offload | Code change | ~16 GB/GPU (optimizer states) | 需改代码、仅省 rollout 阶段 |
| C. Activation offloading | Config only | 数 GB | 训练速度下降 |
| D. 手动分离 backward/step | Code change | ~16 GB/GPU (optimizer states) | 侵入性强 |

**推荐：方案 A（FSDP2 + offload_policy），辅以方案 C（activation offloading）。**

### 3.2 FSDP2 CPUOffloadPolicy 工作原理

```
Forward:  layer_1[CPU] → GPU → compute → GPU → layer_1[CPU]
          layer_2[CPU] → GPU → compute → GPU → layer_2[CPU]
          ...

Backward: layer_N[CPU] → GPU → grad → GPU → layer_N[CPU]
          layer_N-1[CPU] → GPU → grad → GPU → layer_N-1[CPU]
          ...

Opt Step: layer_1[CPU+GPU] → update → CPU
          layer_2[CPU+GPU] → update → CPU
          ...
```

在任何时刻，GPU 上只有 1-2 个 transformer layer 的参数 + 对应的 optimizer states。对于 8B 模型（~32 layers），峰值 VRAM 减少约 30/32。

### 3.3 内存估算

8B 模型 / 4 GPUs / FSDP sharding：

| 组件 | v7 (FSDP1, 无有效 offload) | v9 (FSDP2 + CPUOffload) |
|------|--------------------------|------------------------|
| Model params (bf16 sharded) | ~4 GB/GPU | ~0.25 GB/GPU peak |
| Optimizer states (fp32) | ~16 GB/GPU | ~1 GB/GPU peak |
| Gradients | ~4 GB/GPU | ~0.25 GB/GPU peak |
| vLLM KV cache (0.22->0.20) | ~21 GB/GPU | ~19 GB/GPU |
| Activations (w/ grad ckpt) | ~10-20 GB/GPU | ~5-10 GB/GPU (w/ act offload) |
| **Backward peak** | ~55-65 GB/GPU | ~26-36 GB/GPU |

v7 的 OOM 显示 ~5 GiB 剩余，v9 应能提供充足空间。

## 4. 与 vLLM 的兼容性分析

### 4.1 Training -> Rollout 切换（rollout_mode）

权重同步流程（verl/verl/workers/fsdp_workers.py:650-730）：

```python
async def rollout_mode(self):
    # 1. 提取 FSDP state dict（FSDP2 返回 DTensor，可能在 CPU）
    params = self.actor_module_fsdp.state_dict()

    # 2. 逐参数移到 GPU 并 unshard（generator，内存友好）
    per_tensor_param = (
        (name, param.to(device).full_tensor() if isinstance(param, DTensor) else param)
        for name, param in params.items()
    )

    # 3. 加载到 vLLM
    await self.rollout.update_weights(per_tensor_param, ...)
```

**兼容性：OK** — DTensor 的 `.to(device).full_tensor()` 处理了 CPU->GPU 转换。Generator 惰性求值，每次只有一个 tensor 在 GPU 上。

### 4.2 Rollout -> Training 切换（trainer_mode）

```python
async def trainer_mode(self):
    await self.rollout.release()  # 释放 vLLM 资源
    self.actor_module_fsdp.train()  # 切回训练模式
    aggressive_empty_cache()
```

**兼容性：OK** — 无 FSDP1-specific API。

### 4.3 RAGEN generate_sequences

RAGEN 的 `generate_sequences` 调用父类的 `rollout_mode()` / `trainer_mode()`，不涉及 FSDP1-specific API。兼容性无问题。

### 4.4 RAGEN update_actor

RAGEN 重写的 `update_actor` 不包含手动 offload 逻辑。FSDP2 的 CPUOffloadPolicy 是自动的（内建于 FSDP2 wrapper），不需要手动调用 offload 函数。所以 RAGEN 的简化 update_actor 反而与 FSDP2 更兼容。

## 5. v9 Config

文件：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_cell_c_v9.yaml`

**相对于 v7 的变更：**

```diff
 actor_rollout_ref:
+  model:
+    enable_activation_offload: true       # 新增：activation offload
   actor:
+    strategy: fsdp2                       # FSDP1 -> FSDP2
     fsdp_config:
-      optimizer_offload: True             # 删除：在 RAGEN 中无效
+      strategy: fsdp2                     # 匹配 actor strategy
+      offload_policy: True               # 新增：FSDP2 native CPU offload
+      optimizer_offload: False            # 显式关闭无效选项
+      param_offload: False               # 显式关闭（FSDP2 offload_policy 接管）
   rollout:
-    gpu_memory_utilization: 0.22
+    gpu_memory_utilization: 0.20          # 降低：为 weight sync 峰值留空间
 trainer:
-  experiment_name: 8b-cell-c-episode-level
+  experiment_name: 8b-cell-c-v9-fsdp2-offload
```

## 6. 风险清单

| # | 风险 | 等级 | 缓解措施 |
|---|------|------|---------|
| 1 | FSDP2 训练正确性未充分验证 | HIGH | val_before_train 后对比 v7 的 val loss |
| 2 | 训练速度下降 2-3x | MEDIUM | 可接受（vs 不能运行） |
| 3 | Gradient accumulation 正确性 | MEDIUM | ppo_mini_batch_size=2 + 4 GPUs 需验证 |
| 4 | Weight sync 内存峰值 | MEDIUM | gpu_memory_util 0.22->0.20 |
| 5 | FSDP1->FSDP2 checkpoint 格式 | LOW | resume_mode="disable"，从头训练 |
| 6 | LoRA 兼容性 | N/A | Cell C 不用 LoRA |

## 7. 后备方案

如果 FSDP2 方案失败：

**方案 B：修复 RAGEN update_actor**
- 在 RAGEN 的 `update_actor` 中添加 `load_fsdp_optimizer` / `offload_fsdp_optimizer` 调用
- 使 v7 的 `optimizer_offload: True` 生效
- 限制：仅在 rollout 期间省内存，backward 期间 optimizer states 仍在 GPU
- 不足以解决 backward OOM（optimizer 在 backward 前就加载到 GPU）

**方案 C-only：仅 activation offloading**
- 不改 FSDP strategy，仅添加 `enable_activation_offload: True`
- 如果 activation 内存 > 3.7 GiB 缺口，可能够用

**方案 D：分离 backward 和 optimizer.step()**
- 修改 `update_policy`：backward 时不加载 optimizer，step 时再加载
- 改动最大但效果确定，可省 ~16 GB/GPU 在 backward 期间
