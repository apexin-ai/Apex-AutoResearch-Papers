# ops fix gpt2m symlinks and resubmit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-gpt2m-symlinks-and-resubmit_20260515T120441_result.json`
- **Structured JSON:** [`cdde834a1de462a88e58.json`](../../sessions/cd/cdde834a1de462a88e58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载验证通过。符号链接实际上并未断裂——完整链路正常工作。

**结果：**

1. **方案**：无需修复，symlink 链路完好（`models/` → `snapshots/` → `blobs/`，blobs 为真实文件）
2. **模型路径**：`/root/autodl-tmp/models/gpt2-medium`
3. **验证**：params=354,823,168，vocab=50257，GPT-2-medium VERIFIED
4. 目录内容为指向 HF cache snapshot 的符号链接，snapshot 文件再指向 blobs 真实文件，全链路可达

---
