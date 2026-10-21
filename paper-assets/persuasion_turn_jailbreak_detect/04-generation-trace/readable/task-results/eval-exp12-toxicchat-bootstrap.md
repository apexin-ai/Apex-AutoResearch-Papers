# eval exp12 toxicchat bootstrap

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp12-toxicchat-bootstrap_20260518T233003_result.json`
- **Structured JSON:** [`93cfe4b933198df3e047.json`](../../sessions/93/93cfe4b933198df3e047.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存至 `results/exp12_toxicchat_bootstrap.json`。

**Bootstrap 95% CI（pooled, BCa）：**

| Variant | Pooled F1 | 95% CI | Seed mean ± std |
|---------|-----------|--------|-----------------|
| jb_mlm | 0.8373 | [0.8162, 0.8576] | 0.8371 ± 0.015 |
| wiki_mlm | 0.7969 | [0.7737, 0.8195] | 0.7913 ± 0.114 |
| binary | 0.7092 | [0.6832, 0.7352] | 0.7046 ± 0.088 |
| scrambled | 0.6174 | [0.5900, 0.6448] | 0.6160 ± 0.068 |
| 9class | 0.5962 | [0.5685, 0.6235] | 0.5956 ± 0.107 |
| topic | 0.4975 | [0.4693, 0.5252] | 0.4955 ± 0.051 |
| vanilla | 0.4147 | [0.3896, 0.4429] | 0.4127 ± 0.026 |

**Permutation Tests（全部 p < 0.001）：**

| Comparison | Diff | Pooled p | Sig |
|------------|------|----------|-----|
| jb_mlm vs 9class | +0.2411 | 0.0001 | *** |
| jb_mlm vs vanilla | +0.4226 | 0.0001 | *** |
| wiki_mlm vs 9class | +0.2007 | 0.0001 | *** |

三组对比均高度显著（p < 0.001）。jb_mlm 的 CI 最窄（seed std 仅 0.015），稳定性远优于 wiki_mlm（0.114）和 9class（0.107）。唯一值得注意的是 wiki_mlm vs 9class 在 seed 42 下差异不显著（p=0.057），但 Fisher combined 和 pooled 均显著。

---
