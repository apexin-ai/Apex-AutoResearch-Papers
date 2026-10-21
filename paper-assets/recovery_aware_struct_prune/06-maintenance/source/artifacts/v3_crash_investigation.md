# eval_humaneval_sft_standard_20_2048_v3 进程调查报告

## 结论：正常完成

进程已正常退出，输出文件完整。reconcile_crons 报告 "Process gone, no sentinel, no W&B" 是因为未写 sentinel 文件，属于误报。

## 证据

| 检查项 | 结果 |
|--------|------|
| PID 86171 | 已不存在（正常退出） |
| 输出文件 | 存在，81505 bytes，写入时间 May 19 21:45 |
| JSON 完整性 | 完整，以 `}` 正确结尾 |
| task_id 数量 | 164（= n_total，全部完成） |
| 日志文件 | `/root/runs/.../eval_humaneval_sft_standard_20_2048_v3.log` 不存在（无 v3 后缀日志） |

## Metrics

| 指标 | 值 |
|------|-----|
| pass_at_1 | 0.1341 (13.41%) |
| stderr | 0.0266 |
| n_correct | 22 |
| n_total | 164 |
| avg_response_length | 1809.1 |
| median_response_length | 2048.0 |

## 根因

进程正常完成并写入结果 JSON，但 eval_humaneval.py 脚本没有写 sentinel 文件，导致 reconcile 系统无法识别为已完成状态。

## 备注

median_response_length = 2048（等于 max_new_tokens），说明大量样本触达了 token 上限被截断，这解释了较低的 pass_at_1（13.41%）。许多失败案例中模型在生成代码前输出了大段思考过程（chain-of-thought），耗尽了 token budget。
