# 第三阶段 MCP 与只读数据连接器需求设计文档

## 1. 背景

InvestFlow 第二阶段已经具备 CLI 报告脚手架和结构校验能力。第三阶段需要让 Agent 可以读取结构化数据，但必须保持只读、安全、可审计，不进入交易、荐股或自动决策。

## 2. 目标

第三阶段目标是：

- 提供本地只读数据源目录。
- 提供 CLI 命令列出和读取数据源。
- 提供 MCP server，让兼容 MCP 的 Agent 可以调用 InvestFlow 的只读数据能力。
- 所有数据读取结果必须标注来源、时间和是否为示例数据。

## 3. 非目标

第三阶段不做：

- 不连接券商账户。
- 不执行交易。
- 不做实时行情聚合。
- 不输出买入 / 卖出建议。
- 不承诺数据准确、完整或实时。
- 不接入需要密钥的商业数据源。

## 4. 数据源设计

### 4.1 数据源注册表

文件：

```text
data/sources.json
```

字段：

- `id`：数据源 ID
- `name`：数据源名称
- `type`：`json` 或 `csv`
- `path`：相对项目根目录的文件路径
- `description`：用途说明
- `as_of`：数据时间
- `sample`：是否为示例数据
- `read_only`：必须为 `true`

### 4.2 示例数据

第一版内置示例数据：

- `sample-market-snapshot`：市场快照示例
- `sample-company-profile`：公司资料示例

示例数据只用于演示连接器能力，不代表真实市场信息。

## 5. CLI 命令

### 5.1 `investflow data list`

列出已注册只读数据源。

```bash
./scripts/investflow data list
./scripts/investflow --json data list
```

### 5.2 `investflow data show <source-id>`

展示数据源元数据。

```bash
./scripts/investflow data show sample-market-snapshot
./scripts/investflow --json data show sample-market-snapshot
```

### 5.3 `investflow data read <source-id>`

读取数据源内容。

```bash
./scripts/investflow data read sample-market-snapshot
./scripts/investflow --json data read sample-market-snapshot
```

规则：

- 只能读取 `data/sources.json` 注册过的数据源。
- 只能读取项目目录内的文件。
- 不允许写入数据。
- 输出必须包含 `source`、`as_of`、`sample`、`data`。

## 6. MCP Server

入口：

```text
scripts/investflow-mcp
```

Manifest：

```text
.mcp.json
```

第一版 MCP tools：

- `investflow_list_data_sources`
- `investflow_read_data_source`
- `investflow_render_report`

MCP server 只允许读本地注册数据源和渲染本地 Markdown 报告，不允许联网、交易或写入投资数据。

## 7. 验收标准

第三阶段 MVP 完成时，应满足：

- `data/sources.json` 存在且至少包含 2 个只读示例数据源。
- `investflow data list/show/read` 可用。
- JSON 输出稳定。
- 未注册数据源读取失败。
- 路径逃逸读取失败。
- `.mcp.json` 存在，并声明 `investflow` MCP server。
- `scripts/investflow-mcp` 可响应 `tools/list`。
- `scripts/investflow-mcp` 可调用 `investflow_list_data_sources`。
- `scripts/validate.sh` 覆盖第三阶段测试。
