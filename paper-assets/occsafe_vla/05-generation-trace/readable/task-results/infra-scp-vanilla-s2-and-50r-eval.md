# infra scp vanilla s2 and 50r eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_scp-vanilla-s2-and-50r-eval_20260521T110150_result.json`
- **Structured JSON:** [`a51ca36371ac1162d85f.json`](../../sessions/a5/a51ca36371ac1162d85f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**SCP 失败。**

错误：`ssh: connect to host connect.westd.seetacloud.com port 18685: Connection refused`

原因：AutoDL 实例之间无法直接通过公网 SSH 端口互联（端口被封或网络策略限制）。

**建议替代方案：**
1. **通过本地中转**：从 westd-10894 下载到本地，再上传到 westd-34685（慢，15GB 两次传输）
2. **AutoDL 共享存储**：如果两台机器在同一区域，可通过 AutoDL 的数据盘共享/文件存储功能传输
3. **对象存储中转**：先上传到 OSS/COS 等对象存储，再从目标机下载（需配置 access key）
4. **rsync over SSH proxy**：通过你本地机器做 SSH 隧道中转两台 AutoDL 实例

---
