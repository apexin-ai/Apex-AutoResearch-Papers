# code exp 019 prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-019-prep_20260517T081945_result.json`
- **Structured JSON:** [`4229dcf17c5c35886a52.json`](../../sessions/42/4229dcf17c5c35886a52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**exp-019 已经在运行中**，无需额外准备。当前状态：

| 项目 | 状态 |
|------|------|
| **脚本** | `~/symb_invariant_consensus/scripts/run_exp019_strategyqa_200.sh` ✓ 已存在 |
| **数据** | `data/strategyqa_200.json` ✓ (200题，格式正确) |
| **模型** | LLaMA-3.1-8B-Instruct ✓ 已下载，vLLM 正在服务 (port 8000) |
| **进度** | **8/200 完成** (SICA 75%, SC 75%, delta=0.0)，正在跑 |
| **参数** | K=12, T=0.7, max-tokens=4096, seed=42 |
| **日志** | `~/runs/symb_invariant_consensus/exp-019-llama8b-strategyqa-200.log` |

### 注意事项

1. **K=12 vs K=5**：任务要求 K=5，但现有脚本和正在运行的实验用 K=12（与 exp-011 一致）。如果需要改为 K=5，需要中止当前运行并重跑。请确认是否要继续 K=12 还是改为 K=5。

2. **无阻塞项**：环境、模型、数据、脚本全部就绪，实验已自动启动。

3. **预估运行时间**：每题约 20-25s（从日志看），200题预计 ~70-80 分钟总耗时。已跑约 3 分钟完成 8 题，剩余约 80 分钟。

4. **没有 bootstrap test**：现有脚本不含 bootstrap p-value 计算（exp-011 也没有内建在脚本里）。如果需要 p-value，需要在实验完成后单独跑分析脚本。

---
