# Real API Integration Guide 🔌

## How to Use a Real Straker Verify API Key

Currently, the dashboard uses a **mock API client** for demonstration. Here's how it would work with a real API key:

## Current Setup (Mock API)

Right now, the application uses `src/api/client.py` which contains a `StrakerVerifyClient` class that:
- Simulates API responses
- Returns fake project data
- Doesn't make real HTTP requests
- Works without a real API key

## Switching to Real API

### Option 1: Use the Official Straker Verify SDK (Recommended)

Once the `straker-verify` Python package is available on PyPI:

1. **Install the official SDK**
   ```bash
   pip install straker-verify
   ```

2. **Update the client wrapper** (`src/api/client.py`)
   ```python
   # Replace the mock implementation with:
   from straker_verify import StrakerVerify
   
   class StrakerVerifyClient:
       def __init__(self, api_key: str, base_url: str):
           self.client = StrakerVerify(api_key=api_key)
       
       async def get_languages(self):
           return await self.client.get_languages()
       
       async def create_project(self, project_data):
           return await self.client.create_project(project_data)
       
       # ... etc for all methods
   ```

3. **Add your real API key to `.env`**
   ```bash
   STRAKER_VERIFY_API_KEY=your_real_api_key_here
   ```

4. **Run the dashboard**
   ```bash
   python -m src.main
   ```

### Option 2: Direct HTTP Requests

If the SDK isn't available yet, you can make direct HTTP requests:

1. **Update `src/api/client.py`** to use `httpx`:
   ```python
   import httpx
   
   class StrakerVerifyClient:
       def __init__(self, api_key: str, base_url: str):
           self.api_key = api_key
           self.base_url = base_url
           self.client = httpx.AsyncClient(
               base_url=base_url,
               headers={"Authorization": f"Bearer {api_key}"}
           )
       
       async def get_languages(self):
           response = await self.client.get("/languages")
           response.raise_for_status()
           return [Language(**lang) for lang in response.json()]
       
       async def create_project(self, project_data):
           response = await self.client.post(
               "/project",
               json=project_data.dict()
           )
           response.raise_for_status()
           return Project(**response.json())
       
       # ... etc
   ```

2. **Add your real API key**
   ```bash
   # Edit .env file
   STRAKER_VERIFY_API_KEY=sk_live_your_actual_key_here
   ```

## What Changes When Using Real API

### 1. Real Data Instead of Mock Data

**Mock (Current):**
- Shows 2 pre-defined sample projects
- Fake quality scores
- Simulated processing times

**Real API:**
- Shows YOUR actual projects from Straker Verify
- Real quality scores from AI evaluation
- Actual processing status and times

### 2. Real-time Updates

**Mock (Current):**
- Data doesn't change unless you modify the code
- Refresh (`r`) just reloads the same mock data

**Real API:**
- Data reflects actual project status
- Refresh (`r`) fetches latest data from Straker servers
- See real progress as files are processed

### 3. Actual API Calls

**Mock (Current):**
```python
# Simulated delay
await asyncio.sleep(0.1)
# Return fake data
return [fake_project_1, fake_project_2]
```

**Real API:**
```python
# Real HTTP request
response = await self.client.get("/project")
# Return actual data from Straker
return [Project(**p) for p in response.json()]
```

## Step-by-Step Migration

### 1. Get Your API Key

