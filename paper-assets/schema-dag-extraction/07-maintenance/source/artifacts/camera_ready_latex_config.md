# Camera-Ready LaTeX Configuration Diff

## acl.sty Option Reference (from project's acl.sty L14-21)

| Option | finalcopy | anonymize | linenumbers | pagenumbers |
|--------|-----------|-----------|-------------|-------------|
| `review` (current) | false | **true** | **true** | **true** |
| `final` (camera-ready) | **true** | false | false | false |
| `preprint` | true | false | false | true |

## Required Change

```diff
- \usepackage[review]{acl}
+ \usepackage[final]{acl}
```

Location: `main.tex` line 3

## Effect of `[final]`

1. **Anonymization off**: `\author{}` block renders real names (no longer replaced by "Anonymous ACL submission")
2. **Line numbers off**: margin line numbers removed
3. **Page numbers off**: footer page numbers removed (ACL adds them during proceedings assembly)

## No Other .sty Modifications Needed

The `acl.sty` file should NOT be modified. The single `[review]` → `[final]` switch handles all formatting differences. Do not change margins, font sizes, or spacing.

## Copyright / ISBN (if applicable)

ACL proceedings may require adding copyright info via:
```latex
\aclfinalcopy  % if not handled by [final] option
\setlength\titlebox{5cm}  % adjust if title box height changes
```
Check the specific EMNLP 2026 camera-ready instructions for any additional requirements (e.g., `\aclanthologyid`, copyright footer).
