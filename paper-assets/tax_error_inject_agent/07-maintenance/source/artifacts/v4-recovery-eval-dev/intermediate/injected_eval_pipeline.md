Recovery Eval Pipeline (remote: autodl-5090:/root/autodl-tmp/tax_error_inject_agent/)

Files:
- eval/injected_eval.py (463 lines): Injected Recovery Evaluation script
  - 在 eval 时注入错误 action：在指定步骤替换模型的 action 为随机错误 action
  - 根据 --model_variant 插入训练格式匹配的 error tag (taxei→[Error Type: P1_StepOrderSwap], random→[Error occurred], vanilla→无标签)
  - 输出 JSON: per-task recovery 结果 + aggregate recovery_rate / by_operator / by_task_type
  - 内置 --compare_with 统计检验（McNemar + bootstrap CI）

- scripts/run_injected_eval.sh: 启动脚本
  - bash scripts/run_injected_eval.sh all — 并行跑 3 个模型 + 自动对比
  - 支持单独跑 taxei/random/vanilla/compare

Dry-run: PASS (vanilla checkpoint, 1 task, cuda:3, 注入错误后 13 步 RECOVERED)