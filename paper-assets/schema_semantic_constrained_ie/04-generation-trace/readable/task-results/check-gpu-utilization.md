# check gpu utilization

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_utilization_20260521T114951_result.json`
- **Structured JSON:** [`a3c3bf7b2a77ebae336c.json`](../../sessions/a3/a3c3bf7b2a77ebae336c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入。核心发现：

**GPU 实际状态（与预期不符）：**

| GPU | 状态 | 说明 |
|-----|------|------|
| westd-21461 cuda:0 | **FREE** | 0 MiB |
| westd-21461 cuda:1 | BUSY (92%) | 70B DocRED **unconstrained**（非 s1） |
| westd-16980 cuda:0 | **FREE** | 0 MiB |
| westd-16980 cuda:1 | **FREE** | 0 MiB |

**关键发现：Registry 与实际不一致。** `r16_70b_docred_zs_s1` 标记为 RUNNING，但 PID 247853 实际在跑 `--mode unconstrained`。Constrained (s1) 还没开始。进度 750/998 docs (75%)，预计还需 ~2h。

**3 张空闲 GPU 建议调度：**

1. **P0 — 70B DocRED constrained (s1)** → westd-16980 cuda:0
   - 不用等 unconstrained 结束，直接在 16980 加载 70B 模型并行跑
   - 预计 ~9h

2. **P0 — GoLLIE SciERC 551-doc head-to-head** → westd-16980 cuda:1
   - 目前只有 100-doc pilot (d063)，需要全量测试集对比
   - 预计 1-3h

3. **P1/P2 — Triple validity 分析 或 70B LoRA SciERC** → westd-21461 cuda:0
   - Trie 已完成，70B LoRA 启动条件满足

**立即需要的操作：**
- 修正 registry 中 `r16_70b_docred_zs_s1` 的描述（实际是 unconstrained）
- 将 70B constrained 和 GoLLIE 分别 dispatch 到 westd-16980 两张卡

---
