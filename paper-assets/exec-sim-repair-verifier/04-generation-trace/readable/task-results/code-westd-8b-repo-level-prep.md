# code westd 8b repo level prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_westd-8b-repo-level-prep_20260512T170132_result.json`
- **Structured JSON:** [`ef86cc24057800419f9e.json`](../../sessions/ef/ef86cc24057800419f9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成报告

报告已写入 `artifacts/repo_8b_training_plan.md`。

### 核心结论

**脚本无需修改。** `train_repo_verifier.py` 和 `train_repo_cwm.py` 已支持 `--model_name` 参数，切 8B 只需改 CLI 参数：模型路径改 Qwen3-8B，batch_size 2→1，grad_accumulation 16→32，lr 2e-4→1e-4。LoRA 配置保持不变（函数级 8B 已验证）。

### BLOCKER

**westd-48478 SSH 认证失败。** account=root 连接返回 "Authentication failed"，detect_image 和 ssh_execute 均失败。无法完成环境探测和 dry-run。

需要：
1. 修复 westd-48478 SSH 认证（检查密钥/配置）
2. 确认 Qwen3-8B 模型是否在 westd-48478 上（seetacloud 已有缓存在 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`）
3. 同步代码和数据到 westd-48478

---
