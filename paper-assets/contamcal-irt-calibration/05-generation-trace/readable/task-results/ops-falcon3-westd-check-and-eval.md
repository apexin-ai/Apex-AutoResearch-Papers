# ops falcon3 westd check and eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_falcon3-westd-check-and-eval_20260522T073602_result.json`
- **Structured JSON:** [`c6b6889f42fe6409a50e.json`](../../sessions/c6/c6b6889f42fe6409a50e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练状态：4 个 Falcon3-7B-Base SFT 全部正在运行中，尚未完成。**

| Dosage | Steps | Total | Progress | ETA |
|--------|-------|-------|----------|------|
| d000 | 2438/3125 | 78% | ~34 min |
| d005 | 2443/3177 | 77% | ~39 min |
| d025 | 2505/3384 | 74% | ~44 min |
| d050 | 2123/3642 | 58% | ~1h32min |

训练指标正常（loss ~1.0, token accuracy ~0.76）。所有进程运行约 2h12min，速度 ~3 s/it。

预计完成时间：
- d000/d005/d025: 约 30-45 分钟后
- d050: 约 1.5 小时后

**无法现在启动 eval**——lora_adapter 目录为空是因为训练还没结束（只在最后保存）。需要等训练全部完成后再提交 eval 任务。

---
