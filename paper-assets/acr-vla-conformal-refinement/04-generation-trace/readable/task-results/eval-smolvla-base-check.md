# eval smolvla base check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_smolvla-base-check_20260513T092145_result.json`
- **Structured JSON:** [`e75956b6550b8fda74a4.json`](../../sessions/e7/e75956b6550b8fda74a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

vla_only 正在跑第一个 rollout（K=1, 预计 ~2min/rollout，5 个 rollout 后会有输出）。

以下是目前所有发现的汇总：

---

## 产出汇总

### 1. SmolVLA 训练数据集信息

**SmolVLA base 没有在 LIBERO 上 fine-tuned。** 它是一个通用预训练 VLA 模型：
- README: *"Intended use: Base model to fine tune on your specific use case"*
- 训练数据: *"community-driven data"*（多种机器人数据集混合）
- 骨干: SmolVLM2-500M-Video-Instruct
- 输出: **6D action** (config `action shape: [6]`)，无 gripper 维度

### 2. **关键问题：Gripper 控制缺失**

`utils.py:14` — `ACTION_DIM = 6  # 6 DOF, no gripper`

`evaluate.py` 中 `pad_action_to_7d` 将 gripper 硬编码为 0.0。LIBERO 所有 spatial/object 任务都需要 grasp → **任何方法的 base 成功率都应该是 ~0%**。这不是 reconvla vs vla_only 的差异问题，而是整个管线缺失 gripper 控制。

### 3. 推理速度分析

`smolvla_wrapper.py` 中 `generate_k_samples` 是串行循环：
```python
for _ in range(K):          # K=10 次循环
    for step in range(num_steps):  # 每次 10 步 denoising
        v_t = self.flow.denoise_step(...)
```

- 每个 env step: 1 次 prefix encode + K × num_steps 次 denoising = **100 次 forward**
- 300 steps/rollout → **30,000 forward passes** → ~20min/rollout

**优化方案**：batch K 个 noise samples 到一次 denoising 循环中（B=K 而非逐个循环）。10 步 batched denoising 替代 100 步串行 → **理论 ~10× 加速**。

### 4. 上一次 spatial reconvla 评估状态

从 `plan_014-reconvla-baseline` 日志看：
- Spatial eval 只跑了 task 1 的 5/20 rollouts (0/5 success)
- **然后 crash（可能 MuJoCo segfault）**，无 Python traceback
- JSON 结果未生成（`artifacts/reconvla_spatial.json` 不存在）
- 由于 `| tee` 管道掩盖了 exit code，shell 继续执行了 object eval

### 5. 当前 GPU 占用

| 进程 | PID | GPU 内存 | 状态 |
|------|-----|----------|------|
| reconvla object (K=10, n=20) | 59379 | 5.5GB | 运行中，刚加载完环境 |
| vla_only spatial (K=1, n=5) | 60741 | 6.1GB | 运行中，第一个 rollout 进行中 |
| **总计** | | **11.7GB / 24.6GB** | 充足 |

### 6. 下一步建议

- 等待 vla_only K=1 结果（预计 ~1.5h 完成全部 10 tasks × 5 rollouts）
- **但预期结果是 0% success**，因为缺少 gripper 控制
- 如果要证明论文 story，需要先解决 gripper 问题（要么 fine-tune SmolVLA 使其输出 7D，要么修改 evaluate.py 添加 heuristic gripper policy）
- reconvla object 评估也在运行，但同样会因为 gripper=0 而 0% success

---
