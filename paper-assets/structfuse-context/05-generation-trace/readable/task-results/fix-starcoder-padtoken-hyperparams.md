# fix starcoder padtoken hyperparams

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_starcoder_padtoken_hyperparams_20260513T163817_result.json`
- **Structured JSON:** [`b4a2f98b10ab1fce8a38.json`](../../sessions/b4/b4a2f98b10ab1fce8a38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

复制完成，seed=42 的 embedding negatives 构建已开始，正在加载 StarCoder 模型。现在输出最终汇总。

---

## 执行结果

### Step 1: pad_token 修复
`/root/structfuse/scripts/build_m1_training_data.py` line 127-128，在 tokenizer 加载后添加：
```python
if self.tokenizer.pad_token is None:
    self.tokenizer.pad_token = self.tokenizer.eos_token
```
验证通过（import OK）。

### Step 2: Kill 残留进程
无残留 StarCoder 进程（PID 61960 已消失）。Qwen 训练在 cuda:0 正常运行。

### Step 3: 超参统一
`/root/structfuse/run_m2_full_starcoder.sh` 修改：

| 参数 | 修改前 | 修改后 |
|------|--------|--------|
| batch-size | 4 | **8** |
| num-negatives | 5 | **7** |
| num-epochs | 2 | **3** |
| temperature | 未设置 | **0.07** |
| hard-negative-ratio | 未设置 | **0.5** |
| early-stopping-patience | 3 | **删除**（train.py 默认 0 = 禁用） |

其余参数（lr=2e-5, eval_steps=500, max_seq_length=2048, use-lora, gradient-checkpointing）已与 Qwen 一致。warmup_ratio=0.1, lora_r=16, proj_dim=256, weight_decay 均为 train.py 默认值，两个脚本都未显式传入，行为一致。

### Step 4: 数据构建已启动
- tmux session: `sc_data_build`
- GPU: cuda:1 (`CUDA_VISIBLE_DEVICES=1`)
- 输出目录: `/root/autodl-tmp/structfuse/full_m2_starcoder_data/`
- 日志: `/root/runs/structfuse-context/sc_data_build.log`
- 状态: Qwen 数据复制完成，seed=42 embedding 构建进行中

---
