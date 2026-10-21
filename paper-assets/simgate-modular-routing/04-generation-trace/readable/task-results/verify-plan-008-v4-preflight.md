# verify plan 008 v4 preflight

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_plan-008-v4-preflight_20260515T194340_result.json`
- **Structured JSON:** [`9ba8680d42058c95d3bc.json`](../../sessions/9b/9ba8680d42058c95d3bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here are the results:

```
=== PREFLIGHT RESULT ===
ga_restored:   PASS (当前值: max(1, 32 // args.batch_size) → batch_size=4 时 ga=8，.bak 文件与当前一致)
gpu_available: PASS (cuda:0 util: 0%, 0/32607 MiB; cuda:1 util: 0%, 0/32607 MiB — 双卡 RTX 5090 全空闲)
model_0.6b:    FOUND (path: /root/autodl-tmp/models/Qwen/Qwen3-0.6B, 1.5GB)
model_4b:      FOUND (path: /root/autodl-tmp/models/Qwen/Qwen3-4B, 7.6GB)
model_1.7b_ref:FOUND (path: /root/autodl-tmp/models/Qwen/Qwen3-1.7B)
data_ok:       PASS (lines: 2040, size: 1578366 bytes — md5 无法通过 read_only 验证，行数与文件大小均符合预期)
overall:       PASS
notes:
  - Qwen3-0.6B LoRA batch=4: ~3-4GB 显存，单卡 32GB 绰绰有余
  - Qwen3-4B LoRA batch=4: ~16-20GB 显存，单卡 32GB 可行；若 OOM 降至 batch=2 + ga=16
  - Qwen2.5 备选可用: 1.5B / 3B / 7B-Instruct
  - md5 校验被 ssh_read_only 安全策略阻止，如需严格校验需用 ssh_execute
```

---
