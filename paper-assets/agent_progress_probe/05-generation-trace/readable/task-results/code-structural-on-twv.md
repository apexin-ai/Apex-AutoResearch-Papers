# code structural on twv

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_structural-on-twv_20260514T173953_result.json`
- **Structured JSON:** [`567a22518b74995a98aa.json`](../../sessions/56/567a22518b74995a98aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 和 artifact 均已注册。结果汇总：

## In-Domain (macro_f1)

| Setting | LR | RF | GB |
|---------|------|------|------|
| MV→MV (self) | 0.9860 | 0.9944 | **0.9951** |
| TWV→TWV (self) | 0.9292 | 0.9357 | 0.9383 |
| TWV→MV (cross) | 0.9314 | 0.9433 | 0.9457 |
| MV→TWV (cross) | 0.9175 | 0.9164 | 0.9186 |

## Cross-Agent → OpenHands (macro_f1)

| Setting | LR | RF | GB |
|---------|------|------|------|
| MV→OH all | 0.7527 | 0.9211 | **0.9698** |
| TWV→OH all | 0.8190 | **0.9386** | 0.7529 |
| MV→OH conf≥2 | 0.9626 | **0.9969** | 0.9949 |
| TWV→OH conf≥2 | 0.9674 | **0.9786** | 0.8983 |

关键发现：
- TWV 标签对结构分类器更难（GB 0.9383 vs MV 0.9951），说明 TWV 引入了 MV 没有的细粒度区分
- Cross-label gap 不对称：TWV→MV (0.9457) > MV→TWV (0.9186)，MV-trained 模型不能很好识别 TWV 认为的 stagnation
- Cross-agent 上 TWV-trained 模型表现更不稳定（GB 在 OH-all 仅 0.7529），但 TWV-trained RF 在 OH-conf≥2 上 0.9786 仍然很强
- MV-trained 模型在 cross-agent 转移上更一致，GB 在 OH-all 达到 0.9698

---
