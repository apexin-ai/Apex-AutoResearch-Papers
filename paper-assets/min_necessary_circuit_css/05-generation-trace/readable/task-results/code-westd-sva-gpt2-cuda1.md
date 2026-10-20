# code westd sva gpt2 cuda1

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-sva-gpt2-cuda1_20260513T070226_result.json`
- **Structured JSON:** [`e2336cec1f118950448b.json`](../../sessions/e2/e2336cec1f118950448b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ACDC 32%（10351/32491），2:23 剩余。又是 ~6 分钟总时间。之后还有 Phase C（cross-tabulation，很快）和 Phase D（evaluation，~1-2 分钟）。

总预计：ACDC ~3-4 分钟 + Phase C+D ~2-3 分钟 = ~5-7 分钟完成。

实验状态正常，已注册到 registry。汇总如下：

---

**实验 mvp_sva_gpt2_k3_topk 已在 westd-pro6000 cuda:1 上运行**

| 项 | 状态 |
|---|---|
| PID | 15526 |
| GPU | cuda:1 (NVIDIA RTX PRO 6000 Blackwell) |
| Binarization | top-100（全部三方法统一，非 isinf）✓ |
| GPT-2 加载 | 本地 `/root/autodl-tmp/gpt2-small` (ModelScope 下载) ✓ |
| Phase A: EAP-IG | 完成，32491 edges ✓ |
| Phase B: edge_pruning | 完成，32491 edges ✓ |
| Phase B: ACDC | 运行中 ~32%，预计 ~3-4 分钟 |
| Phase C: cross-tabulation | 待运行 |
| Phase D: evaluation (zero+mean) | 待运行 |
| 日志 | `/root/min_necessary_circuit_css/logs/mvp_sva_gpt2_k3_topk.log` |
| 输出 | `/root/min_necessary_circuit_css/sva_results.json` |

**环境修复记录：**
- 安装 eap 2.0.0 (from `hannamw/EAP-IG` via zip download)
- 创建 transformer_lens 兼容 shim（`HookedTransformerKeyValueCache` → `TransformerLensKeyValueCache`）
- GPT-2 via ModelScope 下载到 `/root/autodl-tmp/.ms_cache/AI-ModelScope/gpt2`，symlink 到 `/root/autodl-tmp/gpt2-small`

预计全 pipeline 在 **~5-7 分钟**内完成。

---
