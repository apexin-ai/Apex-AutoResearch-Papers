# eval exp 033 qwen3 pw600 s2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp-033-qwen3-pw600-s2_20260518T155634_result.json`
- **Structured JSON:** [`70ec1b6ffa0133666745.json`](../../sessions/70/70ec1b6ffa0133666745.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-033 已启动并注册。

**状态汇总：**
- **环境**: vLLM 0.21.0 (已安装), Python 3.12 (`/root/miniconda3/bin/python`)
- **vLLM 服务**: 在 cuda:1 (RTX PRO 6000 Blackwell, 88GB/97GB used) 端口 8001 已启动
- **非思考模式**: 已验证 — `extra_body={"chat_template_kwargs": {"enable_thinking": False}}` 通过 `--no-thinking` 标志传入，响应无 `&lt;think>` 标签
- **tmux session**: `exp033`，正在处理 600 个 ProofWriter 问题 (1/600 已开始)
- **代码改动**: 给 `trace_generator.py`, `constraint_extractor.py`, `run_full_mvp.py` 添加了 `extra_body` 支持和 `--no-thinking` 标志
- **吞吐**: ~500 tokens/s generation, 12 并发请求
- **预计时间**: 600 问题 × 12 traces × (生成+提取), 非思考模式输出更短，估计 2-4 小时

---
