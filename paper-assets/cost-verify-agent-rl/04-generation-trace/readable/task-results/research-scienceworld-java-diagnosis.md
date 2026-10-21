# research scienceworld java diagnosis

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scienceworld_java_diagnosis_20260522T033541_result.json`
- **Structured JSON:** [`495994a5d0c8b7305143.json`](../../sessions/49/495994a5d0c8b7305143.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SFT checkpoint 在 bjb1-17606 上还在。诊断完成，以下是完整报告。

---

## ScienceWorld GRPO 诊断报告

### 1. Java 环境状态
- **两台服务器**：OpenJDK 11.0.30，`/usr/bin/java`
- `JAVA_HOME` 未设置，但不影响运行（py4j 通过 PATH 找到 Java）
- **Java 正常可用**

### 2. ScienceWorld 包状态
- **两台服务器**：scienceworld 1.2.3 + py4j 0.10.9.9
- JAR 随 pip 包自带

### 3. 初始化测试结果
- **westd-47453 上 ScienceWorld 初始化成功**：30 个任务可用，正常关闭
- 仅有 deprecated camelCase API 警告（无害）

### 4. 三次失败的根因分析

| 运行 | 日志文件 | 时间 | 根因 |
|------|---------|------|------|
| **Run 1** | `scienceworld_cell_c.log` | 5/20 20:44→23:29 | JVM 内部错误 → `Py4JError` 未被 `_is_jvm_dead()` 捕获 → 整个训练 crash |
| **Run 2** | `scienceworld_grpo_cell_c_v2.log` | 5/20→5/21 | **磁盘 95% 满**（250GB 仅剩 4.2GB），Ray raylet 无法 spill |
| **Run 3** | `scienceworld_grpo_cell_c_v3.log` | 5/21 02:25→10:43 | SIGTERM + core dump (exit code 129)，可能 OOM 或手动 kill |

**Run 1 核心问题**：`env.py:6` 的 `_is_jvm_dead()` 只检查 `Py4JNetworkError`，不检查 `Py4JError`。当 JVM 返回错误时，异常绕过 graceful abort 逻辑直接杀死整个训练进程。

### 5. 修复方案

**(a) 代码修复 — `_is_jvm_dead()` 缺陷**
```python
# 当前（有 bug）：
def _is_jvm_dead(exc):
    return isinstance(exc, (Py4JNetworkError, ConnectionError, OSError, BrokenPipeError))

# 修复后：
def _is_jvm_dead(exc):
    return isinstance(exc, (Py4JError, Py4JNetworkError, ConnectionError, OSError, BrokenPipeError))
```

**(b) SFT Checkpoint 传输**
- **bjb1-17606 上有**：`/root/autodl-tmp/checkpoints/scienceworld_sft/huggingface/`（完整模型 + tokenizer）
- **westd-47453 上丢失**
- 需从 bjb1 → westd SCP 传输

**(c) Config model_path 不一致**
- GRPO configs 引用 `qwen3_scienceworld_sft/huggingface`
- 实际 checkpoint 路径是 `scienceworld_sft/huggingface`
- 需要：在 westd 上将 SFT checkpoint 放到 `qwen3_scienceworld_sft/huggingface`（或修改 config）

**(d) 磁盘空间**
- westd-47453 当前 200G/250G used (80%)，有 51GB 空闲，比 Run 2 时好
- 仍需监控

**(e) JVM 堆内存**
- 当前 `-Xmx4g`，可考虑增至 `-Xmx8g` 减少 JVM 内部 OOM 导致的 crash

### 6. SFT Checkpoint 位置
- **bjb1-17606**: `/root/autodl-tmp/checkpoints/scienceworld_sft/huggingface/` (2 个 safetensors 分片 + tokenizer 文件)
- **westd-47453**: 已丢失

### 7. 可用的 ScienceWorld 训练配置

| Config 文件 | Context | GPU | Env Tag | model_path |
|---|---|---|---|---|
| `_scienceworld_cell_a.yaml` | step_independent, h=2 | 4 GPU (0,1,2,3) | ScienceWorldBoil | `scienceworld_sft/global_step_448/huggingface` |
| `_scienceworld_cell_c.yaml` | full | 4 GPU (0,1,2,3) | ScienceWorldBoil | `scienceworld_sft/global_step_448/huggingface` |
| `_scienceworld_cell_a_grpo.yaml` | step_independent, h=2 | 2 GPU (0,1) | ScienceWorldSG | `qwen3_scienceworld_sft/huggingface` |
| `_scienceworld_cell_c_grpo.yaml` | full | 2 GPU (2,3) | ScienceWorldSG | `qwen3_scienceworld_sft/huggingface` |
| `_scienceworld_cell_a_2gpu.yaml` | — | 2 GPU | — | — |
| `_scienceworld_cell_c_2gpu.yaml` | — | 2 GPU | — | — |

### 准备启动 GRPO 训练前需完成
1. 将 SFT checkpoint 从 bjb1 传到 westd（或在 bjb1 上跑）
2. 修复 `_is_jvm_dead()` 加入 `Py4JError`
3. 确认 config 的 `model_path` 指向正确位置
4. 确认目标服务器 GPU 可用 + 磁盘充足

---
