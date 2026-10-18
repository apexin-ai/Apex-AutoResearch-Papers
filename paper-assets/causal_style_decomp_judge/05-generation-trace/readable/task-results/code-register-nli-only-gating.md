# code register nli only gating

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_register_nli_only_gating_20260521T002132_result.json`
- **Structured JSON:** [`3f837f81cd2a95816a2b.json`](../../sessions/3f/3f837f81cd2a95816a2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。结果：

**修改 diff:**
- Line 173: `if args.axis == "verbosity":` → `if args.axis in ("verbosity", "register"):`
- NLI-only gating（不检查 BERTScore）对 register axis 生效

**运行结果:**
- **Counterfactual pass rate: 19/20 (95.0%)** — 确认与预期一致
- NLI mean: 0.9404, BERTScore mean: 0.8458
- 使用了 NLI-only gating（passed 只看 NLI ≥ 0.9，不看 BERTScore）
- Double-rewrite pass rate: 15/20 (75.0%)

**注意事项:** 运行时需要设置以下环境变量避免卡住：
- `HF_HOME=/root/autodl-tmp/.hf_cache`
- `TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1`（避免 HF Hub 网络请求挂起）
- `LD_LIBRARY_PATH` 加入 `/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13/lib`（Blackwell GPU CUDA JIT 需要）
- NLI 模型使用本地路径 `--nli-model /root/autodl-tmp/models/nli-deberta-v3-large`

---
