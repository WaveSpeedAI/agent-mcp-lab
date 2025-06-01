# MCP智能体生态：革新开发流程，一键激活多模态能力

> 赋能全球开发者，通过WavespeedAI MCP平台无缝集成并激活AI智能体的高级多模态交互能力。

## 什么是MCP智能体生态？

MCP智能体生态为开发者提供了一个统一的框架，用于连接、增强和部署具有强大多模态能力的AI智能体。通过利用WavespeedAI的MCP（多模态通信协议）服务器，开发者可以：

- **即时激活** 现有AI智能体的多模态能力
- **无缝集成** 实时视觉、语音和文本处理功能
- **加速开发** 使用标准化协议和预构建组件
- **全球扩展** 企业级基础设施支持

本仓库包含连接各种AI智能体到WavespeedAI MCP服务器生态系统的教程、示例和集成指南。

## MCP服务器：多模态能力

[WavespeedMCP服务器](https://github.com/WaveSpeedAI/mcp-server)是我们针对WaveSpeed AI服务的模型控制协议(MCP)服务器的官方实现。它通过MCP协议提供了一个标准化接口，用于访问先进的多模态能力。

### 主要特点

- **高级图像生成**：支持从文本提示创建高质量图像，包括图像到图像生成、图像修复和LoRA模型支持
- **动态视频生成**：将静态图像转换为具有可自定义运动参数的视频
- **优化性能**：增强的API轮询机制，具有智能重试逻辑和详细的进度跟踪
- **灵活的资源处理**：支持URL、Base64和本地文件输出模式
- **全面的错误处理**：专门的异常层次结构，用于精确识别和恢复错误

MCP服务器采用清晰、模块化的架构，包含服务器实现、API客户端优化、资源处理和错误管理等组件。它可以通过环境变量、命令行参数或配置文件轻松配置。

## 智能体列表
|名称|GitHub|简介|备注|集成指南|
|---|---|---|---|---|
|[Cursor](https://cursor.com) |[getcursor/cursor](https://github.com/getcursor/cursor)|AI代码编辑器 - 为程序员打造的强大AI编程助手|提供高级代码生成、编辑和解释功能，支持多种AI模型。具有深度代码库理解和项目级上下文感知能力||
|[Windsurf](https://windsurf.com) |[Windsurf](https://windsurf.com)|为开发者打造的新一代AI IDE，方便开发者保持工作流畅|配备Cascade智能聊天机器人，可与开发者强力协作，具有高级上下文感知和终端集成功能。支持MCP扩展智能体能力||
|[Trae](https://www.trae.ai) |[Trae-AI/Trae](https://github.com/Trae-AI/Trae)|字节跳动推出的免费AI IDE，支持原生中文，集成了Claude 3.7和GPT-4o等主流AI模型|提供Builder和Chat两种模式，支持智能代码生成与优化，原生中文支持|[Trae集成指南](./integrations/trae_integration.md)|
|[AIpy](https://www.aipy.app/) |[knownsec/aipyapp](https://github.com/knownsec/aipyapp)|人工智能驱动的Python和Python驱动的人工智能（Python-Use）- 一种新的AI智能体范式|为LLM提供完整的Python执行环境，允许其自由使用所有Python功能，无需预定义工具接口。支持任务模式和Python模式||