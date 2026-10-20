# eval roberta centered cka

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_roberta-centered-cka_20260518T113006_result.json`
- **Structured JSON:** [`833a440009e0910f57fc.json`](../../sessions/83/833a440009e0910f57fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。RoBERTa centered CKA 结果：

| Pair | Split | Centered | Uncentered | Delta |
|---|---|---|---|---|
| vanilla_vs_mlm | IID | **0.393** | 0.998 | -0.605 |
| vanilla_vs_mlm | DD OOD | **0.255** | 0.998 | -0.743 |
| vanilla_vs_9class | IID | **0.592** | 0.511 | +0.081 |
| vanilla_vs_9class | DD OOD | **0.735** | 0.624 | +0.111 |
| mlm_vs_9class | IID | **0.351** | 0.502 | -0.151 |
| mlm_vs_9class | DD OOD | **0.183** | 0.626 | -0.443 |

与 DeBERTa 一致：uncentered CKA 严重高估 vanilla vs MLM 的相似性（0.998 → centered 后降至 0.393/0.255）。RoBERTa 的 centered CKA 甚至比 DeBERTa（0.442）更低，说明 MLM 微调对 RoBERTa 的表示几何变化更大。

结果已保存至服务器 `results/roberta_centered_cka.json` 和本地 artifact（`art_20260518_5a2d2e`）。

---
