# code confound ctrl 001 prep

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_confound-ctrl-001-prep_20260512T022820_result.json`
- **Structured JSON:** [`a87b7b63c8807eb5e766.json`](../../sessions/a8/a87b7b63c8807eb5e766.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载进行中（PID 18706 存活），约 5% 完成，速度 ~1.5-2.7 MB/s，预计还需 60-80 分钟。

**已完成：**
- [x] 启动 DeepSeek-R1-Distill-Llama-8B 下载 (nohup 后台，PID=18706)
- [x] 创建 `results/confound_ctrl/` 目录
- [x] 编写 `confound_ctrl_001.py`（411 行，语法检查通过）
  - MODEL_PATH → `/root/autodl-tmp/.ms_cache/deepseek-ai/DeepSeek-R1-Distill-Llama-8B`
  - 输出 → `confound_ctrl_001_results.json`
  - metadata 包含完整的对照实验设计（hypothesis, compare_against, interpretation）
  - MAX_NEW_TOKENS = 4096（推理模型长 CoT）

**待完成（下载完成后）：**
- [ ] 验证模型可加载 + 确认架构 (32 layers, 8 KV heads, LlamaForCausalLM)
- [ ] 不提交实验（GPU 被 llama-sparsity-sweep 占用）

要我继续轮询下载进度，还是你稍后再来检查？

---
