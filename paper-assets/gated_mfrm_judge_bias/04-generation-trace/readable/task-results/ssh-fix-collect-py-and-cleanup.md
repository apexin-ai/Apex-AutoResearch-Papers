# ssh fix collect py and cleanup

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_collect_py_and_cleanup_20260522T055454_result.json`
- **Structured JSON:** [`cc18133a0c77169dad2a.json`](../../sessions/cc/cc18133a0c77169dad2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集。tmux sessions 中没有 gemini、sonnet、qwen3 — 已经不存在了，无需清理。

---

## 汇报

### 1. collect.py 修复 ✓

**Diff**（第 45-47 行新增）：
```python
            try:
                obj = json.loads(line)
+               if obj.get("status") == "failed":
+                   continue
                if mode == "pointwise":
```
语法验证：**SYNTAX_OK**。备份已保存为 `collect.py.bak`。

### 2. tmux sessions 清理

已停 judge sessions（gemini、sonnet、qwen3）**已经不存在**，无需清理。

当前存活 sessions：
| Session | 类型 |
|---------|------|
| exp001-gpt55 | proxy judge（保留）|
| exp001-llama | local judge（保留）|
| exp001-qwen | local judge（保留）|
| exp001-mistral | local judge（保留）|
| vllm-llama | vLLM 推理服务（保留）|
| vllm-mistral | vLLM 推理服务（保留）|

### 3. Local judges 状态

| Judge | 独立输出目录 | Judgments | Remaining | 状态 |
|-------|-------------|-----------|-----------|------|
| llama-3.3-70b | ✓ `results/llama-3.3-70b/` | 186 | 2827 | 运行中，~10 done since restart |
| qwen2.5-72b | ✓ `results/qwen2.5-72b/` | 102 | 2907 | 运行中 |
| mistral-large-2 | ✓ `results/mistral-large-2/` | 43 | 2979 | 运行中 |

三个 local judges 均有**独立输出目录**，各自写入独立的 `arena_hard_judgments.jsonl`。

### 4. GPU 状态

| GPU | 显存使用 | 利用率 |
|-----|---------|--------|
| GPU 0 | 73.8 / 97.9 GB | 62% |
| GPU 1 | 88.1 / 97.9 GB | 100% |
| GPU 2 | 90.1 / 97.9 GB | 100% |
| GPU 3 | 88.1 / 97.9 GB | 100% |

4 卡全部在用，GPU 1-3 满载。

---
