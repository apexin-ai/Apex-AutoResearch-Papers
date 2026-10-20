# code plan006 paraphrastic

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-paraphrastic_20260515T212334_result.json`
- **Structured JSON:** [`afcdef10f88a7ca1e062.json`](../../sessions/af/afcdef10f88a7ca1e062.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动。

**状态总结：**
- **脚本**: `autodl-5090:/root/gen-depth-fingerprint/paraphrastic_chains.py` — 3 阶段 all-in-one pipeline
- **运行**: PID 246021，`--phase all --device cuda:1`，日志 `/tmp/plan006_full.log`
- **Dry-run 验证通过**: repetition_penalty=1.3 解决了 base model 的重复退化问题，paraphrastic chains 在每个 depth 产生主题相关但语义漂移的文本（符合 attractor convergence 预期）
- **进度**: generate 阶段运行中（~995 seeds, 预计 ~80 min），之后自动进入 extract → evaluate
- **生成参数**: Pythia-2.8B, temp=0.7, top_p=0.9, repetition_penalty=1.3, max_new_tokens=200
- **对比数据**: 将与 `data/prompt_type_features.csv` 中的 continuation 数据自动对比

预计总运行时间 ~2 小时（generate ~80min + extract ~20min + evaluate <1min）。

---
