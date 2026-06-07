# 平台适配清单

## Codex

- 支持状态：当前支持。
- 安装方式：`./scripts/investflow install codex`
- Skill 目录：`~/.codex/skills`

## MCP Client

- 支持状态：本地基础版。
- Manifest：`.mcp.json`
- Server：`scripts/investflow-mcp`
- 能力：列出数据源、读取只读数据、渲染报告。

## Generic Agent

- 支持状态：手动适配。
- 使用方式：读取 `skills/*/SKILL.md`、调用 CLI、遵守边界。

## 待确认能力

- Skill 自动发现：
- MCP stdio 支持：
- 本地文件读写权限：
- Markdown / HTML 报告输出：

## 不支持能力

- 不执行交易。
- 不连接券商账户。
- 不绕过平台安全策略。
- 不声明未验证的原生集成。
