# code westd validate and qwen ioi

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-validate-and-qwen-ioi_20260513T070211_result.json`
- **Structured JSON:** [`dd093f224daeda0608ef.json`](../../sessions/dd/dd093f224daeda0608ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

---

### Part 1: GPT-2 E2E 验证 — **PASS**
- 服务器：westd-pro6000, 2× RTX PRO 6000 (98GB), conda Python 3.12.3, PyTorch 2.10+cu128
- `eap` 库因 GitHub 不可达无法安装，实现了自定义 EAP-IG (gradient × activation_diff)
- GPT-2 从本地加载（需 monkey-patch AutoConfig 绕过 HF 离线限制）
- EAP-IG: 32,334 edges, 0.9s
- EP-L0: 449 active edges (50 epochs), 122.9s
- CSS pipeline 正常输出，`E2E VALIDATION OK`

### Part 2: Qwen-2.5 0.5B IOI K=3 — **完成 (negative result)**
- **PID**: 14601 (已完成)
- **总耗时**: 83.0s
- **TransformerLens 不支持 Qwen2.5**，全部用 HF-native 实现
- 三个方法均用 top-100 binarization

| 指标 | 值 |
|------|-----|
| Baseline IO-S diff | 7.0764 |
| EAP-IG edges | 179,388 (5.3s) |
| EP edges | 179,388 (70.7s) |
| IFR edges | 141,384 (1.3s) |
| CSS-core (3/3) | **0** |
| Off-diagonal | **100%** |
| EAP-IG vs EP Jaccard | 0.54 |
| EAP-IG vs IFR Jaccard | 0.00 |
| EP vs IFR Jaccard | 0.00 |

**关键发现**: IFR (proximity-based) 聚焦早期层 (m2→a3)，EAP-IG/EP (gradient-based) 聚焦深层 (a20.h9)。三方法在 Qwen2.5-0.5B 上发现完全不同的电路。所有 CPR ≈ 0 因为 top-100 对 361 组件模型太稀疏。

**建议后续**:
1. 尝试 top-500/1000 binarization
2. IFR 用 `unique_score_rank` 处理 tied scores
3. EP 改为 per-edge masking（当前为 per-node）
4. 增大 EP epochs 或调 lambda 以获得更好的 sparsity-task tradeoff

---
