# diagnose w41 full gpu check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w41_full_gpu_check_20260528T043624_result.json`
- **Structured JSON:** [`5c6a4bb41fa258e19e91.json`](../../sessions/5c/5c6a4bb41fa258e19e91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总：

## westd-41074 GPU 状态汇总

| GPU | 实验 | 状态 | SR% | per-task | 耗时 |
|-----|------|------|-----|----------|------|
| **cuda:0** | pi05_random_k09_long_s45 | **已完成** ✓ | **33.4%** | 28,38,36,54,8,40,12,32,0,86 | 180min |
| **cuda:1** | pi05_random_k05_long_s45 | **运行中** | — | 正在跑，43% GPU利用率，10.6GB显存 | 已跑2h06m |
| **cuda:2** | pi05_l2norm_k07_long_s45 | **已完成** ✓ | **61.6%** | 72,86,64,44,60,76,50,64,10,90 | 154min |
| **cuda:3** | pi05_attn_k075_long_s45 | **已完成** ✓ | **53.0%** | 68,74,66,34,42,52,72,30,10,82 | 161min |

**空闲原因**：cuda:0/2/3 的实验已正常完成（EXIT_CODE=0），不是挂起或崩溃。Director 报告的"空闲"就是实验跑完后 GPU 释放了。

**cuda:1** 是唯一还在跑的实验（random k=0.5），预计还需 ~1h 完成。

**3 张空闲卡可立即部署新实验。**

---
