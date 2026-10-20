# deploy mvp pilot v4 full

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_mvp_pilot_v4_full_20260512T135600_result.json`
- **Structured JSON:** [`6031eb27a7e14289a8ea.json`](../../sessions/60/6031eb27a7e14289a8ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇报如下：

---

**Phase 1: 清理** — 成功。杀残留进程、清 lock/incomplete、删旧 cache。

**Phase 2: 文件部署** — 成功。5 个文件已部署：
| 文件 | 大小 |
|------|------|
| `/root/collapse-aware-mixing/env_init.sh` | 359B |
| `/root/collapse-aware-mixing/preflight.sh` | 1.6K |
| `/root/collapse-aware-mixing/launch_pilot_v4.sh` | 284B |
| `/root/collapse-aware-mixing/config.py` | 2.9K |
| `/root/collapse-aware-mixing/data_utils.py` | 4.6K |

config.py 修改确认：`tokens_per_generation=100M`, `checkpoint_interval_tokens=10M`, `real_dataset="wikitext"`, `real_dataset_config="wikitext-103-raw-v1"`

data_utils.py 修改确认：`load_dataset` 使用 `dataset_config` 参数，`split="train"`（不再按 doc 数截断）

**Phase 3: 数据下载** — 成功。
- wikitext-103-raw-v1: **1,801,350** train docs
- Pythia-1B: vocab **50,254**, 参数 **1,012M**

**Phase 4: Preflight** — **全部通过** (`Pre-flight PASSED`)
- Python 3.12.3
- GPU 可用
- GPU 无占用进程
- wikitext 缓存完整
- Pythia-1B 缓存完整（`local_files_only=True`，有一个 `torch_dtype` deprecation warning 可忽略）
- 磁盘空间充足

**Preflight 通过，请求提交 mvp_pilot_v4 训练任务。**

---
