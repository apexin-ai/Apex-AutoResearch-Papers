# prep next batch test eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_next-batch-test-eval_20260521T194550_result.json`
- **Structured JSON:** [`4f7cb831a166e1105b0a.json`](../../sessions/4f/4f7cb831a166e1105b0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总如下：

### 当前状态

**4 个 GPU 全部被 SFT test eval 占用**（4B/8B/14B/Llama，均约 20% 进度）。

### 1.7B SFT test eval

命令已就绪，所有路径已验证。GPU 0（4B eval）预计最先完成释放，届时直接提交：

```bash
CUDA_VISIBLE_DEVICES=0 python -m freige.eval.test_inference \
  --model_path /root/autodl-tmp/models/Qwen/Qwen3-1.7B \
  --sft_adapter /root/autodl-tmp/sft_output_qwen3_1_7b_bf16 \
  --data_path /root/autodl-tmp/data/re-docred-repo/data \
  --output_dir /root/autodl-tmp/eval_results/test_eval_1_7b_sft_s42 \
  --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42 --split test_revised
```

### 4B RSFT adapter 状态

**需重训**。原 checkpoint `/root/autodl-tmp/rsft_output/checkpoint-510` 已删除，`rsft_output_ced_s42/` 为空目录。无 `rsft_candidates*` 训练数据残留，需 generation→scoring→training 完整流程。其他 seed 的 4B RSFT adapter 存在（s43/s44）但不可替代 s42。

### 缺失 test eval 清单

| 缺失项 | 阻塞 | 优先级 |
|--------|------|--------|
| test_eval_1_7b_sft_s42 | GPU 占满 | P1 — 命令就绪 |
| test_eval_4b_rsft_s42 | adapter 丢失 | P2 — 需审批重训 |

---
