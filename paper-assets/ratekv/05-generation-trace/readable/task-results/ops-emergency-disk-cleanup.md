# ops emergency disk cleanup

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency_disk_cleanup_20260515T094759_result.json`
- **Structured JSON:** [`055132f30d2af1fe72e7.json`](../../sessions/05/055132f30d2af1fe72e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pythia-1.4B 下载已启动。汇报：

---

**磁盘清理完成**

1. **OPT 进程** — 已杀 3 个进程（PID 320683, 321236, 321241）
2. **释放空间** — 共释放 ~23GB（228G → 205G）
3. **清理项目**：
   - OPT-6.7B 下载文件及 hub 缓存
   - Falcon-7B（tiiuae 目录 + models 目录 + hub 缓存）— 4.2G
   - ms_deberta — 9.0G
   - cross-encoder/nli-deberta-v3-large — 7.6G
   - pip 缓存 — 1.2G
   - ModelScope 临时目录
4. **Qwen profiling** — 正常运行，209/384 heads，ETA ~73min
5. **当前磁盘** — 205/250GB 使用，**46GB 可用（82%）**
6. **Pythia-1.4B 下载** — 已启动（PID 321467），模型 ~3GB，预计 2-5 分钟完成

---
