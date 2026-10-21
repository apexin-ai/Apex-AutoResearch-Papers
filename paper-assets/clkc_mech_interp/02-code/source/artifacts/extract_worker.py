import json
import os
import re

path = '/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-prod42-projects-clkc-mech-interp--claude-sessions-agent-442f8341/df92b9e9-024b-46bf-8336-dee09310bb02/tool-results/mcp-agent-ml-research-get_worker_status-1779784615189.txt'

size = os.path.getsize(path)
outdir = '/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts'

# Parse the outer JSON to get the inner result string
with open(path, 'r') as f:
    outer = json.load(f)

inner_str = outer.get('result', '')
inner = json.loads(inner_str)
data = inner.get('data', {})

# Extract metadata (non-conversation fields)
meta = {}
for k, v in data.items():
    if k == 'result':
        # This contains the raw conversation - extract just metadata about it
        if isinstance(v, dict):
            raw = v.get('raw', '')
            meta['result_raw_length'] = len(raw)
        elif isinstance(v, str):
            meta['result_length'] = len(v)
        else:
            meta[k] = str(v)[:200]
    elif isinstance(v, (str, int, float, bool, type(None))):
        meta[k] = v
    elif isinstance(v, dict) and len(str(v)) < 1000:
        meta[k] = v
    else:
        meta[k] = f"<{type(v).__name__} len={len(str(v))}>"

with open(f'{outdir}/worker_meta2.txt', 'w') as f:
    json.dump(meta, f, indent=2, ensure_ascii=False, default=str)

# Extract the raw conversation and find the last few assistant messages
raw_conv = data.get('result', {}).get('raw', '') if isinstance(data.get('result'), dict) else ''
if not raw_conv:
    raw_conv = str(data.get('result', ''))

# Find all assistant text messages (look for patterns like "type":"text","text":"...")
# The raw is NDJSON - each line is a JSON object
lines = raw_conv.split('\n')

with open(f'{outdir}/worker_conv_info.txt', 'w') as f:
    f.write(f"Total lines in raw conversation: {len(lines)}\n")
    f.write(f"Total raw length: {len(raw_conv)} chars\n\n")

    # Get last 20 lines
    f.write("=== LAST 20 LINES ===\n\n")
    for line in lines[-20:]:
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
            msg_type = obj.get('type', '?')
            if msg_type == 'assistant':
                msg = obj.get('message', {})
                content = msg.get('content', [])
                texts = []
                for c in content:
                    if isinstance(c, dict):
                        if c.get('type') == 'text':
                            texts.append(c.get('text', '')[:500])
                        elif c.get('type') == 'tool_use':
                            texts.append(f"[TOOL: {c.get('name', '?')}]")
                f.write(f"ASSISTANT: {' | '.join(texts)}\n\n")
            elif msg_type == 'user':
                msg = obj.get('message', {})
                content = msg.get('content', [])
                if isinstance(content, list):
                    for c in content:
                        if isinstance(c, dict) and c.get('type') == 'tool_result':
                            result_content = str(c.get('content', ''))[:300]
                            f.write(f"TOOL_RESULT: {result_content}\n\n")
                elif isinstance(content, str):
                    f.write(f"USER: {content[:300]}\n\n")
            elif msg_type == 'system':
                f.write(f"SYSTEM: subtype={obj.get('subtype', '?')}\n\n")
            else:
                f.write(f"TYPE={msg_type}\n\n")
        except json.JSONDecodeError:
            f.write(f"[unparseable line, len={len(line)}]\n\n")

    # Find ALL assistant text messages (not tool calls) - get the last 10
    f.write("\n=== LAST ASSISTANT TEXT MESSAGES (searching all 1110 lines) ===\n\n")
    assistant_texts = []
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
            if obj.get('type') == 'assistant':
                content = obj.get('message', {}).get('content', [])
                for c in content:
                    if isinstance(c, dict) and c.get('type') == 'text':
                        text = c.get('text', '')
                        if len(text.strip()) > 20:  # Skip tiny fragments
                            assistant_texts.append((i, text))
        except:
            pass

    # Write last 10 substantial assistant text messages
    for line_num, text in assistant_texts[-10:]:
        f.write(f"--- Line {line_num} ---\n{text[:2000]}\n\n")

    # Find the initial task/prompt - check first 50 lines for user or human messages
    f.write("\n=== INITIAL TASK (first user/human message) ===\n\n")
    found_task = False
    for line in lines[:50]:
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
            otype = obj.get('type', '')
            if otype in ('user', 'human'):
                content = obj.get('message', {}).get('content', '')
                if isinstance(content, str) and len(content.strip()) > 10:
                    f.write(f"[type={otype}] {content[:3000]}\n")
                    found_task = True
                    break
                elif isinstance(content, list):
                    for c in content:
                        if isinstance(c, dict) and c.get('type') == 'text' and len(c.get('text','').strip()) > 10:
                            f.write(f"[type={otype}] {c['text'][:3000]}\n")
                            found_task = True
                            break
                    if found_task:
                        break
        except:
            pass
    if not found_task:
        # Check first assistant text messages for task context
        f.write("(no text user message found, checking first assistant texts and first user content)\n")
        for line in lines[:50]:
            try:
                obj = json.loads(line)
                if obj.get('type') == 'assistant':
                    content = obj.get('message', {}).get('content', [])
                    for c in content:
                        if isinstance(c, dict) and c.get('type') == 'text':
                            text = c.get('text', '')
                            if len(text.strip()) > 5:
                                f.write(f"  FIRST ASSISTANT TEXT: {text[:2000]}\n")
                                found_task = True
                                break
                    if found_task:
                        break
                elif obj.get('type') == 'user':
                    content = obj.get('message', {}).get('content', '')
                    f.write(f"  USER content type: {type(content).__name__}\n")
                    if isinstance(content, list):
                        for c in content:
                            if isinstance(c, dict):
                                f.write(f"    item type={c.get('type','?')}, keys={list(c.keys())[:5]}\n")
                                if c.get('type') == 'tool_result':
                                    f.write(f"    tool_result content: {str(c.get('content',''))[:500]}\n")
            except:
                pass

    # Find any "result" or "output" or artifact references
    f.write("\n\n=== ARTIFACT/OUTPUT REFERENCES ===\n\n")
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
            if obj.get('type') == 'assistant':
                content = obj.get('message', {}).get('content', [])
                for c in content:
                    if isinstance(c, dict) and c.get('type') == 'tool_use':
                        name = c.get('name', '')
                        if name in ('Write', 'mcp__agent-ml-research__save_project_file', 'mcp__agent-ml-research__register_artifact'):
                            inp = c.get('input', {})
                            f.write(f"Line {i}: {name} -> {json.dumps(inp, ensure_ascii=False)[:500]}\n\n")
        except:
            pass

    # Look for the "failed" reason - check system messages and last lines
    f.write("\n=== SYSTEM/ERROR MESSAGES ===\n\n")
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
            if obj.get('type') == 'system' and obj.get('subtype') not in ('init', 'task_progress'):
                f.write(f"Line {i}: system/{obj.get('subtype', '?')}: {json.dumps(obj, ensure_ascii=False)[:500]}\n\n")
        except:
            pass
