# ops d030 check eval and prep p0

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d030-check-eval-and-prep-p0_20260514T192232_result.json`
- **Structured JSON:** [`bda5340fe53f9341aabd.json`](../../sessions/bd/bda5340fe53f9341aabd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进程状态

| GPU | 任务 | PID | 当前进度 | 预计完成 |
|-----|------|-----|---------|---------|
| cuda:0 | step-100 eval | 80799 | **53/62 (85%)** | ~12 min |
| cuda:1 | step-90 eval | 83217 | **37/62 (60%)** | ~30 min |
| cuda:2 | multi eval (ckpt-10 DONE → ckpt-20) | 85997 | **12/62 (19%)** on ckpt-20 | ~65 min (仅 ckpt-20) |
| cuda:3 | high eval [60,70,80,90] (ckpt-60) | 81962 | **50/62 (81%)** on ckpt-60 | ~15 min (ckpt-60)，后续还有 70/80/90 |

## 已完成结果（无新增）

SFT baseline: rel_f1=0.4057, evi_f1=0.7979, edcr=0.7118

| Step | rel_f1 | Δ vs SFT | evi_f1 | Δ vs SFT | edcr | precision | recall | pred_count | MVP-2? |
|------|--------|----------|--------|----------|------|-----------|--------|------------|--------|
| 10 | 0.0030 | **-0.403** | 0.7200 | -0.078 | 0.9983 | 0.0031 | 0.0028 | 10839 | FAIL |
| 50 | 0.1563 | **-0.249** | 0.5643 | -0.234 | 0.8858 | 0.2356 | 0.1169 | 6032 | FAIL |

step-90 和 step-100 的 inference 仍在跑，尚未产出 metrics.json。

## 空闲 GPU

**当前无空闲 GPU。** cuda:0 将在 **~12 分钟后** 最先释放（step-100 完成时）。cuda:1 约 30 分钟后释放。

## 注意

- multi eval (cuda:2) 的 batch 列表不含 header，但从日志看它已完成 ckpt-10 并在跑 ckpt-20，可能还有后续 checkpoints
- high eval (cuda:3) 队列中有 [60, 70, 80, 90]，ckpt-60 接近完成但之后还有 3 个，数小时才能全部跑完
- 两个 single eval (step-90, step-100) 才是最关键的——如果这两个 step 也 FAIL，说明 GRPO CED KL0.01 整体崩了

---
