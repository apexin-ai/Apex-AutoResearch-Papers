# diagnose exp 017 strategyqa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-017-strategyqa_20260517T034803_result.json`
- **Structured JSON:** [`8ca424cb9b39c5308ac5.json`](../../sessions/8c/8ca424cb9b39c5308ac5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**失败根因：外部调度器 SIGTERM，非实验本身问题。**

- 进程存活 <1 秒，处理 0 题，vLLM 从未启动
- 日志仅 "Terminated\nEXIT_CODE=143"，脚本第一个 echo 都没执行到
- 排除 OOM（SIGKILL=137，此处是 SIGTERM=143）、排除脚本 bug（未执行）、排除模型加载失败（未到那步）
- GPU 97GB 空闲，模型文件完整，端口无占用
- 前序实验 exp-010-mistral 在 11:27 异常结束（连接重试），exp-017 在 11:46 被 launcher 启动后立即 kill

**可直接重跑**，脚本逻辑无误，资源充足。问题出在 job launcher 的调度逻辑（可能误判前序实验仍在运行或存在 cooldown 冲突）。

---
