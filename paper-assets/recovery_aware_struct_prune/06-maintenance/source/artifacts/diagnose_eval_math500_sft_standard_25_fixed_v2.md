# 诊断报告: eval_math500_sft_standard_25_fixed_v2

## 结论：实验已成功完成，非真正失败

### EXIT_CODE=129 原因

EXIT_CODE=129 = SIGHUP (signal 1)。SSH 会话断开后，SIGHUP 传递给前台进程。

- **v2**：500/500 全部跑完，结果在 `13:50:13` 保存到 JSON，SIGHUP 发生在保存之后。数据完整，无需重跑。
- **v1**：在 101/500 (20%) 时被 SIGHUP 杀掉，未保存结果。这是真正的中断失败。

### 实验结果

| 指标 | 值 |
|------|-----|
| MATH-500 Accuracy | 0.1540 ± 0.0161 (77/500) |
| Natural EOS | 183/500 (36.6%) |
| Truncated | 317/500 (63.4%) |
| Avg response length | 1386.1 tokens |
| 运行时间 | ~8h37m (05:11 → 13:50) |
| 模型路径 | `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25` |
| 结果文件 | `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_25_fixed_v2.json` (154KB, 完整) |

### 是否需要重试

**不需要。** 结果已完整保存。EXIT_CODE=129 是误报——实验在收到 SIGHUP 前已正常结束。

### 潜在质量问题

63.4% 的回复被截断（truncated），可能压低了准确率。如果需要更准确的评估，考虑增大 `max_new_tokens`（当前生成平均 1386 tokens）。

### 防止未来 SIGHUP 中断的建议

启动长时间实验时使用 `nohup ... &` 或 `setsid`，避免 SSH 断开传递 SIGHUP：
```bash
nohup python eval_script.py > ~/runs/.../eval.log 2>&1 &
```
