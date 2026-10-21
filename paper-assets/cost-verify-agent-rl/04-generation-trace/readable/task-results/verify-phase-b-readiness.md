# verify phase b readiness

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_phase_b_readiness_20260513T235057_result.json`
- **Structured JSON:** [`a4817732c72af54dbac3.json`](../../sessions/a4/a4817732c72af54dbac3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是状态报告。

---

## Phase B (B-IAVR) 集成就绪状态报告

### 1. Phase B 代码文件 — ✅ 已在服务器上

| 文件 | 内容 | 状态 |
|------|------|------|
| `ragen/biavr/__init__.py` | 模块入口，导出 BIAVRTracker | ✅ |
| `ragen/biavr/reward.py` | B-IAVR reward + lagrangian 乘子 | ✅ |
| `ragen/biavr/verify_mechanism.py` | VERIFY_TOKEN 机制 | ✅ |
| `ragen/biavr/action_canonicalize.py` | action 标准化 | ✅ |
| `ragen/biavr/pre_action.py` | pre-guidance action 计算 | ✅ |
| `ragen/biavr/tests/test_biavr.py` | 单元测试 | ✅ |
| `ragen/llm_agent/agent_proxy.py` | 集成点：BIAVRTracker | ✅ |
| `ragen/llm_agent/ctx_manager.py` | 集成点：verify_token | ✅ |
| `ragen/trainer/agent_trainer.py` | 集成点：biavr 训练 | ✅ |

### 2. exp003 当前状态

| 指标 | 值 |
|------|-----|
| 进度 | **Step 1/100** (1%) |
| 每步耗时 | ~5743s (~1h36m) |
| ETA 完成 | ~158h (~6.6 天) |
| 启动时间 | 2026-05-14 05:39 (北京时间) |
| 日志最后写入 | 07:28 |
| GPU 进程 | 2× ray::WorkerDict, 各 ~48GB |
| GPU 利用率 | 检查时 0%（可能在 rollout CPU 阶段） |
| Train success | 0.78% |
| Val success | 0% (初始) |
| Logger | console only, **无 wandb** |

### 3. Phase B 配置 — ⚠️ 部分就绪

`config/_alfworld_phase_b.yaml` 已存在，关键配置：
- `experiment_name`: exp003-alfworld-biavr-selective-verify
- `model_path`: **`TO_BE_SET`** ← 需要填入 Phase A checkpoint 路径
- `biavr`: beta=0.3, alpha=1.0, lambda_init=0.0, eta=0.01, enable_a_pre=true
- env tag: `AlfworldBIAVR`
- `max_model_len`: 32768（exp003 是 8192）

### 4. Checkpoint 路径

- exp003 配置 `save_freq: 20`，输出到 `/root/autodl-tmp/checkpoints/exp_003/`
- **两个 checkpoint 目录均不存在**（`/root/autodl-tmp/checkpoints/exp_003/` 和 `/root/cost-verify-agent-rl/RAGEN/checkpoints/...`）
- 首个 checkpoint 将在 step 20 产生，预计 ~30 小时后

### 5. 阻塞项

| # | 问题 | 严重性 | 说明 |
|---|------|--------|------|
| 1 | Phase B `model_path: TO_BE_SET` | 中 | 需等 exp003 产出 checkpoint 后填入 |
| 2 | checkpoint 目录不存在 | **高** | `/root/autodl-tmp/checkpoints/exp_003/` 不存在，step 20 时可能写入失败。建议提前 `mkdir -p` |
| 3 | exp003 无 wandb | 低 | 只能通过 log 文件监控，不影响训练 |
| 4 | 训练极慢 | 信息 | 100 steps 约 6.6 天，首个可用 checkpoint (step 20) 约 30h 后 |

---
