# diagnosis gpu status check

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_gpu-status-check_20260512T040201_result.json`
- **Structured JSON:** [`c288ca672cff1a17dddc.json`](../../sessions/c2/c288ca672cff1a17dddc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### GPU 状态
- **利用率**: 0%, 0 MiB / 32607 MiB — 已空闲（之前确实空转了）

### 各进程状态
| 进程 | PID | 状态 |
|------|-----|------|
| kv-bench-002 | 22623 | **已完成** ✓ |
| DeepSeek-R1-Distill-Llama-8B 下载 | 18706 | **已完成** ✓ (15G) |
| Qwen2-7B-Instruct 下载 | 19552 | **已完成** ✓ (15G) |

### kv-bench-002 结果摘要
只有 30% budget 触发了 eviction (409次)，50%/70% 均未触发。

| Policy | 30% budget PPL | ratio |
|--------|---------------|-------|
| FullCache | 7.7274 | 1.000 |
| CARC-KV | 7.7436 | 1.002 |
| H2O | 7.7000 | 0.997 |
| StreamingLLM | 7.7480 | 1.003 |

**关键发现**: 10条×512 token 的文本太短，50%/70% budget 从未被填满，三种 policy 退化为 FullCache（PPL 完全一致、eviction=0）。只有 30% budget 产生了微弱差异（<0.3%），区分度极低。

### 已执行行动
1. **kv-bench-002** → registry 更新为 DONE (conclusion=success)
2. **confound-ctrl-001** → 已提交运行 (PID 24628, cuda:0, DeepSeek-R1-Distill-Llama-8B)
3. DeepSeek 模型验证通过: LlamaForCausalLM, 32层, 8 KV heads

### 下一步
- 监控 confound-ctrl-001 运行状态
- kv-bench 需要更长序列或更激进的 budget 才能有效区分 policy（当前实验信息量不足）

---
