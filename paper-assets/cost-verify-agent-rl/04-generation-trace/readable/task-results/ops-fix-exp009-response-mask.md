# ops fix exp009 response mask

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_exp009_response_mask_20260514T034101_result.json`
- **Structured JSON:** [`767fa01be53892a73c77.json`](../../sessions/76/767fa01be53892a73c77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

### 结果

- **选择方案 A**：创建含 "qwen" 的软链接
- **原因**：`base.yaml` 默认 `enable_response_mask: True`，exp007 因路径含 "Qwen3" 自然通过断言。exp008 的 SFT checkpoint 底层就是 Qwen3-1.7B，应保持 response_mask 开启，只需路径包含关键词
- **修改内容**：
  1. 创建软链接 `/root/autodl-tmp/checkpoints/exp008_sft/qwen3-1.7b-sft-final` → `final`
  2. 更新 `_alfworld_exp008_sft_grpo.yaml` 的 `model_path` 指向新路径
- **验证**：软链接正常指向原目录，config.json 可通过新路径访问，配置文件已更新

训练未启动，等待 Main Agent 重新提交。

---
