# research check retrain s0 resume

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_check_retrain_s0_resume_20260525T123327_result.json`
- **Structured JSON:** [`a8574cbab9a77f41513a.json`](../../sessions/a8/a8574cbab9a77f41513a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**Fresh train (从头训练)**，是 clean v2 数据点。

### 证据

| 项目 | 内容 |
|------|------|
| **起始模型** | `Fine-tuning OpenVLA Model /root/autodl-tmp/models/openvla-7b` — 从 pretrained base 加载，非 checkpoint |
| **resume 关键词** | `grep -i "resume"` 全文零命中 |
| **起始 step** | `[AUX] step=0, occ_loss=0.0975, depth_loss=0.0000, action_loss=0.5508` |
| **结束 step** | `Max step 50005 reached!` — 完整跑完 50005 步 |
| **训练时长** | 14h12m44s（2026-05-23 11:48 → 05-24 02:01） |
| **checkpoint** | 在 step 50000 保存了 merged model |

### 代码版本：**v2**

- `[AUX]` 日志出现 501 次 — v2 特征
- 日志含 `occ_loss` + `depth_loss` 字段
- `occ_head` trainable params: 1,213,313

---
