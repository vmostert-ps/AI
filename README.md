# LeanIX Survey Integration

This project provides a robust integration between LeanIX surveys and Azure Functions, enabling automated processing of survey responses and updating of fact sheets in LeanIX.

## Overview

The project consists of a Python-based Azure Function that processes survey responses from LeanIX. It calculates assessment scores, determines risk levels, and updates fact sheets with survey results automatically.

### Key Features

- Dynamic survey configuration loading from LeanIX IAPI
- Automated score calculation based on survey responses
- Risk level assessment
- Fact sheet updates with survey results
- Comprehensive logging and error handling
- Azure Function integration

## Architecture

### Components

1. **Azure Function (`function_app.py`)**
   - HTTP trigger for processing survey webhooks
   - Handles incoming survey responses
   - Manages error handling and response formatting

2. **Survey Utils (`src/leanix_utils/survey_utils.py`)**
   - Core survey processing logic
   - Score calculation
   - Fact sheet updates
   - Configuration management

3. **LeanIX Utils (`src/leanix_utils/leanix_utils.py`)**
   - Base class for LeanIX API interactions
   - Authentication handling
   - API request management

### Data Flow

1. Survey is completed in LeanIX
2. Webhook triggers Azure Function
3. Function processes survey response
4. Scores are calculated
5. Fact sheets are updated
6. Response is sent back to LeanIX

## Setup

### Prerequisites

- Python 3.8 or higher
- Azure Functions Core Tools
- LeanIX API access
- Azure subscription

### Environment Variables

Create a `.env` file in the root directory with:

```json
{
    "api_token": "<your_leanix_api_token>",
    "domain": "<your_leanix_domain>"
}
```

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd leanix-survey-integration
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure Azure Function:
```bash
func azure functionapp publish <function-app-name>
```

## Configuration

### Survey Configuration

The survey configuration is loaded from LeanIX IAPI and includes:

- Poll ID
- Questions and their options
- Scoring rules
- Field mappings

### Field Mappings

The following fields are updated in LeanIX fact sheets:

- `cLLMTrustworthinessScore`: Numeric score (0-100)
- `cLLMTrustworthinessLevel`: Risk level (veryHigh, high, medium, low, veryLow)
- Custom fields for each survey question

## Usage

### Local Development

1. Start the Azure Function locally:
```bash
func start
```

2. Test the endpoint:
```bash
curl -X POST http://localhost:7071/api/MyHttpTrigger -H "Content-Type: application/json" -d @test_payload.json
```

### Production Deployment

1. Deploy to Azure:
```bash
func azure functionapp publish <function-app-name>
```

2. Configure webhook in LeanIX to point to your Azure Function URL

## Testing

### Unit Tests

Run the test suite:
```bash
python -m pytest tests/
```

### Integration Tests

Test the full flow with LeanIX:
```bash
python tests/integration/test_survey_flow.py
```

## Logging

Logs are stored in:
- Local: `logs/` directory
- Azure: Application Insights

## Error Handling

The system includes comprehensive error handling for:
- Invalid survey responses
- API failures
- Configuration errors
- Processing errors

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please:
1. Check the documentation
2. Review existing issues
3. Create a new issue if needed

## Acknowledgments

- LeanIX API Team
- Azure Functions Team
- Contributors and maintainers 