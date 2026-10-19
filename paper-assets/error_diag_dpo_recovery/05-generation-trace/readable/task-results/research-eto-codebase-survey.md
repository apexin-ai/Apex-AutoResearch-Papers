# research eto codebase survey

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_eto-codebase-survey_20260512T101322_result.json`
- **Structured JSON:** [`0f5cd6f4dc1b6ce3252a.json`](../../sessions/0f/0f5cd6f4dc1b6ce3252a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册为 artifact。核心发现：

**Repo**: `Yifan-Song793/ETO`，基于 FastChat 修改，代码结构清晰：`eval_agent/` 负责环境交互和轨迹收集，`fastchat/train/` 负责 SFT/DPO 训练，`construct_preference.py` 构建 preference pairs。

**Qwen3-8B 适配**（~1-2 天）：
- FastChat 已有 `QwenChatAdapter` + ChatML 模板
- 主要改动：FSDP wrap class（`LlamaDecoderLayer` → `Qwen2DecoderLayer`）、`mask_labels()` 添加 ChatML 分支、tokenizer pad_token 修复、transformers 版本从 4.37 升级到 ≥4.44

**ETADN γ_e 注入**（~4-6 天）：
- DPO loss 中 `self.beta` 是全局标量（`dpo_trainer.py:770`），改为 per-sample `gamma` tensor 即可
- ALFWorld 6 个 task type 天然提供 error-type 粗分类，还需从轨迹分析具体 failure pattern（wrong object / wrong receptacle / missing step 等）
- 数据层需要在 preference json 中添加 `error_type` 字段

**关键风险**：transformers 大版本升级可能导致 FastChat 兼容性问题，建议考虑绕过 FastChat 服务层直接用 vLLM 做推理。

---
