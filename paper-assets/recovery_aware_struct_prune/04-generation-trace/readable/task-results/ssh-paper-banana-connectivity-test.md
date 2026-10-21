# ssh paper banana connectivity test

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_paper_banana_connectivity_test_20260523T124402_result.json`
- **Structured JSON:** [`2de582e78fade8062975.json`](../../sessions/2d/2de582e78fade8062975.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

| 项目 | 结果 |
|------|------|
| **API 连通性 — westd-32935** | **失败** — 连接超时 (HTTP 000, curl exit 28) |
| **API 连通性 — westb-23072** | **失败** — 连接超时 (HTTP 000, curl exit 28) |
| **PaperBanana 安装** | 未执行（API 不可达） |
| **图生成** | 未执行（API 不可达） |

**原因**：Gemini API (`generativelanguage.googleapis.com`) 在两台 AutoDL 服务器上均不可达，开启 `network_turbo` 代理后仍然超时。Google API 整体被墙，AutoDL 的代理仅加速 GitHub/HuggingFace，不覆盖 Google 服务。

**替代方案**（如需要）：
1. 在本地有梯子的机器上运行 PaperBanana
2. 用 matplotlib 手写概念图代码（不依赖外部 API），通过 `draw-paper-figure` skill 在服务器上执行

---
