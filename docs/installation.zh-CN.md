# 安装说明

InvestFlow 既是一个源码仓库，也是一组兼容 Codex 的 skills。

## 克隆项目

```bash
git clone https://github.com/Zach0911/investflow.git
cd investflow
```

## 安装到 Codex

```bash
./scripts/install-codex-skills.sh
```

该脚本会把项目内置 skills 复制到：

```text
~/.codex/skills/
```

安装后，Codex 可以发现这些 skills：

- `using-investflow`
- `investment-briefing`
- `company-research`
- `thesis-builder`
- `valuation-check`
- `risk-review`
- `dialectic-investment-decision`
- `postmortem`

## 自定义安装目录

```bash
CODEX_SKILLS_DIR=/path/to/skills ./scripts/install-codex-skills.sh
```

## 修改源码后如何同步

安装脚本采用复制方式，不是软链接。

如果你修改了 `skills/` 下的源码，需要重新运行：

```bash
./scripts/install-codex-skills.sh
```

该脚本只更新 InvestFlow 自己的 skill 目录，不会删除 `~/.codex/skills/` 里的其他无关 skill。

## 验证项目

```bash
./scripts/validate.sh
```

## 使用 CLI

```bash
./scripts/investflow doctor
./scripts/investflow list skills
./scripts/investflow new thesis --output work/thesis.md
./scripts/investflow validate work/thesis.md
./scripts/investflow data list
./scripts/investflow render work/thesis.md --output work/thesis.html
./scripts/investflow pack list
```

CLI 是本地离线工具，不获取行情数据，也不生成投资建议。

## MCP Server

本地 MCP manifest：

```text
.mcp.json
```

指向：

```text
./scripts/investflow-mcp
```
