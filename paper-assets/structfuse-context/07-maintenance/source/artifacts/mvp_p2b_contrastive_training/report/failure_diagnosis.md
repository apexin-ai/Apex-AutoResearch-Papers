# mvp_p2b_contrastive_training 失败诊断

## 错误摘要

Run 2/9 (p2b_random_s123) 在模型加载阶段失败，因模型权重分片文件 (.safetensors) 从预期路径消失。脚本使用 `set -e`，Run 2 失败后立即退出，Run 3-9 未执行。

## 完整错误信息

```
Traceback (most recent call last):
  File "/root/autodl-tmp/structfuse/training/train.py", line 446, in <module>
    train(parse_args())
  File "/root/autodl-tmp/structfuse/training/train.py", line 272, in train
    model = StructFuseEncoder(
  File "/root/autodl-tmp/structfuse/training/contrastive_model.py", line 69, in __init__
    self.backbone = AutoModel.from_pretrained(model_name, trust_remote_code=True, dtype=torch.float16)
  File ".../transformers/modeling_utils.py", line 484, in load_state_dict
    with safe_open(checkpoint_file, framework="pt") as f:
FileNotFoundError: No such file or directory: /root/structfuse/models/Qwen/Qwen2.5-Coder-3B/model-00001-of-00002.safetensors
```

## 根因分析

模型目录 `/root/structfuse/models/Qwen/Qwen2.5-Coder-3B/` 中的 safetensors 分片文件被移至 ModelScope 临时目录 `._____temp/`：

- **Run 1 (s42)** 于 20:58:50 启动时模型文件完整，加载成功并训完（21:15:28）
- 在 Run 1 运行期间（~21:05-21:06），一个并发的 ModelScope 下载触发了模型重新下载
- 下载流程将原始 safetensors 文件从主目录移除，开始下载新副本到 `._____temp/`
- **Run 2 (s123)** 于 21:15:33 启动时，safetensors 文件已不在主目录
- `._____temp/` 中的下载于 21:18 完成，但文件未被移回主目录（ModelScope finalize 步骤可能失败或被中断）

当前状态：
- `._____temp/model-00001-of-00002.safetensors` (682MB) 和 `model-00002-of-00002.safetensors` (487MB) 存在且完整
- 主目录仅有 config.json、tokenizer 等小文件，缺少 safetensors 分片
- GPU 4 已释放，磁盘空间充足 (31%)
- Run 1 的 checkpoint 已保存：`/root/autodl-tmp/structfuse/checkpoints/p2b_random_s42/final`

## 修复建议

1. **移动 safetensors 文件回主目录**：
   ```bash
   mv /root/structfuse/models/Qwen/Qwen2.5-Coder-3B/._____temp/*.safetensors /root/structfuse/models/Qwen/Qwen2.5-Coder-3B/
   rmdir /root/structfuse/models/Qwen/Qwen2.5-Coder-3B/._____temp/
   ```

2. **从 Run 2 开始重跑**：修改 `run_p2b_all.sh` 跳过已完成的 p2b_random_s42，或写一个只跑剩余 8 个 run 的脚本。

3. **防止复发**：将模型文件放到数据盘 `/root/autodl-tmp/` 上独立目录，不要与可能触发重新下载的 ModelScope cache 路径重叠。