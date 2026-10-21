# analysis advbench layer bias r1 8b

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_advbench_layer_bias_r1_8b_20260522T094258_result.json`
- **Structured JSON:** [`96c807128385c27aeba6.json`](../../sessions/96/96c807128385c27aeba6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验 `advbench_layer_bias_r1_8b` 完全失败。**

**核心事实**：520 条 AdvBench prompts 在 1.2 秒内全部报错，错误消息为空（`ERROR —`），0 条 trace 生成成功。Phase 2 因无数据崩溃。

**最可能原因**：服务器上安装的 **transformers 5.9.0** 与模型保存时的 **4.43.0** 存在 API 不兼容。每条 prompt 仅需 ~2ms 就失败，说明异常发生在推理之前（可能是 `apply_chat_template` 返回类型变更或 `model.generate` 参数验证）。`except Exception as e` 吞掉了详细堆栈，且 `str(e)` 为空。

**修复方向**：
1. 改错误处理为 `traceback.print_exc()` 获取完整堆栈
2. 用单条 prompt 最小复现
3. 可能需要降级 transformers 到 4.46.x

分析报告已写入 `artifacts/worker_output_advbench_layer_bias_r1_8b.md`。

---
