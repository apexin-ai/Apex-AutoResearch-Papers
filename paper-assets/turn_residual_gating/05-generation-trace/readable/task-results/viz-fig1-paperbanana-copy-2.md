# viz fig1 paperbanana

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig1_paperbanana_20260523T032854_result.json`
- **Structured JSON:** [`6067d3ca41929455c07f.json`](../../sessions/60/6067d3ca41929455c07f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**连通性问题：`generativelanguage.googleapis.com` 无法访问。**

即使启用了 AutoDL 的 `network_turbo` 代理，curl 仍然超时（exit code 28, HTTP 000）。Google Gemini API 在该服务器上被阻断，PaperBanana 依赖 Gemini API 无法运行。

可选方案：
1. **换一台有 Google API 访问权限的服务器**运行 PaperBanana
2. **在本地机器**（能访问 Google API）上运行 PaperBanana，再把生成的图传到服务器
3. **直接用 matplotlib 在服务器上画**——不依赖外部 API，按照同样的 intent 写 Python 代码生成 Figure 1

要怎么处理？

---
