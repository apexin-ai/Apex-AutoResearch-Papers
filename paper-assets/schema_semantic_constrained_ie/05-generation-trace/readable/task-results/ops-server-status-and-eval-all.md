# ops server status and eval all

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server_status_and_eval_all_20260514T010339_result.json`
- **Structured JSON:** [`79fea08cb879e72199f2.json`](../../sessions/79/79fea08cb879e72199f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全面状态如下：

## 服务器状态汇总

### GPU 使用
| GPU | 显存占用 | 利用率 | 运行实验 |
|-----|---------|--------|---------|
| 0 | 40.8/97.9 GB | 93% | docred_schema (PID 137719) + semantic_only_v2 (PID 140804) |
| 1 | 16.5/97.9 GB | 85% | full_s1_v2 (PID 142639) |

### 实验进度

| 实验 | PID | 行数 | 预期 | 进度 | 状态 |
|------|-----|------|------|------|------|
| docred_schema (resume) | 137719 | 936 | 998 | **94%** | 运行中，从880恢复，还剩62 |
| semantic_only_v2 | 140804 | 148 | 551 | **27%** | 运行中 |
| full_s1_v2 | 142639 | 244 | 551 | **44%** | 运行中 |
| **full_s2** | **无** | 88 | 551 | 16% | **已崩溃** — exit code 130 (SIGINT) @ 00:48 UTC |
| semantic_only (旧) | - | 10 | 551 | - | 废弃（被 v2 替代） |
| full_s1 (旧) | - | 7 | 551 | - | 废弃（被 v2 替代） |

### 关键发现

1. **full_s2 被 SIGINT 杀死**（exit code 130），仅产出 88 行，需要重启（带 `--resume`）
2. **GPU 0 同时跑两个模型**（docred + semantic_only_v2），各自速度受影响
3. **docred_schema 最接近完成**（936/998），预计还需 ~30 分钟
4. **没有任何实验完成**，无法运行 violation_checker

### 速度估算
- full_s1_v2：log 显示每样本 ~4-8s，剩余 307 个，预计 ~30-40 分钟
- semantic_only_v2：剩余 403 个，GPU 0 被共享，预计 ~60+ 分钟
- docred_schema：剩余 62 个文档（batch_size=4），预计 ~20-30 分钟

### 建议操作
- **立即**：在 GPU 1 上重启 full_s2（docred 快完成后 GPU 0 会空出来，但 GPU 1 目前 full_s1_v2 在跑，只用了 16.5GB，96GB 显存足够再跑一个）
- **等待**：docred_schema 最快完成，可先评估

是否要重启 full_s2？

---
