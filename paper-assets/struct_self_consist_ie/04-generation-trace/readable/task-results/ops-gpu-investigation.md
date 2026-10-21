# ops gpu investigation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-investigation_20260522T171414_result.json`
- **Structured JSON:** [`7136d628f69e57fc1a9c.json`](../../sessions/71/7136d628f69e57fc1a9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存。核心发现：

**3 个 vLLM 进程，全部是本项目实验：**

| 服务器 | GPU | 实验 | 进度 | 状态 |
|--------|-----|------|------|------|
| autodl-5090 | cuda:3 | exp_fewnerd_pretrained_n32_s42_v2 | 4.6%, ETA ~13:00 UTC | ✅ 正常 |
| autodl-5090-c | cuda:1 | exp_fewnerd_pretrained_n16_s42_v2 | 22%, ETA ~07:15 UTC | ⚠️ Registry 未更新（仍为 PREPARING） |
| autodl-5090-c | cuda:3 | exp_fewnerd_pretrained_n32_s42 **v1 孤儿** | 81.5%, ETA ~04:10 UTC | ❌ 应 kill |

**建议操作：**
1. **P0**: Kill autodl-5090-c 上 PID 387495（v1 孤儿进程）— 使用旧代码，save 阶段会崩溃，白占 GPU
2. **P1**: 更新 `exp_fewnerd_pretrained_n16_s42_v2` registry 为 RUNNING
3. **P2**: `exp_fewnerd_mf4_s123_v2` 和 `exp_fewnerd_mf4_s456` 无残留进程，纯等分析

---
