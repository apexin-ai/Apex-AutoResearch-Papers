# 诊断报告: eval_grpo_standard_25 失败

## 根本原因

**Checkpoint config.json 中 `"use_cache": false`，导致 `model.generate()` 不使用 KV cache。**

路径: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25/config.json`

### 失败链条

1. GRPO 训练时设置 `use_cache: false`（训练时正常，不需要 KV cache）
2. 训练完成后 checkpoint 保留了该设置
3. `eval_gsm8k.py` 的 `gen_kwargs` 未显式覆盖 `use_cache=True`
4. `model.generate()` 继承 config 的 `use_cache=False`
5. 无 KV cache 下，每个 generation step 重算全序列 attention（O(n^2) 时间）
6. DeepSeek-R1 思维链模型 + `max_new_tokens=4096` → 单样本生成极慢（sample #2 耗时 195s）
7. 长序列 generation 累积 VRAM 占用，在 sample ~16 时 CUDA OOM 崩溃（无 Python traceback，进程直接被 kill）

### 日志证据

```
05:19:52 模型加载成功
05:22:35 开始评估 1319 samples
进度: sample 1 = 4.61s, sample 2 = 195.77s (暴涨!)
sample 3-16: 逐步恢复到 2.88s/it
进程在 ~06:05 无任何错误信息终止
```

日志仅 13 行，无 traceback → CUDA 层面崩溃，Python 无法捕获。

### GPU 状态（当前）

- GPU 2 显示 59182 MiB 已用但无活跃进程 → 疑似 5 次崩溃留下的 zombie VRAM
- GPU 0/1 被其他实验占用（alpha ablation SFT）

## 可修复性

**配置问题，易修复。**

## 修复方案

**方案 A（推荐）: 修改 eval_gsm8k.py**

在 `gen_kwargs` 中加入 `use_cache=True`:

```python
gen_kwargs = dict(
    max_new_tokens=max_new_tokens,
    use_cache=True,  # 覆盖 config 中的 False
    pad_token_id=tokenizer.pad_token_id or tokenizer.eos_token_id,
    eos_token_id=[151643, 151645],
)
```

**方案 B: 修改 checkpoint config**

```bash
cd /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25
python -c "import json; c=json.load(open('config.json')); c['use_cache']=True; json.dump(c, open('config.json','w'), indent=2)"
```

**方案 A 更好**——在 eval 脚本层面统一处理，避免所有 GRPO checkpoint 都有此问题。

### 重跑前额外步骤

1. 清理 GPU 2 zombie VRAM: `nvidia-smi --gpu-reset -i 2`（或重启容器）
2. 确认用 `CUDA_VISIBLE_DEVICES=2` 或 `3` 运行（0/1 被占用）

---

## inference_speedup_plan016

日志文件 `/root/runs/recovery_aware_struct_prune/inference_speedup_plan016.log` **不存在**。`find` 也未找到任何匹配文件。该实验可能从未成功启动（脚本或路径配置错误），或日志路径与预期不同。无法进一步诊断。
