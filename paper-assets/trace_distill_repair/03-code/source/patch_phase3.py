"""Patch run_phase3_repair.py to add missing features:
1. count_tokens / truncate_trace functions
2. full_trace truncation at 16K tokens (was 8K)
3. LLM-as-judge (Layer 2) evaluation
4. token_efficiency column
5. original/truncated trace token counts
"""
import re
import sys

filepath = "/root/trace_distill_repair/run_phase3_repair.py"
with open(filepath, "r") as f:
    content = f.read()

changes = []

# 1. Add new CSV fields
old_csv = '''CSV_FIELDS = [
    "instance_id", "condition", "repair_success", "eval_method",
    "line_overlap", "tokens_input", "tokens_output",
    "full_trace_tokens", "num_structural_segments", "num_structural_keep",
    "num_line_keep", "generated_fix",
]'''
new_csv = '''CSV_FIELDS = [
    "instance_id", "condition", "repair_success", "eval_method",
    "line_overlap", "tokens_input", "tokens_output",
    "full_trace_tokens", "original_trace_tokens", "truncated_trace_tokens",
    "num_structural_segments", "num_structural_keep",
    "num_line_keep", "token_efficiency",
    "llm_judge_score", "llm_judge_reasoning", "generated_fix",
]'''
if old_csv in content:
    content = content.replace(old_csv, new_csv)
    changes.append("CSV_FIELDS updated")
else:
    print("ERROR: Could not find CSV_FIELDS block", file=sys.stderr)
    sys.exit(1)

# 2. Add count_tokens, truncate_trace after CSV_FIELDS block
new_funcs = '''


def count_tokens(text):
    return len(text.split())


def truncate_trace(trace_text, max_tokens=16000):
    tokens = trace_text.split()
    original_count = len(tokens)
    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]
    return ' '.join(tokens), original_count, len(tokens)
'''
content = content.replace(new_csv + "\n\n", new_csv + new_funcs + "\n")
changes.append("count_tokens + truncate_trace added")

# 3. Add 'import re' if not present
if "\nimport re\n" not in content:
    content = content.replace("\nimport time\n", "\nimport re\nimport time\n")
    changes.append("import re added")

# 4. Add LLM_JUDGE_PROMPT and llm_judge_evaluate before run_instance
judge_code = '''

LLM_JUDGE_PROMPT = """\\
Given the following bug fix evaluation:

## Ground truth fix:
```python
{ground_truth}
```

## Generated fix:
```python
{generated}
```

Rate the semantic correctness of the generated fix on a scale of 1-5.
1=completely wrong, 2=partially addresses the issue, 3=correct approach but implementation errors, 4=mostly correct with minor differences, 5=functionally identical to ground truth.
Output ONLY a JSON object: {{"score": N, "reasoning": "..."}}
"""


def llm_judge_evaluate(pipeline, generated_fix, fixed_code):
    if not generated_fix or not fixed_code:
        return 0, "empty input"
    prompt = LLM_JUDGE_PROMPT.format(
        ground_truth=fixed_code[:3000], generated=generated_fix[:3000],
    )
    try:
        client = pipeline._get_repair_client()
        response = client.chat.completions.create(
            model=pipeline.repair_model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            max_tokens=256,
        )
        raw = response.choices[0].message.content
        text = raw.strip() if raw else ""
        match = re.search(r'\\{[^}]+\\}', text)
        if match:
            data = json.loads(match.group())
            return int(data.get("score", 0)), data.get("reasoning", "")[:500]
        return 0, f"parse_error: {text[:200]}"
    except Exception as e:
        return 0, f"error: {str(e)[:200]}"

'''
old_run_instance = "\ndef run_instance("
if old_run_instance in content:
    content = content.replace(old_run_instance, judge_code + "\ndef run_instance(")
    changes.append("LLM_JUDGE_PROMPT + llm_judge_evaluate added")
else:
    print("ERROR: Could not find run_instance function", file=sys.stderr)
    sys.exit(1)

# 5. Change max_tokens=8000 to max_tokens=16000
old_ft = "full_trace_text, _ = pipeline._format_full_trace(events, max_tokens=8000)"
new_ft = "full_trace_text, trunc_info = pipeline._format_full_trace(events, max_tokens=16000)"
if old_ft in content:
    content = content.replace(old_ft, new_ft)
    changes.append("full_trace max_tokens 8000->16000")
else:
    print("ERROR: Could not find _format_full_trace call", file=sys.stderr)
    sys.exit(1)

# 6. Add truncation tracking after full_trace_tokens
old_ftt = "    full_trace_tokens = estimate_tokens(full_trace_text)"
new_ftt = """    original_trace_tokens = count_tokens(full_trace_text)
    full_trace_text, _, trunc_word_count = truncate_trace(full_trace_text, max_tokens=16000)
    full_trace_tokens = estimate_tokens(full_trace_text)
    truncated_trace_tokens = count_tokens(full_trace_text)"""
if old_ftt in content:
    content = content.replace(old_ftt, new_ftt)
    changes.append("truncation tracking added")
else:
    print("ERROR: Could not find full_trace_tokens line", file=sys.stderr)
    sys.exit(1)

