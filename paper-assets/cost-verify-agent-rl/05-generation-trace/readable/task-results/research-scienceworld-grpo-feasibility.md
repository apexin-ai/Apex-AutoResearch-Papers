# research scienceworld grpo feasibility

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scienceworld_grpo_feasibility_20260519T201151_result.json`
- **Structured JSON:** [`4a85ea3b9d2070fe5c8c.json`](../../sessions/4a/4a85ea3b9d2070fe5c8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完毕。以下是结论。

---

## ScienceWorld GRPO 开发工作量评估

### 1. 集成状态：**完整**

所有核心组件已就绪：

| 组件 | 状态 | 路径 |
|------|------|------|
| Env Wrapper | ✅ 完整 | `ragen/env/scienceworld/env.py` — `ScienceWorldTXTEnv` 继承 `BaseLanguageBasedEnv` |
| Config | ✅ 完整 | `ragen/env/scienceworld/config.py` — `ScienceWorldEnvConfig` |
| 注册 | ✅ 完整 | `ragen/env/__init__.py` — `REGISTERED_ENVS['scienceworld']` |
| Env Tags | ✅ 4个 | `envs.yaml`: `ScienceWorldBoil`, `ScienceWorldMelt`, `ScienceWorldFreeze`, `ScienceWorldMixed` |
| Python 包 | ✅ 已装 | `scienceworld==1.2.3` |
| SFT Checkpoint | ✅ 4个 | `global_step_{112,224,336,448}`，每个都有 `huggingface/` HF 格式模型 |
| SFT 训练数据 | ✅ 有 | `scienceworld_sft_{train,val}.parquet` |
| GRPO Config | ❌ 缺 | 无 `_scienceworld_*.yaml` GRPO 配置文件 |

### 2. 需要开发的内容

**唯一缺少的是 GRPO 训练配置文件**，可以直接从 ALFWorld 的 `_alfworld_exp029_episode_level.yaml` 复制并修改：

需改动的字段：
- `model_path` → `/root/autodl-tmp/checkpoints/scienceworld_sft/global_step_448/huggingface`
- `experiment_name` → `scienceworld-grpo-cell-a`（或 cell-c）
- `es_manager.train/val.env_configs.tags` → `["ScienceWorldBoil"]` 或 `["ScienceWorldMixed"]`
- `CUDA_VISIBLE_DEVICES` → `"0,1,2,3"`（westd-47453 有 4 张 GPU）
- `n_gpus_per_node` → 4
- `agent_proxy.max_turn` → 按 ScienceWorld 调整（当前 env 的 `max_steps=100`，但单次 GRPO turn 不一定等于 100 steps）
- `local_log_dir` / `default_local_dir` → 新路径

### 3. ScienceWorld vs ALFWorld 关键技术差异

| 维度 | ALFWorld | ScienceWorld |
|------|----------|-------------|
| Action Space | 文本命令，admissible actions 动态生成 | 同样文本，`get_valid_action_object_combinations()` |
| Observation | 房间描述 + 物品 | 房间描述 + 物品 + task description |
| Reward | Binary sparse (won=1 → 10.0) | Continuous sparse (score/100 * 10.0, 0~10) |
| 并行 | 可多 worker | `max_workers=1`，JVM 单例（`_ENV_CACHE` per thread）|
| Episode 长度 | ~50 steps | ~100 steps（更长） |
| 环境启动 | 快（TextWorld） | 慢（JVM 启动） |

**关键风险**：`parallel_friendly: false` + `max_workers: 1`。ScienceWorld 底层是 JVM，当前实现用 thread-local 单例缓存，多 worker rollout 可能需要验证 JVM 线程安全性。ALFWorld 也是 `parallel_friendly: false`，但它基于 TextWorld，不涉及 JVM。

### 4. 工作量估计

| 任务 | 估时 |
|------|------|
| 写 GRPO config yaml（Cell A + Cell C） | 30 min |
| 验证 SFT checkpoint 能正确加载 | 15 min |
| Dry-run 验证 env + rollout 能跑通 | 1-2 hr（JVM 启动、多线程问题排查） |
| 正式训练 | 取决于 GPU 时间 |

**总开发工作量：~2-3 小时**（含排查时间）。核心工作就是写一个 yaml 配置文件 + dry-run 验证。

### 5. 建议优先级

1. **先跑 `ScienceWorldBoil` 单任务**（最简单，变量最少）
2. Dry-run 重点验证 JVM 多线程在 GRPO rollout 下是否稳定
3. 确认后再扩展到 `ScienceWorldMixed`

---
