# analysis openvla per task gap

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_openvla-per-task-gap_20260517T224616_result.json`
- **Structured JSON:** [`94ee1c856511fbf467eb.json`](../../sessions/94/94ee1c856511fbf467eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成。核心发现：

**Per-task 成功率** (官方 eval 脚本, seed=42, 10 trials each):

| Task | SR |
|------|--:|
| alphabet_soup | 90% |
| cream_cheese | 80% |
| salad_dressing | **50%** |
| bbq_sauce | **20%** |
| ketchup | 80% |
| tomato_sauce | 80% |
| butter | **50%** |
| milk | 90% |
| chocolate_pudding | 80% |
| orange_juice | 70% |
| **Overall** | **69%** |

**69% vs 88.4% gap 的主要原因**（按贡献排序）：

1. **样本量太小**（最主要）：10 trials vs 论文的 50 trials，3 个 task 严重偏低（bbq_sauce 20%）就拉低 12pp
2. **Initial state 子集偏差**：只用了 0-9 号初始状态，论文用了 0-49
3. **flash_attn 未安装**：模型训练时用 flash_attn 2.5.5，我们环境缺失
4. **GPU 差异**：RTX 4090 vs A100，OpenVLA 作者明确说不同 GPU 会有差异
5. **Seed 选择**：单个 seed=42 vs 论文 3 seeds 平均

**建议**：安装 flash_attn，用 50 trials + seed=7 重跑。69% 不应作为 baseline 引用。

报告已写入 `artifacts/openvla_gap_analysis.md`。

---
