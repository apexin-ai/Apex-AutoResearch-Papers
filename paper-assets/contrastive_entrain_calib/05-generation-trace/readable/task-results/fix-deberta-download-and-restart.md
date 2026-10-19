# fix deberta download and restart

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_deberta_download_and_restart_20260518T152525_result.json`
- **Structured JSON:** [`99abddc81162a16fd4e0.json`](../../sessions/99/99abddc81162a16fd4e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**修复内容**：
1. **根因**：`microsoft/deberta-v3-base` 是 base 模型（2 labels），不是 NLI 模型（3 labels），R3 reward 计算时 `probs[:, 2]` 越界
2. **附加问题**：transformers 5.8.1 有 DeBERTa tokenizer 转换 bug → 降级到 4.57.6 + 安装 sentencepiece/tiktoken
3. **修复**：
   - 两台服务器 transformers 降级到 4.57.x
   - NLI 模型换为 `cross-encoder/nli-deberta-v3-base`（3 labels）
   - `dcgrpo_trainer.py` patch：`DebertaV2Tokenizer` 替代 `AutoTokenizer` + 动态查找 entailment label index
   - 两台服务器预缓存新 NLI 模型

**当前状态**：
- **exp-002** (cuda:0): RUNNING, step 1/8000 ✓, PID 63704, tmux `exp-002`
- **exp-003** (cuda:1): RUNNING, step 1/8000 ✓, PID 63563, tmux `exp-003`
- Registry 已更新

---
