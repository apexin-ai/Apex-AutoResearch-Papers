# code exp013f setup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp013f-setup_20260514T092427_result.json`
- **Structured JSON:** [`a2c7be3b240c6a9bf652.json`](../../sessions/a2/a2c7be3b240c6a9bf652.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部步骤完成。汇报：

---

## exp013f 准备报告

### 1. 环境清理结果
- Ray sessions 已清除（`/root/autodl-tmp/tmp/ray/session_*` 和 `/tmp/ray/session_*`）
- 无残留 ray/train 进程
- GPU：2× RTX PRO 6000 96GB，0MiB 占用，0% 利用率
- 内存：总 1TB，可用 919GB

### 2. val env_groups 调查结论
- **当前值**：`es_manager.val.env_groups: 16`，`es_manager.val.env_configs.n_groups: [16]`
- **可以单独设置**：val 和 train 在 yaml 中是独立字段，Hydra override 可直接覆盖
- **设置方式**：Hydra override `es_manager.val.env_groups=4 'es_manager.val.env_configs.n_groups=[4]'`
- **约束**：`es_manager.py:65` 断言 `sum(n_groups) == env_groups`，两者必须一致

### 3. yaml config 未修改
val env_groups 通过 Hydra override 设置，未改动 `_alfworld_exp013b_dense_reward.yaml`。

### 4. 启动脚本
`/root/cost-verify-agent-rl/scripts/run_exp013f.sh`，已 chmod +x。关键参数：
- `RAY_memory_monitor_refresh_ms=0`（禁用 MemoryMonitor）
- `RAY_SYSTEM_MEMORY=210000000000`（210GB，cgroup 220GB - 10GB 余量）
- `es_manager.val.env_groups=4`（从 16 降到 4）
- `es_manager.val.env_configs.n_groups=[4]`（匹配 env_groups）

### 5. dry-run 验证结果
```
experiment_name: exp013f-alfworld-dense-reward
train: env_groups=4, group_size=16, n_groups=[4]
val:   env_groups=4, group_size=1,  n_groups=[4]
```
配置解析通过，无报错。

### 6. object_store_memory 硬编码确认
`train.py:203`：`ray_init_kwargs["object_store_memory"] = 30 * 1024**3`（30GB 硬编码）。

---
