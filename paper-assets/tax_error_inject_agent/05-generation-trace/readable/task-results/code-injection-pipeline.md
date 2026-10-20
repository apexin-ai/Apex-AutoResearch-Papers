# code injection pipeline

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_injection-pipeline_20260514T064609_result.json`
- **Structured JSON:** [`984c330d681b3e09ee32.json`](../../sessions/98/984c330d681b3e09ee32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### 1. Qwen3-8B 下载状态：**已完成**
- 路径：`/root/autodl-tmp/models/Qwen/Qwen3-8B/`
- 5 个 safetensors 分片全部就位（共 ~15.2GB）
- 日志确认：`Download model 'Qwen/Qwen3-8B' successfully.`

### 2. Qwen3-32B 下载状态：**已完成（AWQ 量化版）**
- 路径：`/root/autodl-tmp/models/Qwen/Qwen3-32B-AWQ/`
- 日志确认：`Download model 'Qwen/Qwen3-32B-AWQ' successfully.`
- 注意：下载的是 AWQ 量化版本而非原始精度

### 3. inject_and_generate.py 实现概要
- **InjectionPipeline** 核心类，集成 4 个注入算子（P1/P2/C1/C4），均匀分配变体数
- 对每条成功轨迹：选注入点 → 截取 history prefix → 调用算子生成 corrupted history → 构建 recovery prompt → 调 GPT-5.2 生成恢复示范
- 自动处理 `observation`/`text_obs` 键名映射（兼容 C4 算子）
- `--dry_run` 模式跳过 API 调用，只生成注入变体
- 多线程 API 并发 + CostTracker 记账 + JSONL 输出

### 4. 语法检查：**通过**
- `py_compile` 通过
- `--help` 正常输出
- dry-run 20 条变体：16 成功 / 4 失败（短轨迹注入点不足），4 算子各 4 条，分布均匀

---
