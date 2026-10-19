# check wikitext2 fix status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_wikitext2_fix_status_20260517T111313_result.json`
- **Structured JSON:** [`69e67ba5f02652b34539.json`](../../sessions/69/69e67ba5f02652b34539.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

| # | 检查项 | 状态 | 详情 |
|---|--------|------|------|
| 1 | wikitext-2 本地数据 | ✅ | `test/` 和 `validation/` 均有 arrow 文件就位 |
| 2 | data_utils.py 修改 | ✅ | L95: 本地路径 `/root/autodl-tmp/data/wikitext2/test`，L100: fallback 到 HF 下载 |
| 3 | benchmark_eval.py 修改 | ⚠️ | wikitext2 逻辑完整（L149/238/308/380-386），但**无 OFFLINE/fallback/local 关键字**，依赖 data_utils.py 的本地优先逻辑 |
| 4 | GPU 状态 | 🔥 | GPU 0: 67G/98G, 100% util; GPU 1: 49G/98G, 100% util — 双卡满载 |
| 5 | 运行中进程 | ✅ 2个 | **PID 25429**: `kl_50pct_s123_global` eval (cuda:0, 19:02起) — MMLU 19% (11k/58k)&lt;br>**PID 29795**: `kl_30pct_s123` eval (cuda:1, 19:11起) — winogrande 40% (1874/4687)，wikitext2 PPL=8.9748 已完成 |
| 6 | Multi-seed checkpoints | 🟡 | **已有**: bce s123+s456, kl_norm_v2 s123+s456, kl_50pct s123, kl_30pct s123&lt;br>**缺失**: kl_50pct s456, kl_30pct s456 |
| 7 | Multi-seed 日志 | ❌→✅ | 旧日志 (`multiseed_kl50.log`, `multiseed_kl30_fixed.log`) 崩溃于 HF httpx `RuntimeError: Cannot send a request, client closed`&lt;br>**当前重跑**的 eval 已设 `HF_DATASETS_OFFLINE=1` + 本地缓存，正常推进中 |

**要点**：
- kl_50pct s123 和 kl_30pct s123 的 eval 正在运行，预计各还需 ~15-30 min
- s456 的 checkpoint 尚未训练（kl_50pct 和 kl_30pct 两个配置都缺）
- 旧的 multi-seed 脚本因 HF 网络问题挂了，当前的重跑用了 offline 模式绕过

---
