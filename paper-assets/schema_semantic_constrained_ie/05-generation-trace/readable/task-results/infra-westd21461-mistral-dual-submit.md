# infra westd21461 mistral dual submit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd21461_mistral_dual_submit_20260516T051719_result.json`
- **Structured JSON:** [`75467d9b1e55fc2f9f46.json`](../../sessions/75/75467d9b1e55fc2f9f46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个 Mistral 实验已在 westd-21461 上提交并运行：

| 实验 | GPU | 数据集 | 模式 | 状态 |
|------|-----|--------|------|------|
| w6_mistral_scierc_constrained | cuda:0 | SciERC test (551) | full_s1 | RUNNING |
| w6_mistral_docred_unconstrained | cuda:1 | DocRED dev (998) | unconstrained | RUNNING |

环境：2× RTX PRO 6000 Blackwell (98GB), torch=2.8.0+cu128, transformers=5.8.1。模型通过 ModelScope 下载完成，符号链接到 `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3`。Registry 已更新为 RUNNING。

---
