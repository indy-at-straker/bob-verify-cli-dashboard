# Smart API Key Detection

## Overview

The Straker Verify Dashboard automatically detects whether you're using a real API key or a demo key, and switches between real API calls and mock data accordingly.

## How It Works

### API Key Detection Logic

The system analyzes your API key in `.env` to determine if it's real or demo:

**Demo Keys** (triggers mock mode):
- Contains patterns like: `demo`, `test_key`, `your_api_key`, `12345`, `placeholder`
- Short keys (less than 20 characters)
- Example: `demo_api_key_12345`

**Real Keys** (triggers real API mode):
- Starts with `sk_live_` or `sk_test_`
- UUID format (e.g., `25faea7b-8cee-4d57-9e6b-a918000929c8`)
- Longer than 20 characters and doesn't match demo patterns

### Visual Feedback

When the dashboard loads, you'll see a notification:
- ✓ **"Connected to Straker Verify API"** - Using real API
- ℹ **"Using demo mode with mock data"** - Using mock data

## Real API Mode

When a real API key is detected:

1. **HTTP Client Initialized**: Creates an async HTTP client with proper authentication
2. **Real API Calls**: All methods call actual Straker Verify endpoints
3. **Error Handling**: Graceful fallback to empty data on API errors
4. **Resource Cleanup**: HTTP client properly closed when app exits

### Supported Endpoints

- `GET /v1/projects` - List all projects
- `GET /v1/projects/{id}` - Get project details
- `GET /v1/stats` - Get account statistics
- `GET /v1/account/balance` - Get token balance
- `GET /v1/languages` - Get supported languages
- `GET /v1/files/{id}/download` - Download translated files

## Mock Mode

When a demo key is detected:

1. **Sample Data**: Uses pre-generated mock projects and statistics
2. **Instant Response**: No network calls, immediate UI updates
3. **Full Functionality**: All features work with simulated data
4. **Perfect for Testing**: Try the UI without a real API key

### Mock Data Includes

- 2 sample projects (1 completed, 1 processing)
- Quality scores and segments
- Realistic timestamps and metadata
- 10,000 token balance

## Switching Between Modes

To switch modes, simply update your `.env` file:

```bash
# For demo mode
STRAKER_VERIFY_API_KEY=demo_api_key_12345

# For real API mode
STRAKER_VERIFY_API_KEY=your_actual_api_key_here
```

Then restart the application:
```bash
./run.sh
```

## API Key Security

**Important**: Never commit your real API key to version control!

- Real keys are in `.env` (which is gitignored)
- Use `.env.example` as a template
- Demo keys are safe to share

## Troubleshooting

### "No projects yet" with Real API Key

This is normal if:
- Your account has no projects yet
- The API key is valid but the account is empty

**Solution**: Create a project through the Straker Verify web interface or API

### Connection Errors

If you see error messages:
1. Check your internet connection
2. Verify the API key is correct
3. Ensure `STRAKER_VERIFY_BASE_URL` is set correctly
4. Check if the Straker Verify API is accessible

### Falling Back to Mock Data

The app will automatically fall back to mock data if:
- API calls fail
- Network is unavailable
- Invalid API key format

## Implementation Details

### Client Initialization

```python
def __init__(self, api_key: str, base_url: str):
    self.use_real_api = self._is_real_api_key(api_key)
    
    if self.use_real_api:
        self.http_client = httpx.AsyncClient(
            base_url=base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30.0,
        )
    else:
        self._init_sample_data()
```

### Method Pattern

```python
async def list_projects(self) -> List[Project]:
    if self.use_real_api:
        # Real API call
        response = await self.http_client.get("/v1/projects")
        # Parse and return real data
    else:
        # Mock mode
        return list(self._projects.values())
```

## Benefits

1. **Seamless Experience**: No configuration needed, works automatically
2. **Safe Testing**: Try features without affecting real data
3. **Graceful Degradation**: Falls back to mock data on errors
4. **Developer Friendly**: Easy to switch between modes
5. **Production Ready**: Real API integration when you need it

## Next Steps

- Get your API key from [Straker Verify](https://api-verify.straker.ai/)
- Add it to `.env`
- Restart the app
- Start managing real translation projects!