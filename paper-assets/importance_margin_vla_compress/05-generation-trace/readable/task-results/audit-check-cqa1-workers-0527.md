# audit check cqa1 workers 0527

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_check_cqa1_workers_0527_20260527T021848_result.json`
- **Structured JSON:** [`943f9eed52c0461d06a1.json`](../../sessions/94/943f9eed52c0461d06a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1-33015 状态报告

### GPU 状态
| GPU | 显存使用 | 利用率 |
|-----|---------|--------|
| 0 | 0 MiB | 0% |
| 1 | 0 MiB | 0% |
| 2 | 0 MiB | 0% |
| 3 | 0 MiB | 0% |

**全部 4 GPU 空闲，无任何 Python 进程在运行。** Worker 的实验已全部完成/停止。

### 代码同步
项目目录存在，`eval_pi05_pruning_libero.py` 最后更新 May 26 05:43。代码已同步但不一定是最新版本（主仓库可能有更新的 commit）。

### 可用模型
- **OpenVLA**: `openvla-libero-object`, `openvla-libero-spatial`, `openvla-libero-goal`, `openvla-repo`
- **π0.5**: `pi05-libero-finetuned`, `pi05-libero-base`, `pi05_libero_finetuned`

### 最近完成的实验（π0.5 Long libero_10 seed42）

最新一批（今天）：
| 方法 | keep_ratio | SR | 完成时间 |
|------|-----------|-----|---------|
| l2norm | 0.85 | 77.8% | 09:56 |
| random | 0.70 | 62.4% | 08:59 |
| attention | 0.70 | 50.8% | 06:40 |
| attention | 0.85 | 51.6% | ~May 27 00:26 |

### π0.5 Long cliff curve (seed42) 已有数据点

| k | l2norm | random | attention |
|---|--------|--------|-----------|
| 0.30 | **缺** | ✅ | **缺** |
| 0.50 | ✅ | ✅ | ✅ |
| 0.70 | ✅ | ✅ | ✅ |
| 0.75 | ✅ | ✅ | ✅ |
| 0.85 | ✅ | ✅ | ✅ |
| 0.90 | ✅ | **缺** | ✅ |
| 0.93 | ✅ | ✅ | **缺** |
| 0.95 | ✅ | **缺** | ✅ |

### 缺失数据点（seed42, libero_10）
1. **l2norm k=0.30**
2. **random k=0.90**
3. **random k=0.95**
4. **attention k=0.30**
5. **attention k=0.93**

### 建议
5 个缺失数据点，4 个空闲 GPU，每个 eval 约 3-4 小时。可以立即启动 4 个并行 eval，然后再跑第 5 个。考虑到 C002 截止时间（明天 5/28 12:00 UTC），时间充裕。

---
