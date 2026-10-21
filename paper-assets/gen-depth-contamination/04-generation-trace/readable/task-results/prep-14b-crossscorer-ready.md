# prep 14b crossscorer ready

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_14b_crossscorer_ready_20260518T042246_result.json`
- **Structured JSON:** [`44b4f4bb176e898742f4.json`](../../sessions/44/44b4f4bb176e898742f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 准备状态确认

**全部就绪：**

| 检查项 | 状态 |
|--------|------|
| 14B AWQ 模型 | 存在于 cqa1 (`/root/autodl-tmp/.hf_cache/Qwen2.5-14B-Instruct-AWQ/`) |
| `score_14b_confound.py` | 存在，scorer path 正确指向 AWQ 模型 |
| `exp_14b_scorer_confound.sh` | 存在，可执行，配置正确 |
| `fetch_14b_data.sh` | 已创建于 cqa1，配置 westd 地址 `connect.westd.seetacloud.com:42896` |
| cqa1 → westd SSH 连通性 | 已通（生成 ed25519 key 并添加到 westd authorized_keys） |
| westd 数据进度 | depth_0~3 已完成，depth_4/5 生成中 |

**执行计划**已写入 `artifacts/14b_scorer_contingency/execution_plan.md`。

exp_14b_c4 完成后，三步执行：`fetch_14b_data.sh` 拉数据 → `exp_14b_scorer_confound.sh` 启动 scoring → 对比 K* 结果。

---
