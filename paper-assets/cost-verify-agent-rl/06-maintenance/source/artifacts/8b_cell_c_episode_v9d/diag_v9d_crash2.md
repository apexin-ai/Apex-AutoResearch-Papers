# 诊断报告：8b_cell_c_episode_v9d 第二次崩溃

**时间**: 2026-05-20 05:11:34 ~ 05:12:55（运行 82 秒）  
**服务器**: westd-47453  
**退出码**: 1

## 崩溃原因

**SFT 基础模型被删除。**

Config 中 `model_path: /root/autodl-tmp/checkpoints/qwen3_8b_sft_v1/checkpoint-231`，但该路径已不存在（大概率在第一次崩溃后的磁盘清理中被删除）。

`huggingface_hub 0.36.2` 发现本地路径不存在后，尝试将其解析为 HF repo ID，因格式不符而抛出异常：

```
HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': 
'/root/autodl-tmp/checkpoints/qwen3_8b_sft_v1/checkpoint-231'. Use `repo_type` argument if needed.
```

即使 `resume_mode: auto` 会加载 step 5 checkpoint，代码初始化阶段仍需要 model_path 有效（用于加载 tokenizer/model config）。

## 磁盘状态

```
/dev/md0  250G  145G  106G  58%  /root/autodl-tmp
```

磁盘空间充足（106GB free），不再是瓶颈。

## Checkpoint 可用性

| 路径 | 状态 |
|------|------|
| `/root/autodl-tmp/checkpoints/8b-cell-c-v9/global_step_5/actor/` | 存在，92GB |
| `latest_checkpointed_iteration.txt` | 内容为 `5` |
| `/root/autodl-tmp/checkpoints/qwen3_8b_sft_v1/checkpoint-231` (SFT模型) | 已删除 |
| `/root/autodl-tmp/models/Qwen3-8B/` (base model) | 存在（5个 safetensors） |

## Config 修改状态

`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_8b_cell_c_v9.yaml` 中 ops worker 的修改已生效：
- `save_freq: 5` — 正确
- `max_actor_ckpt_to_keep: 2` — 正确
- `save_contents: ["model", "extra"]`（去掉 optimizer）— 正确
- `load_contents: ["model", "extra"]` — 正确

## 修复建议

**方案 A（推荐）：将 model_path 改为 base Qwen3-8B**

```yaml
model_path: /root/autodl-tmp/models/Qwen3-8B
```

配合 `resume_mode: auto`，训练会：
1. 从 base Qwen3-8B 加载 tokenizer + model config
2. 自动检测 `global_step_5` checkpoint 并从 step 5 恢复权重
3. 从 step 6 继续训练

前提：Qwen3-8B 与 SFT checkpoint-231 架构完全一致（同一 base model 的 SFT 微调），tokenizer/config 可互换。

**方案 B：从其他服务器恢复 SFT 模型**

如果 bjb1-17606 上仍有 `qwen3_8b_sft_v1/checkpoint-231`，可 rsync 回来。但耗时较长且需要约 16GB 磁盘。

**方案 C：直接指定 resume_from_path**

```yaml
resume_from_path: /root/autodl-tmp/checkpoints/8b-cell-c-v9/global_step_5/
```

仍需 model_path 有效，所以需搭配方案 A 一起用。

**推荐执行方案 A**：改 model_path 为 `/root/autodl-tmp/models/Qwen3-8B`，其余配置不变，重启训练。
