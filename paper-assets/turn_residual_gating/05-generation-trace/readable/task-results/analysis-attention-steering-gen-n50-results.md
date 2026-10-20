# analysis attention steering gen n50 results

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_attention_steering_gen_n50_results_20260520T193757_result.json`
- **Structured JSON:** [`83d51f220afdbba94ef2.json`](../../sessions/83/83d51f220afdbba94ef2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程仍在运行。** 当前状态：

### 进度

| β | 状态 | 进度 |
|---|------|------|
| 0.0 | 完成 | 50/50 |
| 2.0 | 完成 | 50/50 |
| 3.0 | 完成 | 50/50 |
| 4.0 | **运行中** | 12/50 |
| 5.0 | 待运行 | 0/50 |
| 10.0 | 待运行 | 0/50 |

总进度：162/300 convs (54%)

### 已完成 β 的中间结果

| β | Mid-turns avg GAR | Avg PPL |
|---|-------------------|---------|
| 0.0 | 0.1011 | 1.43 |
| 2.0 | 0.2068 | 1.48 |
| 3.0 | 0.6662 | 1.56 |

### 与 N=5 gen 对比（已完成部分）

| β | N=50 GAR | N=5 GAR | N=50 PPL | N=5 PPL |
|---|----------|---------|----------|---------|
| 0 | 0.101 | 0.028 | 1.43 | 1.41 |
| 2 | 0.207 | 0.062 | 1.48 | 1.41 |
| 3 | 0.666 | — | 1.56 | — |

### 初步发现

1. **Phase transition 重现**：β=2→3 出现 GAR 从 0.21 跳到 0.67 的剧烈跃迁（3.2×），与 N=5 中 β=2→5 的跳跃模式一致，但 N=50 的 transition point 更早（β≈3 而非 β≈5）
2. **N=50 的 GAR 系统性偏高**：β=0 时 N=50 GAR (0.101) 比 N=5 (0.028) 高 3.6×，β=2 时差距更大（0.207 vs 0.062）。更多 conversation 样本暴露了更高的 baseline GAR
3. **PPL 稳定**：β=0~3 的 PPL 增幅很小（1.43→1.56），说明 moderate β 下 attention steering 没有显著损害生成质量

### 剩余时间估算

已完成 3.24/6 个 beta（β=4 完成 24%），约 54%。每个 beta 约需 ~25-30 分钟（gen mode 需要逐 token 生成），剩余约 2.76 个 beta，预计还需 **70-85 分钟**。

需要我稍后再次检查，还是等完成后再汇报完整数据？

---
