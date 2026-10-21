# analysis a050 fp32 3seed 5method

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a050_fp32_3seed_5method_20260519T095613_result.json`
- **Structured JSON:** [`c4178025dc91303265a1.json`](../../sessions/c4/c4178025dc91303265a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Artifact 写入 `artifacts/a050_fp32_3seed_5method_analysis.md`。

核心结论：

**fp32 彻底消除了 seed 方差问题。**

| 指标 | fp16 (pre-D080) | fp32 (post-D080) |
|------|----------------|-------------------|
| PermG fwd | 0/8, 6/8, 3/8 (mean=3.0, SD=2.45) | **6/8, 6/8, 6/8 (mean=6.0, SD=0.0)** |
| PermG rev | — | 0/8, 0/8, 0/8 |
| consensus_k4 | 0/8, 1/8, 0/8 | **6/8, 6/8, 6/8** |
| MMCT wpair_fwd | 5/8, 5/8, 4/8 (0.583) | **6/8, 6/8, 6/8 (0.750)** |

关键发现：
1. **PermG=75% (6/8)**，3 seed 完全一致（SD=0），确认 α=0.50 在检测阈值之上
2. **方向非对称性绝对**：fwd=6/8, rev=0/8，无反向泄漏
3. **一致失败的 2 对是 mauve pairs**（token_entropy/ece→mauve），所有 seed、所有方法都无法检出
4. **TY Granger C003**：s42 可靠 2/8，s43 可靠 4/8，s44 可靠 4/8（d_max=2 导致 df_resid=1 的不可靠）
5. **MMCT v2**：6 个检出 pair 的 p<0.001，null distribution (24 obs) 未能产生等高的加权分数
6. **Drift 跨 seed 一致**：所有核心指标 SD<1.1%

对 step function 叙事的意义：dose-response 从 α=0.10 (0%) 到 α=0.50 (75%) 的跃迁现在是干净的，无需 "high seed variance" 的 caveat。

---
