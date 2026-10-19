# 诊断报告: factorial_h2_episodeadv_seed1 实验失败

## 错误信息

```
huggingface_hub.errors.HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4'. Use `repo_type` argument if needed.
```

完整调用链:
```
train.py:181 main() -> run_ppo(config)
train.py:212 run_ppo() -> ray.get(runner.run.remote(config))
ray worker -> huggingface_hub validate_repo_id()
```

## 根因分析

**模型 checkpoint 未同步到 westd-47453 服务器。**

配置文件 `_alfworld_factorial_h2_episode_adv.yaml` 指定:
```yaml
model_path: /root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4
```

该路径在 westd-47453 上是一个**断裂的符号链接**:
```
qwen3_exp021_ragen_sft_v4 -> /root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final  (目标不存在)
```

模型实际存在于 bjb1-17606 的 `/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final`（~3.4GB, model.safetensors + tokenizer 等）。

**报错机制**: `transformers.AutoModel.from_pretrained()` 检测 `os.path.isdir(path)` 时, 断裂符号链接返回 `False`, 代码回退到 HuggingFace Hub 解析, Hub 拒绝以 `/` 开头的路径作为 repo ID。

## 修复方案

**方案 A（推荐）**: 从 bjb1-17606 传输模型到 westd-47453

```bash
# 在 westd-47453 上执行
rm /root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4  # 删除断裂符号链接
mkdir -p /root/autodl-tmp/checkpoints/exp021_ragen_sft_v4
scp -r bjb1-17606:/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final /root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final
ln -s /root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final /root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4
```

或直接修改配置指向实际路径（跳过符号链接）:
```yaml
model_path: /root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final
```

**方案 B**: 如果两台服务器间无法直接 scp, 通过中间机器中转或用 HuggingFace Hub 上传后再下载。

## 其他发现

- 配置路径正确: `/root/autodl-tmp/cost-verify-agent-rl/RAGEN/config/_alfworld_factorial_h2_episode_adv.yaml`（注意是 `config/` 不是 `configs/`）
- westd-47453 上完全没有任何 model.safetensors 文件, 说明这台服务器从未完成过模型传输
- 这属于 pre-flight checklist (C002) 第4项"确认 checkpoint 路径存在"应拦截的问题
