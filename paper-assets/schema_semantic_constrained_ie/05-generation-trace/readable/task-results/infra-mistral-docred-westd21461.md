# infra mistral docred westd21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mistral-docred-westd21461_20260516T051708_result.json`
- **Structured JSON:** [`f9dd5bdc21a42f6c56bd.json`](../../sessions/f9/f9dd5bdc21a42f6c56bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

双实验已提交并在运行，registry 已更新。

**总结：**

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| w6_mistral_docred_unconstrained | cuda:0 | 5571 | 运行中 |
| w6_mistral_docred_constrained | cuda:1 | 6789 | 运行中 |

**环境处理：**
- Mistral-7B-Instruct-v0.3 通过 ModelScope 下载到 ms_cache，符号链接到 `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3`
- 修复了 xgrammar 0.2.0 的 `accept_token` 类型兼容性 bug（`input_ids[i][-1]` → `.item()` 转 int），该 bug 导致 constrained 实验首次启动时崩溃
- 服务器: westd-21461, 2x NVIDIA RTX PRO 6000 Blackwell 98GB

---