Visit [https://api-verify.straker.ai/](https://api-verify.straker.ai/) to:
- Sign up for an account
- Generate an API key
- Note your key (starts with `sk_live_` or `sk_test_`)

### 2. Update Configuration

Edit `.env`:
```bash
# Replace the demo key
STRAKER_VERIFY_API_KEY=sk_live_your_actual_key_here

# Confirm the base URL
STRAKER_VERIFY_BASE_URL=https://api-verify.straker.ai
```

### 3. Modify the Client

Choose one of these approaches:

**A. Minimal Changes (Keep Mock Structure)**
```python
# In src/api/client.py
class StrakerVerifyClient:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        
        # Add real HTTP client
        self.http_client = httpx.AsyncClient(
            base_url=base_url,
            headers={"Authorization": f"Bearer {api_key}"}
        )
        
        # Remove mock data initialization
        # self._init_sample_data()  # DELETE THIS
```

**B. Use Official SDK (When Available)**
```python
from straker_verify import StrakerVerify

class StrakerVerifyClient:
    def __init__(self, api_key: str, base_url: str):
        self.client = StrakerVerify(
            api_key=api_key,
            base_url=base_url
        )
```

### 4. Update Each Method

For each method in the client, replace mock logic with real API calls:

**Before (Mock):**
```python
async def list_projects(self) -> List[Project]:
    await asyncio.sleep(0.1)  # Fake delay
    return list(self._projects.values())  # Fake data
```

**After (Real):**
```python
async def list_projects(self) -> List[Project]:
    response = await self.http_client.get("/project")
    response.raise_for_status()
    return [Project(**p) for p in response.json()]
```

### 5. Test the Integration

```bash
# Run the dashboard
python -m src.main

# You should now see:
# - Your actual projects (or empty if you have none)
# - Real quality scores
# - Actual processing status
```

## What You'll See with Real API

### Empty Dashboard (No Projects Yet)
```
┌─────────────────┐┌──────────────────┐┌─────────────────┐┌──────────────┐
│ 0              ││ 0               ││ N/A            ││ 0            │
│ Projects       ││ Active          ││ Avg Quality    ││ Files        │
└─────────────────┘└──────────────────┘└─────────────────┘└──────────────┘

No projects yet. Create one to get started!
```

### With Real Projects
```
┌─────────────────┐┌──────────────────┐┌─────────────────┐┌──────────────┐
│ 5              ││ 2               ││ 91.2%          ││ 12           │
│ Projects       ││ Active          ││ Avg Quality    ││ Files        │
└─────────────────┘└──────────────────┘└─────────────────┘└──────────────┘

┌────────────────────────────────────────────────────────────────────────┐
│ My_Website_Translation                             ✓ Complete         │
│ EN → ES                                            3 days ago         │
│ Quality: █████████░ 91.2%                                            │
└────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────┐
│ Legal_Documents_FR                                 ⟳ Processing       │
│ EN → FR                                            5 mins ago         │
└────────────────────────────────────────────────────────────────────────┘
```

## API Endpoints to Implement

Based on Straker Verify API documentation, implement these endpoints:

```python
# Languages
GET /languages

# Projects
GET /project                    # List all projects
POST /project                   # Create new project
GET /project/{project_id}       # Get project details

# Files
POST /project/{project_id}/file # Upload file
GET /file/{file_id}            # Download file

# Quality
GET /project/{project_id}/segments/{file_id}/{language_id}

# Human Verification
POST /project/human-verification

# User
GET /user/balance              # Get token balance
```

## Error Handling

Add proper error handling for real API:

```python
async def list_projects(self) -> List[Project]:
    try:
        response = await self.http_client.get("/project")
        response.raise_for_status()
        return [Project(**p) for p in response.json()]
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 401:
            raise ValueError("Invalid API key")
        elif e.response.status_code == 429:
            raise ValueError("Rate limit exceeded")
        else:
            raise ValueError(f"API error: {e}")
    except httpx.RequestError as e:
        raise ValueError(f"Network error: {e}")
```

## Testing with Real API

1. **Start with test API key** (if available)
   ```bash
   STRAKER_VERIFY_API_KEY=sk_test_...
   ```

2. **Create a test project** via Straker Verify web interface

3. **Run the dashboard** and verify it shows your project

4. **Test refresh** - Press `r` to reload data

5. **Monitor updates** - Watch as projects process

## Benefits of Real API Integration

✅ **Real Data** - See your actual translation projects
✅ **Live Updates** - Track real-time processing status
✅ **Accurate Metrics** - Get genuine quality scores
✅ **Full Workflow** - Create, upload, review, download
✅ **Production Ready** - Use for actual translation management

## Summary

**Current State:**
- Mock API with fake data
- Works without real API key
- Perfect for demo and development

**With Real API Key:**
- Replace mock client with real HTTP calls
- Add your API key to `.env`
- Dashboard shows YOUR actual projects
- All data comes from Straker Verify servers

The architecture is designed to make this transition seamless - just swap the client implementation!