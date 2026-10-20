# ops d158 post restart check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d158_post_restart_check_20260524T111703_result.json`
- **Structured JSON:** [`4f9fb7c14bf85b6636e5.json`](../../sessions/4f/4f9fb7c14bf85b6636e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程均存活，GPU 服务器未重启。

## 状态汇总

| 实验 | PID | 状态 | 进度 | GPU | 运行时间 |
|------|-----|------|------|-----|---------|
| d158_1_7b_rsft_s44_generate | 302254 | **存活** | 821/3027 (27%) | cuda:0, 7.2GB, 75% util | 2h25m |
| d158_14b_rsft_s44_generate | 306172 | **存活** | 193/3027 (6.4%) | cuda:2, 32.5GB, 93% util | 1h06m |

**输出文件行数：**
- 1.7B: 6568 行 (821 docs × 8 generations)
- 14B: 1544 行 (193 docs × 8 generations)

**质量指标（最近 100 docs 批次）：**
- 1.7B: format_ok 100%, truncation 22.4%, diversity 7.5/8
- 14B: format_ok 100%, truncation 8.4%, diversity 7.3/8

**预计剩余时间：**
- 1.7B: ~7-8h（~10s/doc 均速）
- 14B: ~15-16h（~20s/doc 均速）

**磁盘：** /root/autodl-tmp 102GB 可用 (72% used)

**注意：** 1.7B truncation_rate 22.4% 偏高，日志持续报 warning 建议 max_new_tokens=3072。14B 的 8.4% 在可接受范围。

---
