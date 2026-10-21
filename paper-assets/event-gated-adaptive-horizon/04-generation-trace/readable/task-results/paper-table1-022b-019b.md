# paper table1 022b 019b

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table1-022b-019b_20260517T155319_result.json`
- **Structured JSON:** [`e11713c8225b6a57a08e.json`](../../sessions/e1/e11713c8225b6a57a08e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。Table 1 修改如下：

1. **022b** 添加在 015b 之后（line 35），配置为 "Frozen emb + Gumbel gate"，frz$^b$/ON/8，Eval 300.7 @105K，NVE 1.22×，Outcome "No CIVO"
2. **019b** 添加在 cross-environment section（line 46），配置为 "PickCube-v1"，trn/ON/8，Eval 26.64 @200K，NVE 3.78×$^c$，Outcome "Transient onset"
3. Cross-environment 标题从 "(Cheetah Run)" 改为通用标题
4. 脚注 $^c$ 说明 019b 的 NVE 是 raw V/E ratio（peak 5.66 @52.5K），无同环境 baseline 做归一化

列数（8列）、`&` 对齐、`\\` 行尾均一致，无编译问题。

---
