# ops gemini connectivity test

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gemini-connectivity-test_20260523T052408_result.json`
- **Structured JSON:** [`e8913255826cf5a7048c.json`](../../sessions/e8/e8913255826cf5a7048c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 环境 | 连通性 | HTTP Status |
|------|--------|-------------|
| cqa1-21977 | **不通（被墙）** | 000（连接超时） |
| 本地 | **连通** | 404 / 403（能建立连接） |

cqa1 服务器无法访问 Google Gemini API，两个端点均超时（exit code 28）。本地正常连通（返回 404/403 说明 TCP+TLS 握手成功，只是缺 API key 被拒）。

---
