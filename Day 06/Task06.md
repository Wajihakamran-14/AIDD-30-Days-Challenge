# AI-Driven Development - 30-Day Challenge-Task-06

## 📌 Steps Task 6

### 🔹 Step 1 - Create GitHub Personal Access Token (PAT)
https://github.com/settings/personal-access-tokens/new 
### Generate a token with:    
- ✔ repo (Read & Write)    
- Copy the token and save it safely.

![Token](/Screenshots/token-generate.png)

### 🔹 Step 2 - Store Token Securely

store token in .env file inside .gemini folder as below

![Env](/Screenshots/env.png)

### 🔹 Step 3 - Configure Gemini to Use GitHub MCP Server

![settings.json](/Screenshots/Json-file.png)

### 🔹 Step 4 - Restart Gemini CLI

![gemini restart](/Screenshots/MCP-Connected.png)

### 🔹 Step 5 - Verify Connection
Run /mcp list command to verify connection to GitHub MCP server.

![mcp-list](/Screenshots/mcp-list.png)

### 🔹 Step 6 - Test the Server
**Ask:**   
“List my GitHub repositories”        

![test-mcp](/Screenshots/process.png)


![repos](/Screenshots/Repo-list.png)