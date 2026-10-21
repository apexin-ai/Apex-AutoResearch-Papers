# exp null t15 and gpt2m

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_null_t15_and_gpt2m_20260524T032404_result.json`
- **Structured JSON:** [`bcdab1562292d8576586.json`](../../sessions/bc/bcdab1562292d8576586.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部成功启动，正在训练 Generation 0。

## 启动状态
| exp_id | Server | GPU | 状态 | PID |
|--------|--------|-----|------|-----|
| null_t15_s42_fp32 | westd-19828 | 0 | 运行中 (Gen 0, 7453 MiB, 83%) | 919940 |
| null_t15_s43_fp32 | westd-19828 | 1 | 运行中 (Gen 0, 7453 MiB, 80%) | 920577 |
| null_gpt2m_s42_fp32 | westd-17855 | 4 | 运行中 (Gen 0, 6151 MiB, 89%) | 861043 |
| null_gpt2m_s43_fp32 | westd-17855 | 5 | 运行中 (Gen 0, 6151 MiB, 78%) | 861354 |

**关键参数差异 vs 模板：**
- 模型名用 `openai-community/gpt2-medium`（非 `gpt2-medium`），与已有 GPT-2m 实验一致
- 添加 `HF_HUB_OFFLINE=1` 解决 AutoDL 网络不可达问题
- 日志：`/tmp/null_t15_s4{2,3}.log`（19828）、`/tmp/null_gpt2m_s4{2,3}.log`（17855）

**注意：** westd-17855 磁盘 95% (18G 剩余)，null 实验占用小（~100MB/实验），但需关注整体空间。

---
