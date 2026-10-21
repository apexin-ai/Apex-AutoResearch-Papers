# ssh westd olmo redistrib scripts

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-olmo-redistrib-scripts_20260519T113304_result.json`
- **Structured JSON:** [`9f5f929a040316c889ef.json`](../../sessions/9f/9f5f929a040316c889ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 OLMo-2 eval 脚本已保存到服务器。正在等待 GPU 空闲，2 分钟后第一次检查。

**当前状态汇总：**
- 脚本：`olmo2_eval_gpu{0,1,2}.sh` 已写入并 `chmod +x`
- GPU 0 → d000+d005，GPU 1 → d025+d050，GPU 2 → d100
- GPU 2 预计 ~19:47 CST 最先空闲
- GPU 3 的 phase2 脚本完成 Gemma-2 后会自动跑 OLMo-2（重复不影响，可交叉验证）

---
