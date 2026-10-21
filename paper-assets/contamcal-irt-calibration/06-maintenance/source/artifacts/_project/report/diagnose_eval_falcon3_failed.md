# 根因
AutoDL 服务器 westd-29999 未 `source /etc/network_turbo` 导致无外网访问，eval 在下载 MMLU/ARC 数据集时因 `[Errno 101] Network is unreachable` 失败。服务器无数据集本地缓存。

# 日志关键错误
三个 log 完全一致：
```
'[Errno 101] Network is unreachable' thrown while requesting HEAD https://huggingface.co/datasets/cais/mmlu/resolve/main/README.md
RuntimeError: Cannot send a request, as the client has been closed.
EXIT_CODE=1
```

# 修复方案
1. **预下载数据集**（已完成）：通过 `source /etc/network_turbo` + `HF_HUB_DISABLE_XET=1` + httpx SSL bypass + `verification_mode="no_checks"` 预下载 MMLU 和 ARC 数据集到 `/root/autodl-tmp/.hf_cache/`
   - 额外问题：MMLU 的 `auxiliary_train` parquet 文件通过代理下载时损坏（Parquet magic bytes not found），需 `verification_mode="no_checks"` 跳过分片校验
2. **重新提交 eval**（已由另一 session 完成）：三个 eval 已以 `_v2` 后缀重新提交
   - PID 627332 → GPU 0 → Falcon3-7B-Base_d000_s42 → eval_falcon3_d000_s42_v2.log
   - PID 627479 → GPU 1 → Falcon3-7B-Base_d005_s42 → eval_falcon3_d005_s42_v2.log
   - PID 627636 → GPU 2 → Falcon3-7B-Base_d025_s42 → eval_falcon3_d025_s42_v2.log
   - output-dir: `/root/autodl-tmp/exp001/eval_results/Falcon3-7B-Base_{d000,d005,d025}_s42_aligned/`
3. **当前状态**：三个 eval 全部正常运行中，MMLU 评估进度约 42%

# 附注
- evaluate.py 大小 37775 bytes，与 C009 参考版 37591 bytes 不一致（差 184 bytes），需确认是否为合法更新
- lora_alpha=32 ✓（符合 C006）
- 未来在 westd-29999 提交 eval 任务时，需确保命令中包含 `source /etc/network_turbo`
