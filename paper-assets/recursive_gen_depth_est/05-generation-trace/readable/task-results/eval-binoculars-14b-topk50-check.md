# eval binoculars 14b topk50 check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_binoculars_14b_topk50_check_20260520T054700_result.json`
- **Structured JSON:** [`484a993d40076b7e9b01.json`](../../sessions/48/484a993d40076b7e9b01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**Binoculars 14B topk50 — 成功**

| Feature Set | 4-class Acc | d1-d3 Bal Acc |
|-------------|------------|---------------|
| merged (30-feat) | **51.49%** | **46.37%** |
| stat_only (19-feat) | 48.84% | 43.45% |
| bino_only (11-feat) | 37.74% | 34.02% |
| bino_single (1-feat) | 25.23% | 25.21% |

**方案A 基线对齐**: merged 51.49% vs main pipeline 47.93% = **+3.56 pp**

注意事项：
- 原始 ablation 脚本因相对路径问题失败（从错误目录运行），已从项目根目录重跑成功
- 原始 binoculars eval 日志末尾有 HF 下载报错，但 JSON 和 npz 已在之前成功生成
- Cron job `binoculars_14b_topk50` 不存在（可能已清理），无需删除
- Registry 已更新为 DONE/success，artifact 已注册

---
