# ops fix westd21461 and resubmit

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_westd21461_and_resubmit_20260516T052856_result.json`
- **Structured JSON:** [`f1b388728c23b19b6a43.json`](../../sessions/f1/f1b388728c23b19b6a43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 修复结果

**1. xgrammar 版本差异**
| 服务器 | xgrammar 版本 |
|--------|--------------|
| westd-16980（正常） | 0.1.33 |
| westd-21461（崩溃） | 0.2.0 → 已降级到 0.1.33 |

**2. 修复方案**: 方案 A — 在 westd-21461 上 `pip install xgrammar==0.1.33`，验证 `accept_token` 调用正常。

**3. 两个实验重提交状态**

| 实验 | GPU | PID | 显存 | GPU利用率 | 状态 |
|------|-----|-----|------|----------|------|
| w6_mistral_docred_unconstrained | GPU 0 | 7740 | 15282MiB | 90% | RUNNING，正在推理 |
| w6_mistral_scierc_constrained | GPU 1 | 7813 | 15352MiB | 85% | RUNNING，已通过 grammar compilation，正在推理 |

constrained 实验日志无 TypeError，确认 xgrammar 降级修复有效。

---
