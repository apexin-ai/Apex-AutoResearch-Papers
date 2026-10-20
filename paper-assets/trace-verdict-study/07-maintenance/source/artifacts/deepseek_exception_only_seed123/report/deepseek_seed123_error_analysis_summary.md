Remote path: /root/trace-verdict-study/docs/paper/deepseek_seed123_error_analysis.md

Key findings:
- 100 errors are ALL format collapse (model outputs garbage tokens: "assert"=54, "["=36), not semantic misclassification
- Root cause is input length, not exception type: <4000 chars = 0% error, 5000-6000 = 79.5%, 6000+ = 90.9%
- seed42 handles same 122 long samples at 100% accuracy
- TypeError/NameError high miss rate is spurious correlation (longer traces, not harder types)
- Errors concentrated in 15 problems generating verbose parameter representations (itertools objects, function addresses)
- Conclusion: LoRA initialization instability causes format-following collapse under long context, not semantic understanding deficit