# 7. Replace row dict with new fields + llm_judge call
old_row = '''        rows.append({
            "instance_id": instance_key,
            "condition": condition,
            "repair_success": eval_result.get("pass", False),
            "eval_method": eval_result.get("method", "none"),
            "line_overlap": round(eval_result.get("line_overlap", 0.0), 4),
            "tokens_input": tokens_in,
            "tokens_output": tokens_out,
            "full_trace_tokens": full_trace_tokens,
            "num_structural_segments": len(structural_scores),
            "num_structural_keep": len(structural_keep),
            "num_line_keep": len(line_keep),
            "generated_fix": generated_fix[:5000],
        })'''
new_row = '''        judge_score, judge_reasoning = llm_judge_evaluate(
            pipeline, generated_fix, fixed_code,
        ) if generated_fix else (0, "empty_response")
        quality_score = judge_score if judge_score > 0 else (
            5.0 if eval_result.get("pass") else eval_result.get("line_overlap", 0.0) * 5
        )
        token_eff = quality_score / max(tokens_in, 1)

        rows.append({
            "instance_id": instance_key,
            "condition": condition,
            "repair_success": eval_result.get("pass", False),
            "eval_method": eval_result.get("method", "none"),
            "line_overlap": round(eval_result.get("line_overlap", 0.0), 4),
            "tokens_input": tokens_in,
            "tokens_output": tokens_out,
            "full_trace_tokens": full_trace_tokens,
            "original_trace_tokens": original_trace_tokens,
            "truncated_trace_tokens": truncated_trace_tokens,
            "num_structural_segments": len(structural_scores),
            "num_structural_keep": len(structural_keep),
            "num_line_keep": len(line_keep),
            "token_efficiency": round(token_eff, 8),
            "llm_judge_score": judge_score,
            "llm_judge_reasoning": judge_reasoning[:500],
            "generated_fix": generated_fix[:5000],
        })'''
if old_row in content:
    content = content.replace(old_row, new_row)
    changes.append("row dict updated with new fields")
else:
    print("ERROR: Could not find rows.append block", file=sys.stderr)
    sys.exit(1)

# 8. Update log line
old_log = '''        logger.info("  %s/%s: success=%s method=%s tokens=%d+%d",
                     instance_key, condition, eval_result.get("pass"),
                     eval_result.get("method", "none"), tokens_in, tokens_out)'''
new_log = '''        logger.info("  %s/%s: success=%s method=%s tokens=%d+%d judge=%d",
                     instance_key, condition, eval_result.get("pass"),
                     eval_result.get("method", "none"), tokens_in, tokens_out, judge_score)'''
if old_log in content:
    content = content.replace(old_log, new_log)
    changes.append("log line updated")
else:
    print("WARNING: Could not find log line to update", file=sys.stderr)

# 9. Add token_efficiency to condition_summary
old_cs = '''        condition_summary[cond] = {
            "count": n,
            "success": successes,
            "success_rate": round(successes / n, 4) if n else 0,
            "avg_tokens_input": round(sum(r["tokens_input"] for r in rows) / n, 1),
            "avg_tokens_output": round(sum(r["tokens_output"] for r in rows) / n, 1),
        }'''
new_cs = '''        avg_te = sum(r.get("token_efficiency", 0) for r in rows) / n
        avg_judge = sum(r.get("llm_judge_score", 0) for r in rows) / n
        condition_summary[cond] = {
            "count": n,
            "success": successes,
            "success_rate": round(successes / n, 4) if n else 0,
            "avg_tokens_input": round(sum(r["tokens_input"] for r in rows) / n, 1),
            "avg_tokens_output": round(sum(r["tokens_output"] for r in rows) / n, 1),
            "avg_token_efficiency": round(avg_te, 8),
            "avg_llm_judge_score": round(avg_judge, 2),
        }'''
if old_cs in content:
    content = content.replace(old_cs, new_cs)
    changes.append("condition_summary updated")
else:
    print("WARNING: Could not find condition_summary block", file=sys.stderr)

# 10. Update print summary
old_pr = '''            print(f"  {cond:25s}: {cs['success']}/{cs['count']} "
                  f"({cs['success_rate']:.1%}) "
                  f"avg_tokens={cs['avg_tokens_input']:.0f}+{cs['avg_tokens_output']:.0f}")'''
new_pr = '''            print(f"  {cond:25s}: {cs['success']}/{cs['count']} "
                  f"({cs['success_rate']:.1%}) "
                  f"avg_tokens={cs['avg_tokens_input']:.0f}+{cs['avg_tokens_output']:.0f} "
                  f"eff={cs.get('avg_token_efficiency', 0):.6f} "
                  f"judge={cs.get('avg_llm_judge_score', 0):.1f}")'''
if old_pr in content:
    content = content.replace(old_pr, new_pr)
    changes.append("print summary updated")
else:
    print("WARNING: Could not find print summary block", file=sys.stderr)

with open(filepath, "w") as f:
    f.write(content)

print(f"Patch applied: {len(changes)} changes")
for c in changes:
    print(f"  - {c}")
