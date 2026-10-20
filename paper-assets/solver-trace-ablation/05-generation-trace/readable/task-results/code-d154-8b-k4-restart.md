# code d154 8b k4 restart

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d154-8b-k4-restart_20260520T062312_result.json`
- **Structured JSON:** [`b69b0cba789b2e24dc21.json`](../../sessions/b6/b69b0cba789b2e24dc21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练稳定运行。汇报结果：

## 执行结果

### 1. 配置修改
- `grpo_exec_only_8b.yaml`: `num_generations` 2→4, `gradient_accumulation_steps` 32→16
- `grpo_isr_b01_8b.yaml`: 同上
- 有效 batch size 不变：1×4×16 = 1×2×32 = 64 completions/step

### 2. K=4 显存使用
- 生成阶段：~33 GiB
- 反向传播峰值：**~54 GiB**（97 GiB 卡的 55%，充裕）
- 对比 K=2：~54 GiB（持平，因为 generation_batch_size=K）

### 3. 每步时间
- K=4: **~26 s/step**（step_time=26.3s）
- K=2: 56 s/step
- **快了 2.15x**，因为 grad_accum 从 32 降到 16，生成轮次减半

### 4. W&B
- **未启用**。服务器无 WANDB_API_KEY、无 .netrc、无 wandb config。所有 4B 实验也是 `no_wandb: true`。需要 `wandb login` 才能启用。

### 5. dtype fix 对 4B 的影响
- `model_init_kwargs={"dtype": "bfloat16"}` 在 `train_grpo.py` 中全局应用（非条件）
- Qwen3-4B 原生 bf16 预训练 → **无副作用**

### 注意事项
- 发现 `--no_wandb` 的 argparse `action="store_true"` 与 YAML config 合并逻辑冲突：YAML 中 `no_wandb: true` 不会覆盖 argparse 默认值 `False`（合并条件是 `current is None`）。本次已通过 CLI `--no_wandb` 绕过。后续若要启用 W&B，需配置服务器凭证并去掉 CLI flag。
- 预估 500 步总时间：~3.6h（vs K=2 的 ~7.8h）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "dtype": "bfloat16"
  }
}
```

</details>

---
