# analysis exp009

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp009_20260514T034042_result.json`
- **Structured JSON:** [`d0abf50015e644aa4c44.json`](../../sessions/d0/d0abf50015e644aa4c44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp009 分析结果

**结论：FAILED — 训练从未启动**

### 根因

`train.py:137` 的配置验证检查 `model_path` 是否包含 "qwen" 或 "llama-3" 字符串来判断是否支持 `enable_response_mask`。SFT checkpoint 路径 `/root/autodl-tmp/checkpoints/exp008_sft/final` 不含这些字符串，但模型实际上是 Qwen3ForCausalLM — 这是一个 bug（路径字符串匹配 vs 模型架构检查）。

### 修复方案

在 `_alfworld_exp008_sft_grpo.yaml` 中添加：

```yaml
enable_response_mask: False
```

或者将 checkpoint 路径改为包含 "qwen" 的路径。

### 产出

- 报告：`artifacts/exp009/report/exp009_analysis.md`
- Registry 已更新：status=DONE, conclusion=failed, metrics 记录了失败原因

---
