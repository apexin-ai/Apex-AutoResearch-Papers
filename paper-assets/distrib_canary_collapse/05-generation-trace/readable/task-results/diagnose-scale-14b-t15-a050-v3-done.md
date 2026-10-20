# diagnose scale 14b t15 a050 v3 done

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scale_14b_t15_a050_v3_done_20260523T023703_result.json`
- **Structured JSON:** [`b66d44fd6770bc1e6450.json`](../../sessions/b6/b66d44fd6770bc1e6450.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## 1. 实验状态：成功

- EXIT_CODE = 0，PID 680095 已结束
- gen_0 ~ gen_15 全部完整（16 generations）
- all_metrics.json 含 16 条完整记录
- 服务器：westd-17855

## 2. D102 结果（D105+D111 合规）

| 方法 | Forward sig | Reverse sig |
|------|------------|-------------|
| PermG (FDR) | **3/8** | 0/8 |
| Diff XCorr (FDR) | 8/8 | 8/8 |
| Threshold onset (3sigma) | 2/8 | — |
| TY Granger | 3/8 | — |
| **K≥3 consensus** | **2/8** | — |

K≥3 的 2 对：
- `ece→distinct_1`: **4/5** (naive, diff, threshold, perm)
- `token_entropy→distinct_1`: **3/5** (diff, threshold, ty)

## 3. 与 410M 对比

| 模型 | T=15 α=0.50 K≥3 |
|------|-----------------|
| Pythia-410M | **6/8** |
| Pythia-1.4B | **2/8** |

**检测 does NOT scale well**。1.4B 在 T=15 α=0.50 下 K≥3 从 6/8 降至 2/8，onset shift 在 T=15 同样存在。仅 `→distinct_1` 对保持 robust，其余 pair 均 ≤2/5。

## 4. Registry/Cron 更新

- Registry: `scale_14b_t15_a050_s42_fp32_v3` → DONE (success)，metrics 已写入
- Cron: 无活跃 cron job（已清空或从未设置）
- Artifact: 已注册 `art_20260523_c6639a`

---
