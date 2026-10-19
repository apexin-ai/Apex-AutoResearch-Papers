# infra mvp setup and verify

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mvp_setup_and_verify_20260521T144351_result.json`
- **Structured JSON:** [`8361b045582a584b7d28.json`](../../sessions/83/8361b045582a584b7d28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Qwen verify (base) 在 GPU 0 上运行正常 — 模型已加载，开始处理 3200 条训练数据（1595 unique questions）。

## 当前状态总结

| 步骤 | 状态 |
|------|------|
| 探测服务器 | 完成 |
| 代码同步 | 完成（verify_parametric_knowledge.py + run_mvp.sh） |
| Rename | 完成（3200/800/1600/400 行确认） |
| Llama verify | **已完成** — train: 1096 kept (34.2%), test: 272 kept (34.0%) |
| Qwen verify | **运行中** GPU 0 — 使用 Qwen3-8B **base** |

### 注意事项
**Qwen 用了 base 模型而非 Instruct**，原因：
- HF 主站网络不可达（Errno 101）
- Qwen3-8B-Instruct 是门控模型（需 HF token），服务器无 token
- hf-mirror.com 返回 401，ModelScope 未收录 Qwen3
- Qwen3-8B base 有 chat template，可用于 QA 验证

如果必须用 Instruct 版本，需要在服务器上配置 HF token（`huggingface-cli login`）并等网络恢复。

---
