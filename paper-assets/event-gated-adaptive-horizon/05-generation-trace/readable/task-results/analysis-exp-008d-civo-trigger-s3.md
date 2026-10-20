# analysis exp 008d civo trigger s3

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_008d_civo_trigger_s3_20260517T031958_result.json`
- **Structured JSON:** [`aa2107b9bc4ae05d11b8.json`](../../sessions/aa/aa2107b9bc4ae05d11b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结论：SUCCESS (Late-Onset CIVO Collapse)

**关键发现**：

| 指标 | 值 |
|------|-----|
| NVE onset | 1.50× @ 45K (sustained @ 55K) |
| NVE final | 1.53× @ 105K |
| Eval peak | 451.7 @ 95K |
| Eval final | 267.6 @ 105K (**-41% from peak**) |
| Train returns @ end | 82-214 (severe collapse, still declining) |
| vs baseline | **-70.8%** |

**Collapse pattern**：与 seed=0 的即时单调下降不同，seed=3 呈现"延迟崩溃"模式：先升（eval 36→452@95K），NVE 在中间暂时回落（65-95K），然后 eval 逆转崩溃，NVE 重回 1.53×。训练结束时 train returns 仍在急剧下降（547→82），表明崩溃尚未触底。

**Cross-seed 总结（trained dt_emb + subsample）**：
- NVE ≥ 1.5× onset：**3/3 seeds**（系统性诊断标记）
- 持续崩溃：**2/3 seeds**（seed=0 即时，seed=3 延迟）
- 自修正：**1/3 seeds**（seed=2）

CIVO 机制在所有 seed 上可靠触发 NVE>1.5×，崩溃是多数结果（2/3）。报告已写入 artifacts。

---
