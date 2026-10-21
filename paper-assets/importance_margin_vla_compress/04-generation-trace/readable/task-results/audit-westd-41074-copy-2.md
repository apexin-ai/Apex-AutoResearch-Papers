# audit westd 41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd-41074_20260523T110758_result.json`
- **Structured JSON:** [`ad4ebd346149cc7a773a.json`](../../sessions/ad/ad4ebd346149cc7a773a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇报 — westd-41074

### GPU 状态：4/4 占用，均在运行 π0.5 Long seed43 实验

| GPU | 实验 | 进度 | 当前总 SR | 预计剩余 |
|-----|------|------|----------|---------|
| 0 | Random k=0.3 (v5) | T7 ep10/50 | 34.3% (120/350) | ~30min |
| 1 | L2norm k=0.7 (v4) | T8 ep30/50 | 69.8% (279/400) | ~15min |
| 2 | Random k=0.85 (v3) | T7 ep20/50 | 42.6% (149/350) | ~30min |
| 3 | L2norm k=0.85 (v4) | T8 done, 进入T9 | 75.1% (338/450) | ~10min |

### 已完成的 Long (libero_10) seed43 结果

| 方法 | keep_ratio | SR | 文件 |
|------|-----------|-----|------|
| Random | 0.50 | **51.2%** | `pi05_random_k0.50_libero_10_seed43.json` |
| Random | 0.85 | **41.8%** | `pi05_random_k0.85_libero_10_seed43.json` |
| L2norm | 0.30 | **35.2%** | `pi05_l2norm_k0.30_libero_10_seed43.json` |

### 已完成的 Long (libero_10) seed42 结果（供对比）

| 方法 | keep_ratio | SR |
|------|-----------|-----|
| Random | 0.50 | 52.6% |
| Random | 0.70 | 64.6% |
| Random | 0.85 | 44.4% |
| L2norm | 0.90 | 81.0% |

### 注意
- 之前的 v2/v3 版本因 `Network is unreachable`（tokenizer 下载失败）崩溃，当前 v4/v5 已修复并正常运行
- Random k=0.85 已有一个早期结果（41.8%），当前在重跑
- 空闲 GPU：**0 个**，全部占满，预计 10-30 分钟内陆续完成

---
