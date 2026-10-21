# exp temp curve fix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_temp-curve-fix_20260517T223148_result.json`
- **Structured JSON:** [`9f361e3b638bb8b2a1ce.json`](../../sessions/9f/9f361e3b638bb8b2a1ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报如下：

---

**运行状态：**

| tmux session | GPU | 模型 | 温度 | top_p | 状态 |
|---|---|---|---|---|---|
| `tc_fix` (job 1/3) | cuda:0 | Pythia-2.8B | 0.5 | 0.9 | 运行中 (3/995 seeds) |
| `tc_fix` (job 2/3) | cuda:0 | Pythia-2.8B | 0.9 | 0.9 | 排队（等 job 1 完成） |
| `tc_fix` (job 3/3) | cuda:0 | Qwen3-1.7B | 0.9 | 0.9 | 排队（等 job 2 完成） |

**GPU 利用率：** 62%, 6193 MiB / 32607 MiB (RTX 5090)

**预估完成时间：**
- 每个 job: 995 seeds × ~10s/seed ≈ 2.75h
- 3 个生成 + 3 个特征提取 ≈ **9-10 小时**（约明早 UTC 08:30）

**注意事项：**
- 服务器只有 1 块 GPU，无法并行，改为串行执行
- 已删除 `data/pythia-2.8b-t05/` 中的错误数据（top_p=0.8 生成的部分文件）
- `pythia-2.8b-t09` 和 `qwen3-1.7b-t09` 之前未生成过，不需要清理
- 脚本在生成完成后会自动执行 feature extraction

---
