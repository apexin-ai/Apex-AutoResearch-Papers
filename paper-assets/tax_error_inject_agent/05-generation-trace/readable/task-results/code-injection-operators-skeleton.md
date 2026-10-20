# code injection operators skeleton

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_injection-operators-skeleton_20260514T050719_result.json`
- **Structured JSON:** [`3f9b6db9fbd736862fbe.json`](../../sessions/3f/3f9b6db9fbd736862fbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SSH 仍然不通。代码已全部写好在本地 `artifacts/` 下，等 SSH 恢复后可以一次性同步。

---

## 产出汇报

### 1. 各文件实现概要

| 文件 | 内容 |
|------|------|
| `injection/base.py` | `InjectionOperator` ABC（inject/validate/describe）、`ErrorInjectMemory`（继承 SimpleMemory，重写 fetch 在返回前应用注入链）、`ErrorInjectEnvManager`（继承 AlfWorldEnvironmentManager，用 ErrorInjectMemory 替换默认 memory，step() 支持 obs-level 注入） |
| `injection/planning.py` | `P1_StepOrderSwap`（在最近 N 步内随机选两个相邻步交换）、`P2_SubGoalDeletion`（random/critical 策略删除一个步骤，critical 优先删含 pick/put/heat/cool/clean 等动作的步骤） |
| `injection/context.py` | `C1_ContextTruncation`（按 truncation_ratio 截断早期历史）、`C4_ObservationMasking`（按概率将 obs 替换为空串或 "You see nothing special."） |
| `data/collector.py` | `TrajectoryCollector` 骨架，GPT-4o rollout 逻辑用 TODO 标记等 API key |
| `data/formatter.py` | `format_for_sft()`，将轨迹转为 ms-swift 多轮对话 JSONL 格式 |
| `eval/recovery.py` | `evaluate_recovery()`，per-operator 恢复率 + baseline 成功率评测框架 |
| `configs/default.yaml` | 注入参数、数据收集、LoRA 训练、评测的默认配置 |

### 2. 语法检查
全部 6 个 Python 文件 `py_compile` 通过。

### 3. 关键设计决策

- **注入点分层**：Memory-level 注入（P1/P2/C1）在 `ErrorInjectMemory.fetch()` 中执行，Observation-level 注入（C4）在 `ErrorInjectEnvManager.step()` 返回后执行。两层互不干扰。
- **非破坏性**：`ErrorInjectMemory.fetch()` 在深拷贝上操作，注入后恢复原始 `_data`，不影响真实环境状态。
- **注入日志**：每次注入记录 `InjectionRecord`（env_idx, step, operator, before/after），用于后续分析和数据集构建。
- **配置驱动**：所有算子通过 `inject_config` 字典动态启用/禁用和参数化。

### 4. 待办 TODO

- **SSH 连接**：`~/.ssh/id_ed25519` 不存在，需要配置密钥后同步代码到服务器
- **API Key**：`data/collector.py` 中 GPT-4o 调用需要 API key
- **verl-agent 集成测试**：verl-agent clone 就绪后，验证 import 路径和 SimpleMemory/AlfWorldEnvironmentManager 接口兼容性
- **eval/recovery.py**：模型加载和环境初始化逻辑待实现

---
