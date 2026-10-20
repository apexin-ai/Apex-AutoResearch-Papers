# infra exp028b resume

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp028b-resume_20260519T035853_result.json`
- **Structured JSON:** [`f96792d871bf485ae0c3.json`](../../sessions/f9/f96792d871bf485ae0c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**exp-028b resume 已部署到 westd-16639**

| 项目 | 详情 |
|------|------|
| 服务器 | westd-16639, cuda:2 |
| vLLM tmux | `exp028b_vllm` (port 8002) |
| 实验 tmux | `exp028b_run` |
| 模型 | Qwen3-14B (thinking mode, 内置) |
| 参数 | K=12, temp=0.7, max_tokens=16384, seed=42, max-model-len=32768 |
| 数据 | 38 题 (folio_166~folio_203) |
| 输出 | `results/exp028b_qwen3_thinking_folio204/exp028b_remaining38_results.json` |
| 日志 | `results/exp028b_qwen3_thinking_folio204/exp028b_resume.log` |
| 预计耗时 | ~38 × 120s ≈ 76 分钟 |

**Dry-run 结果**: 3/3 正确 (sica=1.0, sc=1.0)，无 OOM，单题 83-183 秒。

**注意事项**:
- 由于两台服务器无法直传文件，采用了只跑剩余 38 题的策略（而非 --resume）
- 完成后需将此结果与 westd-25068 上的 166 题结果合并为完整的 204 题结果
- Registry 中无 exp-028b 条目（0 条匹配），如需创建请告知

---
