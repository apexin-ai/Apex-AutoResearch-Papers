# submit exp 023 wiki domain

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp_023_wiki_domain_20260516T115910_result.json`
- **Structured JSON:** [`02db4c4138d9e4a8c969.json`](../../sessions/02/02db4c4138d9e4a8c969.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-023 已成功启动并运行。

**汇总：**

| 项目 | 结果 |
|------|------|
| 数据 | `depth_0.jsonl` — 5000 行，字段 `[text, doc_id]` ✓ |
| 模型 | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B` 存在 ✓ |
| 脚本修改 | `CUDA_VISIBLE_DEVICES=3` → `1` ✓ |
| PID | 39530 (tmux session: `exp_023_domain_ablation`) |
| GPU 占用 | cuda:1 已加载模型，3706 MiB |
| 日志 | 模型加载完成，参数确认：`top_p=0.95, temperature=1.0, continuation, 5K samples, depth 0-5` |
| 预估时间 | 5K docs × 6 depths × batch_size=16 → 约 2-4 小时 |

---
