# fix pruned model loading

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_pruned-model-loading_20260514T062825_result.json`
- **Structured JSON:** [`fb5d92a9912409c1016e.json`](../../sessions/fb/fb5d92a9912409c1016e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 修改摘要

| 文件 | 操作 | 内容 |
|------|------|------|
| `src/model_utils.py` | **新建** | `load_pruned_model()` — 检测 `per_layer_intermediate_size`，用 max size 初始化模型骨架，逐层替换 MLP 为正确维度的 `nn.Linear`，再 `load_state_dict(strict=True)` |
| `src/eval_gsm8k.py` | 修改 | `AutoModelForCausalLM.from_pretrained()` → `load_pruned_model()` |
| `src/train_grpo.py` | 修改 | 同上。GRPOTrainer 接受 model 对象，无需额外处理 |
| `src/correlation_analysis.py` | 修改 | 移除旧 `load_pruned_model`（依赖 base model + re-prune），替换为 model_utils 版本。pruned_model 和 recovered_model 两处调用均已更新 |
| `src/run_mvp_resume.sh` | **新建** | 从 Step 3.5 起续跑：post-prune eval → GRPO → post-recovery eval → correlation。`set -e` + 逐步 exit code 检查。cuda:0/cuda:1 并行 |

### Dry-run 结果

```
pruned_standard_35: OK, output shape=torch.Size([1, 4, 152064])  (98.4s)
pruned_rasp_35:     OK, output shape=torch.Size([1, 4, 152064])  (100.2s)
ALL PASSED
```

### 磁盘清理

- 杀死僵尸 wget 进程 (PID 148495)
- 删除 `/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B` 重复副本，释放 15G
- 数据盘: 91% → 83% (44G 可用)
- 根分区: 90% (3.2G 可用)，无可清理项
- tmux session `mvp_rasp_pipeline_v2` 已不存在

### **READY**

`src/run_mvp_resume.sh` 已就绪，待 Main Agent 通过 `submit_training_job` 启动。

---
