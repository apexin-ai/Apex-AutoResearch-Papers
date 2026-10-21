# paper prewrite discussion limitations

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_prewrite-discussion-limitations_20260519T190748_result.json`
- **Structured JSON:** [`b542fddeebcc01d9e83c.json`](../../sessions/b5/b542fddeebcc01d9e83c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。

### 修改汇报

**修改 1: Discussion §Single-LLM confound (行 10-11)**
- 保留原有 ToxicChat + cross-LLM 实验内容（行 10）
- 新增行 11：exp16 mixed-training 结果段落，framing 为 "mitigates but does not eliminate"

**修改 2: Limitations §Dataset scale and diversity (行 28)**
- 原 "500 synthetic conversations" 规模限制替换为 exp17 scale validation 结果
- 保留 perturbation underpowered 警告、synthetic-to-real gap、ToxicChat 转移确认
- 行 29 cross-LLM 内容未动

### 占位符列表

| 占位符 | 对应 metric |
|--------|------------|
| `[EXP16_BASELINE]` | 混合训练前 cross-LLM detection F1（当前 0.37-0.43 区间的具体值） |
| `[EXP16_MIXED_F1]` | 混合训练后 cross-LLM detection F1 |
| `[EXP16_FPR_BASELINE]` | 混合训练前 Llama benign text 上的 false positive rate |
| `[EXP16_FPR_MIXED]` | 混合训练后 Llama benign text 上的 false positive rate |
| `[EXP16_RESIDUAL]` | 混合训练后残余 gap 的定性/定量描述 |
| `[EXP17_1000]` | exp17 实际训练集规模（预期 1000） |
| `[EXP17_OOD_F1]` | 1000-scale 训练后 OOD detection F1 |
| `[EXP17_DAPT_GAP]` | 1000-scale 下 DAPT vs vanilla 的 F1 差距（pp） |

### 字数变化
- 修改 1：原 ~80 词 → ~130 词（+50 词）
- 修改 2：原 ~95 词 → ~80 词（-15 词）
- 净增约 35 词

---
