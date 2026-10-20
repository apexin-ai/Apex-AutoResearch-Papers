# code arith cache rebuild

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_arith-cache-rebuild_20260513T104008_result.json`
- **Structured JSON:** [`77aeba2e1450d8bd53c1.json`](../../sessions/77/77aeba2e1450d8bd53c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交。任务 `arith_cache_rebuild` 在 westd-pro6000 cuda:1 上后台运行，tmux session `arith_cache_rebuild`。

生成流程：
- **Phase A**: EAP-IG → `cache_eap_ig_arith.json`
- **Phase B**: Edge Pruning → `cache_ep_arith.json`，ACDC → `cache_acdc_arith.json`
- Phase C/D 是分析和评估，会一并跑完

日志：`/root/min_necessary_circuit_css/arith_cache_rebuild.log`

预计耗时 15-30 分钟（ACDC 最慢）。缓存文件保存在 `/root/min_necessary_circuit_css/`，命名与 `run_bootstrap_ci.py` 一致。

---
