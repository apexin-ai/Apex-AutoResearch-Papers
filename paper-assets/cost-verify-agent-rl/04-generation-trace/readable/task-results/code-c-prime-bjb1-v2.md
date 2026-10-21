# code c prime bjb1 v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c_prime_bjb1_v2_20260521T214840_result.json`
- **Structured JSON:** [`f3731563ef6fdf74929b.json`](../../sessions/f3/f3731563ef6fdf74929b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并在运行中。

## 产出汇总

### 1. 使用方案：**方案 A**（trajectory-level token cap 代码实现）

### 2. 代码改动（`agent_proxy.py`，694→715 行，+21 行净增）

**3 处修改：**

| 位置 | 行号 | 内容 |
|------|------|------|
| rollout() 初始化区 | L253-254 | `max_response_length = getattr(self.config.agent_proxy, 'max_response_length', None)` + `cumulative_response_tokens = np.zeros(len(env_outputs))` |
| entropy 块之后 | L295-304 | token 计数：优先用 `batch['responses']` tensor 计非 pad token 数，fallback 到 `non_tensor_batch['n_tokens']`，最终 fallback 到 `response_length` 估算 |
| es_manager.step 之后 | L336-339 | cap 检查：`if np.max(cumulative_response_tokens[active_ids]) >= max_response_length: break`，仅 `not val` 时生效 |

**Val/Train 隔离**：所有 cap 逻辑都有 `not val` 守卫，validation 不受影响。

### 3. Config 文件
`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_intervention_c_prime.yaml`
- `response_length: 1024`, `max_response_length: 12000`, `max_turn: 25`
- `seed.train: 999`, `total_training_steps: 7`, `kl_loss_coef: 0.01`, `save_freq: 5`

### 4. Dry-run：成功（`--cfg job` 解析无 Hydra 错误）

### 5. 训练提交
- PID: **347250**
- tmux session: **exp029_intervention_c_prime**
- Log: `~/runs/cost-verify-agent-rl/exp029_intervention_c_prime.log`
- W&B run: `exp029-intervention-c-prime` (run ID: zndyygbn)

### 6. GPU 确认
- cuda:0: RTX PRO 6000 96GB, `ray::WorkerDict` PID 350687, 4706MiB
- cuda:1: RTX PRO 6000 96GB, `ray::WorkerDict` PID 350688, 4706MiB

---
