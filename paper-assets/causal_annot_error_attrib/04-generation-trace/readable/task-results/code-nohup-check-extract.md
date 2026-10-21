# code nohup check extract

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_nohup_check_extract_20260522T102332_result.json`
- **Structured JSON:** [`e6880a4517f27ba1767f.json`](../../sessions/e6/e6880a4517f27ba1767f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果总结：

**进程状态**: 仍在运行（PID 929114, 已跑 ~3h46m），当前在处理 `vast/qwen3/zero-shot`（994/1500）。

**本次新完成的配置（已提取 CM）**:

| 配置 | n_valid | Accuracy | Source |
|------|---------|----------|--------|
| vast/deepseek_few-shot-3 | 1500 | 49.7% | npz |
| vast/deepseek_few-shot-5 | 1500 | 49.3% | npz |

两个 CM 均为 column-stochastic，标签顺序 [pro, con, neutral]。已写入 `artifacts/plan011_new_cms.json`。

**仍在进行/未完成**:
- `vast/qwen3/zero-shot` — 994/1500（进行中）
- `vast/qwen3/few-shot-3`, `vast/qwen3/few-shot-5` — 未开始（0 lines）
- `civil_comments/deepseek_zero-shot`, `deepseek_few-shot-3`, `llama4_*` — 未开始或仅 2 行
- `vast/llama4_few-shot-5` — 346 行，排除（<500）
- `vast/deepseek_zero-shot` — 已更新至 1500 样本但按要求排除（degenerate）

**排除项**: vast/deepseek_zero-shot（指令排除），vast/llama4_few-shot-5（n_valid=346 < 500）

---
