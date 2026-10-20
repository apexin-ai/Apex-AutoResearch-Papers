# fix armo compat restart

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_armo-compat-restart_20260516T094155_result.json`
- **Structured JSON:** [`5291a43cf2b1fe9177a5.json`](../../sessions/52/5291a43cf2b1fe9177a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总：**

1. **Patch 文件**: `/root/autodl-tmp/models/RLHFlow/ArmoRM-Llama3-8B-v0___1/modeling_custom.py`  
   - 将 `from transformers.models.llama.modeling_llama import LLAMA_INPUTS_DOCSTRING` 替换为 try/except，缺失时 fallback 为空字符串

2. **ArmoRM 加载验证**: 成功，类型 `LlamaForRewardModelWithGating`，num_labels=1

3. **Quick Probe PID**: `493974`

4. **启动日志确认正常**:
   - 数据集从本地缓存加载（2000 train + 200 eval prompts）
   - 已开始生成：`Generated 16/2000`
   - 运行条件：`single_reward × 3 generations, K=4`

---
