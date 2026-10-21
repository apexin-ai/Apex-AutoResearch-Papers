# diagnose scale 14b t15 a060 v2 done

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scale_14b_t15_a060_v2_done_20260523T023449_result.json`
- **Structured JSON:** [`eb8ccc6ec6468ddecbb2.json`](../../sessions/eb/eb8ccc6ec6468ddecbb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

## 1. 实验状态：✓ 成功

- EXIT_CODE=0，gen_0 ~ gen_15 全部完成（16 代，含 base）
- 服务器：westd-17855，PID 679656 已退出
- 无 cron 需要清理

## 2. D102 分析结果

| 指标 | 值 |
|------|-----|
| **PermG fwd** | **6/8** |
| **PermG rev** | **0/8** |
| **K≥3 consensus** | **6/8** |
| K≥4 consensus | 3/8 |
| threshold_onset_3sigma | 6/8 |
| diff_xcorr_fdr_fwd | 7/8 |
| TY_granger | 1/8 |

强非对称性：forward 6/8 vs reverse 0/8。

## 3. 与 410M 对比

| 设置 | PermG fwd |
|------|-----------|
| 410M T=15 α=0.60 | **0/8** (sync-dip) |
| **1.4B T=15 α=0.60** | **6/8** (strong signal) |
| 1.4B T=10 α=0.60 (ref) | 4/8 |

**结论：Sync-dip 在 T=15 也不是 scale-invariant。** 1.4B 恢复了强因果信号（6/8），且比 T=10（4/8）更强——更长的时间序列在大模型上放大了 lead-lag 结构。

## 4. Registry/Artifact 更新

- Registry: `scale_14b_t15_a060_s42_fp32_v2` → DONE (success)，metrics 已写入
- Artifact: `D102_14b_t15_a060_s42_fp32_v2.json` 已注册
- Cron: 无活跃 cron

---
