# research code survey

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_code-survey_20260513T010756_result.json`
- **Structured JSON:** [`77b11d9f0dd8668c7554.json`](../../sessions/77/77b11d9f0dd8668c7554.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 `register_artifact` 工具。报告已写入：

`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code_survey_dreamerv3.md`

---

**调研完成，核心发现总结：**

1. **RSSM**（`networks.py:13-291`）：离散 categorical latent (32×32) + GRU deterministic (512)，feat 向量 1536 维。`img_step` 做 prior transition，`obs_step` 做 posterior update。

2. **Imagination Loop**（`models.py:351-369`）：`_imagine()` 用 `tools.static_scan` 固定展开 `imag_horizon=15` 步。步数来自 config 参数，但循环结构 hardcoded 为固定长度——**这是 event gate 改造的核心切入点**。

3. **λ-Return**（`tools.py:691-717`）：标准 GAE-λ 反向扫描，γ 来自 continue head 输出 × 0.997，λ=0.95。

4. **Replay Buffer**（`tools.py:323-361`）：按 episode 长度加权采样，sequence length=64，跨 episode 可拼接，无显式 overlap 控制。

5. **World Model 训练**：KL loss（free bits=1.0, dyn_scale=0.5, rep_scale=0.1）+ decoder MSE + reward SymlogDisc + continue BCE，Adam lr=1e-4。

6. **改造建议**：在 `WorldModel.heads` 添加 event gate head → 重写 `_imagine` 为 max_horizon + gate mask → 将 gate 信号合并到 discount 用于 λ-return 计算。主要风险是离散 gate 的梯度传递和 batch 内不等长 trajectory 的处理。

---
