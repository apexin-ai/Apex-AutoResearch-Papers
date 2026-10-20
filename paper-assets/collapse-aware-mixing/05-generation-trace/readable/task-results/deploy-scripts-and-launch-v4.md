# deploy scripts and launch v4

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_scripts_and_launch_v4_20260512T135337_result.json`
- **Structured JSON:** [`c09d0fd37f7e2335075c.json`](../../sessions/c0/c09d0fd37f7e2335075c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。

---

### 汇报

| 项目 | 结果 |
|------|------|
| **env_init.sh** | ✓ 部署成功 |
| **preflight.sh** | ✓ 部署成功 |
| **launch_pilot_v4.sh** | ✓ 部署成功 |
| **mvp_pilot_v3 session** | ✓ 已清理 |
| **Pythia-1B 下载** | ✓ vocab=50254, params=1012M, safetensors=2.09GB |
| **stale locks** | ✓ 51 个已清理 |

**Pre-flight 各项检查：**
- Python 3.12.3 ✓
- GPU 可用 (1 GPU) ✓
- GPU 无占用进程 ✓
- OpenWebText 缓存: 8,013,769 docs ✓
- Pythia-1B 缓存: 完整 (config.json + model.safetensors 2.09GB + tokenizer) ✓
- /root/autodl-tmp 磁盘: 161GB free ✓
- / 磁盘: 24GB free ✓

**READY_FOR_LAUNCH**

---
