# ops prep t15 a045 d102 and cleanup

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep-t15-a045-d102-and-cleanup_20260523T041221_result.json`
- **Structured JSON:** [`f60bb9a8bc9346419eea.json`](../../sessions/f6/f60bb9a8bc9346419eea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个部分全部处理完毕。汇总结果：

---

### Part 1: 磁盘清理

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 325G (93%) | 297G (85%) |
| 可用 | 26G | 54G |
| **释放** | — | **28G** |

清理内容：
- 3 个 14b 中间 checkpoint（`t10_a045_s43/gen_1`, `scale/14b_t10_a060_s43/gen_5`, `scale/14b_t10_a075_s43/gen_5`）→ 15.9G
- 8 个非 14b 倒数第二代 checkpoint（`t15_a045_s43/gen_14`, `t25_a060/gen_24`, `t25_a050/gen_24`, `t20_a060_s43/gen_19`, `t25_a045_s43/gen_24`, `t15_a075_s43/gen_14`, `t10_a075_s43/gen_9`, `t20_a075_s43/gen_19`）→ 12.8G

注：用户指定的 5 个已完成 14b 实验（t15_a060, t15_a050, t10_a060, t10_a075, t10_a045）的中间 gen 此前已清理过（每个仅 12K），空间集中在最终 gen（不可删）。

### Part 2: t15_a075 路径修正

- 实验数据在 `outputs/scale_14b_t15_a075_s42_fp32`（19828）
- 已创建 symlink：`results/phase_diagram/t15_a075_s42_fp32_14b → outputs/scale_14b_t15_a075_s42_fp32` ✓
- **实验仍在运行**（PID 793171），当前训练 gen_14（gen_0~gen_15 共 16 代），还剩 gen_14 + gen_15 两代
- 19828 上还有另一个实验 `14b_t10_a050_s43`（PID 822048, GPU1）在跑

### Part 3: t15_a045_s42 状态

- **PID 680608 仍在运行**（已跑 15h10m）
- 当前正在训练 gen_15（最后一代）：synthetic_data 已生成（12:06），training 进行中
- gen_14 checkpoint 保存于 11:38，gen_15 训练开始于 ~12:06
- 每代训练约 35-40 分钟
- **预计完成时间：~12:40-12:50 CST（约 25-30 分钟后）**
- 完成后会生成 all_metrics.json，届时可跑 D102

需要我设置一个定时检查来等 t15_a045 完成后自动跑 D102 吗？

---
