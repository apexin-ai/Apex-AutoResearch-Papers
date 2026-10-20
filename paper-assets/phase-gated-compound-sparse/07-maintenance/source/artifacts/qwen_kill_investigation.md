# Qwen 实验 Kill 原因调查报告

**调查时间**: 2026-05-14 13:20 UTC
**服务器**: westd-22162

## 结论：被 v6_random 实验启动挤占，非 OOM

### Kill 原因分析

| 实验 | 进度 | 最后日志时间 | Kill 方式 |
|------|------|-------------|-----------|
| qwen_importance_s015 | 16/50 | 13:07:08 | 被终止 |
| qwen_importance_s020 | 16/50 | 13:07:15 | 被终止 |
| qwen_importance_s025 | 9/50 | 13:07:54 | 被终止 |
| qwen_importance_s030 | 9/50 | 13:08:02 | 被终止 |

**关键证据**：

1. **非 OOM**：`dmesg -T | grep oom` 输出为空，内核未触发 OOM killer
2. **非代码错误**：所有 4 个日志均在正常处理中戛然而止，无任何 error/traceback
3. **同时被杀**：4 个实验在 13:07-13:08 窗口内全部停止
4. **时间线吻合**：v6_random 的 tmux session 在同一时间创建：
   - v6_random_s020: 13:08:02（GPU 1）
   - v6_random_s015: 13:08:13（GPU 0）
   - v6_random_s025: 13:12:37（GPU 3）
   - v6_random_s030: 13:16:11（GPU 2）
5. **无 exit code 文件**：`/tmp/agent-ml-exit/` 中无 `qwen_importance_*.exit` 文件，说明进程被 SIGKILL（trap 未执行）或未通过 agent-ml 框架启动

**结论**：Qwen 实验被手动/程序化终止以释放 GPU 给 v6_random 实验。4 块 GPU 全部被 v6_random 占用。

### Qwen 模型状态

模型完整可用。

路径：`/root/autodl-tmp/models/Qwen2.5-7B-Instruct/`
- 4 个 safetensors 分片（共 ~15GB）
- config.json、tokenizer.json、generation_config.json 齐全
- Qwen 实验在被杀前成功加载模型并正常推理

### v6_random 进程状态（调查时刻）

4 个实验均健康运行中：

| 实验 | PID | GPU | 显存 | 进度 |
|------|-----|-----|------|------|
| v6_random_s015 | 72073 | GPU 0 | 23876 MiB | 18/50 |
| v6_random_s020 | 71488 | GPU 1 | 23876 MiB | 20/50 |
| v6_random_s025 | 73464 | GPU 3 | 21388 MiB | 13/50 |
| v6_random_s030 | 74588 | GPU 2 | 21388 MiB | 4/50 |

### 重跑建议

- **可以安全重跑**所有 4 个 Qwen 实验（模型完整、代码无问题）
- **前提**：等 v6_random 实验跑完释放 GPU 后再启动
- 每个 Qwen 实验需 1 块 GPU（~24GB 显存），处理速度约 40s-75s/问题
- 50 问题全跑完预估 ~35-60 分钟/实验
- 如 4 个并行跑需要 4 块 GPU
