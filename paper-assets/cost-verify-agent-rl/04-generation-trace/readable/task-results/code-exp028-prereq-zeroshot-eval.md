# code exp028 prereq zeroshot eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp028_prereq_zeroshot_eval_20260515T203120_result.json`
- **Structured JSON:** [`5624914a2a2396c1c672.json`](../../sessions/56/5624914a2a2396c1c672.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

配置解析通过。全部产出如下：

---

## 产出总结

### 1. 配置文件
`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp028_prereq_zeroshot.yaml`

关键参数：
- `model_path`: Qwen3-1.7B-Instruct（非 SFT checkpoint）
- `val_only: True` — RAGEN 原生纯 eval 模式，val_before_train 后直接退出
- `val env_groups: 16, group_size: 1` → 16 episodes（满足 C003）
- 环境参数与 exp027 一致（step_independent, max_turn=50, AlfworldSG）
- train 部分设为最小值（不会被执行）

### 2. 启动脚本
`/root/cost-verify-agent-rl/scripts/run_exp028_prereq_zeroshot.sh`
- 含 pre-flight 检查（模型/磁盘/GPU/配置）
- W&B 日志记录
- 不需要模型下载

### 3. 模型路径
**无需下载** — `Qwen3-1.7B-Instruct` 已在 `/root/cost-verify-agent-rl/models/Qwen3-1.7B-Instruct/`

### 4. 模型选择说明
任务标题写的是 Qwen2.5-1.5B-Instruct，但 **SFT checkpoint 是 Qwen3ForCausalLM 架构**（`qwen3_exp021_ragen_sft_v4`）。验证"SFT 是毒药"需要苹果对苹果比较：
- SFT checkpoint（Qwen3-1.7B + SFT）: 6.25%
- **Qwen3-1.7B-Instruct**（原始权重）: ???  ← 这次 eval

用 Qwen2.5-1.5B-Instruct 测的是另一个模型族的零样本能力，无法直接证明 SFT 是否有害。

### 5. 预估耗时
exp027 step_0 val（16 episodes）耗时 ~502s ≈ 8 分钟。本次模型相同规模，预估 **~8-10 分钟**。

### 6. 等待 exp027 完成后启动
```bash
bash /root/cost-verify-agent-rl/scripts/run_exp028_prereq_zeroshot.sh
```

---
