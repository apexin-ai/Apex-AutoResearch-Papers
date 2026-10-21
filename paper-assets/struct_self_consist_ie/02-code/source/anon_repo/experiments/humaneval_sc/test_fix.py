from run_humaneval_sc import *
import os

client = create_client()
problems = load_humaneval()
p = problems[0]
msgs = build_prompt(p)
raw = api_sample(client, msgs, n=1, temperature=1.0)[0]
print("=== RAW COMPLETION (first 500 chars) ===")
print(repr(raw[:500]))
print()
code = extract_code(raw, p["prompt"])
print("=== EXTRACTED CODE ===")
print(code)
print()
print("=== TEST ===")
result = execute_test(code, p["test"], p["entry_point"])
print("passed={}, error={}".format(result["passed"], result["error"]))
