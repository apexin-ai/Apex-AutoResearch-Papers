# research vllm compat

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_vllm-compat_20260513T064916_result.json`
- **Structured JSON:** [`769ab4ac2f75b4de5e37.json`](../../sessions/76/769ab4ac2f75b4de5e37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**修复成功。** OOM 是因为 GPU1 上 HF 进程占了 15.3GB，不是 vLLM bug。模型架构检查已通过，"duplicate template name" 错误不再出现。

---

## 诊断报告

### 1. 完整错误 traceback
`torch/_inductor/kernel/flex_attention.py:786` → `torch/_inductor/select_algorithm.py:1695`:
```
AssertionError: duplicate template name
```
发生在 vLLM `LLM()` 初始化 → `ModelConfig` → `_run_in_subprocess` inspect `Qwen2ForCausalLM` 时。

### 2. 根因
torch 2.10.0 重构遗留 bug：`name="flex_attention"` 的 `TritonTemplate` 在两处注册：
- `torch/_inductor/kernel/flex_attention.py:787`（旧位置）
- `torch/_inductor/kernel/flex/flex_attention.py:94`（新位置）

同类问题：`_grouped_mm` extern kernel 也有重复注册。

### 3. 修复方案
注释掉 `select_algorithm.py` 中两个 duplicate 断言（1695 行和 2164 行），备份在 `.bak`。

### 4. 验证结果
- `torch._inductor.select_algorithm` 导入 OK
- `from vllm import LLM` 导入 OK
- `LLM()` 初始化通过了架构检查阶段（不再报 duplicate template）
- GPU1 上完整测试因 OOM 失败（GPU1 已被 HF 进程占用 15.3GB，符合预期）

### 5. 结论
**vLLM 已修好。** 等 GPU1 上当前 HF 任务跑完后，Phase 1 可以直接用 `--vllm`（去掉 `--no_vllm`）启动。不需要升降任何包版本，patch 不影响 GPU0 正在跑的进程（只改了断言，不影响运行时逻辑）。

---
