# infra 70b gpu debug

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_70b-gpu-debug_20260517T101251_result.json`
- **Structured JSON:** [`f0015bf18dea7331ab02.json`](../../sessions/f0/f0015bf18dea7331ab02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：系统正常运行，无需修复。**

诊断结果：

1. **vLLM 正在运行** — 两个 GPU 都被 vLLM Worker 占用（各 32080MiB），模型已加载。`curl health` 不响应是因为使用的是 offline/LLM engine 模式（非 OpenAI API server 模式），直接通过 Python 调用。

2. **Episode collection 正在活跃执行** — 进程 `python src/episode_level_collection.py` 在 17:52 启动，正在处理 11 个 task types，日志显示持续的推理输出（input ~1000-2000 toks/s, output ~35-55 toks/s）。

3. **GPU 利用率显示 0%** — 这是 `nvidia-smi` 的采样问题。vLLM 的推理是突发式的（每次处理一个 prompt），在两次推理之间 GPU compute utilization 会短暂降为 0%。但显存占满（32089/32607 MiB）且进程活跃，说明在正常工作。

4. **输出目录** — `results/backbone_72b/` 已有 `chemistry-mix` 子目录，json 文件数为 0（可能正在写入第一批结果，或结果在子目录内）。

**状态：一切正常，无需干预。** Episode collection 正在跑，模型在持续推理。GPU "空闲" 是 nvidia-smi 瞬时采样的误报。

---
