# Create AI Job Search Agent
In this branch we will create an AI Job Search Agent using LangChain.
Using the LangChain framework, we will build a job search agent that can help users find relevant job listings based on their skills and preferences.
Tavily from search result in internet
## Doc branch

### Tools

- [LangChain](https://langchain.com/)
- [LangSmith Hub](https://smith.langchain.com/hub?organizationId=5c031c7d-225f-41cf-9def-21161772e1fa)
- [hub hwchase17/react](https://smith.langchain.com/hub/hwchase17/react?organizationId=5c031c7d-225f-41cf-9def-21161772e1fa)
- [LangChain Documentation](https://langchain.readthedocs.io/en/latest/)
- [Tools](https://python.langchain.com/docs/integrations/tools/)
- [Tavily Search](https://python.langchain.com/docs/integrations/tools/tavily_search/)
- [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html)

### Pydantic
Pydantic is a Python library for data validation and settings management using Python type hints. In LangChain, Pydantic is used to define structured data models for inputs and outputs, ensuring type safety and reliable data parsing. This integration allows you to create robust output parsers, validate responses from language models, and serialize/deserialize data efficiently within AI workflows.

- [Output Parser](https://python.langchain.com/docs/concepts/output_parsers/)
- [LangChain PydanticOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.pydantic.PydanticOutputParser.html)

## RunnableLambda
RunnableLambda is a LangChain class that allows you to create executable components from lambda functions (anonymous functions). It is used to encapsulate custom logic that can be integrated into processing chains, making it easy to compose and reuse functions within AI workflows.

- [LCEL](https://python.langchain.com/docs/concepts/lcel/)
- [RunnableLambda](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableLambda.html)
- [Runnable Interface](https://python.langchain.com/docs/concepts/runnables/)